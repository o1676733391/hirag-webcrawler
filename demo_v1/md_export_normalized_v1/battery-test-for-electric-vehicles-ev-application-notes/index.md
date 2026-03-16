# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Battery Test for Electric Vehicles (EV) Application Notes |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/battery-test-for-electric-vehicles-ev-application-notes.html |
| Category     | Application Notes                                  |
| Last Updated | May 23, 2025                                      |

# Overview

This application notes introduce electric vehicles (EV). Arbin works with electric vehicle industry leaders around the world, and provides a comprehensive battery test solution for cells, modules, and packs of all sizes.

# Key Features

| Feature | Description |
|---------|-------------|
| Testing standards | Developed by US Council for Automotive Research, Environmental Protection Agency, and local state governments. |
| Dynamic testing | Requires both cells and battery packs to be charged/discharged based on various real-world applications. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Minimum temperature | -30 | °C | Cold Cranking Test |
| Discharge power | 7 | kW | Cold Cranking Test |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Battery Size Factor | BSF | - | Minimum number of units required for targets. |
| Nominal Voltage | V nominal | - | Difference between Vmax and Vmin. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| HPPC Current | I HPPC | - | Constant Power Discharge target / (Vnominal * BSF) |
| Low Current HPPC Test | Discharge pulse | - | IHPPC * 2.5 |
| High Current HPPC Test | Discharge pulse | - | 75% of max current rating |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Testing temperature | -30 | °C | Cold Cranking Test |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Test duration | 10 | seconds | HPPC Discharge |
| Test intervals | 12 | seconds | Cold Cranking Test |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| HPPC | Hybrid Pulse Power Characterization | Discharge and regen pulses |
| Cold Cranking | Measures power capability at low temperature | 2-s power capability |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| Current simulation | Combines charge and discharge steps | Simulates current |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Arbin Battery Cycler | Equipment used for testing |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| Autocalibration box | Sold separately | - |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| Turnkey Battery Testing | Comprehensive testing solution | https://www.arbin.com/turnkey-battery-testing.html |
| NiMH Battery Detection | Method for detecting fully charged status | https://www.arbin.com/how-to-detect-nimh-battery-fully-charged-status.html |

# Notes

* HPPC Discharge and Regen rate should be defined by the “Low Current HPPC” or “High Current HPPC” rates, or based on manufacturer recommended values.
* Vmin and Vmax should be based on manufacturer recommended values.
* Discharge rate should be based on IHPPC, or manufacturer recommended values.
* Charge and Discharge rate should be based on manufacturer recommended values.
