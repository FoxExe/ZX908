from misc import Power, USB


class BatteryMonitor:
	"""Battery monitoring with accurate voltage-to-percentage conversion"""

	VOLTAGE_TABLE = [
		(4.143, 100), (4.079, 95), (4.023, 90), (3.972, 85), (3.923, 80), (3.877, 75), (3.837, 70),
		(3.804, 65), (3.774, 60), (3.748, 55), (3.722, 50), (3.695, 45), (3.670, 40), (3.647, 35),
		(3.626, 30), (3.607, 25), (3.587, 20), (3.563, 15), (3.529, 10), (3.477, 5), (3.430, 0), (3.100, 0)]

	def __init__(self):
		self.voltage = 0.0
		self.percentage = 0
		self.is_charging = False
		self.usb = USB()
		self.update()

	def update(self):
		"""Update battery status"""
		try:
			self.voltage = Power.getVbatt() / 1000.0
			self.percentage = self._voltage_to_percentage(self.voltage)
			usb_status = self.usb.getStatus()
			self.is_charging = (usb_status == 1)
		except Exception as e:
			print('Battery update error:', e)

	def _voltage_to_percentage(self, voltage):
		"""Convert voltage to percentage using interpolation"""
		if voltage >= self.VOLTAGE_TABLE[0][0]:
			return 100
		if voltage <= self.VOLTAGE_TABLE[-1][0]:
			return 0
		for i in range(len(self.VOLTAGE_TABLE) - 1):
			v_high, p_high = self.VOLTAGE_TABLE[i]
			v_low, p_low = self.VOLTAGE_TABLE[i + 1]
			if v_low <= voltage <= v_high:
				percentage = p_low + (voltage - v_low) * (p_high - p_low) / (v_high - v_low)
				return int(percentage)
		return 0

	def get_percentage(self):
		"""Get battery percentage"""
		return self.percentage

	def get_voltage(self):
		"""Get battery voltage"""
		return self.voltage

	def is_low(self, threshold=20):
		"""Check if battery is low"""
		return self.percentage < threshold
