# Metadata

| Field | Value1 |
|------|------|
| Title | Arbin CAN: BMS-to-Tester Communication with Arbin’s CAN Bus Capability |
| Page Type | Article |
| Source URL | https://www.arbin.com/arbin-can-bms-to-tester-communication-with-arbins-can-bus-capability.html |
| Category | Arbin News |
| Last Updated | March 10, 2022 |

# Overview

Testing the Battery Management System (BMS) for a battery pack is a critical element in the battery validation process. Used to monitor the individual cells in a battery pack, the BMS can communicate essential information to an external interface, such as the battery test equipment. This BMS-to-tester communication has several important functions including verifying the BMS is functioning properly by comparing the BMS readings to the tester measurements. The Arbin CAN interface also allows the BMS to control the tester in real-time and apply dynamic “clamp” limits that can protect or further enhance the testing process. To take advantage of these features, however, the Battery Management System needs a communication protocol. CAN bus is the most common protocol for communication between a cycler and a BMS. It provides a wide range of communication and control capabilities. Arbin’s Mits Pro employs the CAN Bus protocol, allowing CAN messages to be sent and received between the battery test equipment and the Battery Management System, and allows external control of the Arbin tester.

# Key Points

| Topic | Summary |
|-------|---------|
| Advantages of Arbin’s CAN Bus Capability | Arbin’s CAN Bus interface feature offers several important benefits for battery test operators, including flexibility, dynamic control, and customizable configurations. |
| CAN Define | Users can easily import their dbc file with custom CAN protocols, allowing for full customization without additional software or licenses. |
| CAN Control | Full control of the battery test equipment is possible, including read/write integration and dynamic clamp limits. |
| CAN Monitor | The ability to actively monitor CAN information in real-time and generate reports for data comparison. |
| CAN View Data | Options to export CAN and I/V data in CSV or Excel formats for further analysis. |
| Power Clamp Limits | CAN Bus communication allows for dynamic power clamp limits, enhancing testing flexibility without stopping tests. |

# Detailed Explanation

Testing the Battery Management System (BMS) for a battery pack is a critical element in the battery validation process. Used to monitor the individual cells in a battery pack, the BMS can communicate essential information to an external interface, such as the battery test equipment. This BMS-to-tester communication has several important functions including verifying the BMS is functioning properly by comparing the BMS readings to the tester measurements. The Arbin CAN interface also allows the BMS to control the tester in real-time and apply dynamic “clamp” limits that can protect or further enhance the testing process. To take advantage of these features, however, the Battery Management System needs a communication protocol.

CAN bus is the most common protocol for communication between a cycler and a BMS. It provides a wide range of communication and control capabilities. Arbin’s Mits Pro employs the CAN Bus protocol, allowing CAN messages to be sent and received between the battery test equipment and the Battery Management System, and allows external control of the Arbin tester.

## The Advantages of Arbin’s CAN Bus Capability

Arbin’s CAN Bus interface feature offers several important benefits for battery test operators. First, it provides you with a more flexible solution for CAN communication. Versatile enough to address a wide variety of testing applications and profiles, Arbin’s CAN Bus features can be used without third-party equipment, DLL packages, or licenses that are typically required. Through Mits Pro, Arbin’s CAN Bus functionality also allows you to define your own protocols, assign nicknames, and control tests according to your specific needs and testing standards.

Dynamic control of the Arbin cycler is another benefit of this CAN Bus feature. Unlike standard solutions, control of testing with Arbin’s CAN Bus feature is not restricted to static values for the length of the test. You can assign a CAN message to control values dynamically, with different values at various stages of a test. The CAN Bus solution also allows the BMS to fully control the Arbin testers’ charge and discharge using the CAN protocol.

The final key advantage of Arbin’s CAN Bus solution is that it facilitates communication and control between the Arbin battery tester and the Battery Management System in four distinct ways. You can customize the CAN configuration to fit virtually any requirements, allow the BMS to fully control the test equipment, monitor CAN information, and export CAN and I/V data to CSV or Excel formats for reports.

## 1. CAN Define: Customize Your CAN Configuration

Arbin’s CAN interface allows users to easily import their dbc file with custom CAN protocols. Once imported into Arbin’s GUI the CAN dbc is fully customizable to edit, add nicknames to CAN IDs, units can be assigned to IDs, and each can be enabled or disabled for control and logging during the test. No additional 3rd party software, licenses, or DLL packages are required for this level of convenience. A unique CAN configuration file can be assigned to each test channel on the Arbin tester.

## 2. CAN Control: Fully Control the Arbin Battery Tester

Arbin’s CAN Bus capability also offers the ability to fully control your battery test equipment. This includes several key features, such as read/write integration, dynamic upper and lower “clamp” limits, and external control of the tester. Read/write integration with the Battery Management System through CAN Bus allows for full control of the cycler’s charge and discharge. The “Write CAN Message” option can be used to send a command or multiple commands to the BMS throughout a test procedure. Through CAN messages, the BMS can tell the test equipment to charge or discharge at a particular value of current, power, etc. Including dynamic control. This communication can also be used to tell the test equipment to discontinue or slow down the charge or discharge at a certain value.

Dynamic upper and lower “clamp” limits are another important CAN Bus feature enabled through CAN messages. You can set CAN meta-variables that assign dynamic power and current limits in real-time while a test is running, rather than a single static limit that is pre-defined in the test schedule. These dynamic limits help to increase the safety of the system during testing and validate BMS protection of the battery. For example, the BMS can limit the power during a simulation based on the dynamic limit, even when the simulation profile calls for a higher power and/or current level. The dynamic power and current limits are especially important for drive cycle simulations and similar testing applications so the simulation can run without pausing, but the BMS can limit the peak power output of the simulation.

CAN communication also allows for external control of the Arbin battery tester. An external source such as LabView can send CAN messages to control the test equipment. You can also employ the “Write CAN Message” option to send a command to third-party software throughout a test, just as you can through the Battery Management System. This is especially powerful during BMS development.

## 3. CAN Monitor: Monitor CAN Information

Another important feature of CAN is the ability to actively monitor CAN information. The Monitor and Control interface of Arbin’s Mits Pro software lets you monitor CAN details in real-time so that you can see communication and changes as they happen. Additionally, the Monitor and Control interface provides tools to send CAN messages manually. On top of monitoring real-time information, the data monitoring highlights of CAN include generating reports to compare testing data. With this feature, you can conveniently cross-reference the data collected by your battery testing equipment with the data from the Battery Management System in a single results file. Having this data in one location makes it easier to compare and analyze the results.

## 4. CAN View Data: View and Export CAN and I/V Data

Finally, Arbin’s CAN Bus features include export options that give you even more flexibility review, store, and analyze your testing data. You can easily export both CAN and I/V data in either CSV or Excel formats with this capability. The CSV and Excel formats allow you to import your data to third-party programs for more advanced processing.

## Using CAN Bus Communication for Power Clamp Limits

One use case for Arbin’s CAN Bus features in simulation profiles is through power clamp limits. With traditional termination limits, surpassing the limit in an EV (Electric Vehicle) drive profile, for example, means that the test is stopped, halting your testing progress. In addition, the simulation profile will have to be changed manually, to address the battery operating parameters that caused the battery to exceed those safety limits.

Although standard safety limits are still implemented along with the CAN option, CAN Bus communication offers an additional layer of flexibility. CAN protocol can assign a “power clamp” limit that is controlled dynamically over the course of the test. Unlike traditional safety limits, the power clamp limit restricts the power output of the Arbin system without stopping the test. With values that are dynamic over the course of the test, this can better reflect real-life conditions and power output. Using CAN Bus communication to set power clamp limits will not only expedite the testing process, but will also allow for more complex control of the power output limits.

# Data / Statistics

| Metric | Value1 | Value2 | Context | Notes |
|--------|--------|--------|---------|-------|
| Dynamic control capability | Yes |  | Allows for real-time adjustments during testing |  |
| Customizable CAN configuration | Yes |  | Users can import dbc files and customize settings |  |
| Export formats | CSV | Excel | For data analysis and reporting |  |

# Industry Context

| Factor | Description |
|--------|-------------|
| Battery Management System | Essential for monitoring and controlling battery packs during testing. |
| CAN Bus Protocol | Widely used for communication between battery testers and BMS. |

# Related Technologies / Concepts

| Concept | Description |
|---------|-------------|
| Dynamic clamp limits | Allows for real-time adjustments to testing parameters to enhance safety. |
| Real-time monitoring | Enables users to track CAN information and make adjustments as needed. |

# Notes

* Arbin’s CAN Bus feature allows for communication between a BMS and an Arbin battery tester, which is critical for many testing applications.
* Protecting the system and battery and actively controlling test equipment through the Battery Management System are just a few of the benefits from CAN communication.
