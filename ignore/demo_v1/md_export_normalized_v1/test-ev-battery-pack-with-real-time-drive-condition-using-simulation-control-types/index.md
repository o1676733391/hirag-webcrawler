# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Test EV Battery pack with real-time drive condition using Simulation Control types |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/test-ev-battery-pack-with-real-time-drive-condition-using-simulation-control-types.html |
| Category     | Application Notes                                   |
| Last Updated | November 5, 2025                                   |

# Overview

Simulation refers to the ability to input data collected from a non-formulated dynamic regime as a control function. There are three control types: Current Simulation, Load Simulation, and Power Simulation.

# Key Features

| Feature | Description |
|---------|-------------|
| Current Simulation | Uses a current (A) -vs- time (s) profile |
| Load Simulation | Uses a Load (Ohm) -vs- time (s) profile |
| Power Simulation | Uses a power (W) -vs- time (s) profile |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Simulation control interval | 10 | ms | Suggested for best performance |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum channels per board | 16 | channels | Recommended limit for simulation profiles |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Data logging interval | 1 | s | Logged whenever control value changes |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CC | Constant Current | Current profile |
| CV | Constant Voltage | Voltage profile |
| CP | Constant Power | Power profile |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| MITS Pro | Software for creating simulation profiles | Allows creation and editing of .txt files for simulations |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Profile Simulation folder | Directory where simulation profiles are saved |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|

# Notes

* Simulation is generally used on less than 16 channels per channel board. We encourage no more than one simulation profile be run per microcontroller.
* Each line in the simulation profile represents a pulse.
* The pulse amplitude is defined by the right column.
* The pulse ending time is the value on the left column.
* The first pulse’s starting time is 0 by default.
* The "extra 2 points" option adds two additional data points for each line in the simulation file.
* Reference: [Electric Vehicle Battery Testing](https://www.arbin.com/battery-test-equipment/electric-vehicle-battery-testing.html), [INL Digital Library](https://inldigitallibrary.inl.gov/sites/sti/sti/6492291.pdf)
