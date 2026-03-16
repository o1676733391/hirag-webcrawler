# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Schedule and State Machine Diagram for Step        |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/software-solution/schedule-and-state-machine-diagram-for-step.html |
| Category     | Software                                           |
| Last Updated |                                                     |

# Overview

The Schedule and State Machine Diagram for Step allows customers to edit the Schedule to customize and execute specific tests for their applications. The Schedule consists of individual units called steps, each representing a distinct phase or action within the overall testing process.

# Key Features

| Feature | Description |
|---------|-------------|
| Flexible Schedule | Users can specify various control types for battery tests. |
| Customizable Logging | Users can configure log conditions for data recording. |
| State Machine Approach | Ensures smooth transitions between test phases. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Control Value (Current) | 1 | A | Charging or discharging current. |
| Control Value (Voltage) | 1 | V | Voltage value for tests. |
| Control Value (Power) | 1 | W | Power value for tests. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum Subroutines | 500 | steps | Includes main schedule and sub-schedule. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Log Limit | - | - | Trigger for logging data. |
| Step Limit | - | - | Trigger for transitioning to the next state. |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Temperature Control | - | - | Managed through specific control types. |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sub-Schedule Method | - | - | Enhances modularity and maintainability. |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CC | Constant Current | Current value in amperes (A). |
| CV | Constant Voltage | Voltage value in volts (V). |
| CCCV | Constant Current Constant Voltage | CC and CV values in amperes (A) and volts (V). |
| Pause | Control test pause | Options: Normal, ACIM, T_Chamber. |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| Schedule Editor | Tool for creating schedules and sub-schedules. | Allows assignment of sub-schedules. |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Main Schedule | Primary control framework for tests. |
| Sub-Schedule | Modular component for reusable test routines. |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Sub-Schedule Editor | Tool for managing sub-schedules. | - |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| Battery Testing System | Comprehensive system for battery testing. | - |

# Notes

* Autocalibration box is sold separately.
* EIS testing device is sold separately.
