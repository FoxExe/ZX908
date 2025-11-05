from machine import Pin, Timer
import _thread
import utime


class Led:
	"""Single LED controller class"""

	# LED modes
	MODE_OFF = 0
	MODE_ON = 1
	MODE_BLINK_1HZ = 2  # 1 time per second (500ms on, 500ms off)
	MODE_BLINK_4HZ = 3  # 4 times per second (125ms on, 125ms off)
	MODE_BLINK_SLOW = 4  # 1 time per 5 seconds (500ms flash)
	MODE_BLINK_CONNECT = 5  # 250ms on, 750ms off
	MODE_PULSE = 6  # Manual control for data transmission

	def __init__(self, pin_num, name=''):
		self.pin = Pin(pin_num, Pin.OUT, Pin.PULL_DISABLE, 0)
		self.name = name
		self.mode = self.MODE_OFF
		self.state = False
		self.pulse_active = False
		self.pulse_timer = None

	def set_mode(self, mode):
		"""Set LED mode"""
		self.mode = mode
		if mode == self.MODE_OFF:
			self.pin.write(0)
			self.state = False
		elif mode == self.MODE_ON:
			self.pin.write(1)
			self.state = True

	def pulse_start(self, min_duration_ms=100):
		"""Start pulse (for data transmission indication)"""
		if self.mode == self.MODE_PULSE:
			self.pulse_active = True
			self.pin.write(1)
			self.state = True
			# Ensure minimum duration
			if self.pulse_timer:
				self.pulse_timer.stop()

	def pulse_stop(self, delay_ms=100):
		"""Stop pulse with delay"""
		if self.mode == self.MODE_PULSE:
			# Delay before turning off
			if self.pulse_timer:
				self.pulse_timer.stop()
			self.pulse_timer = Timer(Timer.Timer1)
			self.pulse_timer.start(period=delay_ms, mode=Timer.ONE_SHOT, callback=lambda t: self._pulse_off())

	def _pulse_off(self):
		"""Turn off pulse"""
		self.pulse_active = False
		self.pin.write(0)
		self.state = False

	def update(self, counter_ms):
		"""Update LED state based on mode and counter"""
		if self.mode == self.MODE_BLINK_1HZ:
			self.pin.write(1 if (counter_ms % 1000) < 500 else 0)
		elif self.mode == self.MODE_BLINK_4HZ:
			self.pin.write(1 if (counter_ms % 250) < 125 else 0)
		elif self.mode == self.MODE_BLINK_SLOW:
			self.pin.write(1 if (counter_ms % 5000) < 500 else 0)
		elif self.mode == self.MODE_BLINK_CONNECT:
			self.pin.write(1 if (counter_ms % 1000) < 250 else 0)

	def cleanup(self):
		"""Cleanup resources"""
		if self.pulse_timer:
			self.pulse_timer.stop()
		self.pin.write(0)


class Leds:
	"""LED controller for all LEDs"""

	def __init__(self, red_pin=15, blue_pin=16, yellow_pin=17):
		self.red = Led(red_pin, 'red')  # GPS status
		self.blue = Led(blue_pin, 'blue')  # Network status
		self.yellow = Led(yellow_pin, 'yellow')  # Battery status

		self.running = True
		self.lock = _thread.allocate_lock()

		# Start blink thread
		_thread.start_new_thread(self._blink_thread, ())

	def _blink_thread(self):
		"""Thread for LED blinking control"""
		counter = 0

		while self.running:
			with self.lock:
				self.red.update(counter)
				self.blue.update(counter)
				self.yellow.update(counter)

			utime.sleep_ms(50)
			counter = (counter + 50) % 5000

	def set_gps_status(self, mode):
		"""Set GPS status LED (red)"""
		with self.lock:
			self.red.set_mode(mode)

	def set_network_status(self, mode):
		"""Set network status LED (blue)"""
		with self.lock:
			self.blue.set_mode(mode)

	def set_battery_status(self, mode):
		"""Set battery status LED (yellow)"""
		with self.lock:
			self.yellow.set_mode(mode)

	def network_data_start(self):
		"""Indicate data transmission start"""
		with self.lock:
			if self.blue.mode == Led.MODE_PULSE:
				self.blue.pulse_start()

	def network_data_stop(self):
		"""Indicate data transmission stop"""
		with self.lock:
			if self.blue.mode == Led.MODE_PULSE:
				self.blue.pulse_stop()

	def cleanup(self):
		"""Cleanup all LEDs"""
		self.running = False
		utime.sleep_ms(100)
		with self.lock:
			self.red.cleanup()
			self.blue.cleanup()
			self.yellow.cleanup()
