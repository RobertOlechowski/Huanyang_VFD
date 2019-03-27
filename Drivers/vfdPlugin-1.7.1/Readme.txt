This plugin allows you to control a Huanyang VFD with mach3 and RS485.

Prerequisites, setup and configuration will be found at 

http://royaumedeole.fr/informatique/plugin-mach3-pour-vfdhuanyang/mach3-plugin-for-huanyang-vfd/

contact: sebastien@royaumedeole.fr

Version 1.7.1
removiong option dealing with frated frequency..due to vfd internal behaviour.
Checkbox to enable/disable automatic Estop feature
More internal tunable parameters
Special thanks to MikeMaat from Machsupport for his precious debugging help


Version 1.7.0
60% of code rewritten, aiming at simplifying
Checkbox to enable/disable automaticEstop feature
More internal tunable parameters


Version 1.6.1
Added some option to ovveride the rated Frequency, due to chineese spindle configuration.
0 means automatic mode, positive value override the value.

Version 1.6.0
Plugin now reads rated Frequency (pd004) and ratedSpeed (pd144)  to build VFD order..do not forget to update your VFD params if needed!
bad speed Estop mechanism has been disabled, due to the fact that many of yours are fcing noise problem.


Version 1.5.1
Estop Problem when speed increasing while spindle not running.


Version 1.5.0
Fixed issue with offline mode (simulation mode)
Fixed issue with emergency stop detection on Mach3 side
Improved emergency stop detection on VFD side, to take advantage of decelerating stop.


Version 1.4.0
Fixed issue with CW and CCW Now plugin supports both mode (M03 and M04 commands)


Version 1.3.0
Solved mach3 crash issue. Dealing with dynamic memory allocation issue
This version should be stable


Version 1.2.0
Vfd status extraction loop modified. 
When you stops spindle, it's now continue monitoring data until effective stop is detected.
Effective Stop occurs when VFD speed is zero for more than 6 measures (about 1/2 second).



