# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Constant-C-rate w.r.t. actual capacity, rather than constant current with Arbin cyclers |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/constant-c-rate-w-r-t-actual-capacity-rather-than-constant-current-with-arbin-cyclers.html |
| Category     | Application Notes                                   |
| Last Updated | June 30, 2025                                      |

# Overview

This document discusses the method of using a constant C-rate with respect to the actual capacity of batteries during charge and discharge cycles, utilizing Arbin's MITS software.

# Key Features

| Feature | Description |
|---------|-------------|
| Constant C-rate | Maintains cycle time by adjusting current based on actual battery capacity. |
| MITS software | Facilitates the implementation of constant C-rate cycling. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Current   | 1     | A    | Fixed value for testing. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Software  | MITS  |      | Used for battery testing. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Nominal Capacity | Defined in test object |      | Initial capacity of the battery. |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Temperature | N/A |      | Not specified in the document. |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Cycle Method | Constant C-rate |      | Adjusts based on actual capacity. |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| Constant C-rate | Maintains cycle time by adjusting current based on actual battery capacity. | Nominal Capacity, Current |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| MITS     | Software for battery testing | Allows for constant C-rate cycling. |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| MITS Software | Manages battery testing cycles. |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| N/A    | No additional modules specified. |      |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| N/A     | No related products specified. |      |

# Notes

* Autocalibration box is sold separately.
* Evaluating degradation under real-world charging patterns (like EVs charging overnight).
* Conducting accelerated aging tests where cycle time must remain fixed to analyze time-based degradation factors.
* Reference to: 
  * [BU-402: What Is C-rate?](https://batteryuniversity.com/article/bu-402-what-is-c-rate)
  * [ScienceDirect Article](https://www.sciencedirect.com/science/article/pii/S2950345024000198)
  * [Nature Article](https://www.nature.com/articles/s41560-024-01675-8)
