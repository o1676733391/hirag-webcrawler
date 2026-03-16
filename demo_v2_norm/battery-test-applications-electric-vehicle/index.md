# Metadata

| Field | Value1 |
|------|------|
| Title | Electric Vehicle Battery Testing |
| Page Type | Resource |
| Source URL | https://www.arbin.com/battery-test-applications-electric-vehicle/ |
| Category | Battery Testing |
| Last Updated | |

# Overview

Testing for electric vehicle (EV) batteries requires equipment that can address the unique usage conditions that these batteries face on the road. Arbin works with electric vehicle industry leaders around the world, providing comprehensive battery test solutions for dynamic drive cycle simulations, communication with Battery Management Systems (BMS), and more EV battery solutions.

# Key Points

| Topic | Summary |
|---|---|
| Comprehensive solutions | Comprehensive solutions for electric vehicle battery testing |
| Dynamic drive profile simulations | Dynamic drive profile simulations with thousands of data points |
| Cell-isolating battery test chamber | Cell-isolating battery test chamber for temperature stability |
| CAN Bus communication | CAN Bus communication with Battery Management System |

# Detailed Explanation

## Drive Profile (Drive Cycle) Simulations

Compared to traditional battery cycling that may use constant current and constant voltage (CC-CV) charge/discharge profiles, EV testing applications require both cells and battery packs to be charged/discharged based on dynamic drive cycle profiles. Arbin makes performing these drive cycle simulations effortless by simply loading a text file of time-vs-power or time-vs-current data from xlsx, csv, txt, etc., without additional programming. Drive cycle profiles can have millions of data points with intervals as fast as 10mS.

Arbin testers use a power embedded microcontroller for each channel module, so each test channel can perform a unique drive cycle simulation. Additionally, Arbin supports real-time drive profile simulations that can be controlled externally using CANBus protocols.

## True Bipolar Circuitry

Arbin battery test systems use true bipolar circuitry, so there is no switching between charge and discharge. This is critical when performing the dynamic drive cycle simulations for EV battery testing, and allows the Arbin tester to precisely replicate and measure the effects of these drive profiles. Test equipment not using a true bipolar circuit will have undesired spikes and drops in current output when measured with an oscilloscope, even though data reported by the system directly may not show this phenomenon.

## EV Testing and Temperature

Electric vehicle battery testing typically requires a temperature-controlled test environment. By default, US regulators state that all EV cell testing is performed at 30°C unless otherwise stipulated. Arbin has created an innovative temperature chamber for testing EV cells known as the “MZTC” Multi-Chamber.

This cell-isolating battery test chamber isolates each cell or pair of cells (depending on cell size and amperage) to create a safer test environment and maintain greater temperature stability. Each of the 8 mini-chambers offers a unique temperature setpoint and is thermally isolated from the others to prevent thermal run-away or cascading failure events. Arbin’s MZTC battery test chamber also makes connections and interfacing with cells easy.

Arbin also has the option to interface with a variety of third-party temperature chambers from other manufacturers. The software is compatible with most major chamber controller modules around the world, so the Arbin tester can automatically adjust temperature during the test.

## Communication with Battery Management Systems (BMS)

Arbin battery test systems offer an optional CAN Bus interface to communicate with the battery management system (BMS) of electric vehicle battery packs. Arbin’s interface allows both the sending and receiving of CAN messages between the tester and BMS. No third-party equipment, DLL packages, or licenses are needed. It is a complete CAN Bus solution that allows the user to enter or upload their CAN protocols, assign nicknames, and then control the test using these variables and record all data from the BMS to compare with Arbin’s own charge/discharge data.

The Arbin tester can be controlled in real-time via CAN Bus, including assigning a CAN message as a dynamic control value (i.e. charge dynamically based on a CAN signal). This real-time control can come from the BMS or other external source in cases where the BMS is being modeled during testing.

## Auxiliary Inputs for EV Battery Pack Testing

Testing battery packs and modules may require monitoring of the individual cell voltage and/or temperature. Thermocouples or thermistors may be used to monitor cell temperature with an external chamber. Auxiliary inputs will also measure cells within a larger battery pack and allow this data to be compared with data from the BMS (when CAN bus interface is used).

The auxiliary inputs are provided in a small external chassis that is networked with the main Arbin system to allow highly flexible configurations (built-in Ethernet network). Digital and analog voltage signals may be used to send/receive with other hardware such as a digital relay signal to activate a BMS, or notify when a test is ready to proceed.

## Arbin’s Mits Pro Software

Arbin’s Mits Pro software provides the ability to control tests based on current, voltage, power, load, and c-rate, both with constant and dynamic control. Built-in functions are available for Internal Resistance (IR) measurement, drive cycle simulations, mathematical functions, current and voltage ramps, looping, and much more. There are over 90 pre-defined meta variables available to use and users may define and assign custom variables.

## Parallel Test Channels

The ability to parallel test channels is sometimes needed to achieve the high c-rates required for EV battery testing. Individual Arbin test channels may be combined so they function as one to increase the current handling capability. This action is easy to perform in the latest Mits Pro software.

## EV Battery Testing Safety with Arbin Instruments

Arbin systems have multiple layers and redundant safety features to help ensure a failsafe test environment. With Arbin’s testing solutions, you have precise control over safety limits for an entire test, specific steps in the test, and several AI-controlled safety monitoring limits designed by Arbin’s expert engineers. Arbin also uses an exclusive high-power distributed control network that manages a greater number of high-efficiency modules so they last longer and are easier to maintain.

## The Arbin Advantage for Electric Vehicle Battery Testing

At Arbin, we understand the vital role energy storage plays in our everyday life - and its importance to our future. This is why we work hard to provide the best service and testing equipment as a tool for both research and industry. Arbin’s state-of-the-art technology, powerful and flexible software, data capabilities, auxiliaries, and support are all part of the Arbin advantage.

# Data / Statistics

| Metric | Value1 | Context | Notes |
|---|---|---|---|
| Default testing temperature | 30 | °C | US regulators state all EV cell testing is performed at this temperature unless otherwise stipulated. |

# Industry Context

| Factor | Description |
|---|---|
| Electric vehicle testing | Requires specialized equipment to handle unique usage conditions. |

# Related Technologies / Concepts

| Concept | Description |
|---|---|
| Battery Management Systems (BMS) | Systems that manage battery performance and safety. |

# Notes

* Arbin’s MZTC battery test chamber isolates each cell or pair of cells to create a safer test environment and maintain greater temperature stability.
* The Arbin tester can be controlled via CAN Bus, including assigning a CAN message as a dynamic control value.
