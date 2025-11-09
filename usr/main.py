import utime
import _thread
import gc
import net
import dataCall
import checkNet
import ntptime
import modem
from machine import Pin, UART
from misc import Power

from usr.config import Config
from usr.led_controller import Leds, Led
from usr.gps_controller import GPSController
from usr.wifi_scanner import WiFiScanner
from usr.battery import BatteryMonitor
from usr.sms_handler import SMSHandler
from usr.data_buffer import DataBuffer
from usr.gt06_protocol import GT06Protocol
from usr.http_protocol import HTTPProtocol


GNSS_PORT = UART.UART2
GNSS_PIN = Pin.GPIO10


class GPSTracker:
	"""Main GPS Tracker class"""

	def __init__(self):
		print('Initializing GPS Tracker...')
		self.config = Config()
		self.leds = Leds(red_pin=15, blue_pin=16, yellow_pin=17)
		self.leds.set_battery_status(Led.MODE_ON)
		self.battery = BatteryMonitor()
		self.gps = GPSController(GNSS_PORT, GNSS_PIN)
		self.wifi_scanner = WiFiScanner()
		self.sms_handler = SMSHandler(self.config, self._config_callback)
		self.data_buffer = DataBuffer()
		self.protocol = None
		self._init_protocol()
		self.running = True
		self.sleep_mode = False
		self.last_movement_time = utime.time()
		self.last_location = None
		self.connected = False
		self.gps_available = False
		self.ntp_synced = False
		_thread.start_new_thread(self._main_loop, ())
		_thread.start_new_thread(self._battery_monitor_loop, ())
		print('GPS Tracker initialized')

	def _init_protocol(self):
		"""Initialize communication protocol"""
		server = self.config.get('server')
		if server and server['host'] and server['port']:
			protocol_type = server['protocol'].upper()
			if protocol_type == 'GT06':
				self.protocol = GT06Protocol(server['host'], server['port'], self.leds)
			elif protocol_type == 'HTTP':
				self.protocol = HTTPProtocol(server['host'], server['port'], server.get('path', '/api/location'), self.leds)
			else:
				print('Unknown protocol:', protocol_type)
				self.protocol = None
		else:
			self.protocol = None
			print('Server not configured')

	def _config_callback(self, event, *args):
		"""Callback on configuration change"""
		if event in ['apn_changed', 'server_changed']:
			print('Configuration changed, reinitializing...')
			self._init_network()
			self._init_protocol()
		elif event == 'interval_changed':
			print('Update interval changed')
		elif event == 'wifi_server_changed':
			print('WiFi location server changed')
		elif event == 'get_status':
			return self._get_status()
		elif event == 'poweroff':
			self._poweroff()
		elif event == 'reset':
			self._reset()

	def _init_network(self):
		"""Initialize network connection"""
		try:
			checkNet.waitNetworkReady(30)
			apn_config = self.config.get('apn')
			if apn_config['name']:
				dataCall.setApn(1, 0, apn_config['name'], apn_config['user'], apn_config['password'], 0)
			dataCall.setCallback(self._datacall_callback)
			ret = dataCall.activate(1)
			print('Network initialized, PDP active:', ret == 0)
			if ret == 0 and not self.ntp_synced:
				self._sync_ntp()
			return ret == 0
		except Exception as e:
			print('Network init error:', e)
			return False

	def _datacall_callback(self, args):
		"""Callback on PDP context state change"""
		pdp_id = args[0]
		status = args[1]
		print('PDP context', pdp_id, 'status:', status)
		if status == 1:
			print('Network connected')
			if not self.ntp_synced:
				self._sync_ntp()
		else:
			print('Network disconnected')

	def _sync_ntp(self):
		"""Sync time via NTP"""
		try:
			print('Syncing time via NTP...')
			ntptime.host = 'pool.ntp.org'
			ntptime.settime()
			self.ntp_synced = True
			print('NTP time synced')
		except Exception as e:
			print('NTP sync error:', e)

	def _main_loop(self):
		"""Main tracker loop"""
		self._init_network()
		self.gps.enable()
		self.leds.set_gps_status(Led.MODE_BLINK_1HZ)
		update_interval = self.config.get('update_interval', 10)
		last_update = 0
		while self.running:
			try:
				current_time = utime.time()
				if self._check_sleep_mode():
					self._enter_sleep_mode()
					utime.sleep(10)
					continue
				if self.sleep_mode:
					self._exit_sleep_mode()
				if self.gps.is_valid():
					self.leds.set_gps_status(Led.MODE_ON)
					self.gps_available = True
					if not self.sleep_mode:
						self.gps.sync_rtc()
				else:
					self.leds.set_gps_status(Led.MODE_BLINK_1HZ)
					self.gps_available = False
				if current_time - last_update >= update_interval:
					self._send_location_data()
					last_update = current_time
				if self.connected and self.data_buffer.size() > 0:
					self._send_buffered_data()
				utime.sleep(1)
			except Exception as e:
				print('Main loop error:', e)
				utime.sleep(5)

	def _send_location_data(self):
		"""Send location data"""
		try:
			location = None
			wifi_networks = []
			if self.gps_available:
				location = self.gps.get_location()
			if not location or not location.get('valid'):
				wifi_enabled = self.config.get('wifi_location_enabled', False)
				if wifi_enabled:
					print('GPS unavailable, scanning WiFi networks...')
					wifi_networks = self.wifi_scanner.scan_networks()
					if wifi_networks and len(wifi_networks) > 0:
						print('Found {} WiFi networks'.format(len(wifi_networks)))
						location = {'valid': False, 'latitude': 0.0, 'longitude': 0.0, 'altitude': 0.0,
                                                    'speed': 0.0, 'course': 0.0, 'satellites': 0, 'source': 'wifi', 'accuracy': 0}
			if not location:
				print('No location data available')
				return
			if self._detect_movement(location):
				self.last_movement_time = utime.time()
			data = {'timestamp': utime.time(), 'latitude': location['latitude'], 'longitude': location['longitude'], 'altitude': location.get('altitude', 0.0), 'speed': location.get('speed', 0.0), 'course': location.get('course', 0.0), 'satellites': location.get(
				'satellites', 0), 'battery': self.battery.get_percentage(), 'charging': self.battery.is_charging, 'valid': location.get('valid', False), 'source': location.get('source', 'gps'), 'accuracy': location.get('accuracy', 0)}
			if wifi_networks and len(wifi_networks) > 0:
				data['wifi_networks'] = wifi_networks
			if self.protocol:
				self.leds.set_network_status(Led.MODE_PULSE)
				self.leds.network_data_start()
				success = self.protocol.send_location(data)
				self.leds.network_data_stop()
				if success:
					self.connected = True
					print('Location sent successfully')
				else:
					self.connected = False
					if self.config.get('buffer_enabled'):
						if self.data_buffer.add(data):
							print('Data buffered, size:', self.data_buffer.size())
						else:
							print('Buffer full, data lost')
			else:
				if self.config.get('buffer_enabled'):
					self.data_buffer.add(data)
					print('No server, data buffered')
			self.last_location = location
		except Exception as e:
			print('Send location error:', e)

	def _send_buffered_data(self):
		"""Send buffered data"""
		try:
			buffered = self.data_buffer.get_all()
			if not buffered:
				return
			print('Sending buffered data, count:', len(buffered))
			sent_count = 0
			for data in buffered:
				self.leds.network_data_start()
				success = self.protocol.send_location(data)
				self.leds.network_data_stop()
				if success:
					sent_count += 1
				else:
					print('Failed to send buffered data, stopping')
					break
				utime.sleep_ms(100)
			if sent_count > 0:
				self.data_buffer.remove(sent_count)
				print('Sent {} buffered records'.format(sent_count))
		except Exception as e:
			print('Send buffered data error:', e)

	def _detect_movement(self, location):
		"""Detect movement based on location change"""
		if not self.last_location:
			return True
		if location.get('speed', 0) > 1.0:
			return True
		lat_diff = abs(location['latitude'] - self.last_location['latitude'])
		lon_diff = abs(location['longitude'] - self.last_location['longitude'])
		if lat_diff > 0.0001 or lon_diff > 0.0001:
			return True
		return False

	def _check_sleep_mode(self):
		"""Check if should enter sleep mode"""
		if self.sleep_mode:
			return False
		sleep_timeout = self.config.get('sleep_timeout', 1800)
		idle_time = utime.time() - self.last_movement_time
		return idle_time >= sleep_timeout

	def _enter_sleep_mode(self):
		"""Enter sleep mode"""
		if not self.sleep_mode:
			print('Entering sleep mode')
			self.sleep_mode = True
			self.gps.disable()
			self.leds.set_gps_status(Led.MODE_OFF)
			self.wifi_scanner.disable()
			self.leds.set_network_status(Led.MODE_OFF)
			self.leds.set_battery_status(Led.MODE_BLINK_SLOW)
			if self.protocol:
				self.protocol.disconnect()
			print('Sleep mode active')

	def _exit_sleep_mode(self):
		"""Exit sleep mode"""
		if self.sleep_mode:
			print('Exiting sleep mode')
			self.sleep_mode = False
			self.gps.enable()
			self.leds.set_gps_status(Led.MODE_BLINK_1HZ)
			self._update_battery_led()
			if self.protocol:
				self.protocol.connect()
			self.last_movement_time = utime.time()
			print('Sleep mode exited')

	def _battery_monitor_loop(self):
		"""Battery monitoring loop"""
		while self.running:
			try:
				self.battery.update()
				if not self.sleep_mode:
					self._update_battery_led()
				utime.sleep(5)
			except Exception as e:
				print('Battery monitor error:', e)
				utime.sleep(10)

	def _update_battery_led(self):
		"""Update battery status LED"""
		if self.battery.is_charging:
			self.leds.set_battery_status(Led.MODE_BLINK_1HZ)
		elif self.battery.is_low(20):
			self.leds.set_battery_status(Led.MODE_BLINK_4HZ)
		else:
			self.leds.set_battery_status(Led.MODE_ON)

	def _get_status(self):
		"""Get device status"""
		location = self.last_location
		status = 'GPS Tracker Status:\n'
		status += 'Battery: {}%{}\n'.format(self.battery.get_percentage(), ' (Charging)' if self.battery.is_charging else '')
		status += 'Voltage: {:.2f}V\n'.format(self.battery.voltage)
		status += 'Sleep: {}\n'.format('Yes' if self.sleep_mode else 'No')
		status += 'GPS: {}\n'.format('Valid' if self.gps_available else 'Invalid')
		if location and location.get('valid'):
			status += 'Source: {}\n'.format(location.get('source', 'unknown'))
			status += 'Lat: {:.6f}\n'.format(location['latitude'])
			status += 'Lon: {:.6f}\n'.format(location['longitude'])
			status += 'Speed: {:.1f} km/h\n'.format(location.get('speed', 0))
			status += 'Sats: {}\n'.format(location.get('satellites', 0))
		status += 'Buffer: {} records\n'.format(self.data_buffer.size())
		status += 'Connected: {}\n'.format('Yes' if self.connected else 'No')
		gc.collect()
		status += 'Memory free: {} bytes'.format(gc.mem_free())
		return status

	def _poweroff(self):
		"""Power off device"""
		print('Powering off device...')
		try:
			self.config.save()
			self.cleanup()
			utime.sleep(1)
			Power.powerDown()
		except Exception as e:
			print('Poweroff error:', e)

	def _reset(self):
		"""Reset device"""
		print('Resetting device...')
		try:
			self.config.save()
			self.cleanup()
			utime.sleep(1)
			Power.powerRestart()
		except Exception as e:
			print('Reset error:', e)

	def cleanup(self):
		"""Cleanup resources"""
		print('Cleaning up...')
		self.running = False
		self.gps.disable()
		self.wifi_scanner.disable()
		self.leds.cleanup()
		if self.protocol:
			self.protocol.disconnect()
		print('Cleanup complete')


if __name__ == '__main__':
	try:
		print('=== GPS Tracker Starting ===')
		imei = modem.getDevImei()
		print('IMEI:', imei)
		tracker = GPSTracker()
		while True:
			utime.sleep(60)
			gc.collect()
			free_mem = gc.mem_free()
			total_mem = gc.mem_free() + gc.mem_alloc()
			mem_percent = (free_mem / total_mem) * 100
			print('Memory: {} bytes free ({:.1f}%)'.format(free_mem, mem_percent))
	except KeyboardInterrupt:
		print('Interrupted by user')
		tracker.cleanup()
	except Exception as e:
		print('Fatal error:', e)
		import sys
		sys.print_exception(e)
		try:
			tracker.cleanup()
		except:
			pass
