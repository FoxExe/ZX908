from machine import I2C

I2C_ADDRESS = 0x62


if __name__ == '__main__':
	port = I2C(I2C.I2C0, I2C.STANDARD_MODE)
	for i in range(256):
		buff = bytearray([i])
		data = bytearray(64)
		res = port.read(I2C_ADDRESS, buff, len(buff), data, len(data), 100)

		print("[0x%02X] %d: %s" % (i, res, " ".join(["%02X" % b for b in data])))

# 03 13 E0 FF 90 40 20 00 00 00 00 00 00 00 00 00 0F DE 06 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 09 30 01 00 00 00 0A 00 04 0A 18 08
