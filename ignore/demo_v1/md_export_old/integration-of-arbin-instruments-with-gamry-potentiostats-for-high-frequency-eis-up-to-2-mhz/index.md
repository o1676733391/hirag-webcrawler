# Source

- URL: https://www.arbin.com/integration-of-arbin-instruments-with-gamry-potentiostats-for-high-frequency-eis-up-to-2-mhz.html

# Content

#  Integration of Arbin Instruments with Gamry Potentiostats for High-Frequency EIS up to 2 MHz
September 8, 2025
According to the standard specifications published by Arbin, integrating a Gamry device with an Arbin system typically limits the device’s original frequency capability from **2 MHz** down to **100 kHz**. However, in this article, we will introduce a solution that allows the system to **retain the full 2 MHz frequency** , with some trade-offs to consider.
## Pre-Conditions for Achieving 2 MHz EIS with Gamry
Incorporating Electrochemical Impedance Spectroscopy (EIS) into battery testing workflows at high frequencies presents **two major challenges** that must be addressed to maintain Gamry’s full **2 MHz capability** :
1. **Direct Connection to the Battery is Required**
At high frequencies, electrical signals become extremely sensitive to **parasitic inductance** and **contact resistance**. To ensure measurement accuracy, the Gamry device **must be connected directly to the battery terminals** using **Gamry-supplied cables**. Avoid any test fixtures, intermediate connectors, or third-party extensions that could degrade signal quality.
  1. **Use Short, Specialized Cables ( <60 cm)**

Cable length is critical when operating at 2 MHz. Even an extra few centimeters can introduce **signal distortion** or **unwanted noise**. Only **Gamry’s shielded cables** , with a length of **less than 60 cm** , should be used to preserve signal integrity.
## **Connection and Configuration**
**Connection Diagram example**
To assist with proper setup, refer to the example **connection diagram** below:

## Integration Example
In this example, we will integrate the following components:
  * A **High Precision Battery Testing System (HPS All-In-One)** with **two integrated mini temperature chambers**
  * **Two Gamry devices** (one dedicated to each temperature chamber)

By default, Arbin’s standard configuration connects the Gamry device to the system via the **ACIM port** , which restricts the Gamry’s usable frequency to **100 kHz**. To retain the **full 2 MHz capability** , we will instead connect the Gamry device **directly to the battery terminals**.
However, since the user also requires **temperature control during testing** , the Gamry cables must pass through the **hole in the pressure valve** (highlighted in red in the image). After routing the cables through this opening, the cable heads can then be connected directly to the battery.

## Arbin & Gamry software configuration
**Step 1: Gamry software**
Locate the Gamry device’s serial number directly on the device.
For this setup, the relevant serial numbers are **36072** and **36075**.

**Step 2: Device Setup in Gamry**
Assign the two Gamry devices as follows:
  * **Gamry 1** → IFC1010-36072
  * **Gamry 2** → IFC1010-36075

You can adjust the device order using the **green arrow button**.
The system assigns device IDs sequentially from **top to bottom** , starting with **1** , then **2, 3, …** depending on the order.

**Gamry instrument manager**
**Step 3: Mapping Gamry Devices to Arbin Software**
Once the Gamry devices have been set up, they need to be mapped within the Arbin software:
  * **Gamry 1 (IFC1010-36072)** → Map to the first channel in Arbin.
  * **Gamry 2 (IFC1010-36075)** → Map to the second channel in Arbin.

This mapping ensures proper synchronization between the Gamry instruments and Arbin’s control system, allowing the devices to operate correctly during experiments.

**MITS 8 software**

**MITS 10 software**
With the mapping in place, device control is automatically synchronized between the Arbin IV boards and the Gamry instruments:
  * When running a channel on the **first IV board (192.168.1.6)** , the **EIS step (pause step)** will trigger **Gamry 1 (serial 36072)** to perform the EIS test on the battery.
  * When running a channel on the **second IV board** , the **EIS step** will instead trigger **Gamry 2 (serial 36075)** to perform the test.

This configuration ensures that each IV board communicates with its assigned Gamry device consistently during EIS testing.
## Result:
2MHz → 0.1Hz
BODE
Nyquist:

NYQUIST
1Hz → 2MHz

BODE
Nyquist:

NYQUIST
##  _**Trade off**_ :
**Trade-Off Considerations**
  * **Standard Configuration**
In the default setup, Gamry’s cables are connected to the Arbin machine’s **ACIM port** , which is shared by all channels on the same board.
    * This means **two channels can share a single Gamry device**.
    * The devices are able to work **synchronously** , ensuring that one channel can wait for the other as needed.
  * **High-Frequency Configuration (2 MHz)**
To achieve **2 MHz operation** , Gamry’s cables are **not** connected to the **Arbin ACIM port** , but **directly to the battery**.
    * In this mode, schedules can only be executed **on the specific channel being run**.
    * Shared synchronous operation between channels is **not possible** under this setup

[Battery Dynamics Exploration: Insights and Implications of Relaxation Time in Electrochemical Impedance Spectroscopy](https://ris.utwente.nl/ws/portalfiles/portal/425997144/Battery_Dynamics_Exploration_Insights_and_Implications_of_Relaxation_Time_in_Electrochemical_Impedance_Spectroscopy.pdf)
[EIS Integration Solution Highlight](https://www.arbin.com/battery-research/eis-integration-solution-highlight.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Electrochemical Impedance Spectroscopy (EIS)](https://www.arbin.com/category/application-notes/eis-electrochemical-impedance-spectroscopy)
](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← How to perform Internal Resistance measurement according to IEC 61960 with Arbin?](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html)
[Enhancing Battery Testing Safety with a Door Switch Interlock System →](https://www.arbin.com/enhancing-battery-testing-safety-with-a-door-switch-interlock-system.html)
