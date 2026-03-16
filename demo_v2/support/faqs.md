# Source

- URL: https://www.arbin.com/support/faqs.html

# Content

#  Frequently Asked Questions
![FAQ](https://www.arbin.com/wp-content/uploads/2022/08/iStock-1141713510-1024x410.jpg)
####  Topic

####  System Setup
What to do when system showing Communication Failure?
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20106'%3E%3C/svg%3E)![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%2067'%3E%3C/svg%3E)
In CMD window, ping the corresponding MCU address, below screenshot shows the communication of PC and specific MCU is good.
If this communication is good, the issue is located at Mitspro level.
If this communication here is bad(no reply), the issue is located at PC or cable connection level.
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20296'%3E%3C/svg%3E)
(1) Mitspro Level checking:
Check **ArbinSys.cfg** , and make sure the MCU has the correct IP address specified.
(2) PC level checking:
Check PC’s TCP/IP setting, normally Arbin PC is set to a fixed IP address: 196.168.1.100.
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20498'%3E%3C/svg%3E)
(3) Connection level checking:
Check the Ethernet cable connection of the PC and Arbin Cycler, if there is an ethernet switch, make sure the green light is on or flashing at the occupied ethernet port.
Note: Some system has an ethernet switch located on the aux chassis, check the following:
  1. Aux chassis’ power button is on
  2. Power cable is connected
  3. Ethernet cables are connected to ethernet ports instead of CAN ports.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20369'%3E%3C/svg%3E)
####  Schedule
What does “unreasonable Voltage Check Unsafe” means?
It is a preset Unreasonable Voltage Check setting in Schedule Global page, it is by default set to 20% of max voltage of test object file. This safety is usually used for detecting loose connection of load or abnormal low voltage of battery. If your test intends to handle the lower voltage, simply lower the percentage or delete this safety limit.
CCCV vs. CCCV_WRM (CCCV With Relaxation Method)
CCCV is the standard Constant Current to Constant Voltage control, while CCCV_WRM inserts a very short ‘relax’ period between CC period and CV period. During relax time, system current output drops to almost 0, and the corresponding load voltage drop will be measured by the system. Then an Internal Resistance value is calculated by IR = voltage drop / Current drop. This IR value is used for CV stage voltage control (current based PID control).
Advantage of CCCV_WRM: It provides the latest IR value for best Voltage control, it also eliminates the need of adding an IR step before voltage control.
The disadvantage of CCCV_WRM: There is an extra current drop in relax period which does not exist in standard CCCV. Also, the IR value calculated may be less accurate if the CC value is too small to create an effective voltage drop.
How can I synchronize multiple channels? For example letting multiple channels wait for each other and go to next step at the same time.
Currently, there is no way to realize this synchronization by IV system only. But we can use DI/DO module to realize it.
What does Step Control Error Check Unsafe mean?
This unsafe is caused by **Step Control Error Check** setting on the Schedule global page. It will monitor the actual current/Voltage/Power output value and compare it with the schedule setting value, unsafe will happen when the discrepancy between the setting value and the actual value is larger than the setting limit. They are designed to detect open circuits or short circuits caused by loose IV cable connections, it also detects abnormal output when the system has problem.
How can I choose the right aux Channel in Test Setting?
Test Setting and Batch/Mapping file share the same **Auxiliary Channel Virtual Index**.
####  [ Test ](https://www.arbin.com/support/faqs.html#test "Test")
My schedule stopped at beginning, what is the issue?
There are many reasons for schedule stopping, here is a checklist of possible reasons:
  1. Load voltage outside of safety limit.
  2. Load voltage lower than Unreasonable Behavior Check voltage.
  3. EIS function enabled but EIS device not correctly connected.
  4. UPS function is enabled but UPS does not correctly connect.

Why there are large overshoot and oscillation in voltage control step?
Most voltage control requires an _Internal Resistance_ (IR) value of your load. This value can be obtained by an _Internal Resistance_ control step. If you encounter bad voltage control, try adding an IR step before the voltage control step.
My Charge/Discharge current is almost 0 or much less than set value?
**First Check sdu writing issue:**
  1. Check sdu’s **clamp** setting, does the clamp limit current output?
  2. Check step’s Max Current setting, does Max Current smaller than setting current and indicates a smaller current range? 
**Then Check the Hardware issue:**
  3. If the current is almost zero, check Switching Power Supply’s air switch, is it turned on?
  4. If charger/discharge current is less than the setting value: 
    1. Check power V++ and V--, possibly Power supply module issue.
    2. In the manual calibration window, check multiple current points, if the output current value is always a certain portion of the set current value, it indicates there are some small current loops broken.
    3. Check the current output in different current range, more information could be get with Circuit diagram.(fuse burned, Main current loop broken, etc)
  5. If charge current only drops when the voltage is high(For LBT21), it indicates V++ is too low, check V++.

My test stopped due to an error called “Tokenbroken”.
This error indicates too much data logged at a very short period of time. Check the schedule, make sure the data log setting is appropriate.
My test stopped due to an error called “IR Inf”.
This error indicates an IR(Internal Resistance) step can not get a valid result value. Typically because the **Setting Current(Amp)** is too small or the **Time Period** is too short. Try to increase the setting current and Time period(>50ms).
My test stopped due to an error called “Aux CAN Lost” or ”Aux ACK Failed”.
This error indicates Aux channel lost communication with IV channels. It usually happens when the Batch/Mapping file was created/modified without downloading to cycler. It could be solved by downloading Batch/Mapping file:
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20191'%3E%3C/svg%3E)
“Conflict Clamp V” pop up when I start a test.
This checking will only be performed when **Channel Based Voltage Clamp** option is not checked in **ArbinAdvSys.cfg** , which means all IV channels on the same IV channel board share a single voltage clamp/voltage check. Then Mitspro needs to ensure all schedules in the same IV board channels have the same Voltage Clamp setting, if not, this “**Conflict Clamp V”** will pop up.
Recently, almost no Arbin system has shared Voltage clamp, so most of the time, this unsafe is due to wrong Advanced feature setting. Simply check **Channel Based Voltage Clamp** in **ArbinAdvSys.cfg** would solve the issue.
####  Monitor & Control Window
How to change or disable test sound?
In Control & Monitor window, click the top menu Settings -> Monitor Settings…, then choose the General tab in the pop-up window, you can change the sound file or enable/disable sound under different circumstances.
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20495'%3E%3C/svg%3E)
Why I can’t see auxiliary value even I mapped auxiliary already?
You need to assign a schedule to this channel, and this schedule needs to have a corresponding auxiliary channel configured(added).
####  Aux Module
MTCI Common issue
MTCI module is used to communicate with different chamber controllers, troubleshooting procedures are below:
_If Monitor &Control Window shows MTCI channel reading 0.00 degree, it means Mitspro setting issue:_
(1) Check ArbinSys.cfg, make sure MTCI is configured there, and the **Auxiliary** page has MTCI channel row’s Controllable checked.
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20199'%3E%3C/svg%3E)
(2) Map/Batch file has MTCI channel correctly mapped to IV channel.
(3) Iv channel already has a sdu assigned, and this sdu has added enough temperature channels inside.
_If Monitor &Control Window shoes MTCI channel reading 22 degree, it means Mitspro setting is ok, MTCI board or chamber controller issue:_
(1) Check MTCI board setting using ListenForNet, make sure MTCI’s controller type matches chamber’s controller type, and other parameters are matched.
(2) Check the Chamber controller’s setting, and make sure the baudrate, parity, and other parameters match MTCI setting.
(3) Check serial cable, some controller requires crossover wire, but some others do not.
(4) Use Serial Port simulator/monitor software to communicate with MTCI or Chamber Controller directly.
Why I can’t see auxiliary value even I mapped auxiliary already?
You need to assign a schedule to this channel, and this schedule needs to have a corresponding auxiliary channel configured(added).
####  Result Data
In mits 7 ACCESS database environment, what can I do if ACCESS data file gets too large?
This is a common issue at Microsoft Access, you can open this .res file in Microsoft ACCESS, then click File-> Compact&Repair Database to shrink this file. This action can only be done when a related test is not running.
When I export data to CSV file, and index number(>1000) has extra comma, how to fix it?
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20243'%3E%3C/svg%3E)
This issue roots from the Windows system, which adds a comma to >1000 number automatically. We can fix it by changing a regional setting:
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20408'%3E%3C/svg%3E)
####  PC Related
How to see file’s extension name(format)?
Files extension is hidden in Windows by default. You can unhide it by:
  1. Open Control Panel > Appearance and Personalization. 
  2. Click on **Folder Options or****File Explorer Option**.
  3. Click the **View** tab, under Advanced Settings, you will see the option **Hide extensions for known file types.** Uncheck this option and click on Apply and OK.

**Windows 10** users may also search for **File Explorer Options** in the Start search box and open this box.
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20474'%3E%3C/svg%3E)
For more details, refer to <https://www.thewindowsclub.com/show-file-extensions-in-windows>
I reinstalled/upgraded to Window 10 OS, then occurred this error message when open DAQ?
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20322%20232'%3E%3C/svg%3E)
Usually, it’s related to MitsDB.dll registration. Try the following steps:
  1. Make sure these three files are in the Mitspro location:  
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20128'%3E%3C/svg%3E)
  2. Search “cmd” at bottom left window then open Command App and “Run as administrator”.  
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20500'%3E%3C/svg%3E)
  3. Input “cd C:ArbinSoftwareMITS_PRO”, press ENTER.
  4. Then input “C:WindowsMicrosoft.NETFrameworkv4.0.30319RegAsm C:ArbinSoftwareMITS_PROMits_DB_Ent.dll”, press ENTER

You should see something similar to:
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20137'%3E%3C/svg%3E)
![arbin products grouped](https://www.arbin.com/wp-content/uploads/2022/05/hero-reduced-1536x817.jpg)
##  Ready to Build Your Arbin Battery Testing System?
Our expert team is ready to help you build a complete testing system that meets your specifications. Fill out the form linked below to request a quote and start the process.
