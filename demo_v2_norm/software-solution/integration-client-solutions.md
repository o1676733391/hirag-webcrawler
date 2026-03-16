# Metadata

| Field | Value1 |
|------|------|
| Title | Integration Client Solutions |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/integration-client-solutions.html |
| Category | Integration Solutions |
| Last Updated | |

# Overview

Arbin Intelligent Client (ArbinClient) is a significant upgrade from its predecessors and built upon the Data Acquisition Service (DAS), which is a core component of MITS 11. ArbinClient offers a streamlined and user-friendly API that simplifies the control and management of Arbin machines, reducing development time and minimizing command latency.

# Key Features

| Feature | Description |
| Granular control and scripting capabilities | ArbinClient empowers users with precise management of various experiment parameters and settings. Its support for Python and C# scripting enables automated testing and the creation of complex experiment sequences. |
| Faster development | The intuitive API of ArbinClient facilitates rapid integration, allowing developers to create custom applications and workflows with minimal effort. This accelerates development cycles and reduces time-to-market. |
| Hardware-in-Loop (HIL) integration | Adjusts the experiment schedule based on real-time measurements, enabling more dynamic and responsive testing. |
| Downward compatibility | ArbinClient is designed to be compatible with MITS 10. If you're still using MITS 10, ArbinClient can call the built-in Arbin CTI interface, ensuring seamless communication and functionality. This allows you to benefit from ArbinClient's advanced features without the immediate need to upgrade to MITS 11. |

# Software Integration

| Module | Purpose | Methods |
| Authentication | Authenticates the user and establishes a connection to the DAS backend. | /ArbinEOL/Login |
| Test Profile Management | Creates, manages, and executes test profiles. | /ArbinEOL/GetTestObjects, /ArbinEOL/GetSchedules, /ArbinEOL/GetEOLVariables |
| Test Execution and Monitoring | Controls the operational state of channels during a test and monitors test progress. | /ArbinEOL/GetEOLChannelsData, /ArbinEOL/StartTest, /ArbinEOL/GetCANConfig |
| Test Reporting | Generates and manages test reports. | /ArbinEOL/GetAllTestsRecords, /ArbinEOL/GetTestsRecordByTestID, /ArbinEOL/GetTestsRecordsByResult |

# Notes

*All commands are executed 1000 times except for the command involving control channel operation, which is executed only 100 times.*
