# Source

- URL: https://www.arbin.com/synchronize-different-battery-charge-discharge-channels-in-one-environmental-temperature-chamber.html

# Content

#  Synchronize different battery charge/discharge channels in one environmental temperature chamber
June 17, 2025
**MTCI Introduction**
Arbin’s **MTCI (Multi-Temperature Chamber Interface)** module offers seamless and sophisticated integration with third-party environmental chambers, enabling **direct control of temperature and humidity setpoints** from within the Arbin test schedule. This streamlined setup allows test engineers to program and adjust environmental conditions alongside electrical cycling parameters, eliminating the need for separate chamber control systems.
Environmental conditions—including temperature and humidity—are **synchronously logged with current, voltage, and other electrical data** , offering a unified dataset for analysis. These parameters can be **visualized in real time** through Arbin’s software interface and exported for detailed post-test evaluation, ensuring full traceability and high-resolution insights into test behavior.
**MTCI Features**
  * **Seamless Chamber Control:**

  *     * Read and write temperature and humidity set points with compatible third-party chamber controllers.

  * **Multi-Channel Synchronization:**

  *     * Ensure multiple test channels reach the same step before applying a new temperature setting.

  * **Temperature-Driven Test Logic:**

  *     * Advance test steps only when the chamber reaches the target temperature.

  *     * Use chamber temperature within a formula alongside measured cell temperature to proceed only when both have equilibrated.

  * **Automated Standby Mode:**

  *     * Set a chamber standby temperature after test completion.

![](https://www.arbin.com/wp-content/uploads/2025/06/Auxiliary-MTCI-Module-e1750207597375.png)
Figure 1: Auxiliary MTCI Module
  * **Group T_Chamber Management Feature**

The Group T_Chamber Management feature is especially valuable when multiple battery cells are tested simultaneously inside a single environmental chamber. In these cases, consistent chamber conditions must be maintained across all test channels to ensure valid and repeatable results. However, when each channel progresses through its test independently, coordinating shared chamber conditions becomes more complex.
Without proper coordination, a single test channel may prematurely trigger a change in the chamber’s temperature or humidity setpoint—**before other channels have reached the corresponding control point** in their respective test schedules. This can lead to **inconsistent environmental exposure** , potentially compromising the **accuracy, repeatability, and comparability** of the test results. To address this challenge, Arbin’s system includes a **synchronization mechanism** that ensures all test channels reach the designated temperature control step before the chamber conditions are adjusted. This approach guarantees cohesive and reliable execution in shared-chamber testing environments.
**Application Example**
**How to use Arbin’s “test setting” functionality to control temperature chamber:**
Create a test setting to define temperature condition as illustrated below(set chamber temperature to 25C):
![](https://www.arbin.com/wp-content/uploads/2025/06/Arbin-Application-Note-Group-Temperature-Chamber-Management.png)
Figure 2: Test Settings Window
Reference test setting to the test schedule as illustrated below:
![](https://www.arbin.com/wp-content/uploads/2025/06/Select-Test-Settings-in-Test-Schedule-Arbin-Application-Note.png)
Figure 3: Select Test Settings in Test Schedule
In the example above, when “TestStg_A” is selected, Step A will set the [**temperature chamber**](https://www.arbin.com/synchronize-different-battery-charge-discharge-channels-in-one-environmental-temperature-chamber.html) to 25°C. More details of the function can be found inside Arbin MITS manual.
**Group T_Chamber Feature**
Arbin systems support synchronization for a group of test channels where multiple cells/batteries are tested inside the same temperature chamber together. The chamber temperature can be adjusted after all channels have reached the same stage in the test.
**Example Test Schedule**
Below is a sample schedule implemented by Chamber Group Management.
![](https://www.arbin.com/wp-content/uploads/2025/06/Example-Test-Schedule-Arbin-Application-Note.png)
Figure 4: Example Test Schedule
**Illustration of Test Sequence**
  * All IV channels will be synchronized at step 2, then go to step 3 together.

  * The first IV channel sets the chamber temperature to T1 (the IV channel with the lowest channel number, here is channel 1)

  * While Channel 1 sets the temperature, the other channels will wait until the Step 3 limit is reached. This step limit of these channels must be the same because they are using the same schedule; however, the time it happens can be different.
  * After a charge/discharge cycle, all IV channels reach step 6 successively and be synchronized here again before continuing to step 7 and set chamber temperature to T2.

![Illustration of Test Sequence - Arbin Application Note](https://www.arbin.com/wp-content/uploads/2025/06/Illustration-of-Test-Sequence-Arbin-Application-Note.png)Figure 5: Illustration of Test Sequence
**Pause Step Behavior and Data Logging**
When using the **Pause → T_Chamber** step for synchronized temperature control, each IV channel enters a pause state and waits for all other channels in the same chamber group to reach the same point in the schedule. Only once all channels arrive at the synchronization step will the test proceed to the next step, often involving a new chamber temperature setpoint.
**Important Note:**
During the pause step, the Arbin system does **not log test data**. This includes current, voltage, temperature, or any auxiliary inputs. The pause step is considered an inactive waiting period and does not produce test measurements. This design ensures that data logs only reflect active test execution and avoid artificial flatlines or gaps due to idle time.
Below is an example screenshot illustrating this behavior, where logging is suspended during the pause period:
![Example data log showing no recorded measurements during pause step while waiting for synchronization](https://www.arbin.com/wp-content/uploads/2025/06/Example-data-log-Arbin-Application-Note-e1750207490623.png)  

Figure 6: Example data log showing no recorded measurements during pause step while waiting for synchronization
This behavior is consistent across all channels using Group T_Chamber control and is important to consider during data analysis, especially when calculating cycle durations or interpreting time-based performance trends.
Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Schedules](https://www.arbin.com/category/application-notes/schedules)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Formula and variables used in Arbin MITS software for flexible battery testing](https://www.arbin.com/formula-and-variables-used-in-arbin-mits-software-for-flexible-battery-testing.html)
[Constant-C-rate w.r.t. actual capacity, rather than constant current with Arbin cyclers →](https://www.arbin.com/constant-c-rate-w-r-t-actual-capacity-rather-than-constant-current-with-arbin-cyclers.html)
