import crcmod
import serial
import struct

_crc16 = crcmod.predefined.mkPredefinedCrcFun('modbus')


class HuanyangDev:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def open(self):
        self.conn = serial.Serial(
            port=self.config["port"],
            baudrate=self.config["rate"],
            parity=self.config["parity"],
            timeout=self.config["timeout"]
        )

    def close(self):
        self.conn.close()

    def _build_packet(self, function, data):
        packet = [self.config["address"], function, len(data)]
        packet.extend(data)
        crc = self._hy_crc(packet)
        packet.extend(crc)
        return packet

    @staticmethod
    def _hy_crc(message):
        return list(struct.pack('<H', _crc16(bytes(message))))

    def _check_crc(self, message):
        if len(message) > 5:
            calc_crc = self._hy_crc(message[:-2])
            msg_crc = list(message[-2:])
            return calc_crc == msg_crc
        return False

    def _check_msg(self, message):
        if self._check_crc(message):
            if int(message[1]) & 0xF0 > 0:
                return False
            return int(message[2]) == len(message[3:-2])
        return False

    def read_function_data(self, parameter):
        packet = self._build_packet(0x01, [parameter])
        self.conn.write(bytes(packet))
        ans = self.conn.read(8)
        if not self._check_msg(ans):
            return None

        data = ans[3:-2]
        value = int.from_bytes(bytes(data[1:]), byteorder='big')
        return value

    def write_function_data(self, parameter, value):
        value = int(value)
        value_length = max(1, (value.bit_length() + 7) // 8)
        pdata = [parameter]
        pdata.extend(list(value.to_bytes(value_length, 'big')))
        packet = self._build_packet(0x02, pdata)
        self.conn.write(bytes(packet))
        ans = self.conn.read(8)

        if self._check_msg(ans):
            rdata = ans[3:-2]
            value = int.from_bytes(bytes(rdata[1:]), byteorder='big')
            return value
        return None

    def write_control_data(self, data):
        packet = self._build_packet(0x03, [data])
        self.conn.write(bytes(packet))
        ans = self.conn.read(6)
        if self._check_msg(ans):
            value = int.from_bytes(bytes(ans[3:-2]), byteorder='big')
            return value
        return None

    def read_control_data(self, parameter):
        packet = self._build_packet(0x04, [parameter])
        self.conn.write(bytes(packet))
        ans = self.conn.read(8)
        if not self._check_msg(ans):
            return None

        rdata = ans[3:-2]
        value = int.from_bytes(bytes(rdata[1:]), byteorder='big')
        return value

    def write_freq(self, freq):
        pdata = list(int(freq * 100).to_bytes(2, 'big'))
        packet = self._build_packet(0x05, pdata)
        self.conn.write(bytes(packet))
        ans = self.conn.read(8)
        if self._check_msg(ans):
            value = int.from_bytes(bytes(ans[3:-2]), byteorder='big')
            ret = value / 100
            return ret
        return None
