# Source

- URL: https://www.arbin.com/how-to-perform-dc-internal-resistance-measurement-with-arbin.html

# Content

#  How to perform DC Internal Resistance measurement with Arbin?
September 22, 2025
**Mechanism explanations:**
Arbin’s MITS software uses pulse method to calculate IR. In order to achieve better accuracy, the software measures the IR 10 times and takes the average.
The pulse looks like the graph bellow:
![pulse graph mits arbin software](https://www.arbin.com/wp-content/uploads/2025/09/pulse-graph-mits-arbin-software.png)Pulse Graph - MITS, Arbin Software
IIR is the amplitude value
T2 is the extra control value1
I0 is the offset value
IR Calculation Formula:
IR = Average {(Voltage at P2 - Voltage at P3)/ (2IIR)}
****Writing t** he schedule for IR calculation is quite simple**.
You will only need 2 steps:
  1. Rest step: Mainly plays the role of initial safety check
  2. Internal Resistance steps

  * Amplitude: Amplitude determines the applied current value. For optimized accuracy, the applied current value should generate at least 10mV voltage change during the IR measurement. In general, the current should be at least 0.1C of your battery.
  * You can also set the current range by inputting a suitable number in the box of the Max Current (A)
  * Current ranges are written on the label attached on the Arbin chassis. For example, you can see all the ranges from I1 to I6 as in the picture bellow.
  * You should only use the values that are written on the label, in this case 5A, 1A, 0.1A, 0.01A, 0.001A, 0.0001A. If you put 0 (default), the range will be chosen automatically by the machine

Extra Control Value1:
  * This value determines the current pulse length before voltage change is measured. It is determined by your IR test needs (Ohmic resistance or polarization resistance), this value should be at least 100ms.

  * Offset: This is the offset current value (A), at default value 0, the output current pulse will be symmetric.

Above is IR measuring with Arbin’s method. If you want to follow an international standard, you can refer to this article: [How to perform Internal Resistance measurement according to IEC 61960 with Arbin?](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Schedules](https://www.arbin.com/category/application-notes/schedules)
](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Enhancing Battery Testing Safety with a Door Switch Interlock System](https://www.arbin.com/enhancing-battery-testing-safety-with-a-door-switch-interlock-system.html)
[How to run cyclic voltammetry(CV) using Arbin Tester →](https://www.arbin.com/how-to-run-cyclic-voltammetrycv-using-arbin-tester.html)
