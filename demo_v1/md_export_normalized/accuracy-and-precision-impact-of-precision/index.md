# Metadata

| Field | Value |
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
| dV/dt analysis | In a very short time, even if we assume that the battery voltage is constant, noise can cause a fake ΔV, resulting in a false peak in dV/dt. |
| dQ/dV analysis | The accuracy analysis of dQ/dV and dV/dt are narrowed down to dV/dt accuracy analysis. |
| Case Study | Voltage precision affects dV/dt and dQ/dV calculation in battery analyzers. |

# Detailed Explanation

The value of derivative capacity curve can be expressed as follows:

Because dQ/dt = I, we can write:

dV/dt can be re-written in details as follows:

We can see that in a very short time, even if we assume that the battery voltage is constant, let say V0, the noise can cause a fake ΔV (ΔV = Vi+1 – Vi), resulting in a false peak in dV/dt. To be more precise, if we take dt as 1ms, and Voltage is constant during that 1ms, dV/dt = 0.

If we take the precision as 0.01% FSR, let’s take the FSR as 10V (From -5V to 5V). Then the absolute value of voltage precision is: 10 * 0.01% = 0.001 V or 1 mV.

We examine the worst case where Vi+1 = V0 + 1 mV, Vi = V0 – 1 mV. Then ΔV = Vi+1 – Vi = (V0 + 1mV) – (V0 – 1 mV) = 2 mV. 

dV/dt = 1mV/2ms = 0.5 V/s. The real Voltage is 0 as assumption above, the value of dV/dt should be 0. However, we can see that due to precision limitation, the value of dV/dt measured becomes 0.5V/s, which is a huge difference. 

In reality, the worst case may hardly happen, however, the example above shows us how substantially the precision limitation can affect the result of dV/dt. It’s worth highlighting that even with some inaccuracy, if the precision is perfect, the measurement of ΔV is still perfect, because the values of both Vi+1 and Vi are shifted equally.

Because we can assume that the accuracy and precision of time measurement is very high and ignore it. In a very short time, the error of current measurement can be ignored also, therefore the accuracy analysis of dQ/dV and dV/dt are narrowed down to dV/dt accuracy analysis. 

Similar to the analysis above, take the example in which dV changes in a very short time of 5ms. Let’s say dV = 0.08mV. In this case dV/dt = 0.08mV/5ms = 0.016V/s. With the precision of 1 mV, the dV can easily be distorted from 0.08mV to be 0, causing dV/dt to be 0, and the infinite high in dQ/dV.

# Data / Statistics

| Metric | Value | Context |
|------|------|------|
| Voltage precision - Certain Brand X | ±4 mV | 10 times of voltage precision: ±40 mV, Min time interval: 2500ms |
| Voltage precision - LBT5V | ±1 mV | 10 times of voltage precision: ±10 mV, Min time interval: 625ms |
| Voltage precision - Arbin HPS | ±120 µV | 10 times of voltage precision: ±1200 µV = 1.2 ms, Min time interval: 75ms |

# Industry Context

| Factor | Description |
|------|------|
| Measurement noise | If ΔV is extremely small (tens of µV), measurement noise becomes larger than the real signal, causing dV/dt to collapse to zero and dQ/dV to spike to extremely large values. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| Battery analyzers | Most battery analyzers (including Arbin) do not compute dV/dt every few milliseconds, instead they wait until the voltage change (ΔV) is larger than a threshold. |

# Notes

* Reference: Arbin Instruments. (2021). _Battery test system accuracy and calibration white paper._ College Station, TX: Arbin Instruments.
* Reference: Arbin Instruments. (2023). _LBT Series product manual (Rev. 2.3)._ College Station, TX: Arbin Instruments.
* Reference: ASTM International. (2020). _ASTM E177-20: Standard practice for use of the terms precision and bias in ASTM test methods._ West Conshohocken, PA: ASTM International. [Standard Practice for Use of the Terms Precision and Bias in ASTM Test Methods](https://doi.org/10.1520/E0177-20).
* Reference: IEC. (2018). _IEC 62660-1:2018 – Secondary lithium-ion cells for the propulsion of electric road vehicles – Part 1: Performance testing._ Geneva, Switzerland: International Electrotechnical Commission.
* Reference: Newman, J., & Thomas-Alyea, K. E. (2004). _Electrochemical systems_ (3rd ed.). Hoboken, NJ: Wiley-Interscience.
