# Metadata

| Field | Value1 |
|------|------|
| Title | How to perform Internal Resistance measurement according to IEC 61960 with Arbin? |
| Page Type | Article |
| Source URL | https://www.arbin.com/how-to-perform-internal-resistance-measurement-accroding-to-iec-61960-with-arbin.html |
| Category | Application Notes |
| Last Updated | August 17, 2025 |

# Overview

IR measurement is crucial to have an insight into a battery. There are many ways, i.e. many standards to measure battery’s IR. This article will introduce IEC 61960 standard and how to implement it using Arbin’s equipment.

# Key Points

| Topic | Summary |
|------|------|
| IEC 61960 standard for battery IR | In this standard, a discharge pulse of 0.2C is given for 10 seconds and V1 and I1 values are measured. Then, another discharge pulse of 1C is given for 1 second and V2 and I2 values are measured. DCIR is calculated using the formula: DCIR = (V1 – V2) / (I2 – I1). |
| Implement the test using Arbin cyclers | The following schedule in Arbin’s MITS software uses C-Rate control type and SetValues Control type to implement the IR calculation. If you want the MV_UD variables to be shown in exported data, you can configure it in Arbin’s Data Watcher software. |
| Discussion | Users may compare the DCIR value obtained by Arbin equipment measurement with other brands. Some devices measure ACIR rather than DCIR. |

# Detailed Explanation

## IEC 61960 standard for battery IR

In this standard, a discharge pulse of 0.2C is given for 10 seconds and V1 and I1 values are measured. Then, another discharge pulse of 1C is given for 1 second and V2 and I2 values are measured. DCIR is calculated using the formula:

DCIR = (V1 – V2) / (I2 – I1)

One point worth highlighting is that in theory, it’s expected to have the transfer between the two pulses immediate. The purpose is to avoid the relaxation effect of the battery. However, in reality, it will take a small time, be it some milliseconds or some tens of milliseconds depending on the limitation of the equipment used to implement the test.

## Implement the test using Arbin cyclers

The following schedule in Arbin’s MITS software uses C-Rate control type and SetValues Control type to implement the IR calculation. 

If you want the MV_UD variables to be shown in exported data, you can configure it in Arbin’s Data Watcher software. In the Additional Filter tab, you can see the list of MV_UD variables and you can choose what to export by checking the corresponding check boxes.

Back to the issue of switching time between the two pulses, which is from step 14’s end to step 17’s begin. Mostly it’s caused by step 15 and 16. According to our software engineer: “The execution speed of Set Variable varies depending on the number of channels that a MCU on IV boards needs to manage: 1 millisecond for 8 channels, 2 milliseconds for 16 channels, and 5 milliseconds for 32 channels.” 

Therefore, we are totally confident that the switching from step 14 to 17 is less than 50ms, and most of the time, less than 20ms. We believe that this can be considered immediate and quick enough to ignore the relaxation effect. If you find that this time is not short enough, please contact us for further requests.

If we want a faster transition, we can remove the SetValue for Last Step Current, only save Last Step Voltage. The actual current should be very close to the preset control current value. We can use this formula to calculate the current: 

I = C-Rate * Nominal Capacity

Then the formula now becomes:

(MVUD10-MVUD12)/((1 – 0.2)*Nominal Capacity)

## Discussion

In many cases, users may compare the DCIR value obtained by Arbin equipment measurement with other brand’s devices. Please note that some devices measure ACIR rather than DCIR. Take this hand-held meter UT677A for example. Many people think that this device is used to measure DCIR; however, when we check its specs, what it measures is ACIR at 1kHz.

In Arbin Cycler, we also have a specific control type to measure DCIR. It will be introduced in another article.

# Data / Statistics

| Metric | Value1 | Value2 | Value3 | Context | Notes |
|------|------|------|------|------|------|
| Execution speed for Set Variable | 1 ms | 2 ms | 5 ms | Number of channels | Varies depending on the number of channels that a MCU on IV boards needs to manage. |

# Industry Context

| Factor | Description |
|------|------|
| Comparison of DCIR and ACIR | Some devices measure ACIR rather than DCIR, which can lead to confusion when comparing measurements. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| DCIR | Direct Current Internal Resistance measurement. |
| ACIR | Alternating Current Internal Resistance measurement. |

# Notes

* If you want faster transition, you can remove the SetValue for Last Step Current, only save Last Step Voltage. 
* Reference links provided in the original document.
