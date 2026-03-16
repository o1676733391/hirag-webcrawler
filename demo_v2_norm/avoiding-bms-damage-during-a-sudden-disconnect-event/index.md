# Metadata

| Field | Value1 |
|------|------|
| Title | Avoiding BMS Damage During a Sudden Disconnect Event |
| Page Type | Article |
| Source URL | https://www.arbin.com/avoiding-bms-damage-during-a-sudden-disconnect-event.html |
| Category | Arbin News |
| Last Updated | May 27, 2022 |

# Overview

Safety is a critical concern in undertaking battery testing, regardless of the battery format or the scale of the test. Poor safety practices or safety features in a battery management system (BMS) can result in inaccurate test data or worse, damaged batteries and risk of injury to researchers and team members. Even in the best-case scenario, the effects of unaddressed safety risks inhibit your testing progress.

While many battery chemistries will always have an inherent risk associated with their use, many of these risks can be mitigated through thorough testing and robust BMS. Protection circuits are common in most battery management systems that can disconnect a battery module/pack from a device if it senses an unsafe condition such as high temperature, cell/module voltage imbalance, or other abnormal behavior. Testing this protection circuit is important to fully qualify the BMS and battery.

**Testing battery packs? Arbin’s RBT Series is engineered to test high-power batteries for complex, real-world scenarios.** [Learn more](https://www.arbin.com/products/battery-test-equipment/pack-testing/).

# Key Points

| Topic | Summary |
|---|---|
| Sudden Disconnect | A sudden disconnect happens when a battery is disconnected while testing (charge or discharge) is in progress. This can happen when the protection circuit of a BMS is triggered. |
| Potential Dangers | The sudden disconnect of the battery creates several potential dangers, including damage to the battery under test, the BMS, or both due to a spike in current. |
| Arbin’s Protective Features | Arbin Instruments offers features such as "damping" and "voltage clamp" to minimize risks associated with sudden disconnects. |

# Detailed Explanation

A sudden disconnect happens when a battery is disconnected while testing (charge or discharge) is in progress. This can happen when the protection circuit of a Battery Management System (BMS) is triggered. The BMS protection circuit disconnects the battery pack or internal modules to halt the unsafe condition that triggered it. In response, your testing equipment will immediately react to the sudden drop in voltage down to 0V.

This sudden disconnect of the battery typically happens for one of two reasons. The first is that the protection circuit has detected a true unsafe condition during the testing cycle. In the second case, the sudden disconnect is the planned result of testing the BMS protection circuit, to ensure that it works properly.

Whether intentional or not, the sudden disconnect of the battery creates several potential dangers. Your test equipment will detect the dramatic decrease in voltage and, to regain the previous voltage value, may apply the maximum possible current. In addition to the impact on the test results, the sudden increase in current could produce a spike that can damage the battery under test, the BMS, or both.

## Arbin’s Protective Features

Arbin Instruments offers two features that, especially when applied together, can minimize the risks associated with the sudden disconnect of a battery mid-test. Arbin’s “damping” feature can be set in the test schedule for specific steps of the test and helps to prevent the channel voltage from reacting as strongly to the sudden disconnect.

![Damping Feature Screenshot showing Damping Enabled](https://www.arbin.com/wp-content/uploads/2022/05/Damping-Feature-1.jpg) **Damping Option in the Test Schedule**

In addition, Arbin’s “voltage clamp” may be applied at an appropriate voltage limit and has a rapid response time of <1 mS. The clamp features can be [applied dynamically when using Arbin’s CANBus interface](https://www.arbin.com/arbin-can-bms-to-tester-communication-with-arbins-can-bus-capability/). This can effectively let an external source such as a BMS control the Arbin tester in real-time.

![Voltage Clamp Protection](https://www.arbin.com/wp-content/uploads/2022/12/Clamp-Protections-1.jpg) **Voltage Clamp Protection**

Following a sudden disconnect situation, the Arbin system can also receive CAN message or other signal to confirm if the protection circuit did indeed disconnect the battery and stop the test.

Whether testing the function of a BMS protection circuit or running other tests, these preventative features help to ensure safety in the event of a sudden battery disconnect. They are just two of the many ways that Arbin Instruments prioritizes safety with our battery testing solutions. Our [test equipment’s built-in safety features](https://www.arbin.com/5-features-of-arbins-regenerative-battery-testing-series/) significantly reduce risk, which is especially important for a high-power testing application such as [electric vehicle battery testing](https://www.arbin.com/safe-testing-for-ev-batteries/).

To learn more about the damping and voltage clamp features, as well as other mechanisms that reduce risk in battery testing, [contact us today through our online contact form](https://www.arbin.com/request-a-quote/).

# Data / Statistics

| Metric | Value1 | Context | Notes |
|---|---|---|---|
| Response time of voltage clamp | <1 mS | Rapid response time for safety | |

# Industry Context

| Factor | Description |
|---|---|
| Battery Management System (BMS) | A system that manages a rechargeable battery, ensuring safety and performance. |

# Related Technologies / Concepts

| Concept | Description |
|---|---|
| Damping | A feature that helps to prevent voltage spikes during sudden disconnects. |
| Voltage Clamp | A feature that limits voltage to prevent damage during sudden disconnects. |

# Notes

*Autocalibration box is sold separately.*
