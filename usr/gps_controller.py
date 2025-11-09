from machine import Pin, UART
import utime
import _thread
import ntptime
from gnss import GNSS


class GPSController:
	"""GPS controller using GNSS module"""

	def __init__(self, gnss_port, gnss_power_pin):
		self.gnss = GNSS(gnss_port, 9600, 8, 0, 1, 0)
		self.power_pin = Pin(gnss_power_pin, Pin.OUT, Pin.PULL_DISABLE, 0)
		self.enabled = False
		self.last_sync_time = 0
		self.lock = _thread.allocate_lock()

	def enable(self):
		"""Enable GPS module"""
		try:
			self.power_pin.write(1)
			self.enabled = True
			print('GPS enabled')
			return True
		except Exception as e:
			print('GPS enable error:', e)
			return False

	def disable(self):
		"""Disable GPS module"""
		try:
			self.power_pin.write(0)
			self.enabled = False
			print('GPS disabled')
		except Exception as e:
			print('GPS disable error:', e)

	def is_valid(self):
		"""Check if GPS has valid fix"""
		# TODO: Add last update time check!
		return self.enabled and self.isFix()

	def get_course(self):
		rmc_data = self.gnss.getRMC()
		if rmc_data != -1 and rmc_data[2] == "A":
			try:
				return int(rmc_data[7])
			except ValueError:
				pass
		return 0

	def get_accuracy(self):
		data = self.gnss.getGGA()
		# data = ['$GNGGA', '103416.000', '5000.12345', 'N', '05000.12345', 'E', '1', '10', '1.5', '13.8', 'M', '-11.1', 'M', '', '*50']
		if data:
			return float(data[8])
		else:
			return -1

	def get_date(self):
		data = self.gnss.getRMC()
		# data = ['$GNRMC', '103416.000', 'A', '5322.44671', 'N', '05858.01250', 'E', '0.00', '16.51', '091125', '', '', 'A', 'V*36']
		if data and data[9]:
			return (int(data[9][0:2]), int(data[9][2:4]), int('20' + data[9][4:6]))
		else:
			return None

	def get_time(self):
		data = self.gnss.getRMC()
		if data and data[1]:
			return (int(data[1][0:2]), int(data[1][2:4]), int('20' + data[1][4:6]))
		else:
			return None

	def get_datetime(self):
		return "%02d.%02d.%d" % self.get_date() + " %02d:%02d:%02d" % self.get_time()

	def get_satellites_info(self):
		data = self.gnss.getGSV()
		if not data or len(data) == 0:
			return []
		"""
		Example:
		data = (
			['$GPGSV', '4', '1', '13', '05', '21', '278', '', '07', '65', '105', '23', '08', '39', '067', '23', '09', '13', '161', '', '0*67'],
			['$GPGSV', '4', '2', '13', '13', '33', '307', '14', '14', '45', '226', '', '15', '09', '323', '', '20', '07', '250', '', '0*6D'],
			['$GPGSV', '4', '3', '13', '21', '17', '246', '', '22', '28', '226', '', '27', '18', '039', '18', '30', '83', '273', '', '0*68'],
			['$GPGSV', '4', '4', '13', '194', '28', '069', '27', '0*6B']
		)
		"""
		sat_info = []
		for msg in data:
			# Start from 4th element (Skipping sat_type, msg_count, msg_num, sat_count)
			sats_in_msg = int((len(msg) - 5) / 4)
			for i in range(sats_in_msg):
				info = msg[4 + (i * 4): 4 + (i * 4) + 4]

				number = int(info[0])
				elevation = int(info[1])
				azimuth = int(info[2])
				signal = int(info[3]) if info[3] else -1
				sat_info.append((number, elevation, azimuth, signal))

		return sat_info

	def isFix(self):
		rmc = self.gnss.getRMC()
		if rmc != -1 and rmc[2] == "A":
			return True
		else:
			return False

	def get_location(self):
		"""Get current GPS location"""
		if not self.enabled:
			return None
		try:
			ret = self.gnss.readAndParse()
			if ret == 0 or not self.isFix():
				return {'valid': False}

			lat, lat_dir, lon, lon_dir = self.gnss.getLocation()
			return {
				'valid': True,
				'latitude': lat,
				'longitude': lon,
				'altitude': self.gnss.getAltitude(),
				'speed': self.gnss.getSpeed(),
				'course': self.get_course(),
				'satellites': self.gnss.getUsedSateCnt(),
				'source': 'gps',
				'accuracy': self.get_accuracy(),
				'timestamp': utime.time()
			}
		except Exception as e:
			print('Get location error:', e)
			return {'valid': False}

	def sync_rtc(self, force=False):
		"""Sync RTC with GPS time (once per week unless forced)"""
		if not self.is_valid():
			return False

		current_time = utime.time()
		week_seconds = 7 * 24 * 3600
		if not force and (current_time - self.last_sync_time) < week_seconds:
			return False
		try:
			day, month, year = self.get_date()
			hour, minute, second = self.get_time()
			ntptime.settime(0, (year, month, day, hour, minute, second, 0, 0))
			self.last_sync_time = current_time
			print('RTC synced with GPS time: {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(year, month, day, hour, minute, second))
			return True
		except Exception as e:
			print('RTC sync error:', e)
		return False
