# Metadata

| Field | Value1 |
|------|------|
| Title | Smart Data Logging (Acquisition) User's Guideline |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/smart-data-logging-acquistion-users-guideline.html |
| Category | Data Logging |
| Last Updated | |

# Overview

For battery researchers and testers who need to study battery performance, data logging is an important factor. It can provide more accurate current, voltage, time, and temperature data to increase the efficiency of testing analysis. These technical strategies will need to apply Smart Data Logging (SDL) feature in the battery testing industry. The Arbin Testing System can be used with SDL filtering unchanged data measurement in the experiment, reducing data logging rates, increasing efficiency, and preventing overload of data collections that cause the System Under Test (SUT) to fail the experiment.

# Key Points

| Topic | Summary |
|------|------|
| Criteria on change logging data point | Parameters include Voltage, Current, and Time Interval with specific change calculations. |
| SDL-Disable | Regular logging method. |
| SDL-Enable | Smart Data Logging method. |
| Logging Rate | Fast logging rates may stress database servers and lead to data loss. |
| Arbin Mits 8.x | Utilizes an SQL database server with a maximum logging rate of 20 points/ms. |

# Detailed Explanation

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

Use Kafka/PostgreSQL to get better logging speed. Transitioning to a Kafka database offers a solution to the limitation of the SQL database, enabling unlimited insertion speed.

### Method 5

Lua Script Control Type that directly controls the MCU in real-time. Users can craft their own scripts using Arbin's Control Type, offering greater flexibility compared to writing schedules.

# Data / Statistics

| Metric | Value1 | Value2 | Value3 | Context | Notes |
|------|------|------|------|------|------|
| Insertion Rate | 2000 | 80,000 | 100,000 | MSSQL, PostgreSQL, Kafka | All units in pps (points per second) |
| Query Rate | 2000 | 200,000 | 333,000 | MSSQL, PostgreSQL, Kafka | OnDemand |

# Industry Context

| Factor | Description |
|------|------|
| Database Options | Arbin provides PostgreSQL as a database option in MITS, offering advantages over MSSQL. |

# Related Technologies / Concepts

| Concept | Description |
|------|------|
| Smart Data Logging | A method to log data based on variable changes rather than time intervals. |
| Sub-Schedule | A feature that allows for the integration of multiple testing steps. |
| Kafka | A distributed streaming platform for high-throughput data processing. |

# Notes

* All units in pps (points per second).
* Arbin data point takes 10 bytes in size, which contains two floats (1 byte per float number) and two unsigned char (4 bytes per char).
* Lua Script is not available in Mits Pro8.
