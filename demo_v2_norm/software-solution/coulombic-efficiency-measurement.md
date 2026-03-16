# Metadata

| Field | Value1 |
|------|------|
| Title | Measure Battery's Actual Capacity and Coulombic Efficiency (CE) using Arbin |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html |
| Category | Battery Testing |
| Last Updated | |

# Overview

Battery capacity and Coulombic Efficiency (CE) are critical indicators of a battery's characteristics and suitability for various applications. Researchers use these metrics to evaluate material properties and understand their impact on battery performance. Battery manufacturers rely on these measurements to screen and grade batteries, ensuring that only units meeting quality standards are approved for use. Battery users can assess the State of Health (SOH) of their batteries, enabling accurate predictions of battery life and performance. Battery integrators can grade and match batteries with similar capacities, optimizing overall product performance and extending service life.

# Key Features

| Feature | Description |
|---------|-------------|
| Real-time capacity calculation | Automatically calculates real-time capacity with 100 microseconds time resolution. |
| High-precision measurements | Utilizes high-precision voltage and current measurements during battery tests. |
| Automated testing | Simplifies the measurement of coulombic efficiency, ensuring precise evaluation of battery performance. |

# Measurement Method

A common method for measuring a battery’s performance involves cycling the battery between its empty and full states. During each cycle, the battery’s actual capacity is determined by calculating the total discharged capacity, while the coulombic efficiency (CE) is calculated by dividing the discharge capacity by the charge capacity.

| Metric | Formula |
|--------|---------|
| Charge/Discharge Capacity | ∫ 𝑖(𝑡)𝑑𝑡 |
| Coulombic Efficiency | CE = Discharge Capacity / Charge Capacity |

To achieve stable and repeatable results, it is recommended to use a consistent charge/discharge pattern across all cycles.

# Conduct CE Test on Arbin

Arbin equipment facilitates accurate CE testing by automatically calculating real-time capacity through high-precision voltage and current measurements during battery tests. This automated approach makes measuring coulombic efficiency straightforward and reliable.

## Typical CE Test Procedure

| Step | Description |
|------|-------------|
| Step 1 | Initial Rest |
| Step 2 | Charge battery to full (SOC=100%) |
| Step 3 | Rest for battery reaching electrochemical balance |
| Step 4 | Discharge Battery to empty (SOC=0%) |
| Step 5 | Rest for battery reaching electrochemical balance |
| Step 6 | Loop back to Step 2 |

## Implement this Procedure to Arbin Schedule File

### Criteria for Charge/Discharge Cutoff, Loop Times, and Data Log

# Complete Test Data Summary

## Test Statistics by Cycle

Auto Calculate Capacity and Coulombic efficiency per cycle.

## Test Statistics by Step

## Detailed Test Data

# Notes

*Images are used for illustrative purposes and may not represent actual data.*
