# Source

- URL: https://www.arbin.com/how-to-test-a-protection-circuit-module-pcm-using-arbin-eol.html

# Content

#  How to Test a Protection Circuit Module (PCM) Using ARBIN EOL
July 23, 2025
## **I. Purpose and Scope:**
The Protection Circuit Module (PCM) is a critical electronic component responsible for monitoring and protecting devices across a wide range of applications—from small consumer electronics to large-scale industrial equipment. Its core function is to ensure battery and device safety by preventing hazardous conditions such as overcharging, over-discharging, overcurrent, and short circuits
![protection circuit module pcm](https://www.arbin.com/wp-content/uploads/2025/07/protection-circuit-module-pcm-using-arbin.png)
Arbin offers an End-of-Line (EOL) testing solution tailored for customers’ production lines to evaluate the functionality and reliability of Protection Circuit Modules (PCMs). This testing ensures that the PCM responds appropriately when a battery’s voltage or current exceeds its designed minimum or maximum thresholds. Under such conditions, the PCM should automatically disconnect to prevent damage or safety hazards associated with overvoltage, undervoltage, overcurrent, or short-circuit events.
## II. Testing
  1. **Procedure**

![How to test Protection Circuit Module](https://www.arbin.com/wp-content/uploads/2025/07/How-to-test-Protection-Circuit-Module.png)
The following steps outline the standard procedure implemented using the Arbin EOL system to verify the PCM’s key protection functions. Each step simulates fault conditions to validate the PCM’s ability to disconnect or recover as designed.
**Step** |  **Test Item** |  **Description**

1 |  **Overcharge Protection** |  Simulate battery overcharging. Gradually increase voltage until the PCM disconnects. Record the voltage at which the output current drops to 0 A.
2 |  **Overcharge Release** |  Slowly decrease the variable power supply voltage. Record the voltage at which current output resumes.
3 |  **Undercharge Protection** |  Simulate battery undercharging. Gradually decrease the voltage until the PCM disconnects. Record the voltage when the output current drops to 0 A.
4 |  **Undercharge Release** |  Slowly increase the variable power supply voltage. Record the voltage at which current output resumes.
5 |  **Charge Overcurrent Detection** |  Confirm the overcurrent protection during charging. Gradually increase current and record the value at which the PCM activates the cutoff.
6 |  **Discharge Overcurrent Detection** |  Confirm the overcurrent protection during discharging. Gradually increase discharge current and record the value at which the PCM activates the cutoff.
Implementing it using Arbin MITS 11 software:
**Step** |  Test Name |  Description |

|  **Test Overcharge Voltage** |  Simulate a battery overcharge condition by gradually increasing the voltage. The PCM should disable the output once the voltage exceeds the predefined threshold. This is confirmed by observing that the output current drops to **0 A**. |  ](https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png)
**2** |  **Confirm Overcharge Recovery** |  Slowly decrease the voltage to verify that the PCM automatically re-enables output when the voltage returns to a safe range. This step ensures proper recovery behavior after an overcharge event. |  ](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png)
**3** |  **Test Undercharge Voltage** |  Simulate a deep discharge by gradually lowering the voltage. The PCM should cut off the output to protect the battery from over-discharge once the voltage drops below the safe limit. |  ](https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png)
**4** |  **Confirm Undercharge Release** |  Reverse the undercharge condition by increasing the voltage gradually. The PCM should restore output when the voltage reaches a safe level, ensuring the circuit doesn’t remain unnecessarily disabled. |  ](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png)
**5** |  **Confirm Charge Overcurrent Protection** |  Apply a charging current ramp. The PCM must detect when the charging current exceeds the allowable limit and disconnect to prevent overheating or damage. **Note:** To calculate the overcurrent value (**I <sub>end</sub>**), the following formulas are used:
• `Iend = (2 × Capacity × 3600) / t - Istart`
• or `Iend = Istart + DI/sec × LS_Chan_Step_Time` **Capacity logging methods:**
• Use `TestCounter`
• Or fetch the last (previous) step value from the channel |  ](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png) ](https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png) LS_charge_capacity ](https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png) TC_Charge_Capacity
**6** |  **Confirm Discharge Overcurrent Protection** |  Test the PCM’s response to an excessive discharge current. The PCM should cut off the output once the discharge current exceeds the safety threshold. **Note:** Same formula applies as in Step 5:
  * Iend = -(2 × Capacity × 3600) / t + Istart
  * Iend = Istart + DI/sec * LS_Chan_Step_Time

**Capacity logging methods:**
• Use `TestCounter`
• Or fetch the final step value from the channel |  ](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png) ](https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png) LS_discharge_capacity ](https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png) TC_discharge_capacity
  1. **EOL Automation line integration:**

The following images showcase the configuration and automation capabilities of **MITS 11** software in an End-of-Line (EOL) testing environment. These setups are specifically designed to implement the PCM validation tests described above:
**Interface of EOL dashboard** |

**EOL Test Report** |
**Test Summary Details** |  Test |  Criteria |  Measured Value |  Result
1 |  **Overcharge Voltage** |  In Range [4.1, 4.4] V |  4.007742A |  ❌ Failed
2 |  **Overcharge Voltage release** |  In Range [3.5, 4] V |  3.6116747 V |  ✅ Passed
3 |  **Undercharge Voltage** |  In Range [2.8, 3,2] V |  2.992585 V |  ✅ Passed
4 |  **Undercharge Voltage Release** |  In Range [3.35, 3.8] V |  3.406495 V |  ✅ Passed
5 |  **Charge Overcurrent** |  In Range [0.8, 1.26] A |  1.257388 A |  ✅ Passed
6 |  **Discharge Overcurrent** |  In Range [-1.2,- 0.8] A |  -1.191427 |  ✅ Passed
After completing all six critical test steps using ARBIN’s EOL platform, the result shows that the first criteria fails and 5 others succeed. Since one test failed, we can conclude that the PCM does not perform exactly as designed, meaning it failed the test. Only when all 6 tests are passed, the PCM is considered passed.
The set of tests like this ensures that the PCM’s protection logic works well in real operation of the battery after leaving factories. This is essential not only for **battery longevity** but also for **user safety** and **product reliability**.
For further assistance, please contact us: support.asia@arbin.com
For more detail: [Protection Circuit Modules for Custom Battery Packs](https://www.epectec.com/articles/protection-circuit-modules-for-custom-battery-packs.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes)
](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Auxiliary Voltage Measurement](https://www.arbin.com/auxiliary-voltage-measurement.html)
[Integrated Electrochemical Impedance Spectroscopy (EIS) With Arbin Charge/Discharge Channels →](https://www.arbin.com/integrated-electrochemical-impedance-spectroscopy-eis-with-arbin-charge-discharge-channels.html)
