# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Smart Data Logging (Acquisition) User's Guideline   |
| Page Type    | Resource                                            |
| Source URL   | https://www.arbin.com/software-solution/smart-data-logging-acquistion-users-guideline.html |
| Category     | Data Logging Solutions                              |
| Last Updated |                                                     |

# Overview

For battery researchers and testers who need to study battery performance, data logging is an important factor, providing accurate current, voltage, time, and temperature data to increase testing analysis efficiency.

# Key Features

| Feature | Description |
| Logging method | Smart Data Logging (SDL) |
| Data accuracy | Provides precise measurements to enhance testing efficiency |
| Flexibility | Allows for various logging limits based on voltage, current, and time |

# Technical Specifications

## Electrical Specifications

| Parameter | Config 1 | Config 2 | Config 3 | Unit | Notes |
|-----------|----------|----------|----------|------|-------|
| Voltage change threshold | 1 | 1 | mV | Change in voltage for logging |
| Current change threshold | 2 | 2 | mA | Change in current for logging |
| Time interval threshold | 10 | 10 | ms | Time interval for logging |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum logging rate | 20,000 | points/sec | Maximum for Arbin Mits 8.x |
| SQL database | Yes | | Utilizes SQL for data logging |
| Kafka support | No | | Not supported in Mits Pro 8 |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Data point size | 10 | bytes | Contains two floats and two unsigned chars |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Operating temperature | Not specified | | |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Channel count | 2, 4, 6, 8, 16, 32, 64, 96, 128 | | Number of channels supported |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CC | Constant Current | Current setting |
| CV | Constant Voltage | Voltage setting |
| CCCV | Constant Current Constant Voltage | Combination of CC and CV |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| Arbin Mits 8.x | Data logging software | Supports SDL and SQL database |
| Arbin MITS | Advanced data logging | Supports SDL and Kafka |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| SQL Database | Used for logging data points |
| Kafka | Distributed streaming platform for high throughput |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Autocalibration box | Sold separately | |
| EIS testing device | Sold separately | |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| Arbin Cyclers | Battery testing systems | |

# Notes

* The granularity of ∆V, ∆I, and ∆t value range must be within the precision and accuracy of ADC specification or Arbin Precision System in terms of PPM.
* A system with 100 PPM (100/1M) precision level requires ∆V and ∆I to be in the range of 0.1mV or 0.1mA for valuable data acquisition.
* Lua Script is not available in Mits Pro 8.
