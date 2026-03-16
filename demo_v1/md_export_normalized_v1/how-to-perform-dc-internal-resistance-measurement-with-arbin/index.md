# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | How to perform DC Internal Resistance measurement with Arbin? |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/how-to-perform-dc-internal-resistance-measurement-with-arbin.html |
| Category     | Application Notes                                  |
| Last Updated | September 22, 2025                                |

# Overview

Arbin’s MITS software uses a pulse method to calculate internal resistance (IR) by measuring the IR 10 times and taking the average.

# Key Features

| Feature | Description |
|---------|-------------|
| Measurement method | Pulse method |
| Accuracy | Average of 10 measurements |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Minimum voltage change | 10 | mV | During IR measurement |
| Offset current | 0 | A | Default value |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Max current | 5, 1, 0.1, 0.01, 0.001, 0.0001 | A | Ranges available on Arbin chassis |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Extra control value | 100 | ms | Minimum pulse length before voltage change is measured |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| IR measurement | Internal resistance measurement using pulse method | Average of 10 measurements |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| MITS | Software for measuring internal resistance | Uses pulse method for accuracy |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Arbin chassis | Contains current ranges for measurement |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Autocalibration box | Sold separately | N/A |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| IEC 61960 measurement | Internal resistance measurement according to international standard | [Link](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html) |

# Notes

* Autocalibration box is sold separately.
