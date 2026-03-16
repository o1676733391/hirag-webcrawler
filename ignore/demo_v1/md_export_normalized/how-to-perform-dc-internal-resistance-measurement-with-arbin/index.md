# Metadata

| Field | Value |
|------|------|
| Title | How to perform DC Internal Resistance measurement with Arbin? |
| Page Type | Technique |
| Source URL | https://www.arbin.com/how-to-perform-dc-internal-resistance-measurement-with-arbin.html |
| Category | Application Notes |
| Last Updated | September 22, 2025 |

# Overview

Arbin’s MITS software uses pulse method to calculate internal resistance (IR). To achieve better accuracy, the software measures the IR 10 times and takes the average.

# Principle

The IR calculation formula is as follows:
IR = Average {(Voltage at P2 - Voltage at P3) / (2 * IIR)}

# Key Parameters

| Parameter | Description |
|-----------|-------------|
| IIR | Amplitude value |
| T2 | Extra control value |
| I0 | Offset value |

# Applications

The schedule for IR calculation involves two steps:
1. Rest step: Mainly plays the role of initial safety check.
2. Internal Resistance steps.

# Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Amplitude | 10 | mV | Applied current value should generate at least this voltage change during IR measurement. |
| Current range | 0.1C | A | Current should be at least this value of the battery. |
| Extra control value | 100 | ms | Determines the current pulse length before voltage change is measured. |
| Offset | 0 | A | Default value; output current pulse will be symmetric. |

# Related Techniques

For international standard measurement, refer to the article: [How to perform Internal Resistance measurement according to IEC 61960 with Arbin?](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html)

# Notes

* Current ranges are written on the label attached to the Arbin chassis, including values such as 5A, 1A, 0.1A, 0.01A, 0.001A, 0.0001A. If 0 (default) is set, the range will be chosen automatically by the machine.
