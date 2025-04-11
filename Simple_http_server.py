from misc import USBNET, Power
from machine import Pin
import _thread
import usocket
import ql_fs
import utime
import sys
import uos
import log


"""
Simple HTTP server, worked throught internal network adapter (USB Lan).
"""


BIND_ADDR = "192.168.43.1"
BIND_PORT = 80

TYPE_DIR = 0x4000
TYPE_FILE = 0x8000

TPL_HTML_BODY = """\
<!DOCTYPE HTML>
<html lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
		<title>%(title)s</title>
	</head>
	<body>
		%(body)s
	</body>
</html>
"""

TPL_TABLE_ROW = "\t\t<tr><td><a href=\"%s\">%s</a></td><td>%s</td></tr>\n"


class HTTP_Server:
	def __init__(self):
		self.log = log.getLogger(__name__)
		self.sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
		self._public_paths = {}
		self._hidden_paths = {}

	def listen(self, address: str, port: int):
		self.sock.bind((address, port))
		self.sock.listen(3)
		self.log.info("Server listening on %s:%s", address, port)
		while True:
			conn, addr, port = self.sock.accept()
			_thread.start_new_thread(self._client_handler, (conn, addr, port))

	def add_path(self, path: str, name: str, callback, hidden: bool = False):
		if hidden:
			self._hidden_paths[path] = (name, callback)
		else:
			self._public_paths[path] = (name, callback)

	def _client_handler(self, sock: usocket.socket, addr: str, port: int):
		data: bytes = sock.recv(1024)
		headers, data = data.decode().split("\r\n\r\n", 1)
		headers = headers.split("\r\n")

		self.log.info("%s:%d -> %s", addr, port, headers[0])
		self.log.debug("\t" + "\n\t".join(headers[1:]))

		# [0] = "GET /some/path HTTP/1.1"
		method, path, http_ver = headers[0].split(" ")
		if path.endswith("/"):
			path = path[:-1]

		if method.upper() == "GET":
			if p := self._public_paths.get(path) or self._hidden_paths.get(path):
				_, fn = p
				fn(self, sock)
			elif not self.is_exists(path):
				self.send_error(sock, 404, "File not found")
			else:
				if self.is_dir(path):
					response = "<h1>Hello, %s:%s!</h1>\n" % (addr, port)
					response += "<table>\n"
					response += "\t<tr><td>Name</td><td>Size</td></tr>\n"

					if path != "":
						# Show only on subpages
						parent = self.get_parent_dir(path)
						response += TPL_TABLE_ROW % (parent, "..", "DIR")
					else:
						# Show only on main page
						for p, info in self._public_paths.items():
							response += TPL_TABLE_ROW % (p, info[0], "APP")

					try:
						for entry in uos.ilistdir(path):
							if len(entry) == 3:
								# Root dir only
								name, mode, _ = entry
								size = uos.stat(path + "/" + name)[6]
							else:
								# All other files and folders
								name, mode, _, size = entry

							if mode == TYPE_DIR:
								size = "DIR"
							response += TPL_TABLE_ROW % (path + "/" + name, name, size)
					except OSError as e:
						response += "\t<tr><td colspan=\"2\">%s</td></tr>\n" % e

					response += "</table>\n"
					self.send_html(sock, "Index of %s" % path, response)
				else:
					self.send_file(sock, path)
		sock.close()

	def is_dir(self, path: str):
		return uos.stat(path)[0] == TYPE_DIR

	def is_exists(self, path):
		try:
			uos.stat(path)
		except OSError as e:
			# 2 = ENOENT
			# 19 = ENODEV
			# if e.args[0] in (2, 19):
			return False
		return True

	def get_parent_dir(self, path: str):
		if path.endswith("/"):
			path = path[:-1]
		path = "/".join(path.split("/")[:-1])
		if not path.startswith("/"):
			path = "/" + path
		return path

	def send(self, sock: usocket.socket, code: int, message: str, content_type: str, body, add_headers: list[str] = []):
		headers = [
			"HTTP/1.1 %d %s" % (code, message),
			"Content-Type: %s" % content_type,
			"Content-Length: %d" % len(body),
		]
		headers.extend(add_headers)
		headers.append("\r\n")  # newline at headers end
		sock.sendall("\r\n".join(headers).encode() + body)

	def send_html(self, sock: usocket.socket, page_title: str, body_text: str):
		body = TPL_HTML_BODY % {
			"title": page_title,
			"body": body_text,
		}
		self.send(sock, 200, "OK", "text/html; charset=utf-8", body)

	def send_error(self, sock: usocket.socket, code: int, message: str):
		body = TPL_HTML_BODY % {
			"title": "HTTP Error %s" % code,
			"body": "<center><h1>HTTP Error %d: %s</h1></center>" % (code, message),
		}
		self.send(sock, code, message, "text/html; charset=utf-8", body)

	def send_file(self, sock: usocket.socket, path: str):
		size = uos.stat(path)[6]
		headers = [
			"HTTP/1.1 200 OK",
			"Content-Type: application/octet-stream",
			"Content-Length: %d" % size,
			"\r\n"
		]

		# Send headers
		sock.write("\r\n".join(headers).encode())

		# Send file by chunks for save memoty
		with open(path, 'rb') as f:
			while chunk := f.read(1024):
				sock.write(chunk)


if __name__ == "__main__":
	if USBNET.get_worktype() != USBNET.Type_RNDIS:
		print("Not in RNDIS mode! Restarting...")
		USBNET.set_worktype(USBNET.Type_RNDIS)
		Power.powerRestart()

	log.basicConfig(log.DEBUG)

	def print_uname(server: HTTP_Server, client: usocket.socket):
		html = "<a href=\"/\">Go back</a><br>\n"
		html += "<hr>\n"
		html += "<ul>\n"
		for line in uos.uname():
			html += "\t<li><b>%s</b>: %s</li>\n" % tuple(line.split("=", 1))
		html += "</ul>"

		body = TPL_HTML_BODY % {
			"title": "About this board",
			"body": html,
		}
		server.send_html(client, "System info", body)

	def turn_off(server: HTTP_Server, client: usocket.socket):
		server.send_html(client, "Power control", "Shutting down...")
		utime.sleep(1)
		Power.powerDown()

	def led_red_on(server: HTTP_Server, client: usocket.socket):
		Pin(Pin.GPIO15, Pin.OUT, Pin.PULL_DISABLE, 1)
		server.send_html(client, "Led control", "<b>DONE!</b> <a href=\"/\">Go back</a>")

	def led_red_off(server: HTTP_Server, client: usocket.socket):
		Pin(Pin.GPIO15, Pin.OUT, Pin.PULL_DISABLE, 0)
		server.send_html(client, "Led control", "<b>DONE!</b> <a href=\"/\">Go back</a>")

	server = HTTP_Server()
	server.add_path("/uname", "Run uname()", print_uname)
	server.add_path("/poweroff", "Shutdown device", turn_off)
	server.add_path("/led/red/on", "Turn on RED led", led_red_on)
	server.add_path("/led/red/off", "Turn off RED led", led_red_off)
	server.listen(BIND_ADDR, BIND_PORT)
