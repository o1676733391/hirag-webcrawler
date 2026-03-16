# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Frequently Asked Questions                          |
| Page Type    | Resource                                            |
| Source URL   | https://www.arbin.com/support/faqs.html            |
| Category     | Support                                             |
| Last Updated |                                                     |

# Overview

This document provides answers to frequently asked questions regarding the Arbin battery testing system, including troubleshooting steps and technical details.

# Key Features

| Feature | Description |
|---------|-------------|
| Communication Failure | Steps to diagnose communication issues between PC and MCU. |
| Unreasonable Voltage Check | Safety feature to detect loose connections or low battery voltage. |
| CCCV vs. CCCV_WRM | Comparison of two control methods for voltage regulation. |
| Synchronization | Methods to synchronize multiple channels using DI/DO modules. |
| Step Control Error Check | Explanation of error monitoring for current/voltage discrepancies. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Fixed IP Address | 196.168.1.100 | | Default setting for Arbin PC. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| MTCI Channel Reading | 0.00 | degree | Indicates Mitspro setting issue. |
| MTCI Channel Reading | 22 | degree | Indicates MTCI board or chamber controller issue. |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Internal Resistance | | | Calculated during CCCV_WRM control. |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Temperature Channel | | | Must be mapped correctly in the system. |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Safety Limit for Voltage | 20% | | Default setting for unreasonable voltage check. |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CCCV | Constant Current to Constant Voltage control | |
| CCCV_WRM | CCCV with Relaxation Method | |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| ArbinSys.cfg | Configuration file for system settings | Defines IP addresses and control parameters. |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| DI/DO Module | Used for synchronization of multiple channels. |
| MTCI Module | Communicates with chamber controllers. |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| None | | |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| None | | |

# Notes

- Autocalibration box is sold separately.
- EIS testing device is sold separately.
- "Conflict Clamp V" error indicates voltage clamp settings mismatch.
- For large ACCESS database files, use Compact & Repair Database to shrink.
- Windows 10 users can unhide file extensions through Folder Options.
