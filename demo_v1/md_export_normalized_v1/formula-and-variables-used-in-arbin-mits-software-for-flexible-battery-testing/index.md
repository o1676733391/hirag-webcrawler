# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Formula and variables used in Arbin MITS software for flexible battery testing |
| Page Type    | Article                                            |
| Source URL   | https://www.arbin.com/formula-and-variables-used-in-arbin-mits-software-for-flexible-battery-testing.html |
| Category     | Battery Testing                                    |
| Last Updated | June 10, 2025                                     |

# Overview

Software allows the user to control a test using variables rather than concrete control values. It is possible to use these variables in a formula to control the system.

# Key Features

| Feature | Description |
|---------|-------------|
| General Description | Control tests using variables instead of fixed values. |
| Formula Feature | Enables the use of formulas for control conditions. |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Formula A | PRESENT CHANNEL VOLTAGE – MAXIMUM CHANNEL VOLTAGE | V | Used for control conditions. |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| N/A       | N/A   | N/A  | N/A   |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| N/A       | N/A   | N/A  | N/A   |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| N/A       | N/A   | N/A  | N/A   |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Function  | ABS, ACOS, ASIN, CEIL, COS, CUBIC, EVEN, EXP, FACT, FLOOR, INT, LN, LOG10, ODD, RANDOM, SIGN, SIN, SQR, SQRT, TAN, TRUNC | N/A | Various mathematical functions available. |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
| Formula   | Allows for dynamic control of tests based on variable conditions. | Label, X1, X2, X3, X4, Operator, Y1, Y2, Y3, Y4 |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
| Arbin MITS | Software for flexible battery testing | Control tests using variables and formulas |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| N/A       | N/A         |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
| N/A    | N/A         | N/A  |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
| N/A     | N/A         | N/A  |

# Notes

1. The Formula Feature is always enabled by default. If it is not available, it must be checked in the config file.
2. It is best to start by entering “1s” for each variable and then fill in values as needed.
3. Formulas with one ‘X’ and one ’Y’ variable should use **X3** and **Y3**. The expression displays best with this variable placement.
4. You can import an existing formula into a new schedule: File > Import > select schedule with existing formula, and then select formula.
5. Example 1: A formula that uses a factor of device capacity as the end of test condition; for our example, we will use 80% of discharge capacity. F=0.8*Nominal Capacity.
6. Example 2: -∆V used with Nickel chemistry to stop charging. The formula we will end with is: F = Present Channel Voltage – Maximum Voltage during the test.
