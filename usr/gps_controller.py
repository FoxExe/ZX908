from machine import Pin, RTC, UART
from gnss import GnssGetData
import utime


GPS_PORT = UART.UART2
ENABLE_PIN = Pin.GPIO10


class GPSController:
	"""GPS controller with power management and RTC sync"""

	def __init__(self, power_pin=ENABLE_PIN):
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
				self.gnss = GnssGetData(GPS_PORT, 9600, 8, 0, 1, 0)  # UART2, 9600 baud
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
		if not self.gnss or not self.gnss.isFix():
			return None

		try:
			# Get location data from GNSS module
			if self.gnss.read_gnss_data() > 0:
				# (longitude, lon_direction, latitude, lat_direction) or -1
				longitude, lon_direction, latitude, lat_direction = self.gnss.getLocation()
				return {
					'valid': self.gnss.checkDataValidity() == (1, 1, 1),  # (gga_valid, rmc_valid, gsv_valid)
					'timestamp': utime.time(),
					'latitude': latitude,
					'longitude': longitude,
					'altitude': self.gnss.getAltitude(),  # In docs its "getGeodeticHeight", but not in firmware.
					'speed': self.gnss.getSpeed(),  # km/h
					'course': self.gnss.getCourse(),
					'satellites': self.gnss.getUsedSateCnt()  # getUsedSateCnt / getViewSateCnt
				}
			return None
		except Exception as e:
			print('Get location error:', e)
			return None

	def is_valid(self):
		"""Check if GPS data is valid"""
		loc = self.get_location()
		return loc is not None and loc.get('valid', False)
