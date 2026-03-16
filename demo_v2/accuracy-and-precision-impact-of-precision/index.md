# Source

- URL: https://www.arbin.com/accuracy-and-precision-impact-of-precision.html

# Content

#  Accuracy and Precision: Impact of Precision
January 22, 2026
We previously examined the impact of measurement accuracy in an earlier article. In this article, we shift our focus to the influence of a battery tester’s **precision** on battery research.
In many research applications, parameters such as **dV/dt** and **dQ/dV** are widely used. The reliability of these measurements depends heavily on the precision of the battery tester, as small fluctuations or noise in voltage or current can significantly distort their interpretation.
The value of derivative capacity curve:
![the value of derivative capacity curve](https://www.arbin.com/wp-content/uploads/2026/01/the-value-of-derivative-capacity-curve.png)
Because dQ/dt = I, we can write:
![the value of derivative capacity curve 2](https://www.arbin.com/wp-content/uploads/2026/01/the-value-of-derivative-capacity-curve-2.png)
dV/dt can be re-written in details as follows:
![the value of derivative capacity curve 3](https://www.arbin.com/wp-content/uploads/2026/01/the-value-of-derivative-capacity-curve-3.png)
  * **dV/dt analysis**

We can see that in a very short time, even if we assume that the battery voltage is constant in reality, let say V0, the noise can cause a fake ΔV (ΔV = Vi+1 – Vi), resulting a false peak in dV/dt. To be more precise, if we take dt as 1ms, and Voltage is constant during that 1ms, dV/dt =0.
If we take the precision as 0.01% FSR, let’s take the FSR as 10V (From -5V to 5V). Then the absolute value of voltage precision is: 10 * 0.01% = 0.001 V or 1 mV.
We examine the worst case where V i+1 = V0 + 1 mV, Vi = V0 – 1 mV.
Then ΔV = Vi+1 – Vi = (V0 + 1mV) – (V0 – 1 mV) = 2 mV
dV/dt = 1mV/2ms = 0.5 V/s.
The real Voltage is 0 as assumption above, the value of dV/dt should be 0. However, we can see that due to precision limitation, the value of dV/dt measured become 0.5V/s, which is a huge difference.
In reality, the worst case may hardly happen, however, the example above shows us how substantially the precision limitation can cause to the result of dV/dt.
It’s worth highlighting that even with some inaccuracy, if the precision is perfect, the measurement of ΔV is still perfect, because value of both Vi+1 and Vi are shifted equally.
  * **dQ/dV analysis:**

Because:
![dq dv analysis](https://www.arbin.com/wp-content/uploads/2026/01/dq-dv-analysis.png)
We can assume that the accuracy and precision of time measurement is very high and ignore it.
In a very short time, the error of current measurement can be ignored also, therefore the accuracy analysis of dQ/dV and dV/dt are narrowed down to dV/dt accuracy analysis.
Similar to the analysis above, take the example in which dV change in a very short time of 5ms. Let’s say dV= 0.08mV.
In this case dV/dt = 0.08mV/5ms=0.016V/s
With the precision of 1 mV, the dV can easily be distorted from 0.08mV to be 0, causing dV/dt to be 0, and the infinite high in dQ/dV
### Case Study: How Voltage Precision Affects dV/dt and dQ/dV Calculation in Battery Analyzers
When analyzing dQ/dV, the system must calculate:
![analyzing dq dv 2](https://www.arbin.com/wp-content/uploads/2026/01/analyzing-dq-dv-2.png)
However, if ΔV is extremely small (tens of µV), measurement noise becomes larger than the real signal. This causes:
  * dV/dt to collapse to zero
  * dQ/dV to spike to extremely large values
  * unusable dQ/dV curves

To avoid this, **most battery analyzers (including Arbin)** do **not** compute dV/dt every few milliseconds.  
Instead, they **wait until the voltage change (ΔV) is larger than a threshold** , typically:
![analyzing dq dv 3](https://www.arbin.com/wp-content/uploads/2026/01/analyzing-dq-dv-3.png)
Then they compute one stable dV/dt.
### Case Study
Examine a case where after 5ms, the voltage change is ΔV = 0.08 mV (80 µV). Assume that in small time interval, the voltage increase linearly. We calculate the smallest time interval for ΔV to get 10 times of the voltage precision for each type of battery tester.
**Products** |  Voltage precision |  **10 times of voltage precision** |  **Min time interval**  
---|---|---|---  
Certain Brand X |  ±4 mV |  ±40 mV |  2500ms  
Voltage precision – LBT5V |  ±1 mV |  ±10 mV |  625ms  
Voltage precision – Arbin HPS |  ±120 µV |  ±1200 µV = 1.2 ms |  75ms  
We can see that for a 5V battery tester with precision of +/- 0.04% FSR (4mV), the minimum time interval to calculate dV/dt is 2.5 seconds, which is substantially higher than Arbin HPS (75ms)
**Reference**
Arbin Instruments. (2021). _Battery test system accuracy and calibration white paper._ College Station, TX: Arbin Instruments.
Arbin Instruments. (2023). _LBT Series product manual (Rev. 2.3)._ College Station, TX: Arbin Instruments.
ASTM International. (2020). _ASTM E177-20: Standard practice for use of the terms precision and bias in ASTM test methods._ West Conshohocken, PA: ASTM International. [Standard Practice for Use of the Terms Precision and Bias in ASTM Test Methods](https://doi.org/10.1520/E0177-20)
IEC. (2018). _IEC 62660-1:2018 – Secondary lithium-ion cells for the propulsion of electric road vehicles – Part 1: Performance testing._ Geneva, Switzerland: International Electrotechnical Commission.
Newman, J., & Thomas-Alyea, K. E. (2004). _Electrochemical systems_ (3rd ed.). Hoboken, NJ: Wiley-Interscience.
Posted in [Application Notes](https://www.arbin.com/category/application-notes)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Arbin Instruments at The Battery Show Asia 2026](https://www.arbin.com/arbin-instruments-at-the-battery-show-asia-2026.html)
[How to plot Potential vs Current Graph by Arbin Data Watcher →](https://www.arbin.com/how-to-plot-potential-vs-current-graph-by-arbin-data-watcher.html)

## Table-like Div HTML (Original)

```html
<div class="pm-table-container with-shadow-observer" data-layout="custom" data-testid="table-container">
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="d8903e23-c29d-40dc-94b0-e2e9c2ce90a5" data-table-width="760" data-vc="table-node-wrapper">
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3248" data-local-id="d7e805f9-baa1-4dea-b3d2-60763a42113e"><strong data-renderer-mark="true">Products</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3260" data-local-id="87cff9a7-c88e-4f64-b8cf-e660087d71b1">Voltage precision</p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3281" data-local-id="ffb5cf18-bf02-4f22-8fc2-50ac3def0833"><strong data-renderer-mark="true">10 times of voltage precision</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3314" data-local-id="907acbe2-f395-4498-a83d-6f951ca3062c"><strong data-renderer-mark="true">Min time interval</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3337" data-local-id="3611b432-a11f-4fb6-bd08-3da277f2394c">Certain Brand X</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3356" data-local-id="0e850ab3-ba17-401b-9b4a-48c7ad5b2af5">±4 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3365" data-local-id="3eff074a-f1df-4911-b484-3ea62651caa4">±40 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3375" data-local-id="6dd2e532-d74a-427a-829c-f887ae06c873">2500ms</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3387" data-local-id="06022dba-6d34-40a4-b6c8-ddfd1eb64ef3">Voltage precision – <span data-highlighted="true" data-vc="highlighted-text"><span class="_kqswh2mm"><span class="_5pioz8co _189e1dm9 _1il9buyh _19lc184f _d0altlke" data-testid="definition-highlighter">LBT5V</span></span></span></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3416" data-local-id="6c2dc3f0-ed66-42dc-aaeb-02cf4fae7f19">±1 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3425" data-local-id="9f449097-8949-415a-8597-05184327f4a9">±10 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3435" data-local-id="ff402599-555f-45b0-8200-8a50848f0d76">625ms</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3446" data-local-id="48285951-f739-428f-ad83-a42f7753f028">Voltage precision – Arbin <span data-highlighted="true" data-vc="highlighted-text"><span class="_kqswh2mm"><span class="_5pioz8co _189e1dm9 _1il9buyh _19lc184f _d0altlke" data-testid="definition-highlighter">HPS</span></span></span></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3479" data-local-id="24ecc001-4fc5-4f28-b033-3749bd4f5fa0">±120 µV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3490" data-local-id="f00fc77b-71be-49d1-9bc8-b5d30f054bb4">±1200 µV = 1.2 ms</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3511" data-local-id="8064e22f-05b7-4129-bff0-1ab95c70e23a">75ms</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right">
<span style="font-size: 16px;">We can see that for a 5V battery tester with precision of +/- 0.04% </span><span style="font-size: 16px;" data-highlighted="true" data-vc="highlighted-text">FSR</span><span style="font-size: 16px;"> (4mV), the minimum time interval to calculate dV/dt is 2.5 seconds, which is substantially higher than Arbin </span><span style="font-size: 16px;" data-highlighted="true" data-vc="highlighted-text">HPS</span><span style="font-size: 16px;"> (75ms)</span>
</div>
<div></div>
</div>
</div>
```

```html
<div class="pm-table-wrapper" data-number-column="false" data-layout="center" data-autosize="false" data-table-local-id="d8903e23-c29d-40dc-94b0-e2e9c2ce90a5" data-table-width="760" data-vc="table-node-wrapper">
<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="center">
<colgroup>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3248" data-local-id="d7e805f9-baa1-4dea-b3d2-60763a42113e"><strong data-renderer-mark="true">Products</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3260" data-local-id="87cff9a7-c88e-4f64-b8cf-e660087d71b1">Voltage precision</p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3281" data-local-id="ffb5cf18-bf02-4f22-8fc2-50ac3def0833"><strong data-renderer-mark="true">10 times of voltage precision</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
<th class="ak-renderer-tableHeader-sortable-column__wrapper" colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#f0f1f2" aria-sort="none">
<div class="ak-renderer-tableHeader-sortable-column">
<p data-renderer-start-pos="3314" data-local-id="907acbe2-f395-4498-a83d-6f951ca3062c"><strong data-renderer-mark="true">Min time interval</strong></p>
<figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
<div role="presentation">
<div class="ak-renderer-tableHeader-sorting-icon css-1f6xth7" tabindex="0" role="button" aria-label="No sort applied to the column" aria-disabled="false" aria-hidden="false">
<div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive css-1asrlx7"></div>
</div>
</div>
</figure>
</div>
</th>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3337" data-local-id="3611b432-a11f-4fb6-bd08-3da277f2394c">Certain Brand X</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3356" data-local-id="0e850ab3-ba17-401b-9b4a-48c7ad5b2af5">±4 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3365" data-local-id="3eff074a-f1df-4911-b484-3ea62651caa4">±40 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3375" data-local-id="6dd2e532-d74a-427a-829c-f887ae06c873">2500ms</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3387" data-local-id="06022dba-6d34-40a4-b6c8-ddfd1eb64ef3">Voltage precision – <span data-highlighted="true" data-vc="highlighted-text"><span class="_kqswh2mm"><span class="_5pioz8co _189e1dm9 _1il9buyh _19lc184f _d0altlke" data-testid="definition-highlighter">LBT5V</span></span></span></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3416" data-local-id="6c2dc3f0-ed66-42dc-aaeb-02cf4fae7f19">±1 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3425" data-local-id="9f449097-8949-415a-8597-05184327f4a9">±10 mV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3435" data-local-id="ff402599-555f-45b0-8200-8a50848f0d76">625ms</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="166" data-cell-background="#ffffff">
<p data-renderer-start-pos="3446" data-local-id="48285951-f739-428f-ad83-a42f7753f028">Voltage precision – Arbin <span data-highlighted="true" data-vc="highlighted-text"><span class="_kqswh2mm"><span class="_5pioz8co _189e1dm9 _1il9buyh _19lc184f _d0altlke" data-testid="definition-highlighter">HPS</span></span></span></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="186" data-cell-background="#ffffff">
<p data-renderer-start-pos="3479" data-local-id="24ecc001-4fc5-4f28-b033-3749bd4f5fa0">±120 µV</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="266" data-cell-background="#ffffff">
<p data-renderer-start-pos="3490" data-local-id="f00fc77b-71be-49d1-9bc8-b5d30f054bb4">±1200 µV = 1.2 ms</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="140" data-cell-background="#ffffff">
<p data-renderer-start-pos="3511" data-local-id="8064e22f-05b7-4129-bff0-1ab95c70e23a">75ms</p>
</td>
</tr>
</tbody>
</table>
<div class="sentinel-right">
<span style="font-size: 16px;">We can see that for a 5V battery tester with precision of +/- 0.04% </span><span style="font-size: 16px;" data-highlighted="true" data-vc="highlighted-text">FSR</span><span style="font-size: 16px;"> (4mV), the minimum time interval to calculate dV/dt is 2.5 seconds, which is substantially higher than Arbin </span><span style="font-size: 16px;" data-highlighted="true" data-vc="highlighted-text">HPS</span><span style="font-size: 16px;"> (75ms)</span>
</div>
<div></div>
</div>
```
