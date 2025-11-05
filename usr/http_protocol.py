import usocket
import ujson
import modem

from usr.led_controller import Led


class HTTPProtocol:
	"""HTTP protocol implementation for data transmission"""

	def __init__(self, host, port, path, leds):
		self.host = host
		self.port = port
		self.path = path
		self.leds = leds
		self.connected = False

		# Get device IMEI

		self.imei = modem.getDevImei()

		print('HTTP protocol initialized: {}:{}{}'.format(host, port, path))

	def connect(self):
		"""HTTP doesn't require persistent connection"""
		self.connected = True
		return True

	def disconnect(self):
		"""Disconnect"""
		self.connected = False

	def send_location(self, data):
		"""Send location data via HTTP POST"""
		try:
			self.leds.set_network_status(Led.MODE_BLINK_CONNECT)

			# Prepare JSON data with IMEI
			json_data = {
				'imei': self.imei,
				'timestamp': data['timestamp'],
				'latitude': data['latitude'],
				'longitude': data['longitude'],
				'altitude': data['altitude'],
				'speed': data['speed'],
				'course': data['course'],
				'satellites': data['satellites'],
				'battery': data['battery'],
				'charging': data['charging'],
				'source': data.get('source', 'gps'),
				'accuracy': data.get('accuracy', 0)
			}

			json_str = ujson.dumps(json_data)

			# Create HTTP request
			request = 'POST {} HTTP/1.1\r\n'.format(self.path)
			request += 'Host: {}\r\n'.format(self.host)
			request += 'Content-Type: application/json\r\n'
			request += 'Content-Length: {}\r\n'.format(len(json_str))
			request += 'User-Agent: QuecPython-Tracker/1.0\r\n'
			request += 'X-Device-IMEI: {}\r\n'.format(self.imei)
			request += 'Connection: close\r\n'
			request += '\r\n'
			request += json_str

			# Send request
			sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
			sock.settimeout(10)

			addr = usocket.getaddrinfo(self.host, self.port)[0][-1]
			sock.connect(addr)
			sock.send(request.encode())

			# Receive response
			response = b''
			while True:
				chunk = sock.recv(1024)
				if not chunk:
					break
				response += chunk
				# Break if we have complete response headers
				if b'\r\n\r\n' in response:
					break

			sock.close()

			# Check response
			if response:
				response_str = response.decode('utf-8', 'ignore')
				if '200 OK' in response_str or '201' in response_str or '204' in response_str:
					print('HTTP: Data sent successfully')
					self.connected = True
					self.leds.set_network_status(Led.MODE_PULSE)
					return True
				else:
					print('HTTP: Server returned error:', response_str.split('\r\n')[0])

			self.connected = False
			self.leds.set_network_status(Led.MODE_OFF)
			return False

		except Exception as e:
			print('HTTP send error:', e)
			self.connected = False
			self.leds.set_network_status(Led.MODE_OFF)
			return False
