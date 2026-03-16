# Metadata

| Field | Value1 |
|------|------|
| Title | How to run cyclic voltammetry on three-electrode(3E) cell using Arbin Tester |
| Page Type | Technique |
| Source URL | https://www.arbin.com/how-to-run-cyclic-voltammetry-on-three-electrode3e-cell-using-arbin-tester.html |
| Category | Application Notes |
| Last Updated | October 21, 2025 |

# Overview

This document explains how to run cyclic voltammetry on a three-electrode (3E) cell using an Arbin Tester. The 3E cell allows for the study of electrochemical reactions on each electrode separately, providing insights into battery performance.

# Principle

In a battery with two electrodes, measuring the voltage only shows the total potential difference between the cathode and anode. The 3E cell includes a working electrode (W), counter electrode (C), and reference electrode (R), allowing for separate analysis of the electrodes. The current flows between W and C, while the voltage is measured between W and R.

# Key Parameters

| Parameter | Description |
| Working electrode | W |
| Counter electrode | C |
| Reference electrode | R |

# Applications

| Application | Description |
| Cyclic voltammetry | A technique used to study the electrochemical properties of materials in a 3E cell configuration. |

# Related Techniques

| Technique | Description |
| Cyclic voltammetry | A method for studying the electrochemical behavior of materials by measuring current as a function of applied voltage. |

# Hardware connection

A typical Arbin system socket has four wires: red, white, black, and green, corresponding to I+, V+, I-, and V-.

## When anodic current is positive

In this connection, the red wire (I+) is connected to the working electrode, and the black wire (I-) is connected to the counter electrode. This configuration allows current to flow from W to C, while the white wire measures the voltage between W and R.

## When anodic current is negative

The Arbin system allows current control in both directions. To reverse the current flow, simply enter a negative current value in the MITS software.

## Auxiliary voltage connector

To measure the voltage between C and W, connect the auxiliary voltage connector as shown in the provided diagrams. The red and black cables of the auxiliary connector must be connected to the battery.

# Software configuration

If measuring voltage between W and C, ensure the auxiliary channel is correctly mapped to the IV channel in the mapping file. For example, map Auxiliary voltage channel 1 to IV channel 1.

# Notes

* The Arbin system is capable of conducting tests with the 3E cell configuration.
* Ensure proper connections to avoid measurement errors.
