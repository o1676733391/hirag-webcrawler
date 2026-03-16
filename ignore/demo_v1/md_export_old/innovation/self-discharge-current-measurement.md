# Source

- URL: https://www.arbin.com/innovation/self-discharge-current-measurement.html

# Content

#  Self-Discharge Current
Measurement

![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Self-Discharge-Current-Measurement-2.png)
Table of Contents

##  What is Self-Discharge Current (SDC)
Battery Self-Discharge Current(SDC) is the small amount of electrical current that is lost naturally from a battery when it is not in use, due to internal chemical reactions within the battery.
Measuring SDC accurately helps in understanding the health and efficiency of a battery, allowing manufacturers and users to predict battery life and performance more effectively.
##  SDC Measurement Methods
####  Traditional Method
Traditional SDC Measurement is estimating the self-discharge current by monitoring the battery's open circuit voltage drop after a long time.
Then find the capacity change corresponding to the OCV change, calculate the estimated SDC by capacity change divides time.
This method requires a long measuring time and a known battery data(OCV vs. Capacity) of the battery.

####  Potentiostatic Method
Another potentiostatic method is using a voltage source to apply the same voltage as the battery OCV, then consider the current flows from the voltage source to the battery to hold the OCV as the battery's SDC.
This method can measure the SDC is a relatively shorter time than traditional method, but it requires additional hardware for it, this method is also sensitive to temperature change and may disturb battery's electrochemical balance when force apply a voltage to it.

####  Galvanostatic Method (Arbin Method)
Arbin utilizes a galvanostatic method, by applying small amount of DC currents to the cell and record the voltage change rate, then the battery's SDC and dynamic capacitance can be calculated by solving below equations:

This method can accurately measure SDC in a short time, it also avoids disturbance of battery electrochemical balance because the applied small current is constant without being affected by temperature change.
####  Galvanostatic Parallel Method(Arbin Method)
Take one step further of galvanostatic method, Arbin offers PDBT modules to parallel a batch of batteries and measure each battery's SDC.
In addition to the previous galvanostatic method's benefits, this parallel method let batteries reach electrochemical balance even faster, and one Arbin channel can support multiple batteries run the SDCM simultaneously.

This method can accurately measure SDC in a short time, it also avoids disturbance of battery electrochemical balance because the applied small current is constant without being affected by temperature change.
##  SDC measurement methods Comparison

##  Arbin SDC Monitoring Feature
Arbin SDC monitoring feature is designed for battery storage, battery manufacturing and battery operation. The procedure of a battery getting bad usually takes a long time.
Continues monitoring SDC of cells along with the life of battery provides early detection of problematic cell and prevent hazardous thermo-runaway from happening.
In the SDC monitoring mode, Arbin monitors each battery's voltage and unbalanced current among all paralleled batteries in real time, without inducing any external current.
Below chart shows a group of 8 coin cells in parallel, the problematic cells(cell_5 and cell_7 in the chart) with higher self-discharge current would drop voltage faster than others, thus get much higher inlet current from other cells.
Arbin SDC monitoring feature keeps log these currents and alarm user when abnormal current appears.

Below chart shows the self-discharge current increase with time while battery turns bad gradually, during this process, battery's SDC increase drastically and much earlier than battery's temperature increase.
Thus it's much more efficient to monitor the SDC than monitor battery's temperature for the purpose of battery failure detection and thermal runaway prevention.

##  Arbin SDC Monitoring application for Early Fault Detection
####  Early Fault Detection in Storage and Shipping
Because Arbin SDC Monitoring does not require active power sources, it can be used in battery storage and shipping without external power.

In battery storage and shipping, it is hard to have someone keep monitoring the status of every cell.
Once the thermal runaway happens on one bad battery, a chain reaction will happen for all other batteries in a box or near the bad battery and cause destructive aftermath.
####  Early Fault Detection in Operation
The modules used in EVs consist of many batteries in parallel. If one battery went bad, usually it is hard to be detected from the system as other batteries will output more power. When the thermal runaway happens, the batteries near the broken one are likely affected.
By having the SDC monitoring feature with BMS, it is straightforward to detect the abnormal behavior of a single battery, and users can receive the alert/alarm/emergency notification at each stage.

####  Early Fault Detection in Manufacturing
The self-discharge current of the batteries from the same production batch should have the similar self-discharge current.
By applying Arbin SDC measurement and monitoring to the batteries, the bad battery with larger self-discharge current can be easily identified.
Arbin's SDCM provides a faster and more accurate solution of self-discharge current measurement and monitoring in battery manufacturing.
With Arbin SDCM, the battery manufacturers will be able to conduct finishing stage with high quality in much shorter time, which means great savings in initial investment cost and operational cost.
The higher accuracy of Arbin SDC measurement also greatly improves accuracy of cell grading and improves the quality of sorting procedure, which eventually improves the quality of battery pack.

More importantly, the SDC monitoring can greatly reduce the risk of thermo-runaway and resulting fire.
This will greatly reduce the cost of safety measures for the battery factory and may relax the regulation for safety measures.
For example, the following measure may not be necessary or at least may not be needed extensively:
  * Temperature measurement, smoke/fire alarm, gas/electrolyte vaper sensor, fire suppressing equipment, etc.…
