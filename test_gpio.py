from machine import Pin
from machine import UART
import utime


for pin in ('GPIO5', 'GPIO6', 'GPIO7', 'GPIO8', 'GPIO9', 'GPIO11', 'GPIO12', 'GPIO13', 'GPIO14',
            'GPIO18', 'GPIO19', 'GPIO20', 'GPIO21', 'GPIO22', 'GPIO37'):

	print("Trying", pin, end=" ")
	p = Pin(getattr(Pin, pin), Pin.IN, Pin.PULL_PU)
	utime.sleep_ms(500)
	print("UP", p.read(), end=" ")
	p = Pin(getattr(Pin, pin), Pin.IN, Pin.PULL_PD)
	utime.sleep_ms(500)
	print("DN", p.read(), end=" ")
	p = Pin(getattr(Pin, pin), Pin.IN, Pin.PULL_DISABLE)
	utime.sleep_ms(500)
	print("NO", p.read(), end=" ")
	print()
