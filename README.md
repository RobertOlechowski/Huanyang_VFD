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

If spindle is getting very hot it is signal that you made mistake in wiring 

## Configuration
It is example of working configuration

PD000 	1 	set as last one
PD001 	0 	
PD002 	1 	
PD004 	400Hz 	
PD005 	400Hz 	
PD006 	20Hz 	
PD007 	0.5Hz 	
PD008 	220V 
PD009 	16V 
PD010 	4V 
PD011 	30Hz 
PD013 	08 	set as first
PD014 	10 
PD015 	10 
PD023 	0 
PD024 	1 
PD071 	20 
PD072 	400Hz 
PD141 	220V 
PD142 	6A 	
PD143 	2 	
PD144 	3000 
PD145 	2.0 
PD146 	40 	
PD147 	0 	
PD150 	1 
PD151 	0 	


### Mach 3 integration
...............

### Linux CNC integration
...............
