# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Arbin APIs Performance Test Results                 |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html |
| Category     | Software                                           |
| Last Updated |                                                     |

# Overview

All commands are executed 1000 times except for the command involving control channel operation, which is executed only 100 times, and the test results are shown in the table below.

# Key Features

| Feature | Description |
|---------|-------------|
| Local Environment | Client and server are both on the same PC, Mits 10.4.14.16 and ArbinCTI 1.0.70, MCU: LBT21084, 8Ch, each command is executed on one channel only. |
| Wi-Fi Experiment Setup | Local area network (Wi-Fi), Two computers: IP192.168.1.54(Client) and IP192.168.1.107(Server), Mits 10.4.14.16 and ArbinCTI 1.0.70, MCU: LBT21084, 8Ch, each command is executed on one channel only. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Max response time |  | s | Maximum time duration between sending command to CTI and receiving CTI feedback. |
| Min response time |  | s | Minimum time duration between sending command to CTI and receiving CTI feedback. |
| Average response time |  | s | Average time duration between sending command to CTI and receiving CTI feedback. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Client PC |  |  | Mits 10.4.14.16 |
| Server PC |  |  | ArbinCTI 1.0.70 |
| MCU | LBT21084 |  | 8Ch |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Connection timeout |  | s | If a timeout is set, a connection timeout error code is returned if a network connection is not received within the time period. |
| Login timeout |  | s | If the client does not call the PostUserLogin interface to log in within the specified time, the server will disconnect from the network. |
| Active timeout |  | s | If the client does not call any interface within the specified time, the server will disconnect from the network. |
| Post Get Meta Variables | 3 | s | A timeout error code will be returned if the feedback is not received within the specified time. |
| Post Upload File | 1.5 | s | A timeout error code will be returned if the feedback is not received within the specified time. |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CC | Constant Current |  |
| CV | Constant Voltage |  |
| CCCV | Constant Current Constant Voltage |  |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| ArbinCTI | Control and test software | Performance testing of APIs |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Client | Local PC running ArbinCTI |
| Server | Remote server for data processing |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|

# Notes

*Autocalibration box is sold separately.*
**EIS testing device is sold separately.**
