# Huanyang VFD
All you have to know about Huanyang VFD

Original manuals:
* [VFD manual 1](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/pdf/HY_Series_Inverter_20100627.pdf)
* [VFD manual 2](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/pdf/Huanyang_English_Manual-c.pdf)
* [VFD manual 3](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/pdf/VFD.pdf)
* [GDZ80x73-2.2 spindle manual](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/pdf/GDZ80X73-2.2_2.pdf)


## Dedicated blog
Blog is in Polish language: [blog](https://blog.robertolechowski.com/HUANYANG-podlaczenie/)

## Equipment photos
![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/vfd_and_spindle.jpg?raw=true)

![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/Spindle_1.jpg?raw=true)

![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/Spindle_4.jpg?raw=true)

![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/vfd_2.jpg?raw=true)

![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/vfd_3.jpg?raw=true)

![vfd_and_spindle](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/vfd_connections_2.jpg?raw=true)

## Wiring
### Power three phases
![Three phases](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/3p.png?raw=true)

### Power single phase
![Single Phase](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/1p.png?raw=true)

### Connection between VFD and spindle
![Single Phase](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/diagram_spindle.png?raw=true)

### analog input
![analog connection](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/analog_diagram.png?raw=true)

![jumper](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/Analog_zwora_2.jpg?raw=true)

![Huanyang](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/photos/Analog/analogowo_2.jpg?raw=true)

### external control
![Huanyang](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/external_controll.jpg?raw=true)

![Huanyang](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Documentations/diagrams/external_2.png?raw=true)

## Configuration
It is sample configuration that works for me

| Parameter  | Value | Comment |
| ------------- | ------------- | ------ |
| PD013 | 08        | 	set as first |
| PD001 | 0         |    |
| PD002 | 1         |    |
| PD004 | 400Hz     |    |
| PD005 | 400Hz     |    |
| PD006 | 20Hz      |    |
| PD007 | 0.5Hz     |    |
| PD008 | 220V      |    |
| PD009 | 16V       |    |
| PD010 | 4V        |    |
| PD011 | 30Hz      |    |
| PD014 | 10        |    |
| PD015 | 10        |    |
| PD023 | 0         |    |
| PD024 | 1         |    |
| PD071 | 20        |    |
| PD072 | 400Hz     |    |
| PD141 | 220V      |    |
| PD142 | 6A        |    |
| PD143 | 2         |    |
| PD144 | 3000      |    |
| PD145 | 2.0       |    |
| PD146 | 40        |    |
| PD147 | 0         |    |
| PD150 | 1         |    |
| PD151 | 0         |    |
| PD000 | 1         |   set as last one |  	

## Control over communication port RS485

| Parameter  | Value |
| ------------- | ------------- |
 |PD001 | 2| 
 |PD002| 2| 
 |PD163 | 1| 
 |PD164 |  2| 
 |PD165 |  3| 
 |port |  COM5|


```
pip install crcmod
pip install pyserial
```

module [HuanyangDev](https://github.com/RobertOlechowski/Huanyang_VFD/blob/master/Python/HuanyangDev.py) is in this repository.

```python
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
```

### Mach 3 integration
...............

### Linux CNC integration
...............
