# Source

- URL: https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html

# Content

#  How to perform Internal Resistance measurement according to IEC 61960 with Arbin?
August 17, 2025
IR measurement is crucial to have an insight into a battery. There are many way, i.e. many standard to measure battery’s IR. This article will introduce IEC 61960 standard and how to implement it using Arbin’s equipments.
  1. ## **IEC 61960 standard for battery IR:**

In this standard, a discharge pulse of 0.2C is given for 10 seconds and V1 and I1 values are measured. Then, another discharge pulse of 1C is given for 1 second and V2 and I2 values are measured. Then, DCIR is calculated with the above-mentioned formula.
Then, DCIR is calculated by
DCIR = (V1 – V2) / (I2 – I1)
![Measure battery’s IR according to IEC 61960 standard](https://www.arbin.com/wp-content/uploads/2025/08/Measure-battery-IR-according-to-IEC-61960-standard.png)
Measure battery’s IR according to IEC 61960 standard
One point worth highlighting is that in theory, it’s expected to have the transfer between the 2 pulse is immediate. The purpose is to avoid relaxation effect of the battery. However, in reality, it will take a small time, be it some milliseconds or some tens milliseconds depends on the limitation of the equipment used to implement the test. This issue will be address again in the next section.
  1. ## **Implement the test using Arbin cyclers**

The following schedule in Arbin’s MITS software uses C-Rate control type and SetValues Control type to implement the IR calculation:
![use CC control type in MITS software to implement the above schedule](https://www.arbin.com/wp-content/uploads/2025/08/CC-control-type-in-MITS-software.png)
(You can also use CC control type in MITS software to implement the above schedule).
The formula is written as follows:
![IR calculation formula ](https://www.arbin.com/wp-content/uploads/2025/08/IR-calculation-formula.png)
IR calculation formula
If you want the MV_UD variables to be shown in exported data, you can config it in Arbin’s Data Watcher software.
In Additional Filter tab, you can see the list of MV_UD variables and you can choose what to export by checking the corresponding check boxes.
![list of MV_UD variables](https://www.arbin.com/wp-content/uploads/2025/08/list-of-MV-UD-variables.png)
Back to the issue of switching time between the 2 pulses, which is from step 14’s end to step 17’s begin. Mostly it’s caused by step 15 and 16. According to our software engineer: “The execution speed of Set Variable varies depending on the number of channels that a MCU on IV boards needs to manage: 1 millisecond for 8 channels, 2 milliseconds for 16 channels, and 5 milliseconds for 32 channels.” 
Therefore we are totally confident that the switching from step 14 and 17 is less than 50ms, and most of the time, less than 20ms. We believe that this can be considered immediate and quick enough to ignore relaxation effect. If you find that this time is not short enough, please contact us for further request.
_If we want faster transition_ , we can remove the SetValue for Last Step Current, only save Last Step Voltage. The actual current should be very close to the preset control current value. We can use this formula to calculate the current: I = C-Rate * Norminal Capacity
Then the formula now become:
(MVUD10-MVUD12)/((1 – 0.2)*Norminal Capacity)
  1. ## **Discussion**

In many case, users may compare the DCIR value got by Arbin equipment measurement, and compare with other brand’s device.
Please note that some device measure the ACIR rather than DCIR. Take this hand-held meter UT677A for example,
![hand-held meter UT677A](https://www.arbin.com/wp-content/uploads/2025/08/hand-held-meter-UT677A.png)
Many people think that is device is used to measure DCIR, however, when we check its’ specs, what it measures is ACIR at 1kHz:
![control type to measure DCIR](https://www.arbin.com/wp-content/uploads/2025/08/measure-DCIR.png)
In Arbin Cycler, we also have a specific control type to measure DCIR. It will be introduced in another article.
Reference:
[https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-10/Qualifying Containers for Safing Batteries in Runaway.pdf](https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-10/Qualifying%20Containers%20for%20Safing%20Batteries%20in%20Runaway.pdf "https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-10/Qualifying%20Containers%20for%20Safing%20Batteries%20in%20Runaway.pdf")
[Measuring Battery DCIR with a 24xx Graphical SMU and TSP Technology](https://www.tek.com/en/documents/application-note/measuring-battery-dc-internal-resistance-with-a-24xx-graphical-smu-and-tsp-technology)
[Internal Resistance: DCIR and ACIR – Battery Design](https://www.batterydesign.net/dcir-acir/)
[Measuring impedance](https://budgetlightforum.com/t/measuring-impedance/58431/7?utm_source=chatgpt.com)
[https://www.uni-trend.co.za/download-catalogue/uni-trend-ut677a-battery-internal-resistance-tester.pdf?srsltid=AfmBOoqd6iqTQB6wkKD6ST4WB03KiDy6ZLqECuSTQhVsr5h5HgXL1R14](https://www.uni-trend.co.za/download-catalogue/uni-trend-ut677a-battery-internal-resistance-tester.pdf?srsltid=AfmBOoqd6iqTQB6wkKD6ST4WB03KiDy6ZLqECuSTQhVsr5h5HgXL1R14 "https://www.uni-trend.co.za/download-catalogue/uni-trend-ut677a-battery-internal-resistance-tester.pdf?srsltid=AfmBOoqd6iqTQB6wkKD6ST4WB03KiDy6ZLqECuSTQhVsr5h5HgXL1R14")
Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Schedules](https://www.arbin.com/category/application-notes/schedules)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Integrated Electrochemical Impedance Spectroscopy (EIS) With Arbin Charge/Discharge Channels](https://www.arbin.com/integrated-electrochemical-impedance-spectroscopy-eis-with-arbin-charge-discharge-channels.html)
[Integration of Arbin Instruments with Gamry Potentiostats for High-Frequency EIS up to 2 MHz →](https://www.arbin.com/integration-of-arbin-instruments-with-gamry-potentiostats-for-high-frequency-eis-up-to-2-mhz.html)
