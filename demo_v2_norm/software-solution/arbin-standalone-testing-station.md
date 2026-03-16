# Metadata

| Field | Value1 |
|------|------|
| Title | Arbin Standalone Testing Station |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/arbin-standalone-testing-station.html |
| Category | Testing Software |
| Last Updated | 2024-10 |

# Overview

The Arbin Standalone Testing Station is a software solution designed for testing and monitoring various systems, providing real-time data transmission and analysis.

# Key Features

| Feature | Description |
|---------|-------------|
| Desktop PCs | Deploying MITS software on a private cloud platform enhances the system's flexibility, scalability, and security. |
| Arbin Testing Systems | Perform various tests and measurements, transmitting data in real time to the MITS software. |
| Temperature Chambers | Perform various tests and measurements, transmitting data in real time to the MITS software. |
| Monitoring and Control | Remote access allows users to view live data, check equipment statuses, and troubleshoot remotely. |
| Kafka Service | MITS software receives raw data from the devices and conducts the essential processes of data cleaning, format conversion, and initial analysis. |
| On Cloud Backup | MITS provides continuous status updates on the test equipment and data, reporting back to the user's interface. |
| API Integrations | Enables remote monitoring and control of the MITS software and connected devices. |
| Database System | Includes local and remote databases (including cloud-based databases), used for data storage and backup. |

# Capabilities

| Capability | Description |
|------------|-------------|
| Upgrade & Downgrade Management | Supports over-the-air (OTA) firmware installation through the Web UI, using AIBin files. An AIBin file contains the firmware's hex as well as hardware-firmware-software compatibility details to prevent version-matching issues. |
| Automatic Configuration & Setting | The intuitive system configuration workflow allows for quickly onboarding new Arbin systems to the DAS software. From the Web UI, simply type the IP segment of the test system, and the software will automatically fill in the details of all the MCUs and their configuration. |

# System Requirements

| Requirement | Value |
|-------------|-------|
| Database Performance | PostgreSQL is better performance with increasing data volume compared to other databases. |

# Notes

*GUI schedules are used to control the testing flow of Arbin systems. In the Schedule, you can define values for output voltage, current, and power that will be applied to the battery under test. Test Variables provide the flexibility to achieve complex control flow. There are also many safety layers in place to protect the devices being tested.*

*The MITS Pro X software allows for convenient management of profiles and for setting permission levels by user or group.*

*Dedicated pages in the Web UI let you view detailed test result data. You can visualize your data with charts, compare multiple channels and cycles, and create and customize chart templates. In addition, your data can be exported to Excel and PDF format.*
