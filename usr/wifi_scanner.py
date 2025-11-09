import wifiScan
import _thread
import utime


class WiFiScanner:
	"""WiFi scanner for location assistance"""

	def __init__(self):
		self.enabled = False
		self.scan_result = None
		self.scan_complete = False
		self.lock = _thread.allocate_lock()

	def enable(self):
		"""Enable WiFi module"""
		try:
			ret = wifiScan.control(1)
			if ret == 0:
				self.enabled = True
				print('WiFi scanner enabled')
				return True
			else:
				print('WiFi scanner enable failed:', ret)
				return False
		except Exception as e:
			print('WiFi enable error:', e)
			return False

	def disable(self):
		"""Disable WiFi module"""
		try:
			wifiScan.control(0)
			self.enabled = False
			print('WiFi scanner disabled')
		except Exception as e:
			print('WiFi disable error:', e)

	def scan_networks(self):
		"""Scan for nearby WiFi networks"""
		if not self.enabled:
			if not self.enable():
				return []
		try:
			self.scan_result = None
			self.scan_complete = False
			wifiScan.setCallback(self._scan_callback)
			ret = wifiScan.asyncStart()
			if ret != 0:
				print('WiFi scan start failed:', ret)
				return []
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
				count, aps = data
				wifi_list = []
				for ap_info in aps:
					mac_addr, rssi = ap_info
					wifi_list.append({'mac': mac_addr, 'signal': rssi})
					print('WiFi AP: MAC={}, RSSI={}dB'.format(mac_addr, rssi))
				self.scan_result = wifi_list
				self.scan_complete = True
		except Exception as e:
			print('Scan callback error:', e)
			self.scan_complete = True
