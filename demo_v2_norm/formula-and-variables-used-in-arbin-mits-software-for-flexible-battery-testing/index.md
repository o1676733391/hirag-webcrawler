# Metadata

| Field | Value1 |
|------|------|
| Title | Formula and variables used in Arbin MITS software for flexible battery testing |
| Page Type | Resource |
| Source URL | https://www.arbin.com/formula-and-variables-used-in-arbin-mits-software-for-flexible-battery-testing.html |
| Category | Application Notes |
| Last Updated | June 10, 2025 |

# Overview

The Arbin MITS software allows the user to control a test using variables rather than concrete control values. For example, instead of using 4.2V for control, the system can use “Last Step Maximum Voltage” as the control type for the following step. It is also possible to use these variables in a formula to control the system.

# Key Points

| Topic | Summary |
|------|------|
| General Description | The software allows control using variables instead of fixed values. |
| Function available | A list of mathematical functions available in the software. |
| Notes | Important considerations for using formulas in the software. |

# Detailed Explanation

## Functions available

| Function | Description |
|------|------|
| ABS | Return the absolute value of a number without its sign. |
| ACOS | Return the arccosine of a number, in radians in the range of 0 to pi. |
| ASIN | Return the arcsine of a number in radians. |
| CEIL | Return the smallest integer that is greater than or equal to a given number. |
| COS | Return the cosine of an angle. |
| CUBIC | Return the cubic of a number. |
| EVEN | Round a number up to the nearest even integer. Negative numbers are adjusted away from zero. |
| EXP | Return e raised to the power of a given number. |
| FACT | Return the factorial of a number. |
| FLOOR | Return the largest integer that is less than or equal to a given number. |
| INT | Round a number down to the nearest integer. |
| LN | Return the natural logarithm of a number. |
| LOG10 | Return the base-10 logarithm of a number. |
| ODD | Round a number up to the nearest odd integer. |
| RANDOM | Return an evenly distributed random number within specified ranges. |
| SIGN | Return the sign of a number: 1 if positive, 0 if zero, -1 if negative. |
| SIN | Return the sine of an angle. |
| SQR | Return the square of a number. |
| SQRT | Return the positive square root of a number. |
| TAN | Return the tangent of an angle. |
| TRUNC | Return an integer for a number by removing the decimal part. |
| Operators | +, -, x, /, % |

## Notes

1. The Formula Feature is always enabled by default. If it is not available, it must be checked in the config file.
2. It is best to start by entering “1s” for each variable and then fill in values as needed.
3. Formulas with one ‘X’ and one ’Y’ variable should use **X3** and **Y3** for best display.
4. You can import an existing formula into a new schedule: File > Import > select schedule with existing formula, and then select formula.

### Example 1: Formula for 80% of discharge capacity

**Formula:** Final_Capacity = 0.8 × Nominal_Capacity  
This means the test will automatically stop when the battery’s capacity decreases to 80% of its original value.

#### Steps to create the formula

1. Go to **Formula** tab of a new schedule.
2. On the menu bar, click Edit → Insert Formula.
3. Enter the following information:
   - Label = F_80%_Capacity
   - X1 = 1
   - X2 = 1
   - X3 = 0.8
   - X4 = 1
   - Operator = *
   - Y1 = 1
   - Y2 = 1
   - Y3 = MV_Norminal Capacity
   - Y4 = 1

### Example 2: Formula using -∆V with Nickel chemistry

**Formula:** F = Present Channel Voltage – Maximum Voltage during the test.  
This formula helps to identify when to stop charging based on voltage drop.

#### Steps to create the formula

1. Enter the following information:
   - Label = F_-DeltaV
   - X1 = 1
   - X2 = 1
   - X3 = PV_Channel_Voltage
   - X4 = 1
   - Operator = –
   - Y1 = 1
   - Y2 = 1
   - Y3 = VmaxOnCycle
   - Y4 = 1

# Data / Statistics

| Metric | Value1 | Value2 | Value3 | Context | Notes |
|------|------|------|------|------|------|
| Discharge capacity threshold | 80% | | | Battery life evaluation | Test stops when capacity drops to this level. |

# Industry Context

| Factor | Description |
|------|------|
| Battery testing | Essential for evaluating performance degradation over time. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| Battery management systems | Systems that monitor and control battery performance. |

# Notes

*The formula feature is essential for flexible battery testing.*
