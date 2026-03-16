# Metadata

| Field | Value |
|------|------|
| Title | Smart Data Logging (Acquisition) User's Guideline |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/smart-data-logging-acquistion-users-guideline.html |
| Category | Data Logging Solutions |
| Last Updated | |

# Overview

For battery researchers and testers who need to study battery performance, data logging is an important factor. It can provide more accurate current, voltage, time, and temperature data to increase the efficiency of testing analysis. These technical strategies will need to apply Smart Data Logging (SDL) feature in the battery testing industry. The Arbin Testing System can be used with SDL filtering unchanged data measurement in the experiment, reducing data logging rates, increasing efficiency, and preventing overload of data collections that cause the System Under Test (SUT) to fail the experiment.

# Key Points

| Topic | Summary |
|------|------|
| Criteria on change logging data point | Parameters include Voltage, Current, and Time Interval with specific change conditions for logging data points. |
| SDL-Disable | High logging rates may not provide more information due to slow state changes in battery testing. |
| SDL-Enable | Fast logging rates can stress database servers and lead to data loss. |

# Detailed Explanation

## Criteria on change logging data point

| Parameter | Different Range | Comparison | Target Range |
|------|------|------|------|
| Voltage | ∆V=Vpresent - Vprevious | ∆V=Vpresent - Vprevious | XXmV |
| Current | ∆I = Ipresent - Iprevious | >, >=, <, <=, &, || | YYmA |
| Time Interval | ∆t = tpresent - tprevious | >=, >, <, = | ZZms |

For example, a tester would like to use SDL to log data if and only if the change in Voltage is equal or greater than 1mV, and current change is greater than 2mA, or time interval is over 10ms to log one data point. In terms of logical expression, it can be expressed as: IF ∆V >= 1mV and ∆I > 2mA OR ∆t >= 10ms, LOG data point.

## SDL-Disable

People think that logging fast is a method to obtain fluctuations in voltage or current during battery testing; however, high logging rates in battery testing may not provide more information because the state of change is very slow. Fast logging rates may put more stress on database servers, RAM, memory resources, and network bandwidth that potentially bring the PC under test to losing data or low performance.

Arbin Mits 8.x utilizes an SQL database server with logging a maximum of 20 points/ms (20,000 data points per second). If we are logging more than 20pts/ms in a test, the data is being buffered in RAM and potentially a PC fails to handle the logged data.

| Channels | Logging Rate | PC Insert Rate | No SDL | SDL | Burst Mode |
|------|------|------|------|------|------|
| 2 CH | 60µS | 33 pts/ms = 33k/sec | No | Yes | Yes |
| 4 CH | 60µS | 66 pts/ms = 66k/sec | No | Yes | Yes |
| 6 CH | 60µS | 100 pts/ms = 100k/sec | No | Yes | Yes |
| 8 CH | 1ms | 8 pts/ms = 8,000/sec | Yes | Yes | No |
| 16 CH | 1ms | 16 pts/ms = 16,000/sec | Yes | Yes | No |
| 32 CH | 1ms | 32 pts/ms = 32,000/sec | No | Yes | No |
| 64 CH | 1ms | 64 pts/ms = 64,000/sec | No | Yes | No |
| 96 CH | 1ms | 96 pts/ms = 96,000/sec | No | Yes | No |
| 128 CH | 1ms | 128 pts/ms = 128,000/sec | No | Yes | No |

The granularity of ∆V, ∆I, and ∆t value range must be within the precision and accuracy of ADC specification or Arbin Precision System in terms of PPM. For example, a system with 100 PPM (100/1M) precision level, then ∆V and ∆I should be in the range of 0.1mV or 0.1mA. If you set the ∆V and ∆I in the range of 0.01mA or 0.01mV, then data acquisition will not be valuable. Please be mindful and calculate the change range to log data points precisely to have good data acquisition from your experiments.

## Arbin Smart Data Logging Solutions

To achieve Smart Data Logging, Arbin has developed 5 flexible solutions that can be applied depending on the need of our customers' demand. We will describe step-by-step how to configure, setup, and run these methods.

### Method 1

Using ∆V or ∆I as logging limit, instead of ∆T. Compared with regular data logging that uses time (∆T) as the log limit, smart data logging uses more variables as the log limit such as voltage, current, ∆V (change in voltage), and ∆I (change in current). For example, you can log the data for every 2mV change in voltage. When using the SDL, the ADC still reads the data continuously, but the system will only log the data based on the user-defined limit.

### Method 2

Using Sub-Schedule to change the logging speed. The Sub-Schedule serves as a reference within the Main-Schedule, allowing it to be included as one of the "Steps" to be tested concurrently. This structure enables seamless integration and organization of testing procedures.

### Method 3

Combining SDL and Sub-Schedule. This approach enables users to utilize a wider range of variables as log limits, allowing for logging at different speeds based on the log limit adjustments.

### Method 4

Use Kafka/PostgreSQL to get better logging speed. Transitioning to a Kafka database offers a solution to the limitation of maximum insertion capacity, enabling unlimited insertion speed.

### Method 5

Lua Script Control Type that directly controls the MCU in real-time. Users can craft their own scripts using Arbin's Control Type, offering greater flexibility compared to writing schedules.

# Data / Statistics

| Metric | Value | Context |
|------|------|------|
| Insertion Rate | 2000 | MSSQL (pps) |
| Insertion Rate | 80,000 | PostgreSQL (pps) |
| Insertion Rate | 100,000 | Kafka (pps) |
| Insertion Rate | Unlimited | Kafka (pps) |
| Query Rate | 2000 | MSSQL (pps) |
| Query Rate | 200,000 | PostgreSQL (pps) |
| Query Rate | 333,000 | Kafka (OnDemand) |

*All units in pps (points per second)*

# Industry Context

| Factor | Description |
|------|------|
| Database Options | Arbin provides PostgreSQL as a database option in MITS, which offers several advantages over MSSQL. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| Smart Data Logging | A method to enhance data acquisition efficiency in battery testing. |
| Sub-Schedule | A feature that allows for quick application of existing schedules to new ones. |
| Kafka | A distributed streaming platform for high-performance message passing. |

# Notes

*Arbin data point takes 10 bytes in size, which contains two floats (1 byte per float number) and two unsigned char (4 bytes per char) which adds up to 10 bytes.*
