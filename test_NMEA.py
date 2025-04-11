from machine import Pin, UART
from gnss import GnssGetData
import utime


NMEA_PORT = UART.UART2
ENABLE_PIN = Pin.GPIO10

"""
if __name__ == '__main__':
	uart = UART(NMEA_PORT, 9600, 8, 0, 1, 0)
	en_pin = Pin(ENABLE_PIN, Pin.OUT, Pin.PULL_DISABLE, 1)

	while True:
		size = uart.any()
		if size > 0:
			data = uart.read(size)
			print(data)
		utime.sleep(1)
"""

GNSS_LOCATION_MODE = {
	-1: "Error",
	0: "Unavailable",
	1: "GPS/SPS",
	2: "DGPS/DSPS",
	6: "Estimation mode",
}

if __name__ == '__main__':
	gnss = GnssGetData(NMEA_PORT, 9600, 8, 0, 1, 0)
	en_pin = Pin(ENABLE_PIN, Pin.OUT, Pin.PULL_DISABLE, 1)

	while True:
		try:
			read_size = gnss.read_gnss_data(1, 0)
		except Exception:
			print("Can't read GNSS data!")
			print(gnss.getOriginalData())
			utime.sleep(2)
			continue

		if read_size > 0:
			print("SAT: %d of %d. MODE: %s" % (
                            gnss.getUsedSateCnt(),
                            gnss.getViewedSateCnt(),
                            GNSS_LOCATION_MODE[gnss.getLocationMode()]
			))

		if gnss.isFix():
			print(gnss.getUtcTime(), gnss.getLocation())

			utime.sleep(1)
