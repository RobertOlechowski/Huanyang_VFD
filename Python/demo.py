import serial
import time
import HuanyangDev

dev = HuanyangDev.HuanyangDev({"port": "COM5", "rate": 19200, "parity": serial.PARITY_NONE, "address": 1, "timeout": 0.1})
dev.open()

dev.write_function_data(8, 2200)
pd008 = dev.read_function_data(8)
print("PD008 = {}".format(pd008))

dev.write_freq(200)
dev.write_control_data(0x03)  # start

# 0: target frequency,  1: output frequency, 2:output current, 3: rpm, 4: DC voltage, 5: AC voltage,6:cont, 7:temp
f1, f2 = dev.read_control_data(0), dev.read_control_data(1)
print("target frequency = {}   output frequency = {}".format(f1, f2))
time.sleep(5)

dev.write_control_data(0x08)  # stop
dev.close()
