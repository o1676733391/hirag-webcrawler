# Source

- URL: https://www.arbin.com/accuracy-and-precision-impact-of-battery-testers-accuracy.html

# Content

#  Accuracy and Precision: Impact of battery tester’s accuracy
January 8, 2026
**In the previous article, we introduced the[concepts of accuracy and precision](https://www.arbin.com/accuracy-and-precision-overview.html), along with a brief overview of their influence on battery testing. In this article, we will take a deeper look at the impact of accuracy.**
We will take an example about the impact on capacity measurement and Coulombic Efficiency measurement.
As we all know, Common Procedure for Measuring Coulombic Efficiency (according to IEC practices and typical laboratory methods) is:
  1. **Charge the cell** (usually using a CC–CV protocol) and record the charged capacity Qcharge
  2. **Discharge the cell** (typically using constant-current to a specified cutoff voltage) to obtain the discharged capacity Qdischarge
  3. **Calculate the ratio Qdischarge/Qcharge​** to determine the Coulombic Efficiency for that cycle.

![accuracy and precision](https://www.arbin.com/wp-content/uploads/2026/01/accuracy-and-precision.webp)
Therefore, the issue of measuring Coulombic Efficiency is reduced to the issue of measuring Capacity.
Measuring charge capacity is inherently more complex because the charging process consists of two distinct stages: a constant-current (CC) interval followed by a constant-voltage (CV) interval. During the CC stage, accurate current measurement is essential, as the charge capacity is obtained by integrating the current over the time required to raise the cell voltage from its lower limit to the upper limit (for example, from 2.5 V to 4.2 V).
Equally important is voltage-measurement accuracy, which determines the exact moment the cell reaches the specified cutoff voltage. If the voltage reading is inaccurate, the system may prematurely terminate charging or continue charging past the intended cutoff. Either scenario results in a deviation from the true charge capacity, leading to a significant measurement error.
Voltage-measurement accuracy becomes even more critical during the CV period, where the voltage must be held constant at the specified cutoff. This is due to some reason as follows:
1.**CV control relies entirely on accurate voltage feedback**
During the constant-voltage stage, the cycler’s goal is to maintain the cell exactly at the upper cutoff (e.g., 4.20 V). The controller continuously adjusts the current based solely on the **measured** voltage. Any offset or drift in voltage measurement directly leads to incorrect current output.
  * If the measured voltage is **too low** , the cycler believes the cell has not reached the cutoff → it increases the charging current unnecessarily.
  * If the measured voltage is **too high** , the cycler prematurely reduces the current.

This mismatch can lead to:
  * unpredictable current behavior
  * incorrect taper patterns
  * oscillation or fluctuation of charging current

  1. **Severe over-measurement can trigger negative current**

If voltage is **substantially over-measured** (e.g., sensing 4.25 V when actual is 4.20 V), the controller thinks the cell is “over-voltage.” The control algorithm may respond by issuing **negative current** (a slight discharge) to bring the “measured” voltage back down. This negative current will be interpreted as **discharge capacity**.
If this occurs for even part of the CV duration, the system can log positive discharge capacity within a charge step, and also underestimate the charge capacity. This is one of the most serious consequences of voltage-measurement inaccuracy.
Arbin’s LBT series, with a voltage accuracy of ±0.02% FSR, and especially the HPS series—featuring 480 µV voltage accuracy and six current ranges with a highest accuracy of 8 nA—are excellent choices for researchers who requires high accuracy and high precision battery testing.
**References** :
Arbin Instruments. (2021). _Battery test system accuracy and calibration white paper._ College Station, TX: Arbin Instruments.
Arbin Instruments. (2023). _LBT Series product manual (Rev. 2.3)._ College Station, TX: Arbin Instruments.
ASTM International. (2020). _ASTM E177-20: Standard practice for use of the terms precision and bias in ASTM test methods._ West Conshohocken, PA: ASTM International. [Standard Practice for Use of the Terms Precision and Bias in ASTM Test Methods](https://doi.org/10.1520/E0177-20)
IEC. (2018). _IEC 62660-1:2018 – Secondary lithium-ion cells for the propulsion of electric road vehicles – Part 1: Performance testing._ Geneva, Switzerland: International Electrotechnical Commission.
Newman, J., & Thomas-Alyea, K. E. (2004). _Electrochemical systems_ (3rd ed.). Hoboken, NJ: Wiley-Interscience.
###### [Case Study: How Voltage Precision Affects dV/dt and dQ/dV Calculation in Battery Analyzers](https://www.arbin.com/accuracy-and-precision-impact-of-precision.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Accuracy and precision: Overview](https://www.arbin.com/accuracy-and-precision-overview.html)
[Arbin Instruments at The Battery Show Asia 2026 →](https://www.arbin.com/arbin-instruments-at-the-battery-show-asia-2026.html)
