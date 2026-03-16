# Metadata

| Field | Value |
|------|------|
| Title | Arbin APIs Performance Test Results |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html |
| Category | Performance Testing |
| Last Updated | 2024-09 |

# Overview

This document presents the performance test results for Arbin APIs. All commands are executed 1000 times except for the command involving control channel operation, which is executed only 100 times.

# Key Points

| Topic | Summary |
|------|------|
| Local Environment | Client and server are both on the same PC with Mits 10.4.14.16 and ArbinCTI 1.0.70, using MCU: LBT21084, 8Ch. Each command is executed on one channel only. |
| Wi-Fi Environment | Local area network (Wi-Fi) with two computers: IP192.168.1.54 (Client) and IP192.168.1.107 (Server), using Mits 10.4.14.16 and ArbinCTI 1.0.70, with MCU: LBT21084, 8Ch. Each command is executed on one channel only. |

# Detailed Explanation

## Definitions

### Max Response Time
The maximum time duration between sending a command to CTI and receiving CTI feedback (confirmation).

### Min Response Time
The minimum time duration between sending a command to CTI and receiving CTI feedback (confirmation).

### Average Response Time
The average time duration between sending a command to CTI and receiving CTI feedback (confirmation).

### Timeout Descriptions

| Timeout Type | Description |
|--------------|-------------|
| Connection Timeout | If a timeout is set, a connection timeout error code is returned if a network connection is not received within the time period. Network connection timeout needs to be set manually; the default is busy waiting for results. |
| Login Timeout | If the client does not call the PostUserLogin interface to log in within the specified time, the server will disconnect from the network. WinDaq has no login timeout. |
| Active Timeout | If the client does not call any interface within the specified time, the server will disconnect from the network. WinDaq has no active timeout. |
| Post Get Meta Variables | A timeout error code will be returned if the feedback is not received within the specified time. |
| Post Upload File | A timeout error code will be returned if the feedback is not received within the specified time. |

## APIs Performance

| Command | Description | Avg (ms) | 99 PCT | 95 PCT | 90 PCT |
|---------|-------------|----------|--------|--------|--------|
| PostAssignFile | Assign files to IV channels | 15.76 | 19.91 | 17.95 | 17.19 |
| PostAssignSchedule | Assign files to IV channels | 21.37 | 23.43 | 22.79 | 22.50 |
| PostCheckFileEx | Check if the file exists | 2.59 | 37.25 | 2.96 | 2.60 |
| PostConvertToAnonymousOrNamedTO | TestObject to anonymous or non-anonymous | 15.82 | 16.58 | 16.37 | 16.30 |
| PostGetChannelInfoEx* | Get TestObject data for IV channel | 0.12 | 0.31 | 0.22 | 0.17 |
| PostGetChannelsDataMinimalistMode* | Getting IV channel data with only current and voltage | 0.11 | 0.30 | 0.19 | 0.15 |
| PostGetChannelsData* | Getting IV channel data | 0.12 | 0.44 | 0.22 | 0.17 |
| PostGetMetaVariables* | Get meta-variables for IV channels | 1.36 | 2.99 | 2.24 | 2.01 |
| PostGetResumeData | Get Resume data for IV channel from database | 22.59 | 26.29 | 24.78 | 24.15 |
| PostGetStartData | Get the initial data needed before Start | 10.27 | 13.26 | 11.96 | 11.39 |
| PostGetServerSoftwareVersionNumber | Get the software version number of the server | 0.90 | 2.24 | 1.36 | 1.26 |
| PostGetStringLimitLength | Get the string limit length, such as: Test Name | 0.93 | 4.18 | 1.38 | 1.24 |
| PostJumpChannel | Control IV channel jump to other step | 17.90 | 19.63 | 18.96 | 18.71 |
| PostResumeChannelEx | Resume IV channel | 118.88 | 134.78 | 125.95 | 124.71 |
| PostResumeChannel | Resume IV channel | 121.41 | 137.65 | 130.98 | 128.67 |
| PostSetMetaVariable | Update a meta-variable of the IV channel | 0.93 | 3.42 | 1.36 | 1.26 |
| PostStartChannelEx | Start IV channel | 49.97 | 56.37 | 54.22 | 53.41 |
| PostStartChannel | Start IV channel | 51.76 | 58.57 | 56.27 | 55.38 |
| PostStopChannel | Stop IV channel | 17.66 | 18.93 | 18.55 | 18.39 |
| PostUpdateMetaVariableAdvanced | Batch update of meta-variables for IV channels | 1.15 | 4.59 | 1.67 | 1.52 |
| PostUpdateParameters | Update parameters, e.g. TestObject parameters | 15.88 | 16.83 | 16.42 | 16.34 |
| PostUserLogin | User login | 2.10 | 5.08 | 3.14 | 2.85 |
| PostBrowseDirectory | Get a list of files and folders in a Directory | 9.56 | 34.15 | 12.15 | 10.40 |
| PostDeleteFile | Delete file | 16.15 | 22.06 | 16.76 | 16.66 |
| PostDownloadFile | Download file | 1.51 | 3.95 | 2.13 | 1.93 |
| PostNewFolder | New Directory | 15.94 | 16.81 | 16.48 | 16.39 |
| PostNewOrDelete | Delete file or new Directory | 15.93 | 16.74 | 16.49 | 16.41 |
| PostUploadFile | Upload file (Block) | 23.47 | 29.84 | 27.49 | 26.57 |
| PostUploadFile | Upload file | 15.76 | 19.91 | 17.95 | 17.19 |

*99% Percentiles (PCT) of client request and response time in milliseconds have proven our integration with other systems will be robust and high performance.

# Notes

*Connection timeout, login timeout, and active timeout descriptions are provided for clarity.*
