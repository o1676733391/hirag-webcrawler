# Metadata

| Field | Value |
|------|------|
| Title | Constant-C-rate w.r.t. actual capacity, rather than constant current with Arbin cyclers |
| Page Type | Technique |
| Source URL | https://www.arbin.com/constant-c-rate-w-r-t-actual-capacity-rather-than-constant-current-with-arbin-cyclers.html |
| Category | Application Notes |
| Last Updated | June 30, 2025 |

# Overview

As we all know, the batteries’ capacity degrade by cycle of charge and discharge. If we set the charge and discharge current of a fixed value, such as 1A, 2A,… the length of each cycle will gradually decrease, simply because the battery’s capacity decreases:  
_Cycle time = (Charge Capacity + Discharge Capacity)/Current_  
Sometimes users want to keep cycle time constant (or almost constant) after even hundreds or thousands of cycles. For example, they want the current to be fixed at 1C w.r.t. the actual capacity through the test. Arbin’s MITS software can help you easily do this.

# Key Parameters

| Parameter | Description |
| Nominal Capacity | Initial capacity of the battery defined in the test object. |

# Applications

| Application | Description |
| Evaluating degradation | Under real-world charging patterns (like EVs charging overnight). |
| Conducting accelerated aging tests | Where cycle time must remain fixed to analyze time-based degradation factors. |

# Detailed Explanation

**1st Step:** A Rest step is normally put at the beginning of every schedule. It will play the role of safety check before entering the real test.  
**2nd Step:** Set meta variable MV_UD1 as Nominal Capacity of the battery. This value is defined in the test object. We assume that the value declared here is the initial capacity of the battery.  
**3rd Step:** Fully charge the battery.  
**4th Step:** Fully discharge the capacity.  
**5th Step:** Update the battery’s latest capacity to the variable MV_UD1, and come back to Charge step (3rd Step). By doing this, after each cycle, when the battery’s capacity decreases, we update it and use it for the next cycle.  
**6th Step:** Reset the charge and discharge capacity variable, prepare to measure the latest capacity of the battery.

# Related Technologies / Concepts

| Concept | Description |
| C-rate | A measure of the rate at which a battery is charged or discharged relative to its capacity. |

# Data / Statistics

| Metric | Value | Context |
| Cycle time | Variable | Depends on charge and discharge capacity and current. |

# Notes

* Reference to:  
  * [BU-402: What Is C-rate?](https://batteryuniversity.com/article/bu-402-what-is-c-rate)  
  * [ScienceDirect Article](https://www.sciencedirect.com/science/article/pii/S2950345024000198)  
  * [Nature Article](https://www.nature.com/articles/s41560-024-01675-8)  
* Autocalibration box is sold separately.
