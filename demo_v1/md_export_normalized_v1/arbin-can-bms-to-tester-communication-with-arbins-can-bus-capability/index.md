# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Arbin CAN: BMS-to-Tester Communication with Arbin’s CAN Bus Capability |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/arbin-can-bms-to-tester-communication-with-arbins-can-bus-capability.html |
| Category     | Arbin News                                        |
| Last Updated | March 10, 2022                                    |

# Overview

Testing the Battery Management System (BMS) for a battery pack is a critical element in the battery validation process. The Arbin CAN interface allows the BMS to communicate essential information to an external interface, such as the battery test equipment, enabling real-time control and dynamic limits.

# Key Features

| Feature | Description |
|---------|-------------|
| Flexible CAN communication | Allows for a wide variety of testing applications without third-party equipment. |
| Dynamic control | Enables real-time adjustments to testing parameters during a test. |
| Customizable protocols | Users can import and customize their own CAN configurations. |
| Monitoring capabilities | Real-time monitoring of CAN information and data comparison. |
| Data export options | Ability to export CAN and I/V data in CSV or Excel formats. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Communication protocol | CAN Bus | - | - |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Interface type | CAN | - | - |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Dynamic upper limit | Variable | - | Controlled via CAN messages |
| Dynamic lower limit | Variable | - | Controlled via CAN messages |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Operating temperature | - | - | Not specified |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Control capability | Full | - | Through BMS and external sources |
| Protocol customization | Yes | - | Import dbc files |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CAN Define | Customize your CAN configuration | Import dbc files, assign nicknames |
| CAN Control | Fully control the Arbin battery tester | Read/write integration, dynamic limits |
| CAN Monitor | Monitor CAN information | Real-time monitoring, report generation |
| CAN View Data | View and export CAN and I/V data | Export to CSV or Excel |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| Mits Pro | Arbin's software for monitoring and control | Real-time CAN monitoring and control |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Arbin Tester | Battery testing equipment that interfaces with BMS via CAN Bus |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| None | - | - |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| None | - | - |

# Notes

* Autocalibration box is sold separately.
* EIS testing device is sold separately.
