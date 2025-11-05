try:
	import usys as sys
except ImportError:
	import sys


print("System: %s v.%s (mPY: %s, Python v%s) on %s" % (
	sys.implementation.name,
	".".join([str(n) for n in sys.implementation.version]),
	sys.implementation.mpy,
	sys.version,
	sys.platform,
))
print("Modules:")
for k, v in sys.modules.items():
	print("\t", v)


from machine import RTC
rtc = RTC()
print("RTC time:", rtc.datetime())


import utime
print("SYS time: %s (TZ: %s)" % (utime.localtime(), utime.getTimeZone()))
print("Uptime:", utime.time())


import sim
if sim.getStatus() == 0:
	print("No SIM card detected!")
else:
	print("SIM Phone:", sim.getPhoneNumber())
	print("SIM ICC ID:", sim.getIccid())
	print("SIM IMSI:", sim.getImsi())


import modem
print("IMEI:", modem.getDevImei())
print("Device:", modem.getDevModel())
print("Product:", modem.getDevProductId())
print("SN:", modem.getDevSN())
print("FW:", modem.getDevFwVersion())


import net
print("Network signal:", net.csqQueryPoll(), "(0..31, 99 = error, -1 = exec fail)")
NETWORKS = ("GSM", "UMTS", "LTE")
cells = net.getCellInfo()
for i in range(3):
	for cell in cells[i]:
		print(NETWORKS[i], cell)
print("Current network type: %s. Roaming: %s" % net.getConfig())
print("SEL: %s, MCC: %s, MNC: %s, ACT: %s" % net.getNetMode())


help('modules')


import wifiScan

def print_result(results):
	count, aps = results
	for info in aps:
		mac_addr, signal = info
		print("MAC: %s, %sdb" % (mac_addr, signal))

wifiScan.setCallback(print_result)
wifiScan.control(1)
wifiScan.asyncStart()
