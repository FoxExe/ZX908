from machine import Pin, UART
from gnss import GNSS
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
	print("GPS data gather example")

	gnss = GNSS(NMEA_PORT, 9600, 8, 0, 1, 0)
	en_pin = Pin(ENABLE_PIN, Pin.OUT, Pin.PULL_DISABLE, 1)

	while True:
		read_size = gnss.readAndParse()
		if read_size < 100:
			# Wait for data...
			# Note: GPS chip can send data up to 10 times per second.
			utime.sleep(1)
			continue

		print("SAT: %d of %d. MODE: %s" % (
			gnss.getUsedSateCnt(),
			gnss.getViewSateCnt(),
			GNSS_LOCATION_MODE[gnss.getLocationMode()],
		))

		rmc_data = gnss.getRMC()
		if rmc_data != -1 and rmc_data[2] == "A":
			# A = Gnss fix OK, V - No GPS fix
			rmc_data = gnss.getRMC()
			date = (int(rmc_data[9][0:2]), int(rmc_data[9][2:4]), int('20' + rmc_data[9][4:6]))
			time = (int(rmc_data[1][0:2]), int(rmc_data[1][2:4]), int(rmc_data[1][4:6]))
			datetime = "%02d.%02d.%d" % date + " %02d:%02d:%02d" % time

			lat, lat_dir, lon, lon_dir = gnss.getLocation()
			print("[%s] Speed: %s, Course: %s, LAT: %3.06f, LON: %3.06f, ACC: %s, ALT: %s" % (
				datetime,
				gnss.getSpeed(),
				rmc_data[7],
				float(lat),
				float(lon),
				rmc_data[8],
				gnss.getAltitude()
			))

		gsv_data = gnss.getGSV()
		if gsv_data != -1:
			print("====Satellites====")
			print("|UUID|ELV|AZM|RSI|")
			for msg in gsv_data:
				sats_in_msg = (len(msg) - 5) // 4
				for i in range(sats_in_msg):
					# Start from 4th element (Skipping sat_type, msg_count, msg_num, sat_count)
					info = msg[4 + (i * 4): 4 + (i * 4) + 4]
					# [Sat_id, elevation, azimuth, signal]
					print("#%3s %3s %3s %3s" % tuple(info))
			print("==================")

		utime.sleep(5)
