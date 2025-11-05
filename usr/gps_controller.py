from machine import Pin
import utime
from gnss import GnssGetData
from machine import RTC


class GPSController:
	"""GPS controller with power management and RTC sync"""

	def __init__(self, power_pin=10):
		self.power_pin = Pin(power_pin, Pin.OUT, Pin.PULL_DISABLE, 0)
		self.gnss = None
		self.enabled = False
		self.rtc_synced = False

	def enable(self):
		"""Enable GPS module"""
		if not self.enabled:
			self.power_pin.write(1)
			utime.sleep_ms(500)  # Wait for power stabilization

			try:
				# Initialize GNSS
				self.gnss = GnssGetData(2, 9600, 8, 0, 1, 0)  # UART2, 9600 baud
				self.enabled = True
				print('GPS enabled')
			except Exception as e:
				print('GPS enable error:', e)
				self.power_pin.write(0)
				return False

		return True

	def disable(self):
		"""Disable GPS module"""
		if self.enabled:
			if self.gnss:
				try:
					del self.gnss
				except:
					pass
				self.gnss = None
			self.power_pin.write(0)
			self.enabled = False
			self.rtc_synced = False
			print('GPS disabled')

	def get_location(self):
		"""Get current location data"""
		if not self.gnss:
			return None

		try:
			# Get location data from GNSS module
			loc_data = self.gnss.read_gnss_data()

			if loc_data:
				# Sync RTC with GPS time if not done yet
				if not self.rtc_synced and loc_data[1]:  # Check if time is valid
					self._sync_rtc(loc_data)

				return self._parse_location(loc_data)

			return None
		except Exception as e:
			print('Get location error:', e)
			return None

	def _parse_location(self, loc_data):
		"""Parse location data from GNSS module"""
		try:
			# loc_data format varies, adapt based on actual GnssGetData output
			# Typically: [fix_status, utc_time, latitude, longitude, altitude, speed, course, satellites]

			return {
				'valid': loc_data[0] if len(loc_data) > 0 else False,
				'timestamp': loc_data[1] if len(loc_data) > 1 else '',
				'latitude': float(loc_data[2]) if len(loc_data) > 2 else 0.0,
				'longitude': float(loc_data[3]) if len(loc_data) > 3 else 0.0,
				'altitude': float(loc_data[4]) if len(loc_data) > 4 else 0.0,
				'speed': float(loc_data[5]) if len(loc_data) > 5 else 0.0,
				'course': float(loc_data[6]) if len(loc_data) > 6 else 0.0,
				'satellites': int(loc_data[7]) if len(loc_data) > 7 else 0
			}
		except Exception as e:
			print('Parse location error:', e)
			return None

	def _sync_rtc(self, loc_data):
		"""Sync RTC with GPS time"""
		try:
			# Parse GPS time (format: HHMMSS.SSS)
			if len(loc_data) > 1 and loc_data[1]:
				gps_time = str(loc_data[1])

				# Parse time components
				hour = int(gps_time[0:2])
				minute = int(gps_time[2:4])
				second = int(gps_time[4:6])

				# Get date from GPS (this might be in a different field)
				# Assuming date is available in the GNSS data
				year = 2024  # Default or parse from GPS
				month = 1
				day = 1

				# Set RTC
				rtc = RTC()
				rtc.datetime((year, month, day, 0, hour, minute, second, 0))

				self.rtc_synced = True
				print('RTC synced with GPS time:', hour, minute, second)
		except Exception as e:
			print('RTC sync error:', e)

	def is_valid(self):
		"""Check if GPS data is valid"""
		loc = self.get_location()
		return loc is not None and loc.get('valid', False)
