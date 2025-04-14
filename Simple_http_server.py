from misc import USBNET, Power
from machine import Pin
import _thread
import usocket
import ujson
import ql_fs
import utime
import sys
import uos
import log
from uio import FileIO, BytesIO

"""
Simple HTTP server, worked throught internal network adapter (USB Lan).
"""
__version__ = "0.6"


BIND_ADDR = "192.168.43.1"
BIND_PORT = 80

SERVER_STRING = "MicroHTTPServer v1.0"

SOCKET_READ_CHUNK_SIZE = 64

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

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
HTTP_CODE_200 = (200, "OK")
HTTP_CODE_301 = (301, "Moved Permanently")
HTTP_CODE_400 = (400, "Bad Request")
HTTP_CODE_401 = (401, "Unauthorized")
HTTP_CODE_403 = (403, "Forbidden")
HTTP_CODE_404 = (404, "Not Found")
HTTP_CODE_500 = (500, "Internal Server Error")


class Request:
	# Request from client
	def __init__(self, client_socket: usocket.socket, client_addr: str, client_port: int):
		self.sock = client_socket
		self.addr = client_addr
		self.port = client_port

		self.headers: dict[str, str] = {}
		data = b''
		while True:
			chunk = self.sock.recv(SOCKET_READ_CHUNK_SIZE)
			if not chunk:
				break
			data += chunk

			if b"\r\n\r\n" in data:
				break

		head, self.body = data.split(b"\r\n\r\n", 1)
		head = head.decode().split("\r\n")
		self.method, self.path, self.version = head[0].split(" ")
		self.method = self.method.upper()
		for line in head[1:]:
			k, v = line.split(":", 1)
			self.headers[k.strip()] = v.strip()

		self.body_size = len(self.body)
		for k, v in self.headers.items():
			# Sometime headers in upper-case, sometime - not
			if k.lower() == "content-length":
				self.body_size = int(v)

	def read_body(self, chunk_size: int = SOCKET_READ_CHUNK_SIZE):
		# If file too big. Save some memory
		yield self.body
		if self.body_size > len(self.body):
			while chunk := self.sock.recv(chunk_size):
				yield chunk

	def text(self):
		return b''.join(self.read_body()).decode()

	def json(self):
		return ujson.loads(b''.join(self.read_body()))

	def close(self):
		self.sock.close()


class Response:
	def __init__(self, req: Request, code: int = 200, headers: dict = {}, content: bytes = b''):
		self.req = req
		self.response_code = code
		self.content = content
		self.headers = headers
		self.headers["Server"] = SERVER_STRING

	@property
	def text(self):
		return self.content.decode()

	@text.setter
	def text(self, value: str):
		self.content = value.encode()

	@property
	def json(self):
		return ujson.loads(self.content)

	@json.setter
	def json(self, value: dict):
		self.content = ujson.dumps(value).encode()

	@property
	def response_text(self):
		for code, message in (HTTP_CODE_200, HTTP_CODE_301, HTTP_CODE_400, HTTP_CODE_401, HTTP_CODE_403, HTTP_CODE_404, HTTP_CODE_500):
			if code == self.response_code:
				return message
		raise ValueError("Unsupported HTTP code %d" % self.response_code)

	def header_bytes(self):
		header = ('HTTP/1.1 %d %s' % (self.response_code, self.response_text)).encode()
		for k, v in self.headers.items():
			header += ("%s: %s\r\n" % (k, v)).encode()
		header += b"\r\n"  # Header end newline
		return header

	def send(self):
		self.headers["Content-Length"] = len(self.content)
		self.req.sock.sendall(self.header_bytes() + self.content)
		self.req.sock.close()

	def send_stream(self, bytes_io: BytesIO, data_size: int, chunk_size: int = 1024):
		self.headers["Content-Length"] = data_size
		self.req.sock.send(self.header_bytes())
		while chunk := bytes_io.read(chunk_size):
			self.req.sock.send(chunk)
		self.req.sock.close()


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

	def _client_handler(self, client: usocket.socket, addr: str, port: int):
		req = Request(client, addr, port)

		self.log.info("%s:%d -> %s %s", addr, port, req.method, req.path)
		self.log.debug("".join(["\t%s: %s\n" % (k, v) for k, v in req.headers.items()]))

		if req.path.endswith("/"):
			path = req.path[:-1]
		else:
			path = req.path

		if req.method == "GET":
			if p := self._public_paths.get(path) or self._hidden_paths.get(path):
				_, fn = p
				fn(self, req)
			elif not self.is_exists(path):
				self.send_error(req, 404, "File not found")
			else:
				if self.is_dir(path):
					self.response_dir_listing(req, path)
				else:
					# if requested + ".gz" is exists - send it instead of original (uncompressed) file
					# Send ofly if accept-encoding contains "gzip"
					self.send_file(req, path)
		elif req.method == "POST":
			# TODO
			# Check publick endpoints
			# Check private endpoints
			# Check if headers contains file_name/file_size, if requested path is a folder - save file intro this folder.
			pass

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

	def response_dir_listing(self, req: Request, path: str):
		body = "<h2>Hello, %s:%s!</h2>\n" % (req.addr, req.port)
		body += "<table>\n"
		body += "\t<tr><td>Name</td><td>Size</td></tr>\n"

		if path != "":
			# Show only on subpages
			parent = self.get_parent_dir(path)
			body += TPL_TABLE_ROW % (parent, "..", "DIR")
		else:
			# Show only on main page
			for p, info in self._public_paths.items():
				body += TPL_TABLE_ROW % (p, info[0], "APP")

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
			body += TPL_TABLE_ROW % (path + "/" + name, name, size)

		body += "</table>\n"

		self.send_html(req, TPL_HTML_BODY, title="Index of " + path, body=body)

	def send(self, req: Request, code: int, content_type: str, body: bytes):
		resp = Response(req, code, {"Content-Type": content_type}, body)
		resp.send()

	def send_html(self, req: Request, template: str, **kwargs):
		resp = Response(req, 200, {"Content-Type": "text/html; charset=utf-8"}, template % kwargs)
		resp.send()

	def send_error(self, req: Request, code: int, message: str):
		body = TPL_HTML_BODY % {
			"title": "HTTP Error %s" % code,
			"body": "<center><h1>HTTP Error %d: %s</h1></center>" % (code, message),
		}
		resp = Response(req, code, {"Content-Type": "text/html; charset=utf-8"}, body)
		resp.send()

	def send_file(self, req: Request, path: str):
		resp = Response(req, 200, {"Content-Type": "application/octet-stream"})
		size = uos.stat(path)[6]
		with open(path, 'rb') as f:
			resp.send_stream(f, size, 1024)


if __name__ == "__main__":
	if USBNET.get_worktype() != USBNET.Type_RNDIS:
		print("Not in RNDIS mode! Restarting...")
		USBNET.set_worktype(USBNET.Type_RNDIS)
		Power.powerRestart()

	log.basicConfig(log.DEBUG)

	def print_uname(server: HTTP_Server, req: Request):
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
		server.send_html(req, TPL_HTML_BODY, title="System info", body=body)

	def turn_off(server: HTTP_Server, req: Request):
		server.send_html(req, TPL_HTML_BODY, title="Power control", body="Shutting down...")
		utime.sleep(1)
		Power.powerDown()

	def led_red_on(server: HTTP_Server, req: Request):
		Pin(Pin.GPIO15, Pin.OUT, Pin.PULL_DISABLE, 1)
		server.send_html(req, TPL_HTML_BODY, title="Led control", body="<b>DONE!</b> <a href=\"/\">Go back</a>")

	def led_red_off(server: HTTP_Server, req: Request):
		Pin(Pin.GPIO15, Pin.OUT, Pin.PULL_DISABLE, 0)
		server.send_html(req, TPL_HTML_BODY, title="Led control", body="<b>DONE!</b> <a href=\"/\">Go back</a>")

	server = HTTP_Server()
	server.add_path("/uname", "Run uname()", print_uname)
	server.add_path("/poweroff", "Shutdown device", turn_off)
	server.add_path("/led/red/on", "Turn on RED led", led_red_on)
	server.add_path("/led/red/off", "Turn off RED led", led_red_off)
	server.listen(BIND_ADDR, BIND_PORT)
