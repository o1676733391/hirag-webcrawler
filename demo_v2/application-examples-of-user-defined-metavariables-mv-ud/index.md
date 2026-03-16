# Source

- URL: https://www.arbin.com/application-examples-of-user-defined-metavariables-mv_ud.html

# Content

#  Application Examples of User-Defined MetaVariables (MV_UD)
February 26, 2026
In Arbin software, **MV_UD** (short for **User-Defined Meta Variables**) is a powerful tool for controlling battery testers. This article explains how to use **MV_UD** in **Arbin MITS** software.
  1. ##### **Storing Values in MV_UD with SetValue(s)**

In the **Control Type** list, select **SetValue(s)**.
**SetValue(s)** assigns a fixed value of a physical quantity at a specific moment to the user-defined meta variable (**MV_UD**). We’ll cover the details in the sections below.
![application examples of user defined metavariables mv ud 1](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-1.webp)
In the **Extra Control Value1** field, select the parameter you want to store. The software provides many parameters; in this example, **LS_CHAN_Charge_Capacity** is selected. **LS_CHAN_Charge_Capacity** is short for **Last Step Channel Charge Capacity**. Here, it captures the channel’s **Charge Capacity** from the previous step (**Step_D – Current**).
In the **Control Value** field, select the **MV_UD** variable where you want to store the value. In this example, **MV_UD3** is used because **MV_UD1** and **MV_UD2** are reserved for another example. In total, there are **16 MV_UD variables** available.
With this setup, the value of **LS_CHAN_Charge_Capacity** at that moment is assigned to **MV_UD3**. For instance, if the value is **1.2 Ah** , then **MV_UD3** will hold **1.2 Ah**. When **MV_UD3** is called in later steps, it will still return **1.2 Ah** unless you assign a new value to **MV_UD3**.
Besides charge capacity, it can store many other variables well—for example, the last-step voltage, formulas, and CAN/SMB messages. To explore these options, right-click the **Control Value** field and choose either **Meta Variable…** or **Goto Formula**.
![application examples of user defined metavariables mv ud 2](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-2.webp)
![application examples of user defined metavariables mv ud 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201293%20805'%3E%3C/svg%3E)
  1. ##### **Store Variables in MV_UD Using SetReference**

**SetReference(s)** stores a reference in an **MV_UD** meta variable. Unlike **SetValue(s)** , the stored reference is _linked_ to the selected metavariables—so when that metavariable’s value changes, the value of **MV_UD** updates automatically. We’ll cover the details in the sections below.
In the **Control Type** list, select **SetReference(s)** instead of **SetValue(s)**.
![application examples of user defined metavariables mv ud 4](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-4.webp)
In the example above, after **Step_E** assigns **Channel Charge Capacity** to **MV_UD3** , **MV_UD3** updates continuously as that quantity changes over the course of the test, as shown in the data below:
![application examples of user defined metavariables mv ud 5](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-5.webp)
We can see that even after **Step 3** , **MV_UD3** continues to update during **Step 4**. This behavior is the key difference compared with the **SetValue(s)** control type.
**SetReference** is usually used to record the referenced value to the exported date file.
  1. ##### **Update MV_UD from third-party software via CTI(Console TCP/IP Interface) and use it to control the channel.**

We’ll walk through a simple example of using **MV_UD** to control the current during a test. In this example, we use the **Current** control type and set the current using an **MV_UD** value rather than a fixed number.
In the **Control Value** field, select **MV_UD1** instead of entering a numeric value (**right-click → Meta Variable**).
Optional: In the **Global** tab, you can assign alias names to **MV_UD1** and **MV_UD2**. In this example, they are named **ChargeCC** and **DischargeCC**. You can also set default values for these variables:
![application examples of user defined metavariables mv ud 6](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-6-1.webp)
As an example of a third-party application using **CTI** , we’ll use **ArbinViewer**. Although ArbinViewer is developed by Arbin, from the **MITS** software perspective it is treated as third-party software. Users can develop their own script/software to update MV_UDs through CTI.
After you complete the connection and setup in ArbinViewer, go to **Control → Set MetaVariables** , then assign the required value to **MV_UD1**.
![application examples of user defined metavariables mv ud 7](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-7.webp)
![application examples of user defined metavariables mv ud 8](https://www.arbin.com/wp-content/uploads/2026/02/application-examples-of-user-defined-metavariables-mv_ud-8.webp)
This value is sent to **MITS** and used to update the current setpoint in the **Current** step.
**Note:** The channel receives MV_UD updates only while the test is already running. If you set **MV_UD** before starting the channel, the value will not take effect.
In addition to the **Current** control type, you can use the same MV_UD method with many other control types, such as **Voltage** , **Power** , and **C-Rate**.
Reference:
ArbinViewer manual
MITS manual
Posted in [Application Notes](https://www.arbin.com/category/application-notes)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← How to plot Potential vs Current Graph by Arbin Data Watcher](https://www.arbin.com/how-to-plot-potential-vs-current-graph-by-arbin-data-watcher.html)
[Arbin to Showcase Advanced Battery Testing Solutions at InterBattery 2026 in Seoul →](https://www.arbin.com/arbin-to-showcase-advanced-battery-testing-solutions-at-interbattery-2026-in-seoul.html)
