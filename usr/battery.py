from misc import Power, USB


# Voltage to percentage lookup table (in volts)
VOLTAGE_TABLE = [
	(4.143, 100), (4.079, 95), (4.023, 90), (3.972, 85), (3.923, 80),
	(3.876, 75), (3.831, 70), (3.790, 65), (3.754, 60), (3.720, 55),
	(3.680, 50), (3.652, 45), (3.634, 40), (3.621, 35), (3.608, 30),
	(3.595, 25), (3.579, 20), (3.548, 15), (3.511, 10), (3.468, 5),
	(3.430, 0), (3.100, 0)
]


class BatteryMonitor:
	"""Battery monitoring with accurate percentage calculation"""

	def __init__(self):
		self.usb = USB()
		self.percent = 100
		self.is_charging = False
		self.voltage = 0.0

	def update(self):
		"""Update battery status"""
		try:
			# Get battery voltage (in mV)
			voltage_mv = Power.getVbatt()
			if voltage_mv:
				self.voltage = voltage_mv / 1000.0  # Convert to volts
				self.percent = self._calculate_percentage(self.voltage)

			# Check charging status
			charge_status = self.usb.getStatus()
			self.is_charging = (charge_status == 1)

			return True
		except Exception as e:
			print('Battery update error:', e)
			return False

	def _calculate_percentage(self, voltage):
		"""Calculate battery percentage from voltage using lookup table"""
		# Below minimum voltage
		if voltage <= VOLTAGE_TABLE[-1][0]:
			return 0

		# Above maximum voltage
		if voltage >= VOLTAGE_TABLE[0][0]:
			return 100

		# Find the two closest points in the table
		for i in range(len(VOLTAGE_TABLE) - 1):
			v_high, p_high = VOLTAGE_TABLE[i]
			v_low, p_low = VOLTAGE_TABLE[i + 1]

			if v_low <= voltage <= v_high:
				# Linear interpolation between two points
				if v_high == v_low:
					return p_high

				percent = p_low + (voltage - v_low) * (p_high - p_low) / (v_high - v_low)
				return max(0, min(100, int(percent)))

		return 0

	def get_percentage(self):
		"""Get battery percentage"""
		return self.percent

	def is_low(self, threshold=20):
		"""Check if battery is low"""
		return self.percent < threshold
