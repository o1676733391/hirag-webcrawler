# Source

- URL: https://www.arbin.com/innovation/arbin-dcim-feature.html

# Content

#  Arbin DCIM Feature

The Arbin DCIM feature is a state-of-the-art technology to measure battery impedance via a DC method. This is a practical substitute of ACIM measurement method to get EIS plot while also providing additional benefits.
Table of Contents

##  Background
There are two methods to analyze a battery's impedance among a frequency range, AC method and DC method.
The AC method, also known as ACIM, applies a set of AC signals with different frequencies to the battery, meanwhile samples both AC current and voltage on the battery. Then the impedance can be derived from voltage/current amplitude and their phase shift at different frequencies.
The DC method, namely DCIM, applies a DC current to the battery, meanwhile sample the current and voltage on the battery. Then the impedance can be derived from fitting value to the battery's equivalent circuit.
##  Impedence Methods in Graphs
![ARBIN-Impedence Methods in Graphs](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Impedence-Methods-in-Graphs.png)
##  Arbin's DCIM Feature Benefits
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
Arbin provides a built-in universal DCIM feature utilizing DC method allowing the user to measure battery's impedance easily.
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
Arbin's DCIM feature focuses on mid-range frequency, does not require additional AC equipment and takes less than 1s test time without disturbing regular battery test.
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
On the contrary, the traditional AC method focuses on a wider frequency range but requires additional AC equipment and a much longer measurement time.
Below is the comparison of AC method and DC method for Battery Impedance measurement:
AC Method
Arbin DC Method
Testing Time
0.5min~1h
<1s
Hardware Requirement
Additional AC source and measurement Equipment required
Built-in Arbin Channel, no additional hardware needed.
Applied Signal to Batter
Sinusoidal current/Voltage wave at different frequency
Constant DC current
Disturb Battery Test
Disturb regular battery test
Does not distrub regular battery test
Frequency Range
1mHz~1MHz
1Hz~1kHz
##  ACIM vs DCIM
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
The DCIM method can generate similar EIS(nyquist) plot compared to the one from traditional ACIM method as seen in Diagram 6, with corresponding fitting model parameters shown in Table 1. Thus, it can be a practical substitute for the traditional ACIM method.
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
The test used to create the plot points outlined in the graph and table below was performed on a 18650 cell at .05 C source current.
[ ](https://www.arbin.com/innovation/arbin-dcim-feature.html)
In the Graph: The black curve is the measured EIS(Nyquist) plot via ACIM method The blue curve is the fitted EIS curve based on measured ACIM method data and battery equivalent circuit. The yellow curve is the fitted EIS curve based on measured DC method data and battery equivalent circuit.
![ARBIN-ACIM vs DCIM](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-ACIM-vs-DCIM.png)
R0
R1
C1
R2
C2
DCIM Fitting
0.02795
0.0091541
4.20221
0.006298
0.24452
ACIM Fitting
0.02741
0.00943
3.1126
0.00677
0.1135
Table 1: Derived parameters using a 18650 cell
##  How to run DCIM on MITS 11
1. Create new Test Plan, choose schedule "[Built-in] DCIM"
![ARBIN-Create new Test Plan](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Create-new-Test-Plan.png)
2. Start the test plan, wait until it finished
![ARBIN-Start the test plan, wait until it finished](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Start-the-test-plan-wait-until-it-finished.png)
3. Go to test summary page of that test plan, press advanced, then press DCIM mode to the result when run DCIM calculation with the default parameters
![ARBIN-Go to test summary page of that test plan](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Go-to-test-summary-page-of-that-test-plan.png)
4. Update the parameters in Initial Guess sections and press calculate to manually calculate the DCIM

## Table-like Div HTML (Original)

```html
<div class="fl-col fl-node-6hjv1tue5oxa fl-col-bg-color specifications-table" data-node="6hjv1tue5oxa">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-o7xn5zkt38e2 responsive" data-node="o7xn5zkt38e2">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<div class="Frame1321315669" style="width: 900px; height: auto; box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.05); border-radius: 24px; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
  <div class="Frame1321315804" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border-top-left-radius: 12px; border: 1px #EAECF0 solid"></div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">AC Method</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">Arbin DC Method</div>
    </div>
  </div>
  <div class="Frame1321315797" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">Testing Time</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.5min~1h</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">&lt;1s</div>
    </div>
  </div>
  <div class="Frame1321315802" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">Hardware Requirement</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Additional AC source and measurement Equipment required</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Built-in Arbin Channel, no additional hardware needed.</div>
    </div>
  </div>
  <div class="Frame1321315805" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">Applied Signal to Batter</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Sinusoidal current/Voltage wave at different frequency</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Constant DC current</div>
    </div>
  </div>
  <div class="Frame1321315806" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">Disturb Battery Test</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Disturb regular battery test</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">Does not distrub regular battery test</div>
    </div>
  </div>
  <div class="Frame1321315803" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border-top-left-radius: 12px; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">Frequency Range</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">1mHz~1MHz</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">1Hz~1kHz</div>
    </div>
  </div>
</div>
</div>
	</div>
</div>
</div>
</div>
```

```html
<div class="fl-col fl-node-bqt3yrfdwl79 fl-col-bg-color specifications-table" data-node="bqt3yrfdwl79">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-d9zn76a2cowx responsive" data-node="d9zn76a2cowx">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<div class="Frame1321315669" style="width: 900px; height: 144px; box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.05); border-radius: 24px; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
  <div class="Frame1321315804" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border-top-left-radius: 12px; border: 1px #EAECF0 solid"></div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">R0</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">R1</div>
    </div>
    <div class="Frame1321315641" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">C1</div>
    </div>
    <div class="Frame1321315642" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">R2</div>
    </div>
    <div class="Frame1321315643" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 20px; font-family: Inter; font-weight: 600; line-height: 26px; word-wrap: break-word">C2</div>
    </div>
  </div>
  <div class="Frame1321315797" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">DCIM Fitting</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.02795</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.0091541</div>
    </div>
    <div class="Frame1321315641" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">4.20221</div>
    </div>
    <div class="Frame1321315642" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.006298</div>
    </div>
    <div class="Frame1321315643" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.24452</div>
    </div>
  </div>
  <div class="Frame1321315803" style="align-self: stretch; justify-content: flex-start; align-items: flex-start; display: inline-flex">
    <div class="Frame5" style="width: 200px; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border-top-left-radius: 12px; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 600; line-height: 23.40px; word-wrap: break-word">ACIM Fitting</div>
    </div>
    <div class="Frame1321315639" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.02741</div>
    </div>
    <div class="Frame1321315641" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.00943</div>
    </div>
    <div class="Frame1321315642" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">3.1126</div>
    </div>
    <div class="Frame1321315643" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.00677</div>
    </div>
    <div class="Frame1321315640" style="flex: 1 1 0; align-self: stretch; padding-left: 24px; padding-right: 24px; padding-top: 12px; padding-bottom: 12px; background: white; border: 1px #EAECF0 solid; flex-direction: column; justify-content: flex-start; align-items: flex-start; display: inline-flex">
      <div class="Label" style="align-self: stretch; color: #18214D; font-size: 18px; font-family: Inter; font-weight: 400; line-height: 23.40px; word-wrap: break-word">0.1135</div>
    </div>
  </div>
</div>
</div>
	</div>
</div>
</div>
</div>
```
