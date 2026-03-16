# Metadata

| Field | Value1 |
|------|------|
| Title | Battery Test for Electric Vehicles (EV) Application Notes |
| Page Type | Resource |
| Source URL | https://www.arbin.com/battery-test-for-electric-vehicles-ev-application-notes.html |
| Category | Application Notes |
| Last Updated | May 23, 2025 |

# Overview

This application notes introduce electric vehicles (EV). Arbin works with electric vehicle industry leaders around the world and provides a comprehensive battery test solution for cells, modules, and packs of all sizes. These tests can be easily performed and installed by Arbin’s equipment and accompanying accessories to ensure the accuracy and reliability of the results.

# Key Points

| Topic | Summary |
|------|------|
| EV Testing | Compared to traditional battery cycling that may use exclusively constant current and constant voltage (CC-CV) charge/discharge profiles, EV testing applications require both cells and battery packs to be charged/discharged based on various real-world applications. These charge/discharge profiles are highly dynamic and require much greater current demands relative to traditional testing. |
| Testing Standards | The US Council for Automotive Research, Environmental Protection Agency, and local state governments have all developed and published testing standards for benchmarking batteries and electric vehicle performance. |
| WLTP Standards | The UN Economic Commission has developed the Worldwide Harmonized Light Vehicles Test Procedures (WLTP) standards for electric vehicle battery testing that is now followed by Europe and most Asian countries (India, Japan, Malaysia, S.Korea, Thailand, Vietnam, etc.). |

# Detailed Explanation

## Hybrid Power Pulse Characterization (HPPC) Testing

The Hybrid Pulse Power Characterization (HPPC) Test is intended to determine dynamic power capability over the device’s usable voltage range using a test profile that incorporates both discharge and regen pulses. The objective of this profile is to demonstrate the discharge pulse and regen pulse power capabilities at various depth of discharge (DOD) values for both the Minimum and Maximum PowerAssist goals (10-s discharge, 10-s regen). The normal test protocol uses constant current (not constant power) at levels derived from the manufacturer’s maximum rated discharge current.

### HPPC Introduction

- **Battery Size Factor (BSF)**: The minimum number of units (cell/modules/or sub-batteries) of a given design required for a device to meet all targets, including cycle life and calendar life. Wherever possible, the Battery Size Factor will be specified by the manufacturer, based on the manufacturer’s testing and best estimates of any allowances needed for system burdens and degradation over life.
- **Nominal Voltage (V nominal)**: Difference between Vmax and Vmin, i.e., Total Energy / Total Capacity.
- **HPPC Current (I HPPC)**: = [PCPD] Constant Power Discharge target / (Vnominal * BSF).
- **Low Current HPPC Test**: Discharge pulse = [IHPPC] * 2.5.
- **High Current HPPC Test**: Discharge pulse = 75% of max current rating, where max current is the manufacturer’s absolute maximum allowable pulse discharge current for 10 seconds.

### HPPC Test Profile

| Time Increment (seconds) | Cumulative Time (seconds) | Relative Currents Pulse |
|---|---|---|
| 10 | 10 | 1.00 (discharge) |
| 40 | 50 | 0 |
| 10 | 60 | -0.75 (regen) |

**Note**: HPPC Discharge and Regen rate should be defined by the “Low Current HPPC” or “High Current HPPC” rates, or based on manufacturer recommended values. Vmin and Vmax should be based on manufacturer recommended values. Discharge rate should be based on IHPPC, or manufacturer recommended values.

### Battery Cycler Testing Profile

1. OCV measurement for 10 seconds (log every 5 seconds).
2. DCIR measurement.
3. Pre-Discharge to Vmin (log every 30 seconds and every 100mV change).
4. Rest after discharge for 1 hour (log every 1 minute).
5. Pre-Charge to Vmax (log every 30 seconds and every 100mV change).
6. Rest after charge for 1 hour (log every 1 minute).
7. Reset Charge & Discharge Capacity and Energy, and TC_Discharge_Capacity1 Counter.

**Method 1**: Using constant current control type (The value of currents here are for your example only, it will depend on the battery).

**Method 2**: Using current simulation control type. The method 1 is for better explanation of each step. In reality, for HPPC test, many people use current simulation method, which means combining all the charge and discharge steps into one step of “current simulation”.

## Cold Cranking Test

The Cold Cranking Test is intended to measure 2-s power capability at low temperature (normally -30ºC) for comparison with the Cold Cranking Power target(s). The test is conducted at the maximum DOD (minimum state-of-charge) where CS and CD Available Energy targets are just met, i.e., after removal of the energy required by both targets, based on the most recent L-HPPC data.

### Cold Cranking Test Profile

| Time Increment (seconds) | Cumulative Time (seconds) | System Power (kW) |
|---|---|---|
| 2 | 2 | 7 |
| 10 | 12 | 0 |
| 2 | 14 | 7 |
| 10 | 24 | 0 |
| 2 | 26 | 7 |

# Data / Statistics

| Metric | Value1 | Value2 | Value3 | Context | Notes |
|---|---|---|---|---|---|
| Testing Standards | FUDS | HPPC | DST | US testing standards | Various standards exist for benchmarking batteries and EV performance. |
| WLTP Standards | - | - | - | European and Asian testing standards | Developed by the UN Economic Commission. |

# Related Technologies / Concepts

| Concept | Description |
|---|---|
| Electric Vehicles | Vehicles powered by electric energy. |
| Battery Testing | Procedures to evaluate battery performance and characteristics. |

# Notes

*Note: Charge and Discharge rate should be based on manufacturer recommended values. Vmin and Vmax should be based on manufacturer recommended values.*
