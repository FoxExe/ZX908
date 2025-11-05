from machine import Pin
from misc import Power
import utime
import _thread
import gc
import net
import dataCall
import checkNet
import modem

# Import tracker modules
from config import Config
from led_controller import Leds, Led
from gps_controller import GPSController
from wifi_location import WiFiLocation
from battery import BatteryMonitor
from sms_handler import SMSHandler
from call_handler import CallHandler
from data_buffer import DataBuffer

# Import protocols
from gt06_protocol import GT06Protocol
from http_protocol import HTTPProtocol


class GPSTracker:
	"""Main GPS Tracker class"""

	def __init__(self):
		print('Initializing GPS Tracker...')

		# Load configuration
		self.config = Config()

		# Initialize LEDs
		self.leds = Leds(red_pin=15, blue_pin=16, yellow_pin=17)
		self.leds.set_battery_status(Led.MODE_ON)  # Device is running

		# Initialize battery monitor
		self.battery = BatteryMonitor()

		# Initialize GPS
		self.gps = GPSController(power_pin=10)

		# Initialize WiFi location
		self.wifi_location = WiFiLocation()
		wifi_server = self.config.get('wifi_server')
		if wifi_server:
			self.wifi_location.set_custom_server(
				wifi_server['host'],
				wifi_server['port'],
				wifi_server['path']
			)

		# Initialize SMS and call handlers
		self.sms_handler = SMSHandler(self.config, self._config_callback)
		self.call_handler = CallHandler(self.config)

		# Data buffer
		self.data_buffer = DataBuffer()

		# Communication protocol
		self.protocol = None
		self._init_protocol()

		# Tracker state
		self.running = True
		self.sleep_mode = False
		self.last_movement_time = utime.time()
		self.last_location = None
		self.connected = False
		self.gps_available = False
		self.use_wifi_fallback = True

		# Start threads
		_thread.start_new_thread(self._main_loop, ())
		_thread.start_new_thread(self._battery_monitor_loop, ())

		print('GPS Tracker initialized')

	def _init_protocol(self):
		"""Initialize communication protocol"""
		server = self.config.get('server')
		if server and server['host'] and server['port']:
			protocol_type = server['protocol'].upper()

			if protocol_type == 'GT06':
				self.protocol = GT06Protocol(
					server['host'],
					server['port'],
					self.leds
				)
			elif protocol_type == 'HTTP':
				self.protocol = HTTPProtocol(
					server['host'],
					server['port'],
					server.get('path', '/api/location'),
					self.leds
				)
			else:
				print('Unknown protocol:', protocol_type)
				self.protocol = None
		else:
			self.protocol = None
			print('Server not configured')

	def _config_callback(self, event):
		"""Callback on configuration change"""
		if event in ['apn_changed', 'server_changed']:
			print('Configuration changed, reinitializing...')
			self._init_network()
			self._init_protocol()
		elif event == 'interval_changed':
			print('Update interval changed')
		elif event == 'wifi_server_changed':
			print('WiFi location server changed')
			wifi_server = self.config.get('wifi_server')
			if wifi_server:
				self.wifi_location.set_custom_server(
					wifi_server['host'],
					wifi_server['port'],
					wifi_server['path']
				)
		elif event == 'get_status':
			return self._get_status()
		elif event == 'poweroff':
			self._poweroff()

	def _init_network(self):
		"""Initialize network connection"""
		try:
			# Check SIM card
			checkNet.waitNetworkReady(30)

			# Configure APN
			apn_config = self.config.get('apn')
			if apn_config['name']:
				dataCall.setApn(
					1,
					0,
					apn_config['name'],
					apn_config['user'],
					apn_config['password'],
					0
				)

			# Activate PDP context
			dataCall.setCallback(self._datacall_callback)
			ret = dataCall.activate(1)

			print('Network initialized, PDP active:', ret == 0)
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
		else:
			print('Network disconnected')

	def _main_loop(self):
		"""Main tracker loop"""
		# Initialize network
		self._init_network()

		# Enable GPS
		self.gps.enable()
		self.leds.set_gps_status(Led.MODE_BLINK_1HZ)  # Searching for satellites

		update_interval = self.config.get('update_interval', 10)
		last_update = 0
		gps_wait_time = 0
		max_gps_wait = 60  # Wait max 60 seconds for GPS before trying WiFi

		while self.running:
			try:
				current_time = utime.time()

				# Check sleep mode
				if self._check_sleep_mode():
					self._enter_sleep_mode()
					utime.sleep(10)
					continue

				# Exit sleep mode if needed
				if self.sleep_mode:
					self._exit_sleep_mode()

				# Update GPS status LED
				if self.gps.is_valid():
					self.leds.set_gps_status(Led.MODE_ON)
					self.gps_available = True
					gps_wait_time = 0
				else:
					self.leds.set_gps_status(Led.MODE_BLINK_1HZ)
					gps_wait_time += 1
					self.gps_available = False

				# Send location data at configured interval
				if current_time - last_update >= update_interval:
					self._send_location_data()
					last_update = current_time

				# Send buffered data if connected
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

			# Try GPS first
			if self.gps_available:
				location = self.gps.get_location()

			# Fallback to WiFi location if GPS unavailable
			if not location or not location.get('valid'):
				if self.use_wifi_fallback:
					print('GPS unavailable, trying WiFi location...')
					location = self.wifi_location.get_location()
					if location:
						print('Using WiFi location')

			if not location or not location.get('valid'):
				print('No valid location data available')
				return

			# Check for movement
			if self._detect_movement(location):
				self.last_movement_time = utime.time()

			# Prepare data packet
			data = {
				'timestamp': utime.time(),
				'latitude': location['latitude'],
				'longitude': location['longitude'],
				'altitude': location.get('altitude', 0.0),
				'speed': location.get('speed', 0.0),
				'course': location.get('course', 0.0),
				'satellites': location.get('satellites', 0),
				'battery': self.battery.get_percentage(),
				'charging': self.battery.is_charging,
				'valid': location.get('valid', False),
				'source': location.get('source', 'gps'),
				'accuracy': location.get('accuracy', 0)
			}

			# Send via protocol
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
					# Buffer data on failure
					if self.config.get('buffer_enabled'):
						if self.data_buffer.add(data):
							print('Data buffered, size:', self.data_buffer.size())
						else:
							print('Buffer full, data lost')
			else:
				# No server configured - only buffer
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

		# Check speed (>1 km/h = movement)
		if location.get('speed', 0) > 1.0:
			return True

		# Check coordinate change
		lat_diff = abs(location['latitude'] - self.last_location['latitude'])
		lon_diff = abs(location['longitude'] - self.last_location['longitude'])

		# Movement detected if change > 0.0001 degrees (~11 meters)
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

			# Disable GPS
			self.gps.disable()
			self.leds.set_gps_status(Led.MODE_OFF)

			# Disable WiFi
			self.wifi_location.disable()

			# Update indicators
			self.leds.set_network_status(Led.MODE_OFF)
			self.leds.set_battery_status(Led.MODE_BLINK_SLOW)

			# Disconnect from server
			if self.protocol:
				self.protocol.disconnect()

			# Reduce power consumption
			print('Sleep mode active')

	def _exit_sleep_mode(self):
		"""Exit sleep mode"""
		if self.sleep_mode:
			print('Exiting sleep mode')
			self.sleep_mode = False

			# Enable GPS
			self.gps.enable()
			self.leds.set_gps_status(Led.MODE_BLINK_1HZ)

			# Restore battery indicator
			self._update_battery_led()

			# Reconnect to server
			if self.protocol:
				self.protocol.connect()

			self.last_movement_time = utime.time()
			print('Sleep mode exited')

	def _battery_monitor_loop(self):
		"""Battery monitoring loop"""
		while self.running:
			try:
				# Update battery status
				self.battery.update()

				# Update battery LED (if not in sleep mode)
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
		status += 'Battery: {}%{}\n'.format(
			self.battery.get_percentage(),
			' (Charging)' if self.battery.is_charging else ''
		)
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

		# Memory info
		gc.collect()
		status += 'Memory free: {} bytes'.format(gc.mem_free())

		return status

	def _poweroff(self):
		"""Power off device"""
		print('Powering off device...')

		try:
			# Save any pending data
			self.config.save()

			# Cleanup
			self.cleanup()

			# Power off
			utime.sleep(1)
			Power.powerDown()
		except Exception as e:
			print('Poweroff error:', e)

	def cleanup(self):
		"""Cleanup resources"""
		print('Cleaning up...')
		self.running = False

		# Stop GPS
		self.gps.disable()

		# Stop WiFi
		self.wifi_location.disable()

		# Stop LEDs
		self.leds.cleanup()

		# Disconnect protocol
		if self.protocol:
			self.protocol.disconnect()

		print('Cleanup complete')


# Main entry point
if __name__ == '__main__':
	try:
		print('=== GPS Tracker Starting ===')
		print('QuecPython Version: 3.4.0')
		print('Module: Quectel EC800N')

		# Get device info
		imei = modem.getDevImei()
		print('IMEI:', imei)

		# Start tracker
		tracker = GPSTracker()

		# Keep main thread alive
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

		# Try to cleanup
		try:
			tracker.cleanup()
		except:
			pass
