# Metadata

| Field | Value |
|------|------|
| Title | Arbin DCIM Feature |
| Page Type | Technique |
| Source URL | https://www.arbin.com/innovation/arbin-dcim-feature.html |
| Category | Battery Testing |
| Last Updated | |

# Overview

The Arbin DCIM feature is a state-of-the-art technology to measure battery impedance via a DC method. This is a practical substitute for the ACIM measurement method to get EIS plots while also providing additional benefits.

# Principle

There are two methods to analyze a battery's impedance among a frequency range: the AC method and the DC method. The AC method, also known as ACIM, applies a set of AC signals with different frequencies to the battery, while sampling both AC current and voltage on the battery. The impedance can be derived from voltage/current amplitude and their phase shift at different frequencies. The DC method, namely DCIM, applies a DC current to the battery while sampling the current and voltage on the battery. The impedance can be derived from fitting values to the battery's equivalent circuit.

# Key Parameters

| Parameter | Description |
|-----------|-------------|
| Testing Time | AC Method: 0.5 min - 1 h; DCIM: <1 s |
| Hardware Requirement | AC Method: Additional AC source and measurement equipment required; DCIM: Built-in Arbin Channel, no additional hardware needed |
| Applied Signal to Battery | AC Method: Sinusoidal current/voltage wave at different frequencies; DCIM: Constant DC current |
| Disturb Battery Test | AC Method: Disturbs regular battery test; DCIM: Does not disturb regular battery test |
| Frequency Range | AC Method: 1 mHz - 1 MHz; DCIM: 1 Hz - 1 kHz |

# Applications

The DCIM method can generate a similar EIS (Nyquist) plot compared to the one from the traditional ACIM method. The test used to create the plot points outlined in the graph and table below was performed on a 18650 cell at 0.05 C source current.

# Data / Statistics

| Metric | Value | Context |
|--------|-------|---------|
| R0 | 0.02795 | DCIM Fitting |
| R1 | 0.0091541 | DCIM Fitting |
| C1 | 4.20221 | DCIM Fitting |
| R2 | 0.006298 | DCIM Fitting |
| C2 | 0.24452 | DCIM Fitting |
| R0 | 0.02741 | ACIM Fitting |
| R1 | 0.00943 | ACIM Fitting |
| C1 | 3.1126 | ACIM Fitting |
| R2 | 0.00677 | ACIM Fitting |
| C2 | 0.1135 | ACIM Fitting |

# Related Techniques

| Technique | Description |
|-----------|-------------|
| ACIM | Traditional method for measuring battery impedance using AC signals |

# Notes

* The black curve is the measured EIS (Nyquist) plot via ACIM method. 
* The blue curve is the fitted EIS curve based on measured ACIM method data and battery equivalent circuit. 
* The yellow curve is the fitted EIS curve based on measured DC method data and battery equivalent circuit.

# How to run DCIM on MITS 11

1. Create a new Test Plan, choose schedule "[Built-in] DCIM".
2. Start the test plan, wait until it finishes.
3. Go to the test summary page of that test plan, press advanced, then press DCIM mode to the result when running DCIM calculation with the default parameters.
4. Update the parameters in the Initial Guess sections and press calculate to manually calculate the DCIM.
