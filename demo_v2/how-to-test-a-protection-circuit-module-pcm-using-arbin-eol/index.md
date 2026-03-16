# Source

- URL: https://www.arbin.com/how-to-test-a-protection-circuit-module-pcm-using-arbin-eol.html

# Content

#  How to Test a Protection Circuit Module (PCM) Using ARBIN EOL
July 23, 2025
## **I. Purpose and Scope:**
The Protection Circuit Module (PCM) is a critical electronic component responsible for monitoring and protecting devices across a wide range of applications—from small consumer electronics to large-scale industrial equipment. Its core function is to ensure battery and device safety by preventing hazardous conditions such as overcharging, over-discharging, overcurrent, and short circuits
![protection circuit module pcm](https://www.arbin.com/wp-content/uploads/2025/07/protection-circuit-module-pcm-using-arbin.png)
Arbin offers an End-of-Line (EOL) testing solution tailored for customers’ production lines to evaluate the functionality and reliability of Protection Circuit Modules (PCMs). This testing ensures that the PCM responds appropriately when a battery’s voltage or current exceeds its designed minimum or maximum thresholds. Under such conditions, the PCM should automatically disconnect to prevent damage or safety hazards associated with overvoltage, undervoltage, overcurrent, or short-circuit events.
## II. Testing
  1. **Procedure**

![How to test Protection Circuit Module](https://www.arbin.com/wp-content/uploads/2025/07/How-to-test-Protection-Circuit-Module.png)
The following steps outline the standard procedure implemented using the Arbin EOL system to verify the PCM’s key protection functions. Each step simulates fault conditions to validate the PCM’s ability to disconnect or recover as designed.
**Step** |  **Test Item** |  **Description**  
---|---|---  
1 |  **Overcharge Protection** |  Simulate battery overcharging. Gradually increase voltage until the PCM disconnects. Record the voltage at which the output current drops to 0 A.  
2 |  **Overcharge Release** |  Slowly decrease the variable power supply voltage. Record the voltage at which current output resumes.  
3 |  **Undercharge Protection** |  Simulate battery undercharging. Gradually decrease the voltage until the PCM disconnects. Record the voltage when the output current drops to 0 A.  
4 |  **Undercharge Release** |  Slowly increase the variable power supply voltage. Record the voltage at which current output resumes.  
5 |  **Charge Overcurrent Detection** |  Confirm the overcurrent protection during charging. Gradually increase current and record the value at which the PCM activates the cutoff.  
6 |  **Discharge Overcurrent Detection** |  Confirm the overcurrent protection during discharging. Gradually increase discharge current and record the value at which the PCM activates the cutoff.  
Implementing it using Arbin MITS 11 software:
**Step** |  Test Name |  Description |   
---|---|---|---  
|  **Test Overcharge Voltage** |  Simulate a battery overcharge condition by gradually increasing the voltage. The PCM should disable the output once the voltage exceeds the predefined threshold. This is confirmed by observing that the output current drops to **0 A**. |  [![est Overcharge Voltage](https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png)](https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png)  
**2** |  **Confirm Overcharge Recovery** |  Slowly decrease the voltage to verify that the PCM automatically re-enables output when the voltage returns to a safe range. This step ensures proper recovery behavior after an overcharge event. |  [![Confirm Overcharge Recovery](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png)](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png)  
**3** |  **Test Undercharge Voltage** |  Simulate a deep discharge by gradually lowering the voltage. The PCM should cut off the output to protect the battery from over-discharge once the voltage drops below the safe limit. |  [![Test Undercharge Voltage](https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png)](https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png)  
**4** |  **Confirm Undercharge Release** |  Reverse the undercharge condition by increasing the voltage gradually. The PCM should restore output when the voltage reaches a safe level, ensuring the circuit doesn’t remain unnecessarily disabled. |  [![Confirm Undercharge Release](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png)](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png)  
**5** |  **Confirm Charge Overcurrent Protection** |  Apply a charging current ramp. The PCM must detect when the charging current exceeds the allowable limit and disconnect to prevent overheating or damage. **Note:** To calculate the overcurrent value (**I <sub>end</sub>**), the following formulas are used:  
• `Iend = (2 × Capacity × 3600) / t - Istart`  
• or `Iend = Istart + DI/sec × LS_Chan_Step_Time` **Capacity logging methods:**  
• Use `TestCounter`  
• Or fetch the last (previous) step value from the channel |  [![Confirm Charge Overcurrent Protection](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png)](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png) [![LS charge capacity](https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png)](https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png) LS_charge_capacity [![TC Charge Capacity](https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png)](https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png) TC_Charge_Capacity  
**6** |  **Confirm Discharge Overcurrent Protection** |  Test the PCM’s response to an excessive discharge current. The PCM should cut off the output once the discharge current exceeds the safety threshold. **Note:** Same formula applies as in Step 5:
  * Iend = -(2 × Capacity × 3600) / t + Istart
  * Iend = Istart + DI/sec * LS_Chan_Step_Time

**Capacity logging methods:**  
• Use `TestCounter`  
• Or fetch the final step value from the channel |  [![Confirm Discharge Overcurrent Protectio](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201367%20662'%3E%3C/svg%3E)](https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png) [![LS discharge capacity](https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png)](https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png) LS_discharge_capacity [![TC discharge capacity](https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png)](https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png) TC_discharge_capacity  
  1. **EOL Automation line integration:**

The following images showcase the configuration and automation capabilities of **MITS 11** software in an End-of-Line (EOL) testing environment. These setups are specifically designed to implement the PCM validation tests described above:
**Interface of EOL dashboard** |  ![](https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png)  
---|---  
**EOL Test Report** |  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201323%20752'%3E%3C/svg%3E)  
**Test Summary Details** |  Test |  Criteria |  Measured Value |  Result  
1 |  **Overcharge Voltage** |  In Range [4.1, 4.4] V |  4.007742A |  ❌ Failed  
2 |  **Overcharge Voltage release** |  In Range [3.5, 4] V |  3.6116747 V |  ✅ Passed  
3 |  **Undercharge Voltage** |  In Range [2.8, 3,2] V |  2.992585 V |  ✅ Passed  
4 |  **Undercharge Voltage Release** |  In Range [3.35, 3.8] V |  3.406495 V |  ✅ Passed  
5 |  **Charge Overcurrent** |  In Range [0.8, 1.26] A |  1.257388 A |  ✅ Passed  
6 |  **Discharge Overcurrent** |  In Range [-1.2,- 0.8] A |  -1.191427 |  ✅ Passed  
After completing all six critical test steps using ARBIN’s EOL platform, the result shows that the first criteria fails and 5 others succeed. Since one test failed, we can conclude that the PCM does not perform exactly as designed, meaning it failed the test. Only when all 6 tests are passed, the PCM is considered passed.
The set of tests like this ensures that the PCM’s protection logic works well in real operation of the battery after leaving factories. This is essential not only for **battery longevity** but also for **user safety** and **product reliability**.
For further assistance, please contact us: support.asia@arbin.com
For more detail: [Protection Circuit Modules for Custom Battery Packs](https://www.epectec.com/articles/protection-circuit-modules-for-custom-battery-packs.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Auxiliary Voltage Measurement](https://www.arbin.com/auxiliary-voltage-measurement.html)
[Integrated Electrochemical Impedance Spectroscopy (EIS) With Arbin Charge/Discharge Channels →](https://www.arbin.com/integrated-electrochemical-impedance-spectroscopy-eis-with-arbin-charge-discharge-channels.html)

## Table-like Div HTML (Original)

```html
<div class="pm-table-container with-shadow-observer" data-layout="custom" data-testid="table-container">
<div class="pm-table-wrapper" data-number-column="false" data-layout="default" data-autosize="false" data-table-local-id="dca9649b-fb24-4b65-8ba5-add1b9044383" data-table-width="760" data-vc="table-node-wrapper">
<div class="sentinel-left"></div>
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
<colgroup>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="91" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1384"><strong data-renderer-mark="true">Step</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="207" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1392"><strong data-renderer-mark="true">Test Item</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="460" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1405"><strong data-renderer-mark="true">Description</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1422">1</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1427"><strong data-renderer-mark="true">Overcharge Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1452">Simulate battery overcharging. Gradually increase voltage until the PCM disconnects. Record the voltage at which the output current drops to 0 A.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1603">2</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1608"><strong data-renderer-mark="true">Overcharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1630">Slowly decrease the variable power supply voltage. Record the voltage at which current output resumes.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1738">3</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1743"><strong data-renderer-mark="true">Undercharge Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1769">Simulate battery undercharging. Gradually decrease the voltage until the PCM disconnects. Record the voltage when the output current drops to 0 A.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1921">4</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1926"><strong data-renderer-mark="true">Undercharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1949">Slowly increase the variable power supply voltage. Record the voltage at which current output resumes.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="2057">5</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="2062"><strong data-renderer-mark="true">Charge Overcurrent Detection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="2094">Confirm the overcurrent protection during charging. Gradually increase current and record the value at which the PCM activates the cutoff.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="2238">6</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="2243"><strong data-renderer-mark="true">Discharge Overcurrent Detection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="2278">Confirm the overcurrent protection during discharging. Gradually increase discharge current and record the value at which the PCM activates the cutoff.</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
</div>
```

```html
<div class="pm-table-wrapper" data-number-column="false" data-layout="default" data-autosize="false" data-table-local-id="dca9649b-fb24-4b65-8ba5-add1b9044383" data-table-width="760" data-vc="table-node-wrapper">
<div class="sentinel-left"></div>
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
<colgroup>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="91" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1384"><strong data-renderer-mark="true">Step</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="207" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1392"><strong data-renderer-mark="true">Test Item</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="460" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="1405"><strong data-renderer-mark="true">Description</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon cc-xy3osd" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66"></div>
</div>
</div>
</figure>
</div>
</th>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1422">1</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1427"><strong data-renderer-mark="true">Overcharge Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1452">Simulate battery overcharging. Gradually increase voltage until the PCM disconnects. Record the voltage at which the output current drops to 0 A.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1603">2</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1608"><strong data-renderer-mark="true">Overcharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1630">Slowly decrease the variable power supply voltage. Record the voltage at which current output resumes.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1738">3</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1743"><strong data-renderer-mark="true">Undercharge Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1769">Simulate battery undercharging. Gradually decrease the voltage until the PCM disconnects. Record the voltage when the output current drops to 0 A.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="1921">4</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="1926"><strong data-renderer-mark="true">Undercharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="1949">Slowly increase the variable power supply voltage. Record the voltage at which current output resumes.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="2057">5</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="2062"><strong data-renderer-mark="true">Charge Overcurrent Detection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="2094">Confirm the overcurrent protection during charging. Gradually increase current and record the value at which the PCM activates the cutoff.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="91">
<p data-renderer-start-pos="2238">6</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="207">
<p data-renderer-start-pos="2243"><strong data-renderer-mark="true">Discharge Overcurrent Detection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="460">
<p data-renderer-start-pos="2278">Confirm the overcurrent protection during discharging. Gradually increase discharge current and record the value at which the PCM activates the cutoff.</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
```

```html
<div class="pm-table-container with-shadow-observer" data-layout="custom" data-testid="table-container">
<div class="pm-table-sticky-scrollbar-sentinel-top" data-testid="sticky-scrollbar-sentinel-top"></div>
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="b3b60ab1-b4eb-4aec-945e-b24ae7ee438e" data-table-width="732" data-vc="table-node-wrapper">
<div class="sentinel-left"></div>
<table data-testid="renderer-table" data-number-column="false" data-table-width="732" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p data-renderer-start-pos="2484"><strong data-renderer-mark="true">Step</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p data-renderer-start-pos="2492">Test Name</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2505">Description</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<p data-renderer-start-pos="2520">
</p>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p data-renderer-start-pos="2526">
</p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Test-Overcharge-Voltage" data-renderer-start-pos="2530"><strong data-renderer-mark="true">Test Overcharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2557">Simulate a battery overcharge condition by gradually increasing the voltage. The PCM should disable the output once the voltage exceeds the predefined threshold. This is confirmed by observing that the output current drops to <strong data-renderer-mark="true">0 A</strong>.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="2791" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-2">
<div class="cc-p9yfsk">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1352" data-height="737" data-id="56a6cdd7-f835-42d4-8267-1f84f1660383" data-collection="contentId-787513446" data-file-name="image-20250507-041850.png" data-file-size="82036" data-file-mime-type="image/png" data-alt="image-20250507-041850.png" data-renderer-start-pos="2792" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-2" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041850.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png"><img decoding="async" class="alignnone size-full wp-image-29981 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" alt="est Overcharge Voltage" width="1080" height="588" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w" data-lazy-sizes="(max-width: 1352px) 100vw, 1352px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" data-ll-status="loaded" sizes="(max-width: 1352px) 100vw, 1352px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29981" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" alt="est Overcharge Voltage" width="1352" height="737" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w" sizes="(max-width: 1352px) 100vw, 1352px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="2" data-renderer-start-pos="2800"><strong data-renderer-mark="true">2</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Overcharge-Recovery" data-renderer-start-pos="2805"><strong data-renderer-mark="true">Confirm Overcharge Recovery</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2836">Slowly decrease the voltage to verify that the PCM automatically re-enables output when the voltage returns to a safe range. This step ensures proper recovery behavior after an overcharge event.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3034" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-3">
<div class="cc-anxq2j">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1331" data-height="739" data-id="4c2f8acf-7915-4a1c-ade4-8a23c5c2ea7c" data-collection="contentId-787513446" data-file-name="image-20250507-041821.png" data-file-size="84446" data-file-mime-type="image/png" data-alt="image-20250507-041821.png" data-renderer-start-pos="3035" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-3" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041821.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png"><img decoding="async" class="alignnone size-full wp-image-29982 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" alt="Confirm Overcharge Recovery" width="1080" height="599" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w" data-lazy-sizes="(max-width: 1331px) 100vw, 1331px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" data-ll-status="loaded" sizes="(max-width: 1331px) 100vw, 1331px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29982" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" alt="Confirm Overcharge Recovery" width="1331" height="739" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w" sizes="(max-width: 1331px) 100vw, 1331px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="3" data-renderer-start-pos="3041"><strong data-renderer-mark="true">3 </strong></p>
<p data-renderer-start-pos="3045">
</p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Test-Undercharge-Voltage" data-renderer-start-pos="3049"><strong data-renderer-mark="true">Test Undercharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3077">Simulate a deep discharge by gradually lowering the voltage. The PCM should cut off the output to protect the battery from over-discharge once the voltage drops below the safe limit.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3263" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-4">
<div class="cc-1nkohnd">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1350" data-height="744" data-id="21beb09f-7ac8-41a9-bf50-a6218c3a44a8" data-collection="contentId-787513446" data-file-name="image-20250507-041927.png" data-file-size="82208" data-file-mime-type="image/png" data-alt="image-20250507-041927.png" data-renderer-start-pos="3264" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-4" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041927.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png"><img decoding="async" class="alignnone size-full wp-image-29983 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" alt="Test Undercharge Voltage" width="1080" height="595" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w" data-lazy-sizes="(max-width: 1350px) 100vw, 1350px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" data-ll-status="loaded" sizes="(max-width: 1350px) 100vw, 1350px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29983" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" alt="Test Undercharge Voltage" width="1350" height="744" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w" sizes="(max-width: 1350px) 100vw, 1350px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<p data-renderer-start-pos="3266">
</p>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="4" data-renderer-start-pos="3272"><strong data-renderer-mark="true">4</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Undercharge-Release" data-renderer-start-pos="3277"><strong data-renderer-mark="true"> Confirm Undercharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3309">Reverse the undercharge condition by increasing the voltage gradually. The PCM should restore output when the voltage reaches a safe level, ensuring the circuit doesn’t remain unnecessarily disabled.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3512" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-5">
<div class="cc-1fxaha7">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1343" data-height="742" data-id="529d96b3-8168-4418-871e-1542c3c3a8fb" data-collection="contentId-787513446" data-file-name="image-20250507-041945.png" data-file-size="79987" data-file-mime-type="image/png" data-alt="image-20250507-041945.png" data-renderer-start-pos="3513" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-5" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041945.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png"><img decoding="async" class="alignnone size-full wp-image-29984 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" alt="Confirm Undercharge Release" width="1080" height="596" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w" data-lazy-sizes="(max-width: 1343px) 100vw, 1343px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" data-ll-status="loaded" sizes="(max-width: 1343px) 100vw, 1343px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29984" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" alt="Confirm Undercharge Release" width="1343" height="742" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w" sizes="(max-width: 1343px) 100vw, 1343px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="5" data-renderer-start-pos="3521"><strong data-renderer-mark="true">5 </strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Charge-Overcurrent-Protection" data-renderer-start-pos="3527"><strong data-renderer-mark="true">Confirm Charge Overcurrent Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3568">Apply a charging current ramp. The PCM must detect when the charging current exceeds the allowable limit and disconnect to prevent overheating or damage.</p>
<p><strong data-renderer-mark="true">Note:</strong> To calculate the overcurrent value (<strong data-renderer-mark="true">I&lt;sub&gt;end&lt;/sub&gt;</strong>), the following formulas are used:<br>
• <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">Iend = (2 × Capacity × 3600) / t - Istart</code><br>
• or <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">Iend = Istart + DI/sec × LS_Chan_Step_Time</code></p>
<p><strong data-renderer-mark="true">Capacity logging methods:</strong><br>
• Use <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">TestCounter</code><br>
• Or fetch the last (previous) step value from the channel</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4023" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-6">
<div class="cc-1idqb4z">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1419" data-height="704" data-id="4bc8265f-3d9a-4d5b-a699-7c7c94b9b062" data-collection="contentId-787513446" data-file-name="image-20250508-012916.png" data-file-size="77930" data-file-mime-type="image/png" data-alt="image-20250508-012916.png" data-renderer-start-pos="4024" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-6" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-012916.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png"><img decoding="async" class="alignnone size-full wp-image-29985 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" alt="Confirm Charge Overcurrent Protection" width="1080" height="535" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w" data-lazy-sizes="(max-width: 1419px) 100vw, 1419px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" data-ll-status="loaded" sizes="(max-width: 1419px) 100vw, 1419px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29985" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" alt="Confirm Charge Overcurrent Protection" width="1419" height="704" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w" sizes="(max-width: 1419px) 100vw, 1419px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-g3f5ts" data-width="228" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4026" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-7">
<div class="cc-1bjx3mm">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1474" data-height="549" data-id="3a8d6833-e86e-4a8d-bf5f-514e76f73d7f" data-collection="contentId-787513446" data-file-name="image-20250701-093031.png" data-file-size="32877" data-file-mime-type="image/png" data-alt="image-20250701-093031.png" data-renderer-start-pos="4027" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-7" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093031.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png"><img decoding="async" class="alignnone size-full wp-image-29986 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" alt="LS charge capacity" width="1080" height="402" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w" data-lazy-sizes="(max-width: 1327px) 100vw, 1327px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" data-ll-status="loaded" sizes="(max-width: 1327px) 100vw, 1327px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29986" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" alt="LS charge capacity" width="1327" height="494" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w" sizes="(max-width: 1327px) 100vw, 1327px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4028">LS_charge_capacity</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-g3f5ts" data-width="228" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4049" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-8">
<div class="cc-1wspy2c">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1486" data-height="568" data-id="6e9c3d98-3cde-4de6-a9fd-3e77d06ad23f" data-collection="contentId-787513446" data-file-name="image-20250701-093121.png" data-file-size="32370" data-file-mime-type="image/png" data-alt="image-20250701-093121.png" data-renderer-start-pos="4050" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-8" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093121.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png"><img decoding="async" class="alignnone size-full wp-image-29987 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" alt="TC Charge Capacity" width="1080" height="412" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w" data-lazy-sizes="(max-width: 1337px) 100vw, 1337px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" data-ll-status="loaded" sizes="(max-width: 1337px) 100vw, 1337px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29987" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" alt="TC Charge Capacity" width="1337" height="511" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w" sizes="(max-width: 1337px) 100vw, 1337px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4051">TC_Charge_Capacity</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="6" data-renderer-start-pos="4076"><strong data-renderer-mark="true">6</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Discharge-Overcurrent-Protection" data-renderer-start-pos="4081"><strong data-renderer-mark="true">Confirm Discharge Overcurrent Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="4125">Test the PCM’s response to an excessive discharge current. The PCM should cut off the output once the discharge current exceeds the safety threshold.</p>
<p data-renderer-start-pos="4276"><strong data-renderer-mark="true">Note:</strong> Same formula applies as in Step 5:</p>
<ul class="ak-ul" data-indent-level="1">
<li>
<p data-renderer-start-pos="4320">Iend = -(2 × Capacity × 3600) / t + Istart</p>
</li>
<li>
<p data-renderer-start-pos="4366">Iend = Istart + DI/sec * LS_Chan_Step_Time</p>
</li>
</ul>
<p data-renderer-start-pos="4412"><strong data-renderer-mark="true">Capacity logging methods:</strong><br>
• Use <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">TestCounter</code><br>
• Or fetch the final step value from the channel</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4512" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-9">
<div class="cc-14m9y23">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1367" data-height="662" data-id="dc990b0a-4f4c-444f-a856-cc02ec66c3b9" data-collection="contentId-787513446" data-file-name="image-20250508-012947.png" data-file-size="78419" data-file-mime-type="image/png" data-alt="image-20250508-012947.png" data-renderer-start-pos="4513" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-9" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-012947.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png"><img decoding="async" class="alignnone size-full wp-image-29988 entered exited" alt="Confirm Discharge Overcurrent Protectio" width="300" height="145" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png 1367w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-500x242.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-768x372.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-1024x496.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-600x291.png 600w" data-lazy-sizes="(max-width: 1367px) 100vw, 1367px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201367%20662'%3E%3C/svg%3E"><noscript><img decoding="async" class="alignnone size-full wp-image-29988" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png" alt="Confirm Discharge Overcurrent Protectio" width="1367" height="662" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png 1367w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-500x242.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-768x372.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-1024x496.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-600x291.png 600w" sizes="(max-width: 1367px) 100vw, 1367px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4515" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-10">
<div class="cc-eos0nu">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1483" data-height="562" data-id="6be6facc-8d29-4df9-bccf-0f68ea333dd5" data-collection="contentId-787513446" data-file-name="image-20250701-093322.png" data-file-size="33576" data-file-mime-type="image/png" data-alt="image-20250701-093322.png" data-renderer-start-pos="4516" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-10" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093322.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png"><img decoding="async" class="alignnone size-full wp-image-29989 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" alt="LS discharge capacity" width="1080" height="409" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w" data-lazy-sizes="(max-width: 1335px) 100vw, 1335px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" data-ll-status="loaded" sizes="(max-width: 1335px) 100vw, 1335px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29989" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" alt="LS discharge capacity" width="1335" height="506" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w" sizes="(max-width: 1335px) 100vw, 1335px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4517">LS_discharge_capacity</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4541" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-11">
<div class="cc-18eoaqp">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1460" data-height="559" data-id="acd0ecc4-984c-4b24-9527-2c6293ea7e94" data-collection="contentId-787513446" data-file-name="image-20250701-093244.png" data-file-size="32629" data-file-mime-type="image/png" data-alt="image-20250701-093244.png" data-renderer-start-pos="4542" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-11" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093244.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png"><img decoding="async" class="alignnone size-full wp-image-29990 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" alt="TC discharge capacity" width="1080" height="413" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w" data-lazy-sizes="(max-width: 1314px) 100vw, 1314px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" data-ll-status="loaded" sizes="(max-width: 1314px) 100vw, 1314px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29990" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" alt="TC discharge capacity" width="1314" height="503" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w" sizes="(max-width: 1314px) 100vw, 1314px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4543">TC_discharge_capacity</div>
</div>
<p data-renderer-start-pos="4569">
</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
</div>
```

```html
<div class="pm-table-sticky-scrollbar-sentinel-top" data-testid="sticky-scrollbar-sentinel-top"></div>
```

```html
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="b3b60ab1-b4eb-4aec-945e-b24ae7ee438e" data-table-width="732" data-vc="table-node-wrapper">
<div class="sentinel-left"></div>
<table data-testid="renderer-table" data-number-column="false" data-table-width="732" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p data-renderer-start-pos="2484"><strong data-renderer-mark="true">Step</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p data-renderer-start-pos="2492">Test Name</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2505">Description</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<p data-renderer-start-pos="2520">
</p>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p data-renderer-start-pos="2526">
</p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Test-Overcharge-Voltage" data-renderer-start-pos="2530"><strong data-renderer-mark="true">Test Overcharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2557">Simulate a battery overcharge condition by gradually increasing the voltage. The PCM should disable the output once the voltage exceeds the predefined threshold. This is confirmed by observing that the output current drops to <strong data-renderer-mark="true">0 A</strong>.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="2791" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-2">
<div class="cc-p9yfsk">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1352" data-height="737" data-id="56a6cdd7-f835-42d4-8267-1f84f1660383" data-collection="contentId-787513446" data-file-name="image-20250507-041850.png" data-file-size="82036" data-file-mime-type="image/png" data-alt="image-20250507-041850.png" data-renderer-start-pos="2792" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-2" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041850.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png"><img decoding="async" class="alignnone size-full wp-image-29981 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" alt="est Overcharge Voltage" width="1080" height="588" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w" data-lazy-sizes="(max-width: 1352px) 100vw, 1352px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" data-ll-status="loaded" sizes="(max-width: 1352px) 100vw, 1352px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29981" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png" alt="est Overcharge Voltage" width="1352" height="737" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage.png 1352w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-500x273.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-768x419.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-1024x558.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Overcharge-Voltage-600x327.png 600w" sizes="(max-width: 1352px) 100vw, 1352px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="2" data-renderer-start-pos="2800"><strong data-renderer-mark="true">2</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Overcharge-Recovery" data-renderer-start-pos="2805"><strong data-renderer-mark="true">Confirm Overcharge Recovery</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="2836">Slowly decrease the voltage to verify that the PCM automatically re-enables output when the voltage returns to a safe range. This step ensures proper recovery behavior after an overcharge event.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3034" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-3">
<div class="cc-anxq2j">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1331" data-height="739" data-id="4c2f8acf-7915-4a1c-ade4-8a23c5c2ea7c" data-collection="contentId-787513446" data-file-name="image-20250507-041821.png" data-file-size="84446" data-file-mime-type="image/png" data-alt="image-20250507-041821.png" data-renderer-start-pos="3035" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-3" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041821.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png"><img decoding="async" class="alignnone size-full wp-image-29982 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" alt="Confirm Overcharge Recovery" width="1080" height="599" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w" data-lazy-sizes="(max-width: 1331px) 100vw, 1331px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" data-ll-status="loaded" sizes="(max-width: 1331px) 100vw, 1331px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29982" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png" alt="Confirm Overcharge Recovery" width="1331" height="739" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery.png 1331w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-500x278.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-768x426.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-1024x569.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Overcharge-Recovery-600x333.png 600w" sizes="(max-width: 1331px) 100vw, 1331px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="3" data-renderer-start-pos="3041"><strong data-renderer-mark="true">3 </strong></p>
<p data-renderer-start-pos="3045">
</p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Test-Undercharge-Voltage" data-renderer-start-pos="3049"><strong data-renderer-mark="true">Test Undercharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3077">Simulate a deep discharge by gradually lowering the voltage. The PCM should cut off the output to protect the battery from over-discharge once the voltage drops below the safe limit.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3263" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-4">
<div class="cc-1nkohnd">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1350" data-height="744" data-id="21beb09f-7ac8-41a9-bf50-a6218c3a44a8" data-collection="contentId-787513446" data-file-name="image-20250507-041927.png" data-file-size="82208" data-file-mime-type="image/png" data-alt="image-20250507-041927.png" data-renderer-start-pos="3264" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-4" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041927.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png"><img decoding="async" class="alignnone size-full wp-image-29983 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" alt="Test Undercharge Voltage" width="1080" height="595" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w" data-lazy-sizes="(max-width: 1350px) 100vw, 1350px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" data-ll-status="loaded" sizes="(max-width: 1350px) 100vw, 1350px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29983" src="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png" alt="Test Undercharge Voltage" width="1350" height="744" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage.png 1350w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-768x423.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-1024x564.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Test-Undercharge-Voltage-600x331.png 600w" sizes="(max-width: 1350px) 100vw, 1350px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<p data-renderer-start-pos="3266">
</p>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="4" data-renderer-start-pos="3272"><strong data-renderer-mark="true">4</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Undercharge-Release" data-renderer-start-pos="3277"><strong data-renderer-mark="true"> Confirm Undercharge Release</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3309">Reverse the undercharge condition by increasing the voltage gradually. The PCM should restore output when the voltage reaches a safe level, ensuring the circuit doesn’t remain unnecessarily disabled.</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="3512" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-5">
<div class="cc-1fxaha7">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1343" data-height="742" data-id="529d96b3-8168-4418-871e-1542c3c3a8fb" data-collection="contentId-787513446" data-file-name="image-20250507-041945.png" data-file-size="79987" data-file-mime-type="image/png" data-alt="image-20250507-041945.png" data-renderer-start-pos="3513" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-5" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250507-041945.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png"><img decoding="async" class="alignnone size-full wp-image-29984 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" alt="Confirm Undercharge Release" width="1080" height="596" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w" data-lazy-sizes="(max-width: 1343px) 100vw, 1343px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" data-ll-status="loaded" sizes="(max-width: 1343px) 100vw, 1343px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29984" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png" alt="Confirm Undercharge Release" width="1343" height="742" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release.png 1343w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-500x276.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-768x424.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-1024x566.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Undercharge-Release-600x331.png 600w" sizes="(max-width: 1343px) 100vw, 1343px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="5" data-renderer-start-pos="3521"><strong data-renderer-mark="true">5 </strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Charge-Overcurrent-Protection" data-renderer-start-pos="3527"><strong data-renderer-mark="true">Confirm Charge Overcurrent Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="3568">Apply a charging current ramp. The PCM must detect when the charging current exceeds the allowable limit and disconnect to prevent overheating or damage.</p>
<p><strong data-renderer-mark="true">Note:</strong> To calculate the overcurrent value (<strong data-renderer-mark="true">I&lt;sub&gt;end&lt;/sub&gt;</strong>), the following formulas are used:<br>
• <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">Iend = (2 × Capacity × 3600) / t - Istart</code><br>
• or <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">Iend = Istart + DI/sec × LS_Chan_Step_Time</code></p>
<p><strong data-renderer-mark="true">Capacity logging methods:</strong><br>
• Use <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">TestCounter</code><br>
• Or fetch the last (previous) step value from the channel</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4023" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-6">
<div class="cc-1idqb4z">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1419" data-height="704" data-id="4bc8265f-3d9a-4d5b-a699-7c7c94b9b062" data-collection="contentId-787513446" data-file-name="image-20250508-012916.png" data-file-size="77930" data-file-mime-type="image/png" data-alt="image-20250508-012916.png" data-renderer-start-pos="4024" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-6" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-012916.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png"><img decoding="async" class="alignnone size-full wp-image-29985 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" alt="Confirm Charge Overcurrent Protection" width="1080" height="535" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w" data-lazy-sizes="(max-width: 1419px) 100vw, 1419px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" data-ll-status="loaded" sizes="(max-width: 1419px) 100vw, 1419px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29985" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png" alt="Confirm Charge Overcurrent Protection" width="1419" height="704" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection.png 1419w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-500x248.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-768x381.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-1024x508.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Charge-Overcurrent-Protection-600x298.png 600w" sizes="(max-width: 1419px) 100vw, 1419px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-g3f5ts" data-width="228" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4026" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-7">
<div class="cc-1bjx3mm">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1474" data-height="549" data-id="3a8d6833-e86e-4a8d-bf5f-514e76f73d7f" data-collection="contentId-787513446" data-file-name="image-20250701-093031.png" data-file-size="32877" data-file-mime-type="image/png" data-alt="image-20250701-093031.png" data-renderer-start-pos="4027" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-7" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093031.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png"><img decoding="async" class="alignnone size-full wp-image-29986 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" alt="LS charge capacity" width="1080" height="402" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w" data-lazy-sizes="(max-width: 1327px) 100vw, 1327px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" data-ll-status="loaded" sizes="(max-width: 1327px) 100vw, 1327px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29986" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png" alt="LS charge capacity" width="1327" height="494" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity.png 1327w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-500x186.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-768x286.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-1024x381.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_charge_capacity-600x223.png 600w" sizes="(max-width: 1327px) 100vw, 1327px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4028">LS_charge_capacity</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-g3f5ts" data-width="228" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4049" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-8">
<div class="cc-1wspy2c">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1486" data-height="568" data-id="6e9c3d98-3cde-4de6-a9fd-3e77d06ad23f" data-collection="contentId-787513446" data-file-name="image-20250701-093121.png" data-file-size="32370" data-file-mime-type="image/png" data-alt="image-20250701-093121.png" data-renderer-start-pos="4050" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-8" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093121.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png"><img decoding="async" class="alignnone size-full wp-image-29987 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" alt="TC Charge Capacity" width="1080" height="412" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w" data-lazy-sizes="(max-width: 1337px) 100vw, 1337px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" data-ll-status="loaded" sizes="(max-width: 1337px) 100vw, 1337px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29987" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png" alt="TC Charge Capacity" width="1337" height="511" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity.png 1337w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-1024x391.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_Charge_Capacity-600x229.png 600w" sizes="(max-width: 1337px) 100vw, 1337px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4051">TC_Charge_Capacity</div>
</div>
</td>
</tr>
<tr>
<th colspan="1" rowspan="1" data-colwidth="57">
<p id="6" data-renderer-start-pos="4076"><strong data-renderer-mark="true">6</strong></p>
</th>
<td colspan="1" rowspan="1" data-colwidth="121">
<p id="Confirm-Discharge-Overcurrent-Protection" data-renderer-start-pos="4081"><strong data-renderer-mark="true">Confirm Discharge Overcurrent Protection</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="327">
<p data-renderer-start-pos="4125">Test the PCM’s response to an excessive discharge current. The PCM should cut off the output once the discharge current exceeds the safety threshold.</p>
<p data-renderer-start-pos="4276"><strong data-renderer-mark="true">Note:</strong> Same formula applies as in Step 5:</p>
<ul class="ak-ul" data-indent-level="1">
<li>
<p data-renderer-start-pos="4320">Iend = -(2 × Capacity × 3600) / t + Istart</p>
</li>
<li>
<p data-renderer-start-pos="4366">Iend = Istart + DI/sec * LS_Chan_Step_Time</p>
</li>
</ul>
<p data-renderer-start-pos="4412"><strong data-renderer-mark="true">Capacity logging methods:</strong><br>
• Use <code class="_ca0qyh40 _u5f3m5ip _n3tdyh40 _19bvm5ip _2rko1sit _11c81u0j _1reo1wug _18m91wug _1dqoglyw _1e0c1nu9 _bfhktkvp _16d9qvcn _syaz1fxt _vwz41kw7 _1i4q1hna _o5721jtm" data-renderer-mark="true">TestCounter</code><br>
• Or fetch the final step value from the channel</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="225">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4512" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-9">
<div class="cc-14m9y23">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1367" data-height="662" data-id="dc990b0a-4f4c-444f-a856-cc02ec66c3b9" data-collection="contentId-787513446" data-file-name="image-20250508-012947.png" data-file-size="78419" data-file-mime-type="image/png" data-alt="image-20250508-012947.png" data-renderer-start-pos="4513" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-9" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-012947.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png"><img decoding="async" class="alignnone size-full wp-image-29988 entered exited" alt="Confirm Discharge Overcurrent Protectio" width="300" height="145" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png 1367w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-500x242.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-768x372.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-1024x496.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-600x291.png 600w" data-lazy-sizes="(max-width: 1367px) 100vw, 1367px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201367%20662'%3E%3C/svg%3E"><noscript><img decoding="async" class="alignnone size-full wp-image-29988" src="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png" alt="Confirm Discharge Overcurrent Protectio" width="1367" height="662" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio.png 1367w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-500x242.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-768x372.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-1024x496.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Confirm-Discharge-Overcurrent-Protectio-600x291.png 600w" sizes="(max-width: 1367px) 100vw, 1367px"></noscript></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4515" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-10">
<div class="cc-eos0nu">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1483" data-height="562" data-id="6be6facc-8d29-4df9-bccf-0f68ea333dd5" data-collection="contentId-787513446" data-file-name="image-20250701-093322.png" data-file-size="33576" data-file-mime-type="image/png" data-alt="image-20250701-093322.png" data-renderer-start-pos="4516" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-10" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093322.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png"><img decoding="async" class="alignnone size-full wp-image-29989 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" alt="LS discharge capacity" width="1080" height="409" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w" data-lazy-sizes="(max-width: 1335px) 100vw, 1335px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" data-ll-status="loaded" sizes="(max-width: 1335px) 100vw, 1335px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29989" src="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png" alt="LS discharge capacity" width="1335" height="506" srcset="https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity-.png 1335w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--500x190.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--768x291.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--1024x388.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/LS_discharge_capacity--600x227.png 600w" sizes="(max-width: 1335px) 100vw, 1335px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4517">LS_discharge_capacity</div>
</div>
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-m62ddy" data-width="227" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4541" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-11">
<div class="cc-18eoaqp">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1460" data-height="559" data-id="acd0ecc4-984c-4b24-9527-2c6293ea7e94" data-collection="contentId-787513446" data-file-name="image-20250701-093244.png" data-file-size="32629" data-file-mime-type="image/png" data-alt="image-20250701-093244.png" data-renderer-start-pos="4542" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-11" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250701-093244.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper"><a href="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png"><img decoding="async" class="alignnone size-full wp-image-29990 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" alt="TC discharge capacity" width="1080" height="413" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w" data-lazy-sizes="(max-width: 1314px) 100vw, 1314px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" data-ll-status="loaded" sizes="(max-width: 1314px) 100vw, 1314px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w"><noscript><img decoding="async" class="alignnone size-full wp-image-29990" src="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png" alt="TC discharge capacity" width="1314" height="503" srcset="https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity.png 1314w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-500x191.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-768x294.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-1024x392.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-18x7.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/TC_discharge_capacity-600x230.png 600w" sizes="(max-width: 1314px) 100vw, 1314px"></noscript></a></div>
</div>
</div>
</div>
</div>
<div class="cc-1h83rgl" data-media-caption="true" data-testid="media-caption" data-renderer-start-pos="4543">TC_discharge_capacity</div>
</div>
<p data-renderer-start-pos="4569">
</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
```

```html
<div class="pm-table-container with-shadow-observer" data-layout="custom" data-testid="table-container">
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="0225a2d8-a282-4118-9a2c-ece9e421f6d4" data-table-width="760" data-vc="table-node-wrapper">
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4851"><strong data-renderer-mark="true">Interface of EOL dashboard</strong></p>
</td>
<td colspan="4" rowspan="1">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-1r5l2wt" data-width="489" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4881" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-12">
<div class="cc-1u7pmpi">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1723" data-height="898" data-id="a3583f8d-270f-427e-b4fd-17613f6469d5" data-collection="contentId-787513446" data-file-name="image-20250508-022307.png" data-file-size="166771" data-file-mime-type="image/png" data-alt="image-20250508-022307.png" data-renderer-start-pos="4882" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-12" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-022307.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper">
<img alt="" decoding="async" class="alignnone size-full wp-image-29978 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" width="1080" height="563" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w" data-lazy-sizes="(max-width: 1723px) 100vw, 1723px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" data-ll-status="loaded" sizes="(max-width: 1723px) 100vw, 1723px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w"><noscript><img alt="" decoding="async" class="alignnone size-full wp-image-29978" src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" width="1723" height="898" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w" sizes="(max-width: 1723px) 100vw, 1723px"></noscript>
</div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4890"><strong data-renderer-mark="true">EOL Test Report</strong></p>
</td>
<td colspan="4" rowspan="1">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-yckpic" data-width="590" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4909" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-13">
<div class="cc-odp283">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1323" data-height="752" data-id="ddc3fdbc-5e97-49d5-bb15-30c5adb2cba5" data-collection="contentId-787513446" data-file-name="image-20250523-045759.png" data-file-size="138281" data-file-mime-type="image/png" data-alt="image-20250523-045759.png" data-renderer-start-pos="4910" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-13" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250523-045759.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper">
<img alt="" decoding="async" class="alignnone size-full wp-image-29979 entered exited" width="264" height="150" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png 1323w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-500x284.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-768x437.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-1024x582.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-600x341.png 600w" data-lazy-sizes="(max-width: 1323px) 100vw, 1323px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201323%20752'%3E%3C/svg%3E"><noscript><img alt="" decoding="async" class="alignnone size-full wp-image-29979" src="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png" width="1323" height="752" srcset="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png 1323w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-500x284.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-768x437.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-1024x582.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-600x341.png 600w" sizes="(max-width: 1323px) 100vw, 1323px"></noscript>
</div>
</div>
</div>
</div>
</div>
</div>
<p data-renderer-start-pos="4912">
</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4918"><strong data-renderer-mark="true">Test Summary Details</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4942">Test</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4950">Criteria</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4962">Measured Value</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4980">Result</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4992">1</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4997"><strong data-renderer-mark="true">Overcharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5019">In Range [4.1, 4.4] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5044">4.007742A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5057">❌ Failed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5071">2</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5076"><strong data-renderer-mark="true">Overcharge Voltage release</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5106">In Range [3.5, 4] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5129">3.6116747 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5144">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5158">3</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5163"><strong data-renderer-mark="true">Undercharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5186">In Range [2.8, 3,2] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5211">2.992585 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5225">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5239">4</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5244"><strong data-renderer-mark="true">Undercharge Voltage Release</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5275">In Range [3.35, 3.8] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5301">3.406495 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5315">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5329">5</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5334"><strong data-renderer-mark="true">Charge Overcurrent</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5356">In Range [0.8, 1.26] A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5382">1.257388 A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5396">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5410">6</p>
</td>
<td colspan="1" rowspan="1">
<p id="Discharge-Overcurrent" data-renderer-start-pos="5415"><strong data-renderer-mark="true"> Discharge Overcurrent </strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5442">In Range [-1.2,- 0.8] A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5469">-1.191427</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5483">✅ Passed</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
<div class="pm-table-sticky-scrollbar-container-view-page" data-vc="table-sticky-scrollbar-container">
<div></div>
</div>
<div class="pm-table-sticky-scrollbar-sentinel-bottom" data-testid="sticky-scrollbar-sentinel-bottom"></div>
</div>
```

```html
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="0225a2d8-a282-4118-9a2c-ece9e421f6d4" data-table-width="760" data-vc="table-node-wrapper">
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4851"><strong data-renderer-mark="true">Interface of EOL dashboard</strong></p>
</td>
<td colspan="4" rowspan="1">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-1r5l2wt" data-width="489" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4881" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-12">
<div class="cc-1u7pmpi">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1723" data-height="898" data-id="a3583f8d-270f-427e-b4fd-17613f6469d5" data-collection="contentId-787513446" data-file-name="image-20250508-022307.png" data-file-size="166771" data-file-mime-type="image/png" data-alt="image-20250508-022307.png" data-renderer-start-pos="4882" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-12" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250508-022307.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper">
<img alt="" decoding="async" class="alignnone size-full wp-image-29978 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" width="1080" height="563" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w" data-lazy-sizes="(max-width: 1723px) 100vw, 1723px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" data-ll-status="loaded" sizes="(max-width: 1723px) 100vw, 1723px" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w"><noscript><img alt="" decoding="async" class="alignnone size-full wp-image-29978" src="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png" width="1723" height="898" srcset="https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard.png 1723w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-500x261.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-768x400.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1024x534.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-1536x801.png 1536w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-18x9.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/Interface-of-EOL-dashboard-600x313.png 600w" sizes="(max-width: 1723px) 100vw, 1723px"></noscript>
</div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4890"><strong data-renderer-mark="true">EOL Test Report</strong></p>
</td>
<td colspan="4" rowspan="1">
<div class="rich-media-item mediaSingleView-content-wrap image-center cc-yckpic" data-width="590" data-width-type="pixel" data-node-type="mediaSingle" data-vc="media-single" data-renderer-start-pos="4909" data-media-vc-wrapper="true" data-ssr-placeholder="Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-13">
<div class="cc-odp283">
<div class=" cc-1t7vnwi" contenteditable="false" data-media-badges="true" data-testid="media-badges"></div>
<div data-type="file" data-node-type="media" data-width="1323" data-height="752" data-id="ddc3fdbc-5e97-49d5-bb15-30c5adb2cba5" data-collection="contentId-787513446" data-file-name="image-20250523-045759.png" data-file-size="138281" data-file-mime-type="image/png" data-alt="image-20250523-045759.png" data-renderer-start-pos="4910" data-ssr-placeholder="nouWf:Eb7Gh:EfLS5:4y5Pz:qz-Pe:F4Zdx-13" data-context-id="787513446">
<div id="newFileExperienceWrapper" class="_2rko1l7b _vchhusvi _kqswh2mm _ect41gqc _p12f1osq _c71l1osq _1bsb1qmm _4t3ine4n _1hlm1l1w _1rquusvi _eg5410xm _mts3kb7n _1ntskb7n _80omtlke new-file-experience-wrapper" data-testid="media-card-view" data-media-vc-wrapper="true">
<div class="_1reo15vq _18m915vq _2rko1sit _1e0c1txw _kqswh2mm _p12f1osq _1bsb1osq _4t3i1osq _c71l1osq media-file-card-view" data-testid="media-file-card-view" data-test-status="complete" data-test-source="remote" data-test-media-name="image-20250523-045759.png" data-test-progress="1">
<div class="_kqswstnw _1bsb1osq _4t3i1osq _1e0c1txw _2lx21bp4 _1bah1h6o _4cvr1h6o" data-testid="ImageRendererWrapper">
<img alt="" decoding="async" class="alignnone size-full wp-image-29979 entered exited" width="264" height="150" data-lazy-srcset="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png 1323w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-500x284.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-768x437.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-1024x582.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-600x341.png 600w" data-lazy-sizes="(max-width: 1323px) 100vw, 1323px" data-lazy-src="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201323%20752'%3E%3C/svg%3E"><noscript><img alt="" decoding="async" class="alignnone size-full wp-image-29979" src="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png" width="1323" height="752" srcset="https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin.png 1323w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-500x284.png 500w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-768x437.png 768w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-1024x582.png 1024w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-18x10.png 18w, https://www.arbin.com/wp-content/uploads/2025/07/EOL-Test-Report-arbin-600x341.png 600w" sizes="(max-width: 1323px) 100vw, 1323px"></noscript>
</div>
</div>
</div>
</div>
</div>
</div>
<p data-renderer-start-pos="4912">
</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4918"><strong data-renderer-mark="true">Test Summary Details</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4942">Test</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4950">Criteria</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4962">Measured Value</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4980">Result</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4992">1</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="4997"><strong data-renderer-mark="true">Overcharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5019">In Range [4.1, 4.4] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5044">4.007742A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5057">❌ Failed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5071">2</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5076"><strong data-renderer-mark="true">Overcharge Voltage release</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5106">In Range [3.5, 4] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5129">3.6116747 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5144">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5158">3</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5163"><strong data-renderer-mark="true">Undercharge Voltage</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5186">In Range [2.8, 3,2] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5211">2.992585 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5225">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5239">4</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5244"><strong data-renderer-mark="true">Undercharge Voltage Release</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5275">In Range [3.35, 3.8] V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5301">3.406495 V</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5315">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5329">5</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5334"><strong data-renderer-mark="true">Charge Overcurrent</strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5356">In Range [0.8, 1.26] A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5382">1.257388 A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5396">✅ Passed</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5410">6</p>
</td>
<td colspan="1" rowspan="1">
<p id="Discharge-Overcurrent" data-renderer-start-pos="5415"><strong data-renderer-mark="true"> Discharge Overcurrent </strong></p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5442">In Range [-1.2,- 0.8] A</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5469">-1.191427</p>
</td>
<td colspan="1" rowspan="1">
<p data-renderer-start-pos="5483">✅ Passed</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right"></div>
</div>
```

```html
<div class="pm-table-sticky-scrollbar-container-view-page" data-vc="table-sticky-scrollbar-container">
<div></div>
</div>
```

```html
<div class="pm-table-sticky-scrollbar-sentinel-bottom" data-testid="sticky-scrollbar-sentinel-bottom"></div>
```
