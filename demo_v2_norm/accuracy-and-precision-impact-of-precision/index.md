# Metadata

| Field | Value1 |
|------|------|
| Title | Accuracy and Precision: Impact of Precision |
| Page Type | Article |
| Source URL | https://www.arbin.com/accuracy-and-precision-impact-of-precision.html |
| Category | Application Notes |
| Last Updated | January 22, 2026 |

# Overview

We previously examined the impact of measurement accuracy in an earlier article. In this article, we shift our focus to the influence of a battery tester’s precision on battery research. In many research applications, parameters such as dV/dt and dQ/dV are widely used. The reliability of these measurements depends heavily on the precision of the battery tester, as small fluctuations or noise in voltage or current can significantly distort their interpretation.

# Key Points

| Topic | Summary |
|------|------|
| dV/dt analysis | In a very short time, even if we assume that the battery voltage is constant, noise can cause a fake ΔV, resulting in a false peak in dV/dt. If we take dt as 1ms, and Voltage is constant during that 1ms, dV/dt = 0. However, due to precision limitation, the value of dV/dt measured becomes 0.5 V/s, which is a huge difference. |
| dQ/dV analysis | The accuracy analysis of dQ/dV and dV/dt are narrowed down to dV/dt accuracy analysis. If dV changes in a very short time of 5ms, with the precision of 1 mV, the dV can easily be distorted from 0.08mV to 0, causing dV/dt to be 0. |
| Case Study | When analyzing dQ/dV, if ΔV is extremely small (tens of µV), measurement noise becomes larger than the real signal, causing dV/dt to collapse to zero and dQ/dV to spike to extremely large values. Most battery analyzers do not compute dV/dt every few milliseconds but wait until the voltage change (ΔV) is larger than a threshold. |

# Detailed Explanation

The value of derivative capacity curve can be expressed as follows:

Because dQ/dt = I, we can write:

dV/dt can be re-written in details as follows:

We can see that in a very short time, even if we assume that the battery voltage is constant in reality, let say V0, the noise can cause a fake ΔV (ΔV = Vi+1 – Vi), resulting in a false peak in dV/dt. To be more precise, if we take dt as 1ms, and Voltage is constant during that 1ms, dV/dt = 0.

If we take the precision as 0.01% FSR, let’s take the FSR as 10V (From -5V to 5V). Then the absolute value of voltage precision is: 10 * 0.01% = 0.001 V or 1 mV.

We examine the worst case where V i+1 = V0 + 1 mV, Vi = V0 – 1 mV. Then ΔV = Vi+1 – Vi = (V0 + 1mV) – (V0 – 1 mV) = 2 mV. 

dV/dt = 1mV/2ms = 0.5 V/s. The real Voltage is 0 as assumption above, the value of dV/dt should be 0. However, we can see that due to precision limitation, the value of dV/dt measured becomes 0.5V/s, which is a huge difference.

In reality, the worst case may hardly happen, however, the example above shows us how substantially the precision limitation can cause to the result of dV/dt. It’s worth highlighting that even with some inaccuracy, if the precision is perfect, the measurement of ΔV is still perfect, because the value of both Vi+1 and Vi are shifted equally.

# Data / Statistics

| Products | Voltage precision | 10 times of voltage precision | Min time interval |
|---|---|---|---|
| Certain Brand X | ±4 mV | ±40 mV | 2500ms |
| Voltage precision – LBT5V | ±1 mV | ±10 mV | 625ms |
| Voltage precision – Arbin HPS | ±120 µV | ±1200 µV = 1.2 ms | 75ms |

# Industry Context

We can see that for a 5V battery tester with precision of +/- 0.04% FSR (4mV), the minimum time interval to calculate dV/dt is 2.5 seconds, which is substantially higher than Arbin HPS (75ms).

# Related Technologies / Concepts

| Concept | Description |
|---|---|
| Battery Test System | A system used to evaluate the performance and characteristics of batteries. |
| Measurement Precision | The degree to which repeated measurements under unchanged conditions show the same results. |

# Notes

* Reference: Arbin Instruments. (2021). _Battery test system accuracy and calibration white paper._ College Station, TX: Arbin Instruments.
* Reference: Arbin Instruments. (2023). _LBT Series product manual (Rev. 2.3)._ College Station, TX: Arbin Instruments.
* Reference: ASTM International. (2020). _ASTM E177-20: Standard practice for use of the terms precision and bias in ASTM test methods._ West Conshohocken, PA: ASTM International. [Standard Practice for Use of the Terms Precision and Bias in ASTM Test Methods](https://doi.org/10.1520/E0177-20)
* Reference: IEC. (2018). _IEC 62660-1:2018 – Secondary lithium-ion cells for the propulsion of electric road vehicles – Part 1: Performance testing._ Geneva, Switzerland: International Electrotechnical Commission.
* Reference: Newman, J., & Thomas-Alyea, K. E. (2004). _Electrochemical systems_ (3rd ed.). Hoboken, NJ: Wiley-Interscience.
