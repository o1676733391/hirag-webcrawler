# Source

- URL: https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html

# Content

#  Measure Battery's Actual Capacity and Coulombic Efficiency (CE) using Arbin
Table of Contents

##  Benefit of Battery’s Capacity and CE measurement
### Battery capacity and Coulombic Efficiency are critical indicators of a battery's characteristics and suitability for various applications: 
Researchers use these metrics to evaluate material properties and understand their impact on battery performance.
Battery manufacturers rely on these measurements to screen and grade batteries, ensuring that only units meeting quality standards are approved for use.
Battery users can assess the State of Health (SOH) of their batteries, enabling accurate predictions of battery life and performance.
Battery integrators can grade and match batteries with similar capacities, optimizing overall product performance and extending service life.
##  Measurement Method
[ ](https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html)
A common method for measuring a battery’s performance involves cycling the battery between its empty and full states. During each cycle, the battery’s actual capacity is determined by calculating the total discharged capacity, while the coulombic efficiency (CE) is calculated by dividing the discharge capacity by the charge capacity.
Charge/Discharge Capacity: This is calculated using the formula:
Charge/Discharge Capacity = ∫ 𝑖(𝑡)𝑑𝑡
Coulombic Efficiency: CE is determined as:
Coulombic Efficiency = Discharge Capacity / Charge Capacity
![material-symbols_battery-status-good](https://www.arbin.com/wp-content/uploads/2025/02/material-symbols_battery-status-good.png)
To achieve stable and repeatable results, it is recommended to use a consistent charge/discharge pattern across all cycles.
##  Conduct CE test on Arbin
[ ](https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html)
Arbin equipment facilitates accurate CE testing by automatically calculating real-time capacity (with 100 microseconds time resolution) through high-precision voltage and current measurements during battery tests. This automated approach makes measuring coulombic efficiency straightforward and reliable, ensuring precise evaluation of battery performance.
####  A typical CE test procedure can be listed below:
**Step 1:** Initial Rest
**Step 2:** Charge battery to full (SOC=100%)
**Step 3:** Rest for battery reaching electrochemical balance
**Step 4:** Discharge Battery to empty (SOC=0%)
**Step 5:** Rest for battery reaching electrochemical balance
**Step 6:** Loop back to Step 2
####  Implement this procedure to Arbin schedule file: 
![ARBIN-Implement this procedure to Arbin schedule file](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-Implement-this-procedure-to-Arbin-schedule-file.png)
####  Then add criteria for charge/discharge cutoff, loop times and data log:
![ARBIN-Then add criteria for charge:discharge cutoff, loop times and data log](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-Then-add-criteria-for-chargedischarge-cutoff-loop-times-and-data-log.png)
##  You are all set!  
Let Arbin system takes care of everything then
![ARBIN-You are all set-i1](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-You-are-all-set-i1.png)
### Real-time voltage/current display
### Zoom in for detailed curve
![ARBIN-You are all set-i2](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-You-are-all-set-i2.png)
### Real Time Capacity Display
##  Complete Test Data Summary
####  Test Statistics by Cycle
Auto Calculate Capacity and Coulombic efficiency per cycle
![ARBIN-Test Statistics by Cycle](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-Test-Statistics-by-Cycle.png)
####  Test Statistics by Step
![ARBIN-Test Statistics by Step](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-Test-Statistics-by-Step.png)
####  Detailed Test Data
![ARBIN-Detailed Test Data](https://www.arbin.com/wp-content/uploads/2025/02/ARBIN-Detailed-Test-Data.png)
