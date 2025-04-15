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
import ure
import unzip
from uio import FileIO, BytesIO

"""
Simple HTTP server, worked throught internal network adapter (USB Lan).
"""
__version__ = "0.6"


BIND_ADDR = "192.168.43.1"
BIND_PORT = 80

SERVER_STRING = "MicroHTTPServer v" + __version__

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


CONTENT_TYPES = {
	"json": "application/json",
	"js": "application/javascript",
	"html": "text/html; charset=utf-8",
	"txt": "text/plain",
	"css": "text/css",
	"bin": "application/octet-stream",
	"jpg": "image/jpeg",
	"png": "image/png",
	"svg": "image/svg+xml",
}


class Request:
	# Request from client
	def __init__(self, client_socket: usocket.socket, client_addr: str, client_port: int):
		self.sock = client_socket
		self.addr = client_addr
		self.port = client_port

		self.headers: dict[str, str] = {}
		data = b''
		while chunk := self.sock.recv(SOCKET_READ_CHUNK_SIZE):
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


class Response:
	def __init__(self, req: Request, code: int = 200, headers: dict = {}):
		self.req = req
		self.response_code = code
		self.content = b''
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
		self.headers["Content-Type"] = CONTENT_TYPES["json"]

	@property
	def response_text(self):
		for code, message in (HTTP_CODE_200, HTTP_CODE_301, HTTP_CODE_400, HTTP_CODE_401, HTTP_CODE_403, HTTP_CODE_404, HTTP_CODE_500):
			if code == self.response_code:
				return message
		raise ValueError("Unsupported HTTP code %d" % self.response_code)

	def header_bytes(self):
		header = 'HTTP/1.1 %d %s\r\n' % (self.response_code, self.response_text)
		for k, v in self.headers.items():
			header += "%s: %s\r\n" % (k, v)
		header += "\r\n"
		return header.encode()

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
		self._paths: list[tuple[ure.ure, callable]] = []

	def run(self, address: str, port: int, web_root: str = "/", backlog: int = 1):
		self.web_root = web_root
		self.sock.bind((address, port))
		self.sock.listen(backlog)
		self.log.info("Server listening on %s:%s", address, port)
		while True:
			conn, addr, port = self.sock.accept()
			_thread.start_new_thread(self._client_handler, (conn, addr, port))

	def add_handler(self, regex_path: str, callback):
		"""Will run `callback(req: Request, matched: ure.Match)`"""
		self._paths.append((ure.compile(regex_path), callback))

	def _client_handler(self, client: usocket.socket, addr: str, port: int):
		req = Request(client, addr, port)

		self.log.info("%s:%d -> %s %s", addr, port, req.method, req.path)
		self.log.debug("Headers:\n" + "".join(["\t%s: %s\n" % (k, v) for k, v in req.headers.items()]))

		fullpath = self.path_join(self.web_root, req.path)
		if fullpath.endswith("/"):
			fullpath = fullpath[:-1]

		for r, fn in self._paths:
			if g := r.match(req.path):
				fn(req, g)
				return

		if req.method == "GET":
			if self.is_exists(fullpath):
				if self.is_dir(fullpath):
					if self.is_exists(fullpath + "/index.html.gz"):
						self.send_file(req, fullpath + "/index.html.gz")
					else:
						self.send_dir_index(req, fullpath)
				else:
					# TODO
					# Add support for compressed files (for style.css.gz / index.html.gz and etc. Save some space!)
					self.send_file(req, fullpath)
			elif self.is_exists(fullpath + ".gz"):
				# Requested file not found, but we have compressed version
				self.send_file(req, fullpath + ".gz")
			else:
				self.send_error(req, 404, "Requested path is not found!")
		elif req.method == "POST":
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

	def path_join(self, a: str, b: str):
		if a.endswith("/"):
			a = a[:-1]
		if b.startswith("/"):
			b = b[1:]
		return a + "/" + b

	def get_parent_dir(self, path: str):
		if path.endswith("/"):
			path = path[:-1]
		path = "/".join(path.split("/")[:-1])
		if not path.startswith("/"):
			path = "/" + path
		return path

	def send_dir_index(self, req: Request, path: str):
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

		resp = Response(req, 200, {"Content-Type": CONTENT_TYPES["html"]})
		resp.text = TPL_HTML_BODY % {
			"title": "Index of " + path,
			"body": body,
		}
		resp.send()

	def send_error(self, req: Request, code: int, message: str):
		resp = Response(req, code, {"Content-Type": CONTENT_TYPES["html"]})
		resp.text = TPL_HTML_BODY % {
			"title": "HTTP Error %s" % code,
			"body": "<center><h1>HTTP Error %d: %s</h1></center>" % (code, message),
		}
		resp.send()

	def send_file(self, req: Request, path: str):
		ext = path.lower().split(".")
		if len(ext) > 2 and ext[-1] == "gz":
			fe = ext[-2]
			compressed = True
		else:
			fe = ext[-1]
			compressed = False
		headers = {"Content-Type": CONTENT_TYPES.get(fe, CONTENT_TYPES["bin"])}
		if compressed:
			headers["Content-Encoding"] = "gzip"

		resp = Response(req, 200, headers)
		size = uos.stat(path)[6]
		with open(path, 'rb') as f:
			resp.send_stream(f, size, 1024)


if __name__ == "__main__":
	if USBNET.get_worktype() != USBNET.Type_RNDIS:
		print("Not in RNDIS mode! Restarting...")
		USBNET.set_worktype(USBNET.Type_RNDIS)
		Power.powerRestart()

	log.basicConfig(log.DEBUG)

	def print_uname(req: Request, _):
		body = "<a href=\"/\">Go back</a><br>\n"
		body += "<hr>\n"
		body += "<ul>\n"
		for line in uos.uname():
			body += "\t<li><b>%s</b>: %s</li>\n" % tuple(line.split("=", 1))
		body += "</ul>"

		resp = Response(req, 200, {"Content-Type": CONTENT_TYPES["html"]})
		resp.text = TPL_HTML_BODY % {
			"title": "About this board",
			"body": body,
		}
		resp.send()

	def turn_off(req: Request, _):
		resp = Response(req, 200, {"Content-Type": CONTENT_TYPES["html"]})
		resp.json = {"success": True}
		resp.send()
		utime.sleep(1)
		Power.powerDown()

	def led_control(req: Request, matched: ure.Match):
		LED_PIN = {
			"red": Pin.GPIO15,
			"blue": Pin.GPIO16,
			"yellow": Pin.GPIO17,
		}
		LED_STATE = {
			"off": 0,
			"on": 1,
		}

		Pin(LED_PIN.get(matched.group(1), LED_PIN[0]), Pin.OUT, Pin.PULL_DISABLE, LED_STATE.get(matched.group(2), 1))

		resp = Response(req, 200, {"Content-Type": CONTENT_TYPES["html"]})
		resp.json = {"success": True}
		resp.send()

	server = HTTP_Server()
	server.add_handler(r"/uname", print_uname)
	server.add_handler(r"/poweroff", turn_off)
	server.add_handler(r"/led/(red|yellow|blue)/(on|off)", led_control)
	server.run(BIND_ADDR, BIND_PORT, "/usr/web/", 1)
