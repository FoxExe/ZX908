
from machine import UART
from machine import Pin
import _thread
import utime


# Find NMEA/GPS power control pin


def reader(port):
	uart = UART(port, 9600, 8, 0, 1, 0)
	while True:
		size = uart.any()
		if size > 0:
			data = uart.read(size)
			print("Got data on %s: %s" % (uart, data))
		utime.sleep_ms(100)


if __name__ == '__main__':
	threads = []
	for port in (UART.UART0, UART.UART1, UART.UART2):
		threads.append(_thread.start_new_thread(reader, (port, )))

	for pin in ('GPIO5', 'GPIO6', 'GPIO7', 'GPIO8', 'GPIO9', 'GPIO10', 'GPIO11', 'GPIO12', 'GPIO13', 'GPIO14', 'GPIO18', 'GPIO19', 'GPIO20', 'GPIO21', 'GPIO22', 'GPIO37'):
		p = Pin(getattr(Pin, pin), Pin.OUT, Pin.PULL_DISABLE, 0)

		p.write(0)
		print(pin, p.read())
		utime.sleep(1)

		p.write(1)
		print(pin, p.read())
		utime.sleep(1)

	for i in range(30):
		print("Waiting...", i)
		utime.sleep(1)

	for tid in threads:
		_thread.stop_thread(tid)

	print("Done!")


# from misc import Power
# Power.powerRestart()
