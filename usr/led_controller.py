from machine import Pin
import _thread
import utime


class Led:
	"""Single LED controller with various modes"""

	MODE_OFF = 0
	MODE_ON = 1
	MODE_BLINK_SLOW = 2
	MODE_BLINK_1HZ = 3
	MODE_BLINK_4HZ = 4
	MODE_BLINK_CONNECT = 5
	MODE_PULSE = 6

	def __init__(self, pin_num):
		self.pin = Pin(pin_num, Pin.OUT, Pin.PULL_DISABLE, 0)
		self.mode = self.MODE_OFF
		self.running = False
		self.thread_started = False
		self.lock = _thread.allocate_lock()

	def set_mode(self, mode):
		"""Set LED mode"""
		with self.lock:
			self.mode = mode
			if not self.thread_started and mode != self.MODE_OFF:
				self.running = True
				self.thread_started = True
				_thread.start_new_thread(self._led_thread, ())

	def _led_thread(self):
		"""LED control thread"""
		pulse_step = 0
		while self.running:
			with self.lock:
				current_mode = self.mode

			if current_mode == self.MODE_OFF:
				self.pin.write(0)
				utime.sleep_ms(100)
			elif current_mode == self.MODE_ON:
				self.pin.write(1)
				utime.sleep_ms(100)
			elif current_mode == self.MODE_BLINK_SLOW:
				self.pin.write(1)
				utime.sleep_ms(500)
				self.pin.write(0)
				utime.sleep(5)
			elif current_mode == self.MODE_BLINK_1HZ:
				self.pin.write(1)
				utime.sleep_ms(500)
				self.pin.write(0)
				utime.sleep_ms(500)
			elif current_mode == self.MODE_BLINK_4HZ:
				self.pin.write(1)
				utime.sleep_ms(125)
				self.pin.write(0)
				utime.sleep_ms(125)
			elif current_mode == self.MODE_BLINK_CONNECT:
				self.pin.write(1)
				utime.sleep_ms(250)
				self.pin.write(0)
				utime.sleep_ms(750)
			elif current_mode == self.MODE_PULSE:
				duty_cycle = [0, 10, 30, 60, 100, 60, 30, 10]
				for duty in duty_cycle:
					if duty > 0:
						on_time = int(10 * duty / 100)
						off_time = 10 - on_time
						self.pin.write(1)
						utime.sleep_ms(on_time)
						self.pin.write(0)
						utime.sleep_ms(off_time)
					else:
						self.pin.write(0)
						utime.sleep_ms(10)

	def cleanup(self):
		"""Cleanup LED"""
		self.running = False
		self.pin.write(0)


class Leds:
	"""LED controller for all status indicators"""

	def __init__(self, red_pin, blue_pin, yellow_pin):
		self.red_led = Led(red_pin)
		self.blue_led = Led(blue_pin)
		self.yellow_led = Led(yellow_pin)
		self.data_blink_active = False

	def set_gps_status(self, mode):
		"""Set GPS status LED (red)"""
		self.red_led.set_mode(mode)

	def set_network_status(self, mode):
		"""Set network status LED (blue)"""
		if not self.data_blink_active:
			self.blue_led.set_mode(mode)

	def set_battery_status(self, mode):
		"""Set battery status LED (yellow)"""
		self.yellow_led.set_mode(mode)

	def network_data_start(self):
		"""Start data transmission indicator"""
		self.data_blink_active = True
		self.blue_led.set_mode(Led.MODE_BLINK_4HZ)

	def network_data_stop(self):
		"""Stop data transmission indicator"""
		self.data_blink_active = False
		self.blue_led.set_mode(Led.MODE_PULSE)

	def cleanup(self):
		"""Cleanup all LEDs"""
		self.red_led.cleanup()
		self.blue_led.cleanup()
		self.yellow_led.cleanup()
