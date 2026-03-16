# Metadata

| Field | Value |
|------|------|
| Title | How to detect NiMH battery fully charged status |
| Page Type | Technique |
| Source URL | https://www.arbin.com/how-to-detect-nimh-battery-fully-charged-status.html |
| Category | Battery Technology |
| Last Updated | May 26, 2025 |

# Overview

The Nickel-Metal Hydride (NiMH) battery is a type of rechargeable battery that uses nickel oxide hydroxide (NiOOH) as the positive electrode (cathode) and a hydrogen-absorbing alloy as the negative electrode (anode). Compared to nickel-cadmium (NiCd) batteries, NiMH batteries offer several distinct advantages, including higher capacity, lower environmental impact, and being more environmentally friendly during both usage and disposal. NiMH batteries are widely used in many modern electronic devices and vehicles, including digital cameras, cordless phones, electronic toys, and hybrid vehicles.

# Principle

Some indicators of a full-charge check for Nickel-Metal Hydride (NiMH) batteries are based on the physical and electrochemical changes that occur within the battery as it approaches full charge. During the charging process, several characteristic indicators are monitored to determine when the battery has reached its maximum capacity:

- **Negative Delta-V (−ΔV) Phenomenon**: As the battery nears full charge, the voltage of each cell rises to a peak and then slightly drops due to internal ion redistribution and the onset of overcharge conditions. This voltage drop—typically in the range of 5–15 mV per cell—is used by many smart chargers to detect the full-charge point.
- **Temperature Rise**: When the battery is nearly full, its ability to efficiently convert electrical energy into chemical energy decreases. Excess energy is instead converted into heat, leading to a rapid increase in cell temperature. This rise can be detected using temperature sensors and is considered a reliable indicator of a full charge.
- **Voltage Threshold Detection**: Toward the end of the charging process, the cell voltage typically reaches a level between 1.4V and 1.5V. While voltage alone is not a definitive indicator of full charge, it contributes valuable data when combined with other metrics.
- **Theoretical Charging Time Calculation**: Based on the battery’s rated capacity (in mAh) and the charging current (in mA), the expected full-charge time can be estimated. This method is often used as a safety cutoff or secondary reference in charger design.

# Key Parameters

| Parameter | Description |
|-----------|-------------|
| Negative Delta-V | Voltage drop of 5–15 mV per cell |
| Temperature Rise | Rapid increase in cell temperature |
| Voltage Threshold | Cell voltage between 1.4V and 1.5V |
| Charging Time | Estimated based on rated capacity and charging current |

# Applications

| Application | Description |
|-------------|-------------|
| NiMH Battery Pack | 7S1P, 8.4V, 4.5Ah |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| CC (Constant Current) | Charging at 1.8A | Negative Delta V Termination: V – Vpeak = -60mV, Failsafe Max Charge Time: 3 hours, Safety Voltage Limit: 10.5V |

# Notes

* The key point of the loop step is for the condition of “10-minute continuous voltage drop”. In step CC, when the voltage starts dropping (dV/dt<0), we jump to this step to the step Loop. The maximum time of this step is 10 minutes. During this 10 minutes, whenever dV/dt >=0, it means that the condition of Voltage 10 mins continuously drop failed, we need to start clocking to monitor for another slot of 10 mins and have to go back to step CC. After 10 mins, if the condition of dV/dt >=0 is not hit, then the voltage has been dropped 10 mins continuously. During this step, whenever the other 3 conditions meet (Negative Delta V Termination: V – Vpeak = -60mV, Failsafe Max Charge Time: 3 hours, Safety Voltage Limit: 10.5V) the battery is also considered fully charged.
