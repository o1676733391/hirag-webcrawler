# Metadata

| Field | Value |
|------|------|
| Title | Auxiliary Voltage Measurement |
| Page Type | Product |
| Source URL | https://www.arbin.com/auxiliary-voltage-measurement.html |
| Category | Measurement Instruments |
| Last Updated | July 17, 2025 |

# Overview

The Arbin Auxiliary Voltage Input Module enables precise, high-resolution voltage monitoring for battery testing applications that require measurements beyond the standard I/V channels. Typical use cases include monitoring individual cell or module voltages within a larger pack, measuring reference electrodes in three-electrode cells, or comparing BMS data with directly measured values. Each module supports 8 independent channels with a ±5 V input range, ultra-high input impedance (100 GΩ), and 24-bit resolution. Measurement accuracy is ±0.05% of full-scale range. Additional voltage ranges (±10 V, ±25 V, ±50 V, ±100 V) are available upon request.

The module features high common-mode isolation on all input channels, allowing signals to float independently or be referenced to different grounds. This design enables safe operation in stacked cell configurations, floating reference setups, or systems where inputs need to be connected in series for differential voltage monitoring. Each channel is electrically isolated and can safely accommodate signals with up to 500 V of common-mode voltage. All auxiliary voltage data is logged synchronously with the main I/V channels in Arbin’s MITS software and can be used for safety thresholds, test control, and dynamic step transitions. Channels can be flexibly mapped in one-to-one, one-to-many, or many-to-one configurations relative to the main charge/discharge channels. Compatible cable options include bare wire, banana plug, or alligator clips. The module connects via standard Phoenix 2-pin connectors and integrates easily with new or legacy Arbin systems via plug-and-play auxiliary enclosures.

# Key Features

| Feature | Description |
|---------|-------------|
| Number of Inputs | 8 |
| Input Range | ±5 V, ±10 V, ±25 V, ±50 V, ±100 V |
| Input Impedance | 100 GΩ |
| Measurement Accuracy | ±0.05% FSR |
| Measurement Resolution | 24-bit |
| Sampling Speed | 45 ms |
| Common Mode Voltage Range | Up to 500 V |
| Channel Isolation | Electrically isolated inputs (high common mode) |
| Series Connection Support | Inputs may be connected in series |

# Technical Specifications

## Electrical Specifications
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Input Range | −5 to 5 | V | Standard range |
| Input Range | −10 to 10 | V | Available upon request |
| Input Range | −25 to 25 | V | Available upon request |
| Input Range | −50 to 50 | V | Available upon request |
| Input Range | −100 to 100 | V | Available upon request |
| Input Impedance | 100 | GΩ |  |
| Measurement Accuracy | ±0.05 | % FSR |  |
| Measurement Resolution | 24 | bit |  |
| Sampling Speed | 45 | ms |  |
| Common Mode Voltage Range | Up to 500 | V |  |
| Channel Isolation | Electrically isolated inputs |  | High common mode |
| Series Connection Support | Yes |  | Inputs may be connected in series |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| Voltage Monitoring | Monitoring individual cell or module voltages | 8 independent channels, ±5 V input range |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| MITS Software | Logs auxiliary voltage data synchronously with main I/V channels | Safety thresholds, test control, dynamic step transitions |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Auxiliary Voltage Input Module | Connects via standard Phoenix 2-pin connectors, integrates with Arbin systems |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Auxiliary Connector | Phoenix, 2-Pin, Female, 5.08 mm | Arbin PN: 306130, Phoenix PN: 1777989 |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| Arbin Testing Systems | Compatible with auxiliary voltage input modules | [Arbin Website](https://www.arbin.com) |

# Notes

*Auxiliary data is logged at the same rate as main I/V channel data and synchronized with the main I/V channel data based on test schedule setting.*
