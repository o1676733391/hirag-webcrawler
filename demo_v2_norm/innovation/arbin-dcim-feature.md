# Metadata

| Field | Value1 |
|------|------|
| Title | Arbin DCIM Feature |
| Page Type | Technique |
| Source URL | https://www.arbin.com/innovation/arbin-dcim-feature.html |
| Category | Battery Testing |
| Last Updated | |

# Overview

The Arbin DCIM feature is a state-of-the-art technology to measure battery impedance via a DC method. This is a practical substitute for the ACIM measurement method to get EIS plot while also providing additional benefits.

# Key Points

| Topic | Summary |
|------|------|
| Background | There are two methods to analyze a battery's impedance among a frequency range, AC method and DC method. The AC method, also known as ACIM, applies a set of AC signals with different frequencies to the battery, meanwhile samples both AC current and voltage on the battery. The DC method, namely DCIM, applies a DC current to the battery, meanwhile samples the current and voltage on the battery. |
| Impedance Methods in Graphs | ![ARBIN-Impedence Methods in Graphs](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Impedence-Methods-in-Graphs.png) |
| Arbin's DCIM Feature Benefits | Arbin provides a built-in universal DCIM feature utilizing DC method allowing the user to measure battery's impedance easily. Arbin's DCIM feature focuses on mid-range frequency, does not require additional AC equipment and takes less than 1s test time without disturbing regular battery test. The traditional AC method focuses on a wider frequency range but requires additional AC equipment and a much longer measurement time. |
| Comparison of AC Method and DC Method | | 
| Testing Time | 0.5min~1h | <1s |
| Hardware Requirement | Additional AC source and measurement Equipment required | Built-in Arbin Channel, no additional hardware needed. |
| Applied Signal to Battery | Sinusoidal current/Voltage wave at different frequency | Constant DC current |
| Disturb Battery Test | Disturb regular battery test | Does not disturb regular battery test |
| Frequency Range | 1mHz~1MHz | 1Hz~1kHz |

# Detailed Explanation

The DCIM method can generate similar EIS (Nyquist) plot compared to the one from traditional ACIM method as seen in Diagram 6, with corresponding fitting model parameters shown in Table 1. Thus, it can be a practical substitute for the traditional ACIM method. The test used to create the plot points outlined in the graph and table below was performed on a 18650 cell at 0.05 C source current.

In the Graph: The black curve is the measured EIS (Nyquist) plot via ACIM method. The blue curve is the fitted EIS curve based on measured ACIM method data and battery equivalent circuit. The yellow curve is the fitted EIS curve based on measured DC method data and battery equivalent circuit.

![ARBIN-ACIM vs DCIM](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-ACIM-vs-DCIM.png)

# Data / Statistics

| Metric | DCIM Fitting | ACIM Fitting |
|------|------|------|
| R0 | 0.02795 | 0.02741 |
| R1 | 0.0091541 | 0.00943 |
| C1 | 4.20221 | 3.1126 |
| R2 | 0.006298 | 0.00677 |
| C2 | 0.24452 | 0.1135 |

# How to run DCIM on MITS 11

1. Create new Test Plan, choose schedule "[Built-in] DCIM"
   ![ARBIN-Create new Test Plan](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Create-new-Test-Plan.png)
2. Start the test plan, wait until it finished
   ![ARBIN-Start the test plan, wait until it finished](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Start-the-test-plan-wait-until-it-finished.png)
3. Go to test summary page of that test plan, press advanced, then press DCIM mode to the result when run DCIM calculation with the default parameters
   ![ARBIN-Go to test summary page of that test plan](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Go-to-test-summary-page-of-that-test-plan.png)
4. Update the parameters in Initial Guess sections and press calculate to manually calculate the DCIM.

# Notes

*EIS testing device is sold separately.*
