from machine import I2C


RECV_SIZE = 32
ADDR = bytearray([0x00])
ADDR_SIZE = len(ADDR)
HEX_STRING = "0123456789ABCDEF"


if __name__ == '__main__':
	port = I2C(I2C.I2C0, I2C.STANDARD_MODE)
	readed = {}

	print("   ", "  ".join(HEX_STRING))
	i = 0
	for row in HEX_STRING:
		print("0x%s" % row, end=" ")
		for col in HEX_STRING:
			recv_data = bytearray(RECV_SIZE)
			res = port.read(i, ADDR, ADDR_SIZE, recv_data, RECV_SIZE, 0)
			if res == 0:
				print("%02X" % i, end=" ")
				readed[hex(i)] = recv_data
			else:
				print("--", end=" ")
			i += 1
			if i == 256:
				break
		print()  # Newline at end of row

	if readed:
		print("=" * 51)
		print("Received from 0x" + "".join("%02x" % x for x in ADDR) + ":")
		for k, v in readed.items():
			print(k, end=": ")
			for b in v:
				print("%02x" % b, end=" ")
			print()

# 0x62: 00 13  e0  ff  90 40 20 00 00 00 00 00 00 00 00 00 0f  de 06 00 20 00 00 00 00 00 00 00 00 00 00 00
#        0 19 224 255 144 64 32  0  0  0  0  0  0  0  0  0 15 222  6  0 32  0  0  0  0  0  0  0  0  0  0  0
