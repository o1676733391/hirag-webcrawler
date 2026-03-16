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
[ ](https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html#)
A common method for measuring a battery’s performance involves cycling the battery between its empty and full states. During each cycle, the battery’s actual capacity is determined by calculating the total discharged capacity, while the coulombic efficiency (CE) is calculated by dividing the discharge capacity by the charge capacity.
Charge/Discharge Capacity: This is calculated using the formula:
Charge/Discharge Capacity = ∫ 𝑖(𝑡)𝑑𝑡
Coulombic Efficiency: CE is determined as:
Coulombic Efficiency = Discharge Capacity / Charge Capacity

To achieve stable and repeatable results, it is recommended to use a consistent charge/discharge pattern across all cycles.
##  Conduct CE test on Arbin
[ ](https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html#)
Arbin equipment facilitates accurate CE testing by automatically calculating real-time capacity (with 100 microseconds time resolution) through high-precision voltage and current measurements during battery tests. This automated approach makes measuring coulombic efficiency straightforward and reliable, ensuring precise evaluation of battery performance.
####  A typical CE test procedure can be listed below:
**Step 1:** Initial Rest
**Step 2:** Charge battery to full (SOC=100%)
**Step 3:** Rest for battery reaching electrochemical balance
**Step 4:** Discharge Battery to empty (SOC=0%)
**Step 5:** Rest for battery reaching electrochemical balance
**Step 6:** Loop back to Step 2
####  Implement this procedure to Arbin schedule file:

####  Then add criteria for charge/discharge cutoff, loop times and data log:

##  You are all set!
Let Arbin system takes care of everything then

### Real-time voltage/current display
### Zoom in for detailed curve

### Real Time Capacity Display
##  Complete Test Data Summary
####  Test Statistics by Cycle
Auto Calculate Capacity and Coulombic efficiency per cycle

####  Test Statistics by Step

####  Detailed Test Data
