import usocket
import ustruct
import utime
import modem
from usr.led_controller import Led


class GT06Protocol:
	"""GT06 protocol implementation with WiFi extension"""

	LOGIN = 0x01
	LOCATION = 0x12
	HEARTBEAT = 0x13
	STATUS = 0x14
	WIFI_LOCATION = 0x69

	def __init__(self, host, port, leds):
		self.host = host
		self.port = port
		self.leds = leds
		self.socket = None
		self.connected = False
		self.serial_number = 1
		self.imei = modem.getDevImei()
		print('GT06 protocol initialized: {}:{}, IMEI: {}'.format(host, port, self.imei))
		self.connect()

	def connect(self):
		"""Connect to server"""
		try:
			if self.socket:
				try:
					self.socket.close()
				except:
					pass
			self.leds.set_network_status(Led.MODE_BLINK_CONNECT)
			print('Connecting to {}:{}'.format(self.host, self.port))
			self.socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
			self.socket.settimeout(10)
			addr = usocket.getaddrinfo(self.host, self.port)[0][-1]
			self.socket.connect(addr)
			if self._send_login():
				self.connected = True
				self.leds.set_network_status(Led.MODE_PULSE)
				print('Connected to server')
				return True
			else:
				self.connected = False
				self.leds.set_network_status(Led.MODE_OFF)
				return False
		except Exception as e:
			print('Connection error:', e)
			self.connected = False
			self.leds.set_network_status(Led.MODE_OFF)
			return False

	def disconnect(self):
		"""Disconnect from server"""
		if self.socket:
			try:
				self.socket.close()
			except:
				pass
			self.socket = None
		self.connected = False
		self.leds.set_network_status(Led.MODE_OFF)

	def _send_login(self):
		"""Send login packet with IMEI"""
		try:
			imei_hex = self.imei[-16:] if len(self.imei) >= 16 else self.imei.zfill(16)
			imei_bytes = bytes.fromhex(imei_hex)
			packet = bytearray()
			packet.append(0x78)
			packet.append(0x78)
			packet.append(0x0A)
			packet.append(self.LOGIN)
			packet.extend(imei_bytes)
			serial = ustruct.pack('>H', self.serial_number)
			packet.extend(serial)
			crc = self._calculate_crc(packet[2:])
			packet.extend(ustruct.pack('>H', crc))
			packet.append(0x0D)
			packet.append(0x0A)
			self.socket.send(packet)
			self.serial_number = (self.serial_number + 1) % 0xFFFF
			response = self.socket.recv(128)
			if response and len(response) > 4:
				print('Login successful')
				return True
			print('Login failed: no response')
			return False
		except Exception as e:
			print('Login error:', e)
			return False

	def send_location(self, data):
		"""Send location data"""
		if not self.connected:
			if not self.connect():
				return False
		try:
			if data.get('wifi_networks') and len(data['wifi_networks']) > 0:
				return self._send_wifi_location(data)
			else:
				return self._send_gps_location(data)
		except Exception as e:
			print('Send location error:', e)
			self.connected = False
			return False

	def _send_gps_location(self, data):
		"""Send GPS location packet"""
		try:
			packet = bytearray()
			packet.append(0x78)
			packet.append(0x78)
			time_tuple = utime.localtime(data['timestamp'])
			date_time = bytearray([time_tuple[0] - 2000, time_tuple[1], time_tuple[2],
			                      time_tuple[3], time_tuple[4], time_tuple[5]])
			satellites = data['satellites'] & 0x0F
			gps_valid = 1 if data.get('valid', False) else 0
			lat = int(abs(data['latitude']) * 30000.0)
			lon = int(abs(data['longitude']) * 30000.0)
			lat_flag = 0 if data['latitude'] >= 0 else 1
			lon_flag = 0 if data['longitude'] >= 0 else 1
			speed = int(data['speed'])
			course = int(data['course']) & 0x03FF
			course |= (gps_valid << 12)
			location_data = bytearray()
			location_data.extend(date_time)
			location_data.append((satellites << 4) | (gps_valid << 3))
			location_data.extend(ustruct.pack('>I', lat))
			location_data.extend(ustruct.pack('>I', lon))
			location_data.append(speed)
			location_data.extend(ustruct.pack('>H', course))
			packet.append(len(location_data) + 5)
			packet.append(self.LOCATION)
			packet.extend(location_data)
			serial = ustruct.pack('>H', self.serial_number)
			packet.extend(serial)
			crc = self._calculate_crc(packet[2:])
			packet.extend(ustruct.pack('>H', crc))
			packet.append(0x0D)
			packet.append(0x0A)
			self.socket.send(packet)
			self.serial_number = (self.serial_number + 1) % 0xFFFF
			try:
				self.socket.settimeout(5)
				response = self.socket.recv(128)
				if response and len(response) > 0:
					print('GPS location sent successfully')
					return True
				else:
					print('No server response')
					return True
			except:
				return True
		except Exception as e:
			print('Send GPS location error:', e)
			self.connected = False
			return False

	def _send_wifi_location(self, data):
		"""Send WiFi location packet (custom extension)"""
		try:
			packet = bytearray()
			packet.append(0x78)
			packet.append(0x78)
			wifi_networks = data['wifi_networks']
			wifi_count = min(len(wifi_networks), 15)
			wifi_data = bytearray()
			wifi_data.append(wifi_count)
			for wifi in wifi_networks[:wifi_count]:
				mac_bytes = bytes.fromhex(wifi['mac'].replace(':', ''))
				wifi_data.extend(mac_bytes)
				wifi_data.append(abs(wifi['signal']) & 0xFF)
			time_tuple = utime.localtime(data['timestamp'])
			date_time = bytearray([time_tuple[0] - 2000, time_tuple[1], time_tuple[2],
			                      time_tuple[3], time_tuple[4], time_tuple[5]])
			wifi_data.extend(date_time)
			packet.append(len(wifi_data) + 5)
			packet.append(self.WIFI_LOCATION)
			packet.extend(wifi_data)
			serial = ustruct.pack('>H', self.serial_number)
			packet.extend(serial)
			crc = self._calculate_crc(packet[2:])
			packet.extend(ustruct.pack('>H', crc))
			packet.append(0x0D)
			packet.append(0x0A)
			self.socket.send(packet)
			self.serial_number = (self.serial_number + 1) % 0xFFFF
			try:
				self.socket.settimeout(5)
				response = self.socket.recv(128)
				if response and len(response) > 0:
					print('WiFi location sent successfully ({} networks)'.format(wifi_count))
					return True
				else:
					print('No server response')
					return True
			except:
				return True
		except Exception as e:
			print('Send WiFi location error:', e)
			self.connected = False
			return False

	def _calculate_crc(self, data):
		"""Calculate CRC16-IBM"""
		crc = 0xFFFF
		for byte in data:
			crc ^= byte
			for _ in range(8):
				if crc & 0x0001:
					crc = (crc >> 1) ^ 0xA001
				else:
					crc >>= 1
		return crc
