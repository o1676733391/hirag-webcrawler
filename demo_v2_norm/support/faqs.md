# Metadata

| Field | Value1 |
|------|------|
| Title | Frequently Asked Questions |
| Page Type | Resource |
| Source URL | https://www.arbin.com/support/faqs.html |
| Category | Support |
| Last Updated | |

# Overview

This document contains frequently asked questions regarding system setup, scheduling, monitoring, control, and PC-related issues for Arbin systems.

# Key Points

| Topic | Summary |
|-------|---------|
| Communication Failure | Steps to diagnose communication issues between PC and MCU. |
| Unreasonable Voltage Check Unsafe | Explanation of the preset safety limit for voltage checks. |
| CCCV vs. CCCV_WRM | Differences between standard CCCV control and CCCV with relaxation method. |
| Synchronizing Multiple Channels | Current limitations in synchronizing channels using the IV system. |
| Step Control Error Check Unsafe | Explanation of the error caused by discrepancies in output values. |
| Auxiliary Channel Configuration | Importance of assigning schedules to auxiliary channels. |
| MTCI Common Issues | Troubleshooting steps for MTCI module communication issues. |
| Database Management | Steps to compact and repair large Microsoft Access database files. |
| File Extension Visibility | Instructions to unhide file extensions in Windows. |
| MitsDB.dll Registration | Steps to resolve issues related to MitsDB.dll after OS upgrade. |

# Detailed Explanation

## System Setup

What to do when the system shows Communication Failure?
In CMD window, ping the corresponding MCU address. If the communication is good, the issue is located at Mitspro level. If the communication is bad (no reply), the issue is located at the PC or cable connection level.

1. **Mitspro Level checking**: Check **ArbinSys.cfg**, and make sure the MCU has the correct IP address specified.
2. **PC level checking**: Check PC’s TCP/IP setting, normally Arbin PC is set to a fixed IP address: 196.168.1.100.
3. **Connection level checking**: Check the Ethernet cable connection of the PC and Arbin Cycler. If there is an ethernet switch, make sure the green light is on or flashing at the occupied ethernet port. Note: Some systems have an ethernet switch located on the aux chassis. Check the following:
   - Aux chassis’ power button is on.
   - Power cable is connected.
   - Ethernet cables are connected to ethernet ports instead of CAN ports.

## Schedule

What does “unreasonable Voltage Check Unsafe” mean?
It is a preset Unreasonable Voltage Check setting in the Schedule Global page, set to 20% of the max voltage of the test object file by default. This safety feature is used for detecting loose connections of load or abnormal low voltage of the battery. If your test intends to handle lower voltage, simply lower the percentage or delete this safety limit.

### CCCV vs. CCCV_WRM (CCCV With Relaxation Method)
CCCV is the standard Constant Current to Constant Voltage control, while CCCV_WRM inserts a very short ‘relax’ period between CC and CV periods. During the relax time, system current output drops to almost 0, and the corresponding load voltage drop will be measured by the system. An Internal Resistance value is calculated by IR = voltage drop / Current drop. This IR value is used for CV stage voltage control (current-based PID control).

**Advantage of CCCV_WRM**: It provides the latest IR value for the best voltage control and eliminates the need for adding an IR step before voltage control.

**Disadvantage of CCCV_WRM**: There is an extra current drop in the relax period which does not exist in standard CCCV. The IR value calculated may be less accurate if the CC value is too small to create an effective voltage drop.

How can I synchronize multiple channels?
Currently, there is no way to realize this synchronization by the IV system only. However, we can use the DI/DO module to achieve it.

What does Step Control Error Check Unsafe mean?
This unsafe condition is caused by the **Step Control Error Check** setting on the Schedule global page. It monitors the actual current/voltage/power output value and compares it with the schedule setting value. An unsafe condition will occur when the discrepancy between the setting value and the actual value is larger than the setting limit. This feature is designed to detect open circuits or short circuits caused by loose IV cable connections and also detects abnormal output when the system has a problem.

How can I choose the right aux Channel in Test Setting?
Test Setting and Batch/Mapping file share the same **Auxiliary Channel Virtual Index**.

## Test

My schedule stopped at the beginning; what is the issue?
There are many reasons for a schedule stopping. Here is a checklist of possible reasons:
1. Load voltage outside of safety limit.
2. Load voltage lower than Unreasonable Behavior Check voltage.
3. EIS function enabled but EIS device not correctly connected.
4. UPS function is enabled but UPS does not connect correctly.

Why are there large overshoot and oscillation in the voltage control step?
Most voltage control requires an _Internal Resistance_ (IR) value of your load. This value can be obtained by an _Internal Resistance_ control step. If you encounter bad voltage control, try adding an IR step before the voltage control step.

My Charge/Discharge current is almost 0 or much less than the set value?
**First Check SDU writing issue:**
1. Check SDU’s **clamp** setting; does the clamp limit current output?
2. Check step’s Max Current setting; is Max Current smaller than the setting current, indicating a smaller current range?

**Then Check the Hardware issue:**
3. If the current is almost zero, check the Switching Power Supply’s air switch; is it turned on?
4. If charger/discharge current is less than the setting value:
   - Check power V++ and V--, possibly indicating a power supply module issue.
   - In the manual calibration window, check multiple current points. If the output current value is always a certain portion of the set current value, it indicates that some small current loops are broken.
   - Check the current output in different current ranges; more information could be obtained with the circuit diagram (fuse burned, main current loop broken, etc.).
5. If charge current only drops when the voltage is high (for LBT21), it indicates V++ is too low; check V++.

My test stopped due to an error called “Tokenbroken”.
This error indicates too much data logged at a very short period of time. Check the schedule and ensure the data log setting is appropriate.

My test stopped due to an error called “IR Inf”.
This error indicates an IR (Internal Resistance) step cannot get a valid result value, typically because the **Setting Current (Amp)** is too small or the **Time Period** is too short. Try to increase the setting current and time period (>50ms).

My test stopped due to an error called “Aux CAN Lost” or “Aux ACK Failed”.
This error indicates the Aux channel lost communication with IV channels. It usually happens when the Batch/Mapping file was created/modified without downloading to the cycler. It could be solved by downloading the Batch/Mapping file.

“Conflict Clamp V” pops up when I start a test.
This checking will only be performed when the **Channel Based Voltage Clamp** option is not checked in **ArbinAdvSys.cfg**, meaning all IV channels on the same IV channel board share a single voltage clamp/voltage check. Mitspro needs to ensure all schedules in the same IV board channels have the same Voltage Clamp setting; if not, this “**Conflict Clamp V**” will pop up. Recently, almost no Arbin system has shared Voltage clamp, so most of the time, this unsafe condition is due to wrong advanced feature settings. Simply check **Channel Based Voltage Clamp** in **ArbinAdvSys.cfg** to solve the issue.

## Monitor & Control Window

How to change or disable test sound?
In the Control & Monitor window, click the top menu Settings -> Monitor Settings…, then choose the General tab in the pop-up window. You can change the sound file or enable/disable sound under different circumstances.

Why can’t I see auxiliary value even though I mapped auxiliary already?
You need to assign a schedule to this channel, and this schedule needs to have a corresponding auxiliary channel configured (added).

## Aux Module

### MTCI Common Issue
MTCI module is used to communicate with different chamber controllers. Troubleshooting procedures are below:

_If Monitor & Control Window shows MTCI channel reading 0.00 degrees, it means Mitspro setting issue:_
1. Check ArbinSys.cfg, make sure MTCI is configured there, and the **Auxiliary** page has MTCI channel row’s Controllable checked.
2. Map/Batch file has MTCI channel correctly mapped to IV channel.
3. IV channel already has an SDU assigned, and this SDU has added enough temperature channels inside.

_If Monitor & Control Window shows MTCI channel reading 22 degrees, it means Mitspro setting is okay, but there may be an MTCI board or chamber controller issue:_
1. Check MTCI board setting using ListenForNet, make sure MTCI’s controller type matches the chamber’s controller type, and other parameters are matched.
2. Check the Chamber controller’s setting, and make sure the baud rate, parity, and other parameters match MTCI setting.
3. Check the serial cable; some controllers require crossover wire, but some others do not.
4. Use Serial Port simulator/monitor software to communicate with MTCI or Chamber Controller directly.

## Result Data

In the Mits 7 ACCESS database environment, what can I do if the ACCESS data file gets too large?
This is a common issue in Microsoft Access. You can open this .res file in Microsoft ACCESS, then click File -> Compact & Repair Database to shrink this file. This action can only be done when a related test is not running.

When I export data to CSV file, and index number (>1000) has an extra comma, how do I fix it?
This issue arises from the Windows system, which automatically adds a comma to numbers greater than 1000. We can fix it by changing a regional setting.

## PC Related

How to see a file’s extension name (format)?
File extensions are hidden in Windows by default. You can unhide them by:
1. Open Control Panel > Appearance and Personalization.
2. Click on **Folder Options** or **File Explorer Options**.
3. Click the **View** tab. Under Advanced Settings, you will see the option **Hide extensions for known file types**. Uncheck this option and click on Apply and OK.

**Windows 10** users may also search for **File Explorer Options** in the Start search box and open this box.

I reinstalled/upgraded to Windows 10 OS, then this error message occurred when opening DAQ?
Usually, it’s related to MitsDB.dll registration. Try the following steps:
1. Make sure these three files are in the Mitspro location.
2. Search “cmd” at the bottom left window, then open Command App and “Run as administrator”.
3. Input “cd C:\ArbinSoftware\MITS_PRO”, press ENTER.
4. Then input “C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm C:\ArbinSoftware\MITS_PRO\mits_DB_Ent.dll”, press ENTER.

You should see something similar to the expected output.

# Notes

*Windows 10 users may also search for File Explorer Options in the Start search box and open this box.*

*For more details, refer to <https://www.thewindowsclub.com/show-file-extensions-in-windows>.*

*Autocalibration box is sold separately.*

*EIS testing device is sold separately.*
