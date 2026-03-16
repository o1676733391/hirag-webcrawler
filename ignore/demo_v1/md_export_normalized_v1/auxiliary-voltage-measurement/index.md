# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Auxiliary Voltage Measurement                        |
| Page Type    | Product                                            |
| Source URL   | https://www.arbin.com/auxiliary-voltage-measurement.html |
| Category     | Measurement Equipment                               |
| Last Updated | July 17, 2025                                      |

# Overview

The Arbin Auxiliary Voltage Input Module enables precise, high-resolution voltage monitoring for battery testing applications that require measurements beyond the standard I/V channels. It supports 8 independent channels with a ±5 V input range, ultra-high input impedance (100 GΩ), and 24-bit resolution.

# Key Features

| Feature | Description |
|---------|-------------|
| Number of inputs | 8 |
| Input range | ±5 V, ±10 V, ±25 V, ±50 V, ±100 V |
| Input impedance | 100 GΩ |
| Measurement accuracy | ±0.05% FSR |
| Measurement resolution | 24-bit |
| Common mode voltage range | Up to 500 V |
| Channel isolation | Electrically isolated inputs (high common mode) |
| Series connection support | Inputs may be connected in series |

# Technical Specifications

## Electrical Specifications

| Parameter | Config 1 | Config 2 | Config 3 | Config 4 | Config 5 | Unit | Notes |
|-----------|-----------|-----------|-----------|-----------|-----------|------|-------|
| Input range | -5 to 5 | -10 to 10 | -25 to 25 | -50 to 50 | -100 to 100 | V | Available options |
| Measurement accuracy | ±0.05 | | | | | % FSR | |
| Measurement resolution | 24 | | | | | bit | |
| Common mode voltage range | Up to 500 | | | | | V | |
| Sampling speed | 45 | | | | | ms | |
| Input impedance | 100 | | | | | GΩ | |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Number of inputs | 8 | | Offered in multiples of 8, up to 512 inputs. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Measurement accuracy | ±0.05% | FSR | |
| Measurement resolution | 24-bit | | |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Operating temperature | | | |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Channel isolation | Electrically isolated inputs | | High common mode |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| Mapping flexibility | User-defined mapping of auxiliary voltage inputs to main I/V channels | 1:1, 1:many, many:1 |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| MITS | Arbin’s software for logging and monitoring | Synchronous logging with main I/V channels |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Auxiliary voltage module | Provides 8 independent channels for voltage measurement |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Auxiliary connector | Phoenix, 2-Pin, Female, 5.08 mm | Arbin PN: 306130, Phoenix PN: 1777989 |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| Auxiliary Temperature Measurement | Measurement module for temperature | [Link](https://www.arbin.com/auxiliary-temperature-measurement.html) |
| Protection Circuit Module Testing | Testing solution for PCM | [Link](https://www.arbin.com/how-to-test-a-protection-circuit-module-pcm-using-arbin-eol.html) |

# Notes

* Auxiliary data is logged at the same rate as main I/V channel data and synchronized with the main I/V channel data based on test schedule setting.
* Autocalibration box is sold separately.
* EIS testing device is sold separately.
