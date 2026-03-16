# Metadata

| Field | Value |
|------|------|
| Title | Integration of Arbin Instruments with Gamry Potentiostats for High-Frequency EIS up to 2 MHz |
| Page Type | Article |
| Source URL | https://www.arbin.com/integration-of-arbin-instruments-with-gamry-potentiostats-for-high-frequency-eis-up-to-2-mhz.html |
| Category | Application Notes |
| Last Updated | September 8, 2025 |

# Overview

According to the standard specifications published by Arbin, integrating a Gamry device with an Arbin system typically limits the device’s original frequency capability from **2 MHz** down to **100 kHz**. However, in this article, we will introduce a solution that allows the system to **retain the full 2 MHz frequency**, with some trade-offs to consider.

# Key Points

| Topic | Summary |
|------|------|
| Pre-Conditions for Achieving 2 MHz EIS with Gamry | Incorporating Electrochemical Impedance Spectroscopy (EIS) into battery testing workflows at high frequencies presents **two major challenges** that must be addressed to maintain Gamry’s full **2 MHz capability**. |
| Direct Connection to the Battery | At high frequencies, electrical signals become extremely sensitive to **parasitic inductance** and **contact resistance**. To ensure measurement accuracy, the Gamry device **must be connected directly to the battery terminals** using **Gamry-supplied cables**. Avoid any test fixtures, intermediate connectors, or third-party extensions that could degrade signal quality. |
| Use Short, Specialized Cables | Cable length is critical when operating at 2 MHz. Only **Gamry’s shielded cables**, with a length of **less than 60 cm**, should be used to preserve signal integrity. |

# Detailed Explanation

## Connection and Configuration

**Connection Diagram example**  
To assist with proper setup, refer to the example **connection diagram** below:

## Integration Example

In this example, we will integrate the following components:
- A **High Precision Battery Testing System (HPS All-In-One)** with **two integrated mini temperature chambers**.
- **Two Gamry devices** (one dedicated to each temperature chamber).

By default, Arbin’s standard configuration connects the Gamry device to the system via the **ACIM port**, which restricts the Gamry’s usable frequency to **100 kHz**. To retain the **full 2 MHz capability**, we will instead connect the Gamry device **directly to the battery terminals**. However, since the user also requires **temperature control during testing**, the Gamry cables must pass through the **hole in the pressure valve** (highlighted in red in the image). After routing the cables through this opening, the cable heads can then be connected directly to the battery.

## Arbin & Gamry Software Configuration

**Step 1: Gamry Software**  
Locate the Gamry device’s serial number directly on the device. For this setup, the relevant serial numbers are **36072** and **36075**.

**Step 2: Device Setup in Gamry**  
Assign the two Gamry devices as follows:
- **Gamry 1** → IFC1010-36072
- **Gamry 2** → IFC1010-36075

You can adjust the device order using the **green arrow button**. The system assigns device IDs sequentially from **top to bottom**, starting with **1**, then **2, 3, …** depending on the order.

**Gamry Instrument Manager**  
**Step 3: Mapping Gamry Devices to Arbin Software**  
Once the Gamry devices have been set up, they need to be mapped within the Arbin software:
- **Gamry 1 (IFC1010-36072)** → Map to the first channel in Arbin.
- **Gamry 2 (IFC1010-36075)** → Map to the second channel in Arbin.

This mapping ensures proper synchronization between the Gamry instruments and Arbin’s control system, allowing the devices to operate correctly during experiments.

**MITS 8 Software**  
**MITS 10 Software**  
With the mapping in place, device control is automatically synchronized between the Arbin IV boards and the Gamry instruments:
- When running a channel on the **first IV board (192.168.1.6)**, the **EIS step (pause step)** will trigger **Gamry 1 (serial 36072)** to perform the EIS test on the battery.
- When running a channel on the **second IV board**, the **EIS step** will instead trigger **Gamry 2 (serial 36075)** to perform the test.

This configuration ensures that each IV board communicates with its assigned Gamry device consistently during EIS testing.

# Data / Statistics

| Metric | Value | Context |
|------|------|------|
| Frequency Range | 0.1 Hz to 2 MHz | EIS testing capability |

# Trade-Off Considerations

| Configuration | Description |
|------|------|
| Standard Configuration | In the default setup, Gamry’s cables are connected to the Arbin machine’s **ACIM port**, which is shared by all channels on the same board. This means **two channels can share a single Gamry device**. The devices are able to work **synchronously**, ensuring that one channel can wait for the other as needed. |
| High-Frequency Configuration (2 MHz) | To achieve **2 MHz operation**, Gamry’s cables are **not** connected to the **Arbin ACIM port**, but **directly to the battery**. In this mode, schedules can only be executed **on the specific channel being run**. Shared synchronous operation between channels is **not possible** under this setup. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| Electrochemical Impedance Spectroscopy (EIS) | A technique used to measure the impedance of a system over a range of frequencies. |

# Notes

*Battery Dynamics Exploration: Insights and Implications of Relaxation Time in Electrochemical Impedance Spectroscopy*  
*EIS Integration Solution Highlight*
