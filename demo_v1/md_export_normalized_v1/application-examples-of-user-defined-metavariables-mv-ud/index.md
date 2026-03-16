# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Application Examples of User-Defined MetaVariables (MV_UD) |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/application-examples-of-user-defined-metavariables-mv_ud.html |
| Category     | Application Notes                                   |
| Last Updated | February 26, 2026                                  |

# Overview

In Arbin software, MV_UD (short for User-Defined Meta Variables) is a powerful tool for controlling battery testers. This article explains how to use MV_UD in Arbin MITS software.

# Key Features

| Feature | Description |
|---------|-------------|
| Storing values in MV_UD | Assigns a fixed value of a physical quantity to the user-defined meta variable. |
| Store variables in MV_UD using SetReference | Stores a reference in an MV_UD meta variable that updates automatically. |
| Update MV_UD from third-party software | Allows control of the current during a test using MV_UD values. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| MV_UD variables available | 16 | - | Total number of MV_UD variables. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Control types | SetValue(s), SetReference(s) | - | Types of controls available for MV_UD. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Charge capacity | 1.2 | Ah | Example value stored in MV_UD3. |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| SetValue(s) | Assigns a fixed value to MV_UD. | Control Value, Extra Control Value1 |
| SetReference(s) | Links a reference to MV_UD that updates automatically. | Control Value |
| Current control | Uses MV_UD value to set current during a test. | MV_UD1 |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| ArbinViewer | Third-party application for updating MV_UDs via CTI. | Allows control of MV_UD values during tests. |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| MITS software | Main software for controlling battery testers. |
| CTI (Console TCP/IP Interface) | Interface for third-party software integration. |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|

# Notes

* Autocalibration box is sold separately.
* EIS testing device is sold separately.
