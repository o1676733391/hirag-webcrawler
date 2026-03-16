# Source

- URL: https://www.arbin.com/integrated-electrochemical-impedance-spectroscopy-eis-with-arbin-charge-discharge-channels.html

# Content

#  Integrated Electrochemical Impedance Spectroscopy (EIS) With Arbin Charge/Discharge Channels
August 6, 2025
## **Introduction**
Electrochemical Impedance Spectroscopy (EIS) is a foundational diagnostic technique for evaluating battery health, internal resistance, degradation mechanisms, and electrochemical behavior over time. However, EIS is traditionally limited by hardware complexity and high per-channel cost, making it difficult to scale across large battery test systems.
To address these challenges, Arbin Instruments offers an integrated EIS solution in partnership with Gamry Instruments. This solution allows a single Gamry potentiostat to be multiplexed across up to 192 Arbin battery test channels, providing seamless impedance measurements without manual reconnection or additional instrumentation per channel.
## **The Challenge: Scaling EIS Across Many Channels**
In research and production environments, battery test setups may involve dozens or even hundreds of test channels operating simultaneously. Incorporating EIS into these workflows typically presents three major barriers:
  * **Cost & Space Constraints****
** Dedicated EIS systems for each test channel are expensive and occupy significant lab space.
  * **Workflow Inefficiency****
** Switching EIS equipment between channels often requires manual cable changes, interrupting long-duration tests or introducing potential user error.
  * **Data Fragmentation****
** EIS data acquired through standalone instruments is often stored separately from the main test data, making analysis more cumbersome and prone to error.

## **Arbin’s Solution: Integrated Multiplexed EIS**
Arbin’s integrated EIS architecture allows a single-channel Gamry potentiostat to be digitally multiplexed across up to **four Arbin channel modules** , supporting up to **192 individual channels** in total. Each channel can be scheduled to perform EIS without any physical reconnection or interruption to adjacent channels.
## **System Capabilities:**
  * **Multiplexed Control:** One Gamry potentiostat shared across 4 modules (Up to 64 channels per module).
  * **Test Integration:** EIS measurements are scheduled within the Arbin MITS test schedule alongside standard cycling routines.
  * **Synchronized Data:** All EIS results are logged within the Arbin database and time-aligned with voltage, current, temperature, and other measurements.
  * **Flexible Operation:** Measurements can be performed on demand or scheduled at specific test points (e.g., after charge, during rest, after formation).
  * **Test Modes:** Supports both potentiostatic and galvanostatic modes.
  * **Frequency Range:** 10 µHz to 100 kHz (limited by Arbin integration).

This approach dramatically reduces cost and system complexity while maintaining high accuracy and full data traceability. |   **Figure 1: Arbin LBTS21324 with one Gamry integrated**

## **How It Works**
EIS steps are programmed directly into Arbin’s MITS software using the “ACIM” (AC Impedance Measurement) step type. Parameters include:
  * **Initial F(Hz):** The frequency of initial ACIM test, referred to as IHz.
  * **Final F(Hz):** The frequency of the final ACIM test, referred to as FHz.
  * **Point/Decade:** The number of test points in each decade. Decade= Log (IHz / FHz) 393
  * **AC Amplitude RMS:** AC voltage or current. e) DC Base: DC voltage or current.
  * **Test Type:** Current Control (galvanostatic) or Voltage Control (potentiostatic).
  * **AC Peak Value:** The peak value of AC voltage or current.

The system automatically coordinates the multiplexing sequence, performs the impedance test, and returns to standard cycling once complete.

**Figure 2: Test schedule step to modify AC Impedance Measurement parameters**
## **Supported Models**
**Name** |  **Specification****1**

**Gamry 1010E** Potentiostat / Galvanostat / ZRA Recommended for all Arbin LBT up to 20 A per channel. |  Capable of performing EIS from 10 µHz to 2 MHz±12 V Maximum Applied Potential ±1 A Maximum Current 9 Current Ranges
**Gamry 5000E** Potentiostat / Galvanostat / ZRA  Recommended for Arbin LBT and LBTS testers with 20 A or higher per channel. |  Capable of performing EIS from 10 µHz to 1 MHz±6 V Maximum Applied Potential ±5 A Maximum Current 6 Current Ranges
**Gamry 5000P** Galvanostat Recommended for Arbin LBT and LBTS testers with 20 A or higher per channel. |  Capable of performing EIS from 10 µHz to 20 kHz±6 V Maximum Applied Potential ±5 A Maximum Current 6 Current Ranges
**Gamry Ref 3000** Potentiostat / Galvanostat / ZRA  Recommended for Arbin LBT and LBTS Module testers |  Capable of performing EIS from 10 µHz to 1 MHz±32 V Maximum Applied Potential ±3 A (or ±1.5 A @ 32 V) Maximum Current 11 Current Ranges
  1. The listed specifications are listed for reference only. Please refer to Gamry Instruments for the current data sheets and specifications.
  2. Max frequency of 100 kHz when integrating with Arbin cycler.

## **Arbin + Gamry 1010E Accuracy Contour Plot**
To validate system accuracy, Arbin performed benchmarking tests using high-precision resistors (5 mΩ to 10 kΩ) with the Gamry 1010E multiplexed through Arbin cyclers.
The **accuracy contour plot** compares the impedance measurement accuracy of the standalone Gamry vs. the multiplexed Arbin + Gamry setup. Results confirm that:
  * **Accuracy remains within ±1%** for a wide range of frequencies and impedances.
  * Performance is well-suited for cell impedance profiling, state-of-health analysis, and degradation tracking.

**Figure 3: Accuracy Contour Plot**
## **Benefits for Battery Test Labs**
**Benefit** | **Impact**

**Reduced Cost** | One EIS unit supports many test channels
**Improved Throughput** | EIS is integrated with automated test schedules
**No Manual Rewiring** | Reduces test setup errors and technician labor
**Unified Data Format** | EIS data logged directly with cycling data
**Scalable Solution** | Supports high channel density Arbin systems
## **Ideal Applications**
  * Cell R&D and formation monitoring
  * State-of-health degradation tracking over lifecycle tests
  * Benchmarking new chemistries or electrolyte formulations
  * Impedance characterization of fuel cells or supercapacitors
  * EIS-based diagnostics for early failure detection

**Next Steps: What to Know Before Setup**
To help ensure a smooth deployment of the EIS integration, users should confirm the following:
  * Verify Arbin cycler model and firmware compatibility.
  * Confirm Gamry model selection based on system current requirements.
  * Understand EIS test frequency range and its integration limits.
  * Plan EIS steps within the test schedule for minimal test interruptions.
  * Discuss calibration and support with Arbin and Gamry for long-term maintenance.

Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Electrochemical Impedance Spectroscopy (EIS)](https://www.arbin.com/category/application-notes/eis-electrochemical-impedance-spectroscopy), [Schedules](https://www.arbin.com/category/application-notes/schedules)
](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← How to Test a Protection Circuit Module (PCM) Using ARBIN EOL](https://www.arbin.com/how-to-test-a-protection-circuit-module-pcm-using-arbin-eol.html)
[How to perform Internal Resistance measurement according to IEC 61960 with Arbin? →](https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html)
