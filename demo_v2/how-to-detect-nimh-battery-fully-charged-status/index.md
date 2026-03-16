# Source

- URL: https://www.arbin.com/how-to-detect-nimh-battery-fully-charged-status.html

# Content

#  How to detect NiMH battery fully charged status
May 26, 2025
**Voltage, Temperature, and Delta-V: Indicators of Full Charge in NiMH Cells**
  1. **Overview of NiMH Battery**

The Nickel-Metal Hydride (NiMH) battery is a type of rechargeable battery that uses **nickel oxide hydroxide (NiOOH)** as the positive electrode (cathode) and a hydrogen-absorbing alloy as the negative electrode (anode).
Compared to nickel-cadmium (NiCd) batteries, NiMH batteries offer several distinct advantages:
  * **Higher capacity** , which helps extend the device’s usage time.
  * **Lower environmental impact** , as they do not contain cadmium—a toxic heavy metal.
  * **More environmentally friendly** during both usage and disposal.

Thanks to these characteristics, NiMH batteries are widely used in many modern electronic devices and vehicles, including:
  * **Digital cameras**
  * **Cordless phones**
  * **Electronic toys**
  * **Hybrid vehicles**

![](https://www.arbin.com/wp-content/uploads/2025/05/NiMH-battery.png)
**NiMH-battery**
  1. **Principle of Full-Charge Check for NiMH Batteries**

Some indicators of a full-charge check for **Nickel-Metal Hydride (NiMH)** batteries is based on the physical and electrochemical changes that occur within the battery as it approaches full charge. During the charging process, several characteristic indicators are monitored to determine when the battery has reached its maximum capacity:
  * **Negative Delta-V (−ΔV) Phenomenon** :  
As the battery nears full charge, the voltage of each cell rises to a peak and then **slightly drops** due to internal ion redistribution and the onset of overcharge conditions. This voltage drop—typically in the range of **5–15 mV per cell** —is used by many smart chargers to detect the full-charge point.
  * **Temperature Rise** :  
When the battery is nearly full, its ability to efficiently convert electrical energy into chemical energy decreases. Excess energy is instead converted into heat, leading to a **rapid increase in cell temperature**. This rise can be detected using temperature sensors and is considered a reliable indicator of a full charge.
  * **Voltage Threshold Detection** :  
Toward the end of the charging process, the cell voltage typically reaches a level between **1.4V and 1.5V**. While voltage alone is not a definitive indicator of full charge, it contributes valuable data when combined with other metrics.
  * **Theoretical Charging Time Calculation** :  
Based on the battery’s **rated capacity (in mAh)** and the **charging current (in mA)** , the expected full-charge time can be estimated. This method is often used as a **safety cutoff** or secondary reference in charger design.

![](https://www.arbin.com/wp-content/uploads/2025/05/NiMH-graph.png)
****NiMH Voltage graph during constant current charge****
Here’s the plotted charging curve for a NiMH battery, showing both:
🔵Voltage per cell: Rising and then slightly dropping (-ΔV) after full charge
🔴Temperature: Rising slowly, then increasing sharply as charging continues past full charge (-90min mark).
  1. **Application of Arbin Instruments for full charge detection of NiMH Batteries**

Object of the test:
  * A NiMH battery pack (7S1P, 8.4V, 4.5Ah)

Assume that the indicators of full charge that are used to check:
  * **Negative Delta V Termination** : V – Vpeak = -60mV
  * 10-minute continuous voltage drop
  * **Failsafe Max Charge Time** : 3 hours
  * **Safety Voltage Limit** : 10.5V

To solve this problem, Arbin engineer wrote a schedule that include 2 steps with 1 control type (CC-constant current at 1.8A) and some step limits as the image below:
![](https://www.arbin.com/wp-content/uploads/2025/05/Schedule-of-the-Test.png)
Schedule of the Test
The key point of the loop step is for the condition of “10-minute continuous voltage drop”. In step CC, when the voltage start dropping, (dV/dt<0), we jump to this step to the step Loop.
The maximum time of this step is 10 minutes. During this 10 minutes, whenever dV/dt >=0, it means that the condition of Voltage 10 mins continuously drop failed, we need to start clocking to monitor for another slot of 10 mins and have to go back to step CC.
After 10 mins, if the condition of dV/dt >=0 is not hit, then the voltage has been dropped 10 mins continuously.
During this step, whenever the other 3 conditions meet (**Negative Delta V Termination** : V – Vpeak = -60mV, **Failsafe Max Charge Time** : 3 hours, **Safety Voltage Limit** : 10.5V) the battery is also considered fully charged.
![](https://www.arbin.com/wp-content/uploads/2025/05/Flow-Chart-of-this-Schedule-.png)
Test Flow Chart of this Schedule
In this schedule, we created CC control type (1.8A):
  * **Safety Voltage Limit** : 10.5V => Test jumps to End Charge step if present channel voltage(PV_CHAN_VOLTAGE) reaches 10.5V.
  * **Failsafe Max Charge Time** : 3 hours => Test jumps to End Charge step if total of test time (PV_CHAN_Test_Time) reaches 3 hours.
  * **Negative Delta V Termination** : -dV/dT, -60mV => We created step limits that include the formula F_A as image below

![](https://www.arbin.com/wp-content/uploads/2025/05/NiMH-Delta-formula-1024x52.png)
**NiMH Delta formula**
![](https://www.arbin.com/wp-content/uploads/2025/05/NiMH-Delta-formula-2-1024x594.png)
NiMH Delta formula 2
In this formula function, we created formula F_A that calculates the difference between the present value of voltage and the highest value of voltage in this cycle. If the result of this formula is less than or equal to -0.06, the test will jump into the End Charge step.
  * **-dV Timer** : 10-minute continuous voltage drop => We created step limits that if 
    * Present value of channel dV/dt is less than 0 (PV_CHAN_dV/dt<0), the test will jump into the LOOP step.
    * Present value of channel dV/dt is not less than 0, the test will rely on the other condition (PV_CHAN_VOLTAGE or PV_CHAN_Test_Time or F_A) to decide to jump into the End Charge step.

Posted in [Arbin News](https://www.arbin.com/category/arbin-news.html), [Featured News](https://www.arbin.com/category/featured-news.html)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Battery Test for Electric Vehicles (EV) Application Notes](https://www.arbin.com/battery-test-for-electric-vehicles-ev-application-notes.html)
[Battery multiple points temperature measurement →](https://www.arbin.com/battery-multiple-points-temperature-measurement.html)
