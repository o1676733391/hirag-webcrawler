# Metadata

| Field | Value |
|------|------|
| Title | Measure Battery's Actual Capacity and Coulombic Efficiency (CE) using Arbin |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/coulombic-efficiency-measurement.html |
| Category | Battery Testing |
| Last Updated | |

# Overview

This document describes the measurement of a battery's actual capacity and coulombic efficiency (CE) using Arbin equipment.

# Key Points

| Topic | Summary |
|-------|---------|
| Benefit of Battery’s Capacity and CE measurement | Battery capacity and coulombic efficiency are critical indicators of a battery's characteristics and suitability for various applications. Researchers use these metrics to evaluate material properties and understand their impact on battery performance. Battery manufacturers rely on these measurements to screen and grade batteries, ensuring that only units meeting quality standards are approved for use. Battery users can assess the State of Health (SOH) of their batteries, enabling accurate predictions of battery life and performance. Battery integrators can grade and match batteries with similar capacities, optimizing overall product performance and extending service life. |
| Measurement Method | A common method for measuring a battery’s performance involves cycling the battery between its empty and full states. During each cycle, the battery’s actual capacity is determined by calculating the total discharged capacity, while the coulombic efficiency (CE) is calculated by dividing the discharge capacity by the charge capacity. Charge/Discharge Capacity is calculated using the formula: Charge/Discharge Capacity = ∫ 𝑖(𝑡)𝑑𝑡. Coulombic Efficiency is determined as: Coulombic Efficiency = Discharge Capacity / Charge Capacity. To achieve stable and repeatable results, it is recommended to use a consistent charge/discharge pattern across all cycles. |
| Conduct CE test on Arbin | Arbin equipment facilitates accurate CE testing by automatically calculating real-time capacity (with 100 microseconds time resolution) through high-precision voltage and current measurements during battery tests. This automated approach makes measuring coulombic efficiency straightforward and reliable, ensuring precise evaluation of battery performance. A typical CE test procedure includes: Initial Rest, Charge battery to full (SOC=100%), Rest for battery reaching electrochemical balance, Discharge Battery to empty (SOC=0%), Rest for battery reaching electrochemical balance, Loop back to Step 2. Implement this procedure to Arbin schedule file and add criteria for charge/discharge cutoff, loop times, and data log. |
| Complete Test Data Summary | Test statistics by cycle and step, auto calculate capacity and coulombic efficiency per cycle. |

# Detailed Explanation

The measurement of a battery's actual capacity and coulombic efficiency is essential for understanding its performance. The process involves cycling the battery between its empty and full states, allowing for accurate calculations of both capacity and efficiency. The Arbin system automates this process, providing real-time data and ensuring reliable results.

# Data / Statistics

| Metric | Value | Context |
|--------|-------|---------|
| Time resolution | 100 | microseconds |

# Industry Context

| Factor | Description |
|--------|-------------|
| Battery performance | Critical for applications in various industries, including electric vehicles and renewable energy storage. |

# Related Technologies / Concepts

| Concept | Description |
|---------|-------------|
| Coulombic Efficiency | A measure of how effectively a battery converts input energy into output energy. |

# Notes

*Auto Calculate Capacity and Coulombic efficiency per cycle.*
