# Metadata

| Field | Value1 |
|------|------|
| Title | How to Test a Protection Circuit Module (PCM) Using ARBIN EOL |
| Page Type | Technique |
| Source URL | https://www.arbin.com/how-to-test-a-protection-circuit-module-pcm-using-arbin-eol.html |
| Category | Application Notes |
| Last Updated | July 23, 2025 |

# Overview

The Protection Circuit Module (PCM) is a critical electronic component responsible for monitoring and protecting devices across a wide range of applications—from small consumer electronics to large-scale industrial equipment. Its core function is to ensure battery and device safety by preventing hazardous conditions such as overcharging, over-discharging, overcurrent, and short circuits. Arbin offers an End-of-Line (EOL) testing solution tailored for customers’ production lines to evaluate the functionality and reliability of Protection Circuit Modules (PCMs). This testing ensures that the PCM responds appropriately when a battery’s voltage or current exceeds its designed minimum or maximum thresholds. Under such conditions, the PCM should automatically disconnect to prevent damage or safety hazards associated with overvoltage, undervoltage, overcurrent, or short-circuit events.

# Key Points

| Topic | Summary |
|------|------|
| Purpose | To ensure battery and device safety by preventing hazardous conditions. |
| Testing Method | EOL testing solution to evaluate PCM functionality and reliability. |

# Detailed Explanation

The following steps outline the standard procedure implemented using the Arbin EOL system to verify the PCM’s key protection functions. Each step simulates fault conditions to validate the PCM’s ability to disconnect or recover as designed.

## Testing Procedure

| Step | Test Item | Description |
|------|-----------|-------------|
| 1 | Overcharge Protection | Simulate battery overcharging. Gradually increase voltage until the PCM disconnects. Record the voltage at which the output current drops to 0 A. |
| 2 | Overcharge Release | Slowly decrease the variable power supply voltage. Record the voltage at which current output resumes. |
| 3 | Undercharge Protection | Simulate battery undercharging. Gradually decrease the voltage until the PCM disconnects. Record the voltage when the output current drops to 0 A. |
| 4 | Undercharge Release | Slowly increase the variable power supply voltage. Record the voltage at which current output resumes. |
| 5 | Charge Overcurrent Detection | Confirm the overcurrent protection during charging. Gradually increase current and record the value at which the PCM activates the cutoff. |
| 6 | Discharge Overcurrent Detection | Confirm the overcurrent protection during discharging. Gradually increase discharge current and record the value at which the PCM activates the cutoff. |

## Implementing it using Arbin MITS 11 software:

| Step | Test Name | Description |
|------|-----------|-------------|
| 1 | Test Overcharge Voltage | Simulate a battery overcharge condition by gradually increasing the voltage. The PCM should disable the output once the voltage exceeds the predefined threshold. This is confirmed by observing that the output current drops to 0 A. |
| 2 | Confirm Overcharge Recovery | Slowly decrease the voltage to verify that the PCM automatically re-enables output when the voltage returns to a safe range. This step ensures proper recovery behavior after an overcharge event. |
| 3 | Test Undercharge Voltage | Simulate a deep discharge by gradually lowering the voltage. The PCM should cut off the output to protect the battery from over-discharge once the voltage drops below the safe limit. |
| 4 | Confirm Undercharge Release | Reverse the undercharge condition by increasing the voltage gradually. The PCM should restore output when the voltage reaches a safe level, ensuring the circuit doesn’t remain unnecessarily disabled. |
| 5 | Confirm Charge Overcurrent Protection | Apply a charging current ramp. The PCM must detect when the charging current exceeds the allowable limit and disconnect to prevent overheating or damage. **Note:** To calculate the overcurrent value (I<sub>end</sub>), the following formulas are used: Iend = (2 × Capacity × 3600) / t - Istart or Iend = Istart + DI/sec × LS_Chan_Step_Time. **Capacity logging methods:** Use TestCounter or fetch the last (previous) step value from the channel. |
| 6 | Confirm Discharge Overcurrent Protection | Test the PCM’s response to an excessive discharge current. The PCM should cut off the output once the discharge current exceeds the safety threshold. **Note:** Same formula applies as in Step 5: Iend = -(2 × Capacity × 3600) / t + Istart or Iend = Istart + DI/sec * LS_Chan_Step_Time. **Capacity logging methods:** Use TestCounter or fetch the final step value from the channel. |

# EOL Automation Line Integration

The following images showcase the configuration and automation capabilities of MITS 11 software in an End-of-Line (EOL) testing environment. These setups are specifically designed to implement the PCM validation tests described above:

| Interface of EOL dashboard | ![](https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png) |
|----------------------------|------------------------------------------|
| EOL Test Report | ![](https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png) |

# Test Summary Details

| Test | Criteria | Measured Value | Result |
|------|----------|----------------|--------|
| 1 | Overcharge Voltage | In Range [4.1, 4.4] V | 4.007742A | ❌ Failed |
| 2 | Overcharge Voltage release | In Range [3.5, 4] V | 3.6116747 V | ✅ Passed |
| 3 | Undercharge Voltage | In Range [2.8, 3.2] V | 2.992585 V | ✅ Passed |
| 4 | Undercharge Voltage Release | In Range [3.35, 3.8] V | 3.406495 V | ✅ Passed |
| 5 | Charge Overcurrent | In Range [0.8, 1.26] A | 1.257388 A | ✅ Passed |
| 6 | Discharge Overcurrent | In Range [-1.2, -0.8] A | -1.191427 | ✅ Passed |

# Notes

* The set of tests like this ensures that the PCM’s protection logic works well in real operation of the battery after leaving factories. This is essential not only for battery longevity but also for user safety and product reliability.
* For further assistance, please contact us: support.asia@arbin.com
* For more detail: [Protection Circuit Modules for Custom Battery Packs](https://www.epectec.com/articles/protection-circuit-modules-for-custom-battery-packs.html)
