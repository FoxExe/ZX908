import wifiScan
import usocket
import ujson
import _thread
import utime


class WiFiLocation:
	"""WiFi-based location using WiFi scanning and geolocation services"""

	# Default geolocation services
	DEFAULT_SERVICES = [
		{
			'name': 'Mozilla Location Service',
			'host': 'location.services.mozilla.com',
			'port': 443,
			'path': '/v1/geolocate?key=test',
			'ssl': True
		},
		{
			'name': 'Unwired Labs',
			'host': 'us1.unwiredlabs.com',
			'port': 443,
			'path': '/v2/process.php',
			'ssl': True,
			'requires_key': True
		}
	]

	def __init__(self, custom_server=None):
		self.enabled = False
		self.scan_result = None
		self.scan_complete = False
		self.custom_server = custom_server
		self.lock = _thread.allocate_lock()

	def enable(self):
		"""Enable WiFi module"""
		try:
			ret = wifiScan.control(1)
			if ret == 0:
				self.enabled = True
				print('WiFi module enabled')
				return True
			else:
				print('WiFi module enable failed:', ret)
				return False
		except Exception as e:
			print('WiFi enable error:', e)
			return False

	def disable(self):
		"""Disable WiFi module"""
		try:
			wifiScan.control(0)
			self.enabled = False
			print('WiFi module disabled')
		except Exception as e:
			print('WiFi disable error:', e)

	def get_location(self):
		"""Get location based on WiFi networks"""
		if not self.enabled:
			if not self.enable():
				return None

		try:
			# Scan for WiFi networks
			wifi_list = self._scan_wifi()

			if not wifi_list or len(wifi_list) == 0:
				print('No WiFi networks found')
				return None

			print('Found', len(wifi_list), 'WiFi networks')

			# Query geolocation service
			location = self._query_geolocation(wifi_list)

			return location
		except Exception as e:
			print('WiFi location error:', e)
			return None

	def _scan_wifi(self):
		"""Scan for nearby WiFi networks"""
		try:
			self.scan_result = None
			self.scan_complete = False

			# Set callback
			wifiScan.setCallback(self._scan_callback)

			# Start async scan
			ret = wifiScan.asyncStart()
			if ret != 0:
				print('WiFi scan start failed:', ret)
				return []

			# Wait for scan to complete (max 10 seconds)
			timeout = 10
			start_time = utime.time()
			while not self.scan_complete and (utime.time() - start_time) < timeout:
				utime.sleep_ms(100)

			if not self.scan_complete:
				print('WiFi scan timeout')
				return []

			return self.scan_result if self.scan_result else []

		except Exception as e:
			print('WiFi scan error:', e)
			return []

	def _scan_callback(self, data):
		"""Callback for WiFi scan results"""
		try:
			with self.lock:
				# data format: (count, [(mac, rssi), (mac, rssi), ...])
				count, aps = data

				wifi_list = []
				for ap_info in aps:
					mac_addr, rssi = ap_info
					wifi_list.append({
						'mac': mac_addr,
						'signal': rssi
					})
					print('WiFi AP: MAC={}, RSSI={}dB'.format(mac_addr, rssi))

				self.scan_result = wifi_list
				self.scan_complete = True

		except Exception as e:
			print('Scan callback error:', e)
			self.scan_complete = True

	def _query_geolocation(self, wifi_list):
		"""Query geolocation service"""
		# Use custom server if configured
		if self.custom_server:
			return self._query_custom_server(wifi_list)

		# Try default services
		for service in self.DEFAULT_SERVICES:
			if service.get('requires_key') and not hasattr(self, 'api_key'):
				continue

			try:
				location = self._query_service(wifi_list, service)
				if location:
					return location
			except Exception as e:
				print('Service {} failed: {}'.format(service['name'], e))
				continue

		return None

	def _query_service(self, wifi_list, service):
		"""Query specific geolocation service"""
		try:
			# Prepare request data
			wifi_data = []
			for ap in wifi_list:
				wifi_data.append({
					'macAddress': ap['mac'],
					'signalStrength': ap['signal']
				})

			request_data = {
				'wifiAccessPoints': wifi_data
			}

			json_data = ujson.dumps(request_data)

			# Create HTTP request
			request = 'POST {} HTTP/1.1\r\n'.format(service['path'])
			request += 'Host: {}\r\n'.format(service['host'])
			request += 'Content-Type: application/json\r\n'
			request += 'Content-Length: {}\r\n'.format(len(json_data))
			request += 'Connection: close\r\n'
			request += '\r\n'
			request += json_data

			# Connect and send
			sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
			sock.settimeout(10)

			addr = usocket.getaddrinfo(service['host'], service['port'])[0][-1]
			sock.connect(addr)

			# For SSL (if supported)
			if service.get('ssl'):
				try:
					import ussl
					sock = ussl.wrap_socket(sock)
				except:
					print('SSL not supported, using plain connection')

			sock.send(request.encode())

			# Receive response
			response = b''
			while True:
				data = sock.recv(1024)
				if not data:
					break
				response += data

			sock.close()

			# Parse response
			response_str = response.decode('utf-8', 'ignore')

			# Extract JSON body
			if '\r\n\r\n' in response_str:
				body = response_str.split('\r\n\r\n', 1)[1]

				try:
					result = ujson.loads(body)

					# Parse location from response
					if 'location' in result:
						lat = result['location'].get('lat', 0)
						lng = result['location'].get('lng', 0)
						accuracy = result.get('accuracy', 0)

						print('WiFi location found: lat={}, lng={}, accuracy={}m'.format(
							lat, lng, accuracy))

						return {
							'valid': True,
							'latitude': lat,
							'longitude': lng,
							'altitude': 0.0,
							'speed': 0.0,
							'course': 0.0,
							'satellites': 0,
							'accuracy': accuracy,
							'source': 'wifi',
							'timestamp': utime.time()
						}

				except Exception as e:
					print('JSON parse error:', e)

			return None

		except Exception as e:
			print('Query service error:', e)
			return None

	def _query_custom_server(self, wifi_list):
		"""Query custom geolocation server"""
		try:
			server = self.custom_server

			# Prepare WiFi data
			wifi_data = []
			for ap in wifi_list:
				wifi_data.append({
					'mac': ap['mac'],
					'rssi': ap['signal']
				})

			request_data = {
				'wifiAccessPoints': wifi_data
			}

			json_data = ujson.dumps(request_data)

			# Parse server URL
			host = server.get('host', '')
			port = server.get('port', 80)
			path = server.get('path', '/api/locate')

			# Create HTTP request
			request = 'POST {} HTTP/1.1\r\n'.format(path)
			request += 'Host: {}\r\n'.format(host)
			request += 'Content-Type: application/json\r\n'
			request += 'Content-Length: {}\r\n'.format(len(json_data))
			request += 'Connection: close\r\n'
			request += '\r\n'
			request += json_data

			# Connect and send
			sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
			sock.settimeout(10)

			addr = usocket.getaddrinfo(host, port)[0][-1]
			sock.connect(addr)
			sock.send(request.encode())

			# Receive response
			response = b''
			while True:
				data = sock.recv(1024)
				if not data:
					break
				response += data

			sock.close()

			# Parse response
			response_str = response.decode('utf-8', 'ignore')

			if '\r\n\r\n' in response_str:
				body = response_str.split('\r\n\r\n', 1)[1]

				try:
					result = ujson.loads(body)

					if 'latitude' in result and 'longitude' in result:
						return {
							'valid': True,
							'latitude': result['latitude'],
							'longitude': result['longitude'],
							'altitude': result.get('altitude', 0.0),
							'speed': 0.0,
							'course': 0.0,
							'satellites': 0,
							'accuracy': result.get('accuracy', 0),
							'source': 'wifi',
							'timestamp': utime.time()
						}

				except Exception as e:
					print('JSON parse error:', e)

			return None

		except Exception as e:
			print('Custom server error:', e)
			return None

	def set_custom_server(self, host, port=80, path='/api/locate'):
		"""Set custom geolocation server"""
		self.custom_server = {
			'host': host,
			'port': port,
			'path': path
		}
		print('Custom WiFi location server set:', host)
