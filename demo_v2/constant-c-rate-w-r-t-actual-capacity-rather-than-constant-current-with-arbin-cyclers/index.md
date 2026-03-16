# Source

- URL: https://www.arbin.com/constant-c-rate-w-r-t-actual-capacity-rather-than-constant-current-with-arbin-cyclers.html

# Content

#  Constant-C-rate w.r.t. actual capacity, rather than constant current with Arbin cyclers
June 30, 2025
As we all know, the batteries’ capacity degrade by cycle of charge and discharge. If we set the charge and discharge current of a fixed value, such as 1A, 2A,… the length of each cycle will gradually decreases, simply because the battery’s capacity decreases:
_Cycle time = (Charge Capacity + Discharge Capacity)/Current_
Sometimes users want to keep cycle time constant (or almost constant) after even hundreds or thousands cycle. For example, they want the current to be fixed at 1C w.r.t. the actual capacity through the test.
Arbin’s MITS software can help you easily doing this. Below is the schedule and the explanation will come at after that.
![](https://www.arbin.com/wp-content/uploads/2025/06/battery-test-Arbin-MITS-software.png)
**1st Step:** A Rest step is normally put at the beginning of every schedule. It will play the role of safety check before entering the real test.
**2nd Step:** Set meta variable MV_UD1 as Nominal Capacity of the battery. This value is defined in test object. We assume that the value declare here is the initial Capacity of the battery.
![](https://www.arbin.com/wp-content/uploads/2025/06/battery-test-object-Arbin-MITS-software.png)
**3rd Step:** Fully charge the battery
**4th Step:** Fully discharge the capacity
**5th Step:** Update the battery’s latest capacity to the variable MV_UD1, and come back to Charge step (3rd Step). By doing this, after each cycle, when the battery’s capacity decrease, we update it and use for the next cycle.
**6th Step:** Reset the charge and discharge capacity variable, prepare to measure the latest capacity of the battery
![](https://www.arbin.com/wp-content/uploads/2025/06/battery-test-Arbin-MITS-software-2.png)
**Application of this cycling method:**
  * Evaluating degradation under real‑world charging patterns (like EVs charging overnight).
  * Conducting accelerated aging tests where cycle time must remain fixed to analyze time‑based degradation factors.

**Reference to:**
  * [BU-402: What Is C-rate?](https://batteryuniversity.com/article/bu-402-what-is-c-rate)
  * [https://www.sciencedirect.com/science/article/pii/S2950345024000198](https://www.sciencedirect.com/science/article/pii/S2950345024000198?utm_source=chatgpt.com "https://www.sciencedirect.com/science/article/pii/S2950345024000198?utm_source=chatgpt.com")
  * <https://www.nature.com/articles/s41560-024-01675-8>

Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Schedules](https://www.arbin.com/category/application-notes/schedules)
[ ![Tung Trinh](https://secure.gravatar.com/avatar/7ae5d8d92f9646066dd6e78c86d03c64ac5f9a8ae4a5890597c0025fd3bd4750?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Tung Trinh ](https://www.arbin.com)
Posts navigation
[← Synchronize different battery charge/discharge channels in one environmental temperature chamber](https://www.arbin.com/synchronize-different-battery-charge-discharge-channels-in-one-environmental-temperature-chamber.html)
[Auxiliary Temperature Measurement →](https://www.arbin.com/auxiliary-temperature-measurement.html)
