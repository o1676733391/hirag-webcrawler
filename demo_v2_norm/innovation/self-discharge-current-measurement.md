# Metadata

| Field | Value1 |
|------|------|
| Title | Self-Discharge Current Measurement |
| Page Type | Technique |
| Source URL | https://www.arbin.com/innovation/self-discharge-current-measurement.html |
| Category | Battery Testing |
| Last Updated | |

# Overview

Battery Self-Discharge Current (SDC) is the small amount of electrical current that is lost naturally from a battery when it is not in use, due to internal chemical reactions within the battery. Measuring SDC accurately helps in understanding the health and efficiency of a battery, allowing manufacturers and users to predict battery life and performance more effectively.

# Key Parameters

| Parameter | Description |
| Self-Discharge Current | The current lost from a battery when not in use due to internal chemical reactions. |

# Applications

| Application | Description |
| Battery storage | Monitoring SDC to detect problematic cells and prevent hazardous thermal runaway. |
| Battery manufacturing | Identifying bad batteries with larger self-discharge currents during production. |
| Battery operation | Detecting abnormal behavior of batteries in parallel systems. |

# Measurement Methods

## Traditional Method

Traditional SDC Measurement is estimating the self-discharge current by monitoring the battery's open circuit voltage drop after a long time. Then find the capacity change corresponding to the OCV change, calculate the estimated SDC by capacity change divided by time. This method requires a long measuring time and known battery data (OCV vs. Capacity) of the battery.

![ARBIN-SDC Traditional Method](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Traditional-Method.png)

## Potentiostatic Method

Another potentiostatic method is using a voltage source to apply the same voltage as the battery OCV, then consider the current flows from the voltage source to the battery to hold the OCV as the battery's SDC. This method can measure the SDC in a relatively shorter time than the traditional method, but it requires additional hardware and is sensitive to temperature changes.

![ARBIN-SDC Potentiostatic Method](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Potentiostatic-Method.png)

## Galvanostatic Method (Arbin Method)

Arbin utilizes a galvanostatic method by applying a small amount of DC currents to the cell and recording the voltage change rate. The battery's SDC and dynamic capacitance can be calculated by solving specific equations.

![ARBIN-SDC Galvanostatic Method \(Arbin Method\) i1](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Galvanostatic-Method-Arbin-Method-i1.png)
![ARBIN-SDC Galvanostatic Method \(Arbin Method\) i2](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Galvanostatic-Method-Arbin-Method-i2.png)

This method can accurately measure SDC in a short time and avoids disturbance of battery electrochemical balance.

## Galvanostatic Parallel Method (Arbin Method)

This method takes the galvanostatic method a step further by using PDBT modules to parallel a batch of batteries and measure each battery's SDC. It allows batteries to reach electrochemical balance faster and supports multiple batteries running the SDCM simultaneously.

![ARBIN-SDC Galvanostatic Parallel Method \(Arbin Method\)](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Galvanostatic-Parallel-MethodArbin-Method.png)

This method can accurately measure SDC in a short time and avoids disturbance of battery electrochemical balance.

# SDC Measurement Methods Comparison

![ARBIN-SDC-measurement-methods-Comparison](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201832%20921'%3E%3C/svg%3E)

# Arbin SDC Monitoring Feature

Arbin SDC monitoring feature is designed for battery storage, battery manufacturing, and battery operation. Continuous monitoring of SDC provides early detection of problematic cells and prevents hazardous thermal runaway.

In the SDC monitoring mode, Arbin monitors each battery's voltage and unbalanced current among all paralleled batteries in real time, without inducing any external current.

![ARBIN-SDC Monitoring Feature i1](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-SDC-Monitoring-Feature-i1.png)

The self-discharge current increases with time while the battery deteriorates, making it more efficient to monitor SDC than battery temperature for failure detection.

![Arbin SDCM](https://www.arbin.com/wp-content/uploads/2024/10/SDCM_EarlyFaultDetection-1.drawio-1.png)

# Arbin SDC Monitoring Application for Early Fault Detection

## Early Fault Detection in Storage and Shipping

Arbin SDC Monitoring does not require active power sources, making it suitable for battery storage and shipping.

![ARBIN-Early Fault Detection in Storage and Shipping i1](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-Early-Fault-Detection-in-Storage-and-Shipping-i1.png)
![ARBIN-Early Fault Detection in Storage and Shipping i2](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-Early-Fault-Detection-in-Storage-and-Shipping-i2.png)

## Early Fault Detection in Operation

The modules used in EVs consist of many batteries in parallel. If one battery fails, it is often hard to detect as other batteries will output more power. The SDC monitoring feature allows for straightforward detection of abnormal behavior.

![ARBIN-Early Fault Detection in Operation i1](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-Early-Fault-Detection-in-Operation-i1.png)
![ARBIN-Early Fault Detection in Operation i2](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-Early-Fault-Detection-in-Operation-i2.png)

## Early Fault Detection in Manufacturing

The self-discharge current of batteries from the same production batch should be similar. Arbin's SDCM provides a faster and more accurate solution for self-discharge current measurement and monitoring in battery manufacturing.

![ARBIN-Early Fault Detection in Manufacturing](https://www.arbin.com/wp-content/uploads/v2/SDCM/ARBIN-Early-Fault-Detection-in-Manufacturing.png)

The SDC monitoring can greatly reduce the risk of thermal runaway and resulting fire, potentially lowering safety measure costs for battery factories.
