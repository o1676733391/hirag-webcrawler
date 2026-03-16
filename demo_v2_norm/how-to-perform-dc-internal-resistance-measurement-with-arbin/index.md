# Metadata

| Field | Value1 |
|------|------|
| Title | How to perform DC Internal Resistance measurement with Arbin? |
| Page Type | Technique |
| Source URL | https://www.arbin.com/how-to-perform-dc-internal-resistance-measurement-with-arbin.html |
| Category | Application Notes |
| Last Updated | September 22, 2025 |

# Overview

Explanation of the DC Internal Resistance measurement technique using Arbin's MITS software.

# Principle

Arbin’s MITS software uses a pulse method to calculate internal resistance (IR). To achieve better accuracy, the software measures the IR 10 times and takes the average.

# Key Parameters

| Parameter | Description |
| Amplitude | Determines the applied current value. For optimized accuracy, the applied current value should generate at least 10mV voltage change during the IR measurement. In general, the current should be at least 0.1C of your battery. |
| Extra Control Value1 | Determines the current pulse length before voltage change is measured. It should be at least 100ms, depending on your IR test needs (Ohmic resistance or polarization resistance). |
| Offset | The offset current value (A). At default value 0, the output current pulse will be symmetric. |

# Applications

| Application | Description |
| Internal Resistance Measurement | The process of measuring the internal resistance of batteries using the Arbin method. |

# Related Techniques

| Technique | Description |
| IEC 61960 Measurement | An international standard for performing internal resistance measurement. |

# Data / Statistics

| Metric | Value1 | Context | Notes |
| Current ranges | 5A, 1A, 0.1A, 0.01A, 0.001A, 0.0001A | Ranges written on the label attached to the Arbin chassis. |

# Notes

* The IR calculation formula is: IR = Average {(Voltage at P2 - Voltage at P3)/ (2IIR)}.
* If you put 0 (default) for the Max Current, the range will be chosen automatically by the machine.
* Above is IR measuring with Arbin’s method. If you want to follow an international standard, you can refer to this article: [How to perform Internal Resistance measurement according to IEC 61960 with Arbin?](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html)
