# Source

- URL: https://www.arbin.com/software-solution/smart-data-logging-acquistion-users-guideline.html

# Content

#  Smart Data Logging  (Acquistion) User's Guideline
For battery researchers and testers who need to study battery performance, data logging is an important factor, it can provide more accurate current, voltage, time, and temperature data to increase the efficiency of testing analysis.
These technical strategies will need to apply Smart Data Logging (SDL) feature in the battery testing industry, the Arbin Testing System can be used with SDL filtering unchanged data measurement in the experiment, reducing data logging rates, increasing efficiency, and preventing overload of data collections that cause the System Under Test (SUT) to fail the experiment.
Table of Contents

####  Criteria on change logging data point
Parameters
Different Range
Comparision
Target Range
Voltage
∆V=Vpresent - Vprevious
∆V=Vpresent - Vprevious
XXmV
Current
∆I = Ipresent - Iprevious
>,>=, <, <=, &, ||
YYmA
Time Interval
∆I = Ipresent - Iprevious
>=, >, <, =
ZZms
Table 1
For Example, a tester would like to use SDL to log data if and only if the change in Voltage is equal or greater than 1mV, and current change is greater than 2mA, or time interval is over 10ms to log one data point.
In terms of logical expression, it can be expressed like the following: IF ∆V >= 1mV and ∆I >2mA OR ∆t >=10ms, LOG data point. Later sections will guide you to implement this logic into Arbin Schedule File.
####  Figure 1. Regular logging (left) vs SDL (right)
### SDL-Disable

### SDL-Enable

People think that logging fast is a method to obtain fluctuations in voltage or current during battery testing, however, high logging rates in battery testing may not provide more information because the state of change is very slow.
Fast logging rates may put more stress on database servers, RAM, memory resources, and network bandwidth that potentially bring the PC under test to losing data or low performance.
Arbin Mits 8.x utilizes an SQL database server with logging a maximum of 20 points/ms (20,000 data points per second). If we are logging more than 20pts/ms in a test, the data is being buffered in RAM and potentially a PC fails to handle the logged data.
Channels
Logging Rate
PC Insert Rate
No SDL
SDL
Burst Mode
2 CH
60µS
33 pts/ms = 33k /sec
No
Yes
Yes
4 CH
60µS
66 pts/ms = 66k /sec
No
Yes
Yes
6 CH
60µS
100 pts/ms = 100k/sec
No
Yes
Yes
8 CH
1ms
8pts /ms = 8,000/sec
Yes
Yes
No
16 CH
1ms
16pts /ms = 16,000/sec
Yes
Yes
No
32 CH
1ms
32 pts /ms = 32,000/sec
No
Yes
No
64 CH
1ms
64 pts /ms = 64,000/sec
No
Yes
No
96 CH
1ms
96 pts/ms = 96,000/sec
No
Yes
No
128 CH
1ms
128 pts/ms = 128,000/sec
No
Yes
No
Table 2: Mits 8.x PC Comparison No-SDL/SDL.
The granularity of ∆V, ∆I, and ∆t value range must be within the precision and accuracy of ADC specification or Arbin Precision System in term PPM.
For example, a system with 100 PPM (100/1M) precision level, then ∆Vand ∆I should be in the range of 0.1mV or 0.1mA, if you set the ∆Vand ∆I in range of 0.01mA or 0.01mV, then data acquisition will not be valuable.
Please be mindful and calculate the change range to log data point precisely to have good data acquisition from your experiments.
##  Arbin Smart Data Logging Solutions
To achieve the Smart data logging, Arbin has developed 5 flexible solutions that can be applied depending on the need of our customers' demand. We will describe step-by-step how to configure, setup, and run these methods.
METHOD 1  METHOD 2  METHOD 3  METHOD 4  METHOD 5
METHOD 1
METHOD 1. Using ∆V or ∆I as logging limit, instead of ∆T.
Compared with regular data logging that uses time (∆T) as the log limit, smart data logging used more variables as the log limit such as voltage, current, ∆V (change in voltage), and ∆I (change in current).
For example, you can log the data for every 2mV change in voltage. When using the SDL, the ADC still reads the data continuously, but the system will only log the data based on the user-defined limit.
Let us look at a sample example of using SDL in battery testing – charging the battery with a constant current. When applying a constant current to a battery, we care more about the voltage change.
Therefore, it is an innovative idea to use ∆V as the log limit. The voltage of the battery will not be a linear curve -- the change in voltage will be faster in the beginning and slower at the end.
By setting a certain ∆V as the limit, we expect to log more data points in the beginning and fewer data points near the end.
Compared with the regular log limit method using a time limit, SDL comes with fewer data points but can still show battery performance.

Figure 2. Voltage/Current vs. Time During Battery Charging Test
We can see another more complicated example of CCCV test (constant current to constant voltage). This test is to charge the battery to a target voltage level using the constant current, and then hold the battery at constant voltage level.
At the CC (Constant Current) stage, the current will be the constant and the major change will be on the voltage. At the CV (Constant Voltage) stage, the voltage will be the constant and the major change will be on the current.
In this condition, neither voltage nor current will be considered as a suitable log limit because they are used as part of the test.
The change in capacity will be a viable choice. Arbin provides multiple variable types that you can choose from for the log limit. Different tests should have different log limit settings.
Regular Data Logging
Charging the battery to 3.8V using 1A current and keep logging data every 2 seconds.

Figure 3. Testing Schedule for Regular Data Logging

Figure 4. Testing Result for Regular Data Logging
Criteria on change logging data point
METHOD1. Applying SDL with Arbin Cyclers using Mits Pro 8
Smart Data Logging
Charging the battery to 3.8V using 1A current and log data when ∆V > 5mV or every 5 minutes.

Figure 5. Testing Schedule for Smart Data Logging (Mits Pro8)
METHOD1. Applying SDL with Arbin Cyclers using MITS
Smart Data Logging
Charging the battery to 3.8V using 1A current and log data when ∆V > 5mV or every 5 minutes.

Figure 6. Testing Schedule for Smart Data Logging (MITS)

Figure 7. Testing Result for Smart Data Logging
METHOD 2
METHOD 2. Using Sub-Schedule to change the logging speed
To facilitate quick application of existing schedules to new ones, the traditional schedule is divided into Main-Schedule and Sub-Schedule.
The Sub-Schedule serves as a reference within the Main-Schedule, allowing it to be included as one of the "Steps" to be tested concurrently.
This structure enables seamless integration and organization of testing procedures.
The Sub-Schedule functions as separate files called upon by a test schedule, akin to simulation profiles. Regardless of the complexity of the simulation file, it is treated as a single step within the test schedule.
This approach circumvents the 200-step limit in Mits Pro 8, enabling tests of unlimited duration. Leveraging the SubSchedule also empowers users to adjust logging speeds as needed.
SubSchedule feature only available in MITS.
Let us see a sample example of using Sub-Schedule to achieve SDL. In this example, we use Sub-Schedule Control Type in the second step (Step_B). In the first step (Step_A) we use Rest as the control type, which the battery is disconnected from the charge/discharge circuit, but is still connected to the voltage measurement circuit, so the open circuit voltage can be measured.
It logs points every 0.005 second for 1 minute long. Then goes to the Sub-Schedule Step (Figure 9), we keep running the rest step, but we changed the logging speed to logs points every 0.001 second for 10 seconds long. To activate this feature, Figure 10 shows that the "Use Sub" check box must be selected. The results of the test using the SubSchedule feature are seen in Figure 11.

Figure 8. Example of Main-Schedule

Figure 9. Example of Sub-Schedule

Figure 10. By clicking the "Use Sub" box in the SubSchedule, when the test goes to SubSchedule step, it will use the logging setting in SubSchedule.

Figure 11. Logging points vs logging speed
METHOD 3
METHOD 3. Combining SDL and Sub-Schedule
When the SDL and Sub-Schedule are combined, data logging's flexibility is greatly enhanced.
This approach enables users to utilize a wider range of variables as log limits, such as voltage, current, ∆V (change in voltage), and ∆I (change in current), allowing for logging at different speeds based on the log limit adjustments.
Additionally, SubSchedule provides more options for changing the logging rate while maintaining the same Control Type.
For instance, users can charge at a constant current of 1A, and log data points every 0.005 seconds for 30 seconds.
Then, within the SubSchedule, they can maintain the same constant current but adjust the logging frequency based on voltage changes, logging data points every 0.2 volt.

Figure 12. Main-Schedule logging points every 0.005 seconds

Figure 13. Sub-Schedule logging points every 0.2 Volt change
METHOD 4
METHOD 4. Use Kafka/PostgreSQL to get better logging speed
As mentioned, Arbin uses a SQL database capable of logging 20,000 data points per second (Mits Pro 8).
However, the maximum insertion capacity of the Arbin PC SQL database imposes a limit of 80,000 points per second on the logging rate (MITS).
Transitioning to a Kafka database offers a solution to this limitation, as it enables unlimited insertion speed, effectively removing the 80,000 data points per second constraint.
Kafka is a distributed streaming platform specifically designed for publishing and subscribing to streams of records. It employs a distributed, partitioned, and replicated architecture to ensure high throughput, durability, and fault tolerance.
With its inherent high throughput capabilities, Kafka excels at handling large volumes of data streams, making it suitable for scenarios requiring extensive data stream processing. Consequently, the maximum logging point can be extended to the hardware limit, or Kafka Cluster Setup Limit.
Kafka is not a traditional database in the sense of having strict data storage and retrieval capabilities. Instead, it functions more like a distributed message queue, focusing on high-performance message passing.
Unlike traditional databases, Kafka does not impose limits on ingestion speed. Its primary objective is to maximize message throughput and processing speed to meet the demands of large-scale data stream processing.
Therefore, Kafka does not restrict ingestion speed because its primary goal is to provide high-performance message passing rather than traditional database functionalities.
Arbin implemented the Kafka platform to leverage its distributed architecture and optimized message passing mechanisms to achieve high throughput and low latency for large-scale data processing.

Figure 14. Basic Kafka structure
Kafka operates as a distributed system, where data is spread across multiple brokers in a cluster. This architecture allows Kafka to horizontally scale by adding more brokers as needed.
Each broker handles a portion of the data partitions, enabling Kafka to handle large volumes of data and distribute the workload across multiple machines.
PostgreSQL Database Server
Arbin also provides PostgreSQL as a database option in MITS. PostgreSQL offers several advantages over MSSQL. First, being open-source, PostgreSQL is freely available for use and enjoys strong community support.
It is also a cross-platform database, that can run on Windows, Linux, and macOS, while MSSQL is primarily designed for Windows.
PostgreSQL also has better performance in data insertion rate as shown in the Table 4 below.
PostgreSQL performs well at handling large numbers of concurrent insert operations, which means it can more efficiently handle situations where multiple clients are inserting data into the database at the same time.
Additionally, PostgreSQL provides extensive customizability, supporting complex data types and rich extension systems, which may be more limited in MSSQL.
Moreover, PostgreSQL's scalability and integration capabilities are notable, thanks to its plugin architecture and active development community.
Overall, these factors contribute to PostgreSQL's appeal for projects requiring open-source solutions, flexibility, and scalability.
Kafka and PostgreSQL only support MITS. Mits Pro 8 does not support Kafka or PostgreSQL.
Insertion/Query Rate Comparison
Database
Access (pps)
MSSQL (pps)
PostgreSQL (pps)
Kafka (pps)
Insertion Rate
2000
80,000
100,000
unlimited
Query Rate
2000
200,000
333,000
OnDemand
*All units in pps (point per second)
Arbin data point takes 10 bytes in size, which contains two floats (1byte per float number) and two unsigned char (4 byte per char) which adds up to 10 bytes.
Table 4
The granularity of ∆V, ∆I, and ∆t value range must be within the precision and accuracy of ADC specification or Arbin Precision System in term PPM.
For example, a system with 100 PPM (100/1M) precision level, then ∆Vand ∆I should be in the range of 0.1mV or 0.1mA, if you set the ∆Vand ∆I in range of 0.01mA or 0.01mV, then data acquisition will not be valuable.
Please be mindful and calculate the change range to log data point precisely to have good data acquisition from your experiments.
METHOD 5
METHOD 5. Lua Script Control Type that directly controls the MCU in real-time.

  * Users can craft their own scripts using Arbin's Control Type, offering greater flexibility compared to writing schedules. This empowers users to edit and modify conditions or control types seamlessly during testing.

  * Lua scripts are primarily developed for swiftly implementing debugging algorithms and addressing unclear or incomplete functions.

  * In instances where algorithms or functions are not fully developed, users can easily adjust and customize them to suit their needs.

  * Using Lua scripting as a Control Type in the schedule offers several benefits, including flexibility in implementing custom logic tailored to specific testing requirements, ease of use due to Lua's lightweight and easy-to-learn nature, and the ability to rapidly prototype test scenarios and algorithms.

Lua Script is not available in Mits Pro8.

Figure 15. Use Lua Script as a Control Type in the Schedule
  * In Figure 16, we have four parameters p1~p4 that can be passed into the program for either the doInit function or the doControl function. The channel number corresponds to the Lua channel currently running.

  * On Line 99, the setODR function enables users to modify the ADC output data rate, providing a user-friendly approach to implementing Smart Data Logging.

Figure 16. Example of Lua Script and setODR
##  Conclusion
Using SDL with Arbin cycler can provide a more accurate and efficient way of data logging when doing the multi-channel testing on cells.
This integration stands as a testament to the commitment to excellence in scientific research and technological advancements, offering a cutting-edge solution for those seeking a robust and efficient approach to data acquisition.
