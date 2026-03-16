# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | How to perform Internal Resistance measurement according to IEC 61960 with Arbin? |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html |
| Category     | Application Notes                                   |
| Last Updated | August 17, 2025                                    |

# Overview

IR measurement is crucial to have an insight into a battery. This article introduces the IEC 61960 standard and how to implement it using Arbin’s equipment.

# Key Features

| Feature | Description |
| --- | --- |
| IEC 61960 standard | Describes the method for measuring battery internal resistance (IR) using specific discharge pulses. |
| Arbin cyclers | Equipment used to implement the IR calculation according to the IEC 61960 standard. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
| --- | --- | --- | --- |
| Discharge pulse 1 | 0.2 | C | Duration: 10 seconds |
| Discharge pulse 2 | 1 | C | Duration: 1 second |
| DCIR calculation | (V1 – V2) / (I2 – I1) |  |  |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
| --- | --- | --- | --- |
| Execution speed for 8 channels | 1 | ms |  |
| Execution speed for 16 channels | 2 | ms |  |
| Execution speed for 32 channels | 5 | ms |  |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
| --- | --- | --- | --- |
| Switching time | <50 | ms | Typically <20 ms |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
| --- | --- | --- | --- |

## General Specifications

| Parameter | Value | Unit | Notes |
| --- | --- | --- | --- |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
| --- | --- | --- |
| C-Rate control | Used for implementing the IR calculation |  |
| SetValues control | Used for implementing the IR calculation |  |
| CC | Constant Current |  |

# Software Integration

| Software | Description | Capability |
| --- | --- | --- |
| MITS | Software for Arbin cyclers | Implements IR calculation |
| Data Watcher | Software for data export | Configures MV_UD variables for export |

# System Architecture / Infrastructure

| Component | Description |
| --- | --- |
| Arbin cyclers | Equipment used for battery testing and IR measurement |

# Accessories / Optional Modules

| Module | Description | Link |
| --- | --- | --- |

# Related Products / Systems

| Product | Description | Link |
| --- | --- | --- |
| UT677A | Hand-held meter for measuring ACIR at 1kHz | [Link](https://www.uni-trend.co.za/download-catalogue/uni-trend-ut677a-battery-internal-resistance-tester.pdf?srsltid=AfmBOoqd6iqTQB6wkKD6ST4WB03KiDy6ZLqECuSTQhVsr5h5HgXL1R14) |

# Notes

* Autocalibration box is sold separately.
* EIS testing device is sold separately.
* Users may compare the DCIR value obtained by Arbin equipment with other brands, noting that some devices measure ACIR rather than DCIR.
* Reference links for further reading:
  - [Qualifying Containers for Safing Batteries in Runaway](https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-10/Qualifying%20Containers%20for%20Safing%20Batteries%20in%20Runaway.pdf)
  - [Measuring Battery DCIR with a 24xx Graphical SMU and TSP Technology](https://www.tek.com/en/documents/application-note/measuring-battery-dc-internal-resistance-with-a-24xx-graphical-smu-and-tsp-technology)
  - [Internal Resistance: DCIR and ACIR – Battery Design](https://www.batterydesign.net/dcir-acir/)
  - [Measuring impedance](https://budgetlightforum.com/t/measuring-impedance/58431/7?utm_source=chatgpt.com)
