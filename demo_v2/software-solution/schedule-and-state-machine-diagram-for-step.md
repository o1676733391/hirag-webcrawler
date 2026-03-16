# Source

- URL: https://www.arbin.com/software-solution/schedule-and-state-machine-diagram-for-step.html

# Content

#  Schedule and State Machine  
Diagram for Step
Customers have the flexibility to edit the Schedule to customize and execute the specific tests they need for their application. 
The Schedule is composed of individual units called steps, each representing a distinct phase or action within the overall testing process.
Each step operates based on the principles of a state machine, meaning it can transition from one state to another based on predefined conditions or triggers.
This state-driven approach ensures that each test can flow smoothly and logically from one phase to the next, while allowing for dynamic responses to changing conditions.
Table of Contents

##  What a schedule look like
Arbin utilizes a flexible Schedule system to control and organize the sequence of battery tests. Within this schedule, users have the ability to specify various control types, which determine the exact type of test to be conducted-whether it's charging, discharging, or cycling, among others.
Additionally, users can configure log conditions to define the specific parameters and intervals at which data is recorded, ensuring that only the most relevant data is logged for further analysis.
This system provides users with a customizable and precise framework to tailor their battery testing procedures to meet specific testing goals.
Video Player
<https://www.arbin.com/wp-content/uploads/2025/11/schedule-clip-v8.mp4>
![](https://www.arbin.com/wp-content/uploads/2025/07/Arbin-Test-Schedule-Video-bg.png)
00:00
00:00
02:19
[Use Up/Down Arrow keys to increase or decrease volume.](javascript:void\(0\);)
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-What-a-schedule-look-like.png)
##  Example of running a test:
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Example-of-running-a-test.png)
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Example-of-running-a-test-i2.png)
##  State Machine Diagram of Step
![ARBIN-State Machine Diagram of Step i1](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-State-Machine-Diagram-of-Step-i1.png)
State
Description
Action
In this state, the system will execute the step with corresponding control type. For example, output constant current with 2A. 
Log Limits
In this state, the system will check if the log limit has been reached. If it does, it will trigger the system to log the data. 
Step Limits
In this state, the system will check if the step limit has been reached. If it does, the system will go to the next state. Otherwise, stay in the current state. 
Transition
In this state, the system will transition from one step to another. 
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-State-Machine-Diagram-of-Step-i2.png)
There are 5 different scenarios:   
  

  1. Stay at the same step.
  2. Restart at the same step
  3. Go to the next step.
  4. Jump to another step.
  5. Finish the test.

  1. End Test
  2. Unsafe

![ARBIN-ACL-State Machine Diagram of Step i3](https://www.arbin.com/wp-content/uploads/v2/ss-schedule-diagram/ARBIN-ACL-State-Machine-Diagram-of-Step-i3.png)
##  Example Schedule:
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Example-Schedule-i1.png)
![ARBIN-ACL-Example Schedule i2](https://www.arbin.com/wp-content/uploads/v2/ss-schedule-diagram/ARBIN-ACL-Example-Schedule-i2.png)
#  Sub-Schedule (Subroutine) Feature
![Arbin Sub-Schedule \(Subroutine\) Feature](https://www.arbin.com/wp-content/uploads/2025/07/Arbin-Sub-Schedule-Subroutine-Feature.png)
##  Introduction to Sub-Schedule
Our current programming approach relies on traditional scheduling methods, but it lacks modularity and is difficult to maintain.
Now, we are introducing an innovative sub-Schedule method that significantly enhances modularity, improves maintainability, and strengthens information hiding.
With this cutting-edge approach, you'll enjoy a simpler, more efficient, and flexible development experience, making it easier to tackle complex projects!
We have integrated the concepts of encapsulation and reusability into our Schedule and Sub-Schedule methods, delivering a **powerful solution** that enhances efficiency and flexibility in your development process.
![ARBIN-ACL-Introduction Sub-Schedule i2](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-ACL-Introduction-Sub-Schedule-i2.png)
The left is main Schedule and the right are Sub-Schedules
##  Advantages
### Modular Testing Routines
With Sub-Schedule, you can create reusable testing routines that can be easily put into your main schedule, like in programming. This allows you to avoid redundancy and maintain cleaner, more organized schedules.
### Flexibility
Quickly adapt your testing protocols by modifying Sub-Schedules without the need to overhaul the entire main schedule. This flexibility is essential for R&D environments where testing parameters may frequently change.
### Streamline Test Design
Reuse commonly performed test sequences to create new battery test recipes faster and more efficiently, reducing the need for repetitive setup.​
### Enhanced Version Control
Maintain better organization and oversight of test variations by isolating and reusing critical components within tests, ensuring consistency across different test versions.​
### Simplified Workflow
Easily integrate previously validated test segments into new tests, enabling smoother test creation while maintaining the accuracy of complex battery testing protocols.​
### Simplified Managed Tests
Reuse commonly performed test sequences to create new battery test recipes faster and more efficiently, reducing the need for repetitive setup.​
### Reusability
Easily integrate previously validated test segments into new tests, enabling smoother test creation while maintaining the accuracy of complex battery testing protocols.​
### Adaptability
Reuse commonly performed test sequences to create new battery test recipes faster and more efficiently, reducing the need for repetitive setup.​
##  Feature & Spec
### Multiple Reference
Many schedules can reference to one or multiple sub-schedules and default global setting from running schedule and allow to overwrite in sub-schedules
### Maximum Subroutines
Support up to 500 steps including main schedule and sub schedule
### Shallow Copy
Sub-Schedule subsequence change will **NOT** reflect to previous reference, and must **FORCE** update
## Sub-Schedule Editor
![ARBIN-ACL-Sub-Schedule Editor v2](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-ACL-Sub-Schedule-Editor-v2.png)
We have a Sub Schedule folder in the Schedule Editor. The way to create a Sub Schedule is the same as creating a Schedule
## Implement Sub-Schedule
### Assignment
Here is how you assign sub schedule
![](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Managed-Sub-Schedule-Assignment.png)
### Monitor Test (Monitor & Control)
Channel View in the Monitor & Control window will also show whether the test is in a SubSchedule step.
![](https://www.arbin.com/images/v2/ss-advanced-control-language/ARBIN-ACL-Monitor-Test-Monitor-Control.png)
### Data Query
A new field in SQL will be added, "Sub_Step_ID" to the database Event_Table, Resume_Table, and other related database tables so that users may view the corresponding data when querying results.
![](https://www.arbin.com/images/v2/ss-advanced-control-language/ARBIN-ACL-Data-Query.png)
### Viewing Data
When exporting data to Excel or CSV file, a new column for SubSch Step has been added.
![](https://www.arbin.com/wp-content/uploads/2025/07/Arbin-Monitor-Test-Monitor-Control-Viewing-data.png)
##  List of control types
Control types
Parameter and Control Strategy
Example Data Plot
Rest
Control Value:   

  * None

  
Control Method:   

  * The battery will be in an open-circuit state, with the relay turned off. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i1.png)
Current
Control Value:   

  * The current value is measured in amperes (A). It can be a numerical value, where '1A' indicates 1 ampere of charging and '-1A' indicates 1 ampere of discharging. Additionally, the control value can be a variable or a formula. 

  
Control Method:   

  * The battery is connected in series with a constant current source, outputting/inputting a constant current, with the current value set by the control value. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i2.png)
Voltage
Control Value:   

  * The value of the voltage is measured in volt (V). It can be a numerical value, or it can be a variable or a formula. 

  
Control Method:   

  * The battery is connected in parallel with a constant voltage source, outputting/inputting a constant voltage, with the voltage value set by the control value. 
  * Some channel boards are equipped with hardware-based constant voltage sources, whereas others rely on software-based PID control to implement a digital constant voltage source. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i3.png)
C-Rate
Control Value:   

  * Charging or discharging at a current that will fully charge or discharge the battery in one hour. For example, for a battery with a capacity of 1000mAh, 0.03C means charging or discharging at a current of 0.03 * 1000mA = 30mA. 

  
Control Method:   

  * The battery is connected in series with a constant current source, outputting/inputting a constant current, with the current value set by the control value. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i4.png)
Power
Control Value:   

  * The power value is measured in walt (W). It can be a numerical value, or it can be a variable or a formula. 

  
Control Method:   

  * Input constant power to/from the load.

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i5.png)
Current Ramp
Control Value:   

  * Start(A): Initial value in ampere (A).
  * dI/sec: Rate of current change per second.

  
Control Method:   

  * Set the output/input current as a linear variable, achieving control through setting the initial value and rate of change. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i6.png)
Voltage Ramp
Control Value:   

  * Start(V): Initial value in voltage (V).
  * dV/sec: Rate of voltage change per second.

  
Control Method:   

  * Set the output/input voltage as a linear variable, achieving control through setting the initial value and rate of change. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i7.png)
Current Staircase
Control Value:   

  * Start(A): Initial value in ampere (A).
  * dI/stair: Rate of current change per stair.
  * Stair Time: Duration of the step, in seconds.

  
Control Method:   

  * Set the output/input current step, achieving control through setting the initial value, step change, and step duration. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i8.png)
Voltage Staircase
Control Value:   

  * Start(A): Initial value in volt (V).
  * dV/stair: Rate of voltage change per stair.
  * Stair Time: Duration of the step, in seconds.

  
Control Method:   

  * Set the output/input voltage step, achieving control through setting the initial value, step change, and step duration. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i9.png)
Current Simulation
Control Value:   

  * Reference a current simulation file (.txt).
  * Options to repeat log points and whether each current value requires logging two points are available. 

  
Control Method:   

  * Through the simulation file, illustrate simulated output/input current values, which must include timestamps and control values. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i10.png)
Internal Resistance
Control Value:   

  * Amplitude: The amplitude of the pulse, in amperes (A).
  * ms: Pulse duration, in milliseconds (ms).
  * Offset: The offset of the pulse.

  
Control Method:   

  * Utilize positive and negative pulses output to the load and calculate the internal resistance by recording the voltage change values. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i11.png)
CCCV
Control Values:   

  * CC: Current value during the CC phase, in amperes (A).
  * CV: The voltage value during the CV phase, in volts (V).
  * IR: The internal resistance value, in ohms (Ω).
  * CC and CV can be numbers, variables, or formulas, while IR only supports numbers. 

  
Control Method:   

  * Utilize CCCV to charge/discharge the load. Before the load reaches the target voltage, charge/discharge at a fixed current using the CC control value. Once the load reaches the target voltage, charge/discharge at a fixed voltage using the CV control value. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i12.png)
Pause
Control value:   
There are 3 options available:   

  * Normal: Normal mode, pauses the test when it reaches this step 
  * ACIM: Alternating Current Impedance Mode
  * T_Chamber: Temperature Control Chamber Mode

  
Control method:   

  * Upon entering this pause step, you can either pause simply, measure alternating current impedance, or set up the temperature control chamber. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i13.png)
Set Variable
Control Values:   
Three control options:   

  * Reset: Reset the variable to 0.
  * Increment: Increase the variable value by 1.
  * Decrement: Decrease the variable value by 1.

  
Control Method:   

  * Provide users with the ability to operate on declared variables, including resetting, incrementing, and decrementing. Users can use these variables to set step limits or log limits, enhancing the flexibility of the schedule design. 

No output data, it's a control step for setting up variables in the schedule. 
Voltage CycleV
Control Values:   

  * IR: Internal resistance value, measured in Ohms.
  * Additionally, reference a pre-set cyclic voltage file.

  
Control Method:   

  * Conduct cyclic testing on voltage, allowing for the definition of start voltage and target voltage by the user. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i14.png)
Current CycleV
Control Values:   

  * Reference a pre-set cyclic current file.

  
Control Method:   

  * Conduct cyclic testing on current, allowing for the definition of starting current and target current by the user. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i15.png)
Power Simulation
Control Values:   

  * Reference a power simulation file (.txt).
  * Options include whether to log points repeatedly and whether each current value needs to log two points. 

  
Control Method:   

  * Through the simulation file, simulate the output/input of current, voltage, and power values, with the file containing timestamps and control values. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i16.png)
Load Simulation
Control Value:   

  * Referencing a load simulation file (.txt)
  * Options to repeat log points and whether each current value requires logging two points are available. 

  
Control Method:   

  * Through the simulation file, simulate output/input load values are described. The file must include timestamps and control values. 

![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i17.png)

## Table-like Div HTML (Original)

```html
<div class="fl-col fl-node-64frsjak8gnl fl-col-bg-color specification-table" data-node="64frsjak8gnl">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-trdk4wjpqya9" data-node="trdk4wjpqya9">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	  <style></style>

  <div class="frame-336110">
    <div class="frame-1321315669">
      <div class="frame-1321315802">
        <div class="frame-5">
          <div class="label">State</div>
        </div>
        <div class="frame-1321315639">
          <div class="label2">Description</div>
        </div>
      </div>
      <div class="frame-1321315797">
        <div class="frame-52">
          <div class="label3">Action</div>
        </div>
        <div class="frame-13213156392">
          <div class="label4">
            In this state, the system will execute the step with corresponding
            control type. For example, output constant current with 2A.
          </div>
        </div>
      </div>
      <div class="frame-1321315798">
        <div class="frame-52">
          <div class="label3">Log Limits</div>
        </div>
        <div class="frame-13213156392">
          <div class="label4">
            In this state, the system will check if the log limit has been
            reached. If it does, it will trigger the system to log the data.
          </div>
        </div>
      </div>
      <div class="frame-1321315801">
        <div class="frame-52">
          <div class="label3">Step Limits</div>
        </div>
        <div class="frame-13213156392">
          <div class="label4">
            In this state, the system will check if the step limit has been
            reached. If it does, the system will go to the next state. Otherwise,
            stay in the current state.
          </div>
        </div>
      </div>
      <div class="frame-1321315799">
        <div class="frame-53">
          <div class="label3">Transition</div>
        </div>
        <div class="frame-13213156393">
          <div class="label5">
            In this state, the system will transition from one step to another.
          </div>
          <img decoding="async" class="image-14004 entered lazyloaded" src="/wp-content/uploads/2024/09/ARBIN-State-Machine-Diagram-of-Step-i2.png" data-lazy-src="/wp-content/uploads/2024/09/ARBIN-State-Machine-Diagram-of-Step-i2.png" data-ll-status="loaded" width="810" height="238"><noscript><img decoding="async" class="image-14004" src="/wp-content/uploads/2024/09/ARBIN-State-Machine-Diagram-of-Step-i2.png"></noscript>
          <div class="label5">
            <span>
              <span class="label-5-span2">
                There are 5 different scenarios:
                <br>
                <br>
              </span>
              <ol class="label-5-span3">
                <li>Stay at the same step.</li>
                <li>Restart at the same step</li>
                <li>Go to the next step.</li>
                <li>Jump to another step.</li>
                <li>Finish the test.</li>
              </ol>
            </span>
          </div>
          <div class="frame-13213158022">
            <div class="label6">
              <span>
                <ol class="label-6-span2">
                  <li>End Test</li>
                  <li>Unsafe</li>
                </ol>
              </span>
            </div>
          </div>
        </div>
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
<div class="fl-col fl-node-cyhf4pe2kx3s fl-col-bg-color specification-table" data-node="cyhf4pe2kx3s">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-tv6nx5z19ecq" data-node="tv6nx5z19ecq">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>
<div class="frame-336110">
  <div class="frame-1321315669">
    <div class="frame-1321315802">
      <div class="frame-5">
        <div class="label">Control types</div>
      </div>
      <div class="frame-1321315640">
        <div class="label2">Parameter and Control Strategy</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Example Data Plot</div>
      </div>
    </div>
    <div class="frame-1321315797">
      <div class="frame-52">
        <div class="label3">Rest</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          <span>
            <span class="label-4-span">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span2">
              <li>None</li>
            </ul>
            <span class="label-4-span3">
               
              <br>
            </span>
            <span class="label-4-span4">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span5">
              <li>
                The battery will be in an open-circuit state, with the relay
                turned off.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-1321315640">
        <img decoding="async" class="image-14007 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i1.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i1.png" data-ll-status="loaded" width="449" height="244"><noscript><img decoding="async" class="image-14007" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i1.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315803">
      <div class="frame-52">
        <div class="label3">Current</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          <span>
            <span class="label-4-span6">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span7">
              <li>
                The current value is measured in amperes (A). It can be a
                numerical value, where '1A' indicates 1 ampere of
                charging and '-1A' indicates 1 ampere of discharging.
                Additionally, the control value can be a variable or a formula.
              </li>
            </ul>
            <span class="label-4-span8">
               
              <br>
            </span>
            <span class="label-4-span9">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span10">
              <li>
                The battery is connected in series with a constant current
                source, outputting/inputting a constant current, with the
                current value set by the control value.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i2.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i2.png" data-ll-status="loaded" width="449" height="244"><noscript><img decoding="async" class="image" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i2.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315804">
      <div class="frame-52">
        <div class="label3">Voltage</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          <span>
            <span class="label-4-span11">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span12">
              <li>
                The value of the voltage is measured in volt (V). It can be a
                numerical value, or it can be a variable or a formula.
              </li>
            </ul>
            <span class="label-4-span13">
              <br>
            </span>
            <span class="label-4-span14">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span15">
              <li>
                The battery is connected in parallel with a constant voltage
                source, outputting/inputting a constant voltage, with the
                voltage value set by the control value.
              </li>
              <li>
                Some channel boards are equipped with hardware-based constant
                voltage sources, whereas others rely on software-based PID
                control to implement a digital constant voltage source.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i3.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i3.png" data-ll-status="loaded" width="449" height="244"><noscript><img decoding="async" class="image" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i3.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315805">
      <div class="frame-52">
        <div class="label3">C-Rate</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span16">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span17">
              <li>
                Charging or discharging at a current that will fully charge or
                discharge the battery in one hour. For example, for a battery
                with a capacity of 1000mAh, 0.03C means charging or discharging
                at a current of 0.03 * 1000mA = 30mA.
              </li>
            </ul>
            <span class="label-4-span18">
              <br>
            </span>
            <span class="label-4-span19">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span20">
              <li>
                The battery is connected in series with a constant current
                source, outputting/inputting a constant current, with the
                current value set by the control value.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image2 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i4.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i4.png" data-ll-status="loaded" width="449" height="185"><noscript><img decoding="async" class="image2" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i4.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315806">
      <div class="frame-52">
        <div class="label3">Power</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span21">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span22">
              <li>
                The power value is measured in walt (W). It can be a numerical
                value, or it can be a variable or a formula.
              </li>
            </ul>
            <span class="label-4-span23">
              <br>
            </span>
            <span class="label-4-span24">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span25">
              <li>Input constant power to/from the load.</li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image2 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i5.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i5.png" data-ll-status="loaded" width="449" height="185"><noscript><img decoding="async" class="image2" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i5.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315807">
      <div class="frame-52">
        <div class="label3">Current Ramp</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span26">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span27">
              <li>Start(A): Initial value in ampere (A).</li>
              <li>dI/sec: Rate of current change per second.</li>
            </ul>
            <span class="label-4-span28">
              <br>
            </span>
            <span class="label-4-span29">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span30">
              <li>
                Set the output/input current as a linear variable, achieving
                control through setting the initial value and rate of change.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image3 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i6.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i6.png" data-ll-status="loaded" width="449" height="343"><noscript><img decoding="async" class="image3" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i6.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315808">
      <div class="frame-52">
        <div class="label3">Voltage Ramp</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span31">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span32">
              <li>Start(V): Initial value in voltage (V).</li>
              <li>dV/sec: Rate of voltage change per second.</li>
            </ul>
            <span class="label-4-span33">
              <br>
            </span>
            <span class="label-4-span34">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span35">
              <li>
                Set the output/input voltage as a linear variable, achieving
                control through setting the initial value and rate of change.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image4 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i7.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i7.png" data-ll-status="loaded" width="449" height="187"><noscript><img decoding="async" class="image4" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i7.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315809">
      <div class="frame-52">
        <div class="label3">Current Staircase</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span36">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span37">
              <li>Start(A): Initial value in ampere (A).</li>
              <li>dI/stair: Rate of current change per stair.</li>
              <li>Stair Time: Duration of the step, in seconds.</li>
            </ul>
            <span class="label-4-span38">
              <br>
            </span>
            <span class="label-4-span39">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span40">
              <li>
                Set the output/input current step, achieving control through
                setting the initial value, step change, and step duration.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image4 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i8.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i8.png" data-ll-status="loaded" width="449" height="187"><noscript><img decoding="async" class="image4" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i8.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315810">
      <div class="frame-52">
        <div class="label3">Voltage Staircase</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span41">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span42">
              <li>Start(A): Initial value in volt (V).</li>
              <li>dV/stair: Rate of voltage change per stair.</li>
              <li>Stair Time: Duration of the step, in seconds.</li>
            </ul>
            <span class="label-4-span43">
              <br>
            </span>
            <span class="label-4-span44">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span45">
              <li>
                Set the output/input voltage step, achieving control through
                setting the initial value, step change, and step duration.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image4 entered lazyloaded" src="https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i9.png" data-lazy-src="https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i9.png" data-ll-status="loaded" width="449" height="187"><noscript><img decoding="async" class="image4" src="https://www.arbin.com/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i9.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315811">
      <div class="frame-52">
        <div class="label5">Current Simulation</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span46">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span47">
              <li>Reference a current simulation file (.txt).</li>
              <li>
                Options to repeat log points and whether each current value
                requires logging two points are available.
              </li>
            </ul>
            <span class="label-4-span48">
              <br>
            </span>
            <span class="label-4-span49">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span50">
              <li>
                Through the simulation file, illustrate simulated output/input
                current values, which must include timestamps and control
                values.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image5 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i10.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i10.png" data-ll-status="loaded" width="449" height="226"><noscript><img decoding="async" class="image5" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i10.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315812">
      <div class="frame-52">
        <div class="label5">Internal Resistance</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span51">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span52">
              <li>Amplitude: The amplitude of the pulse, in amperes (A).</li>
              <li>ms: Pulse duration, in milliseconds (ms).</li>
              <li>Offset: The offset of the pulse.</li>
            </ul>
            <span class="label-4-span53">
              <br>
            </span>
            <span class="label-4-span54">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span55">
              <li>
                Utilize positive and negative pulses output to the load and
                calculate the internal resistance by recording the voltage
                change values.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image6 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i11.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i11.png" data-ll-status="loaded" width="449" height="200"><noscript><img decoding="async" class="image6" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i11.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315813">
      <div class="frame-52">
        <div class="label5">CCCV</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span56">
              Control Values:
              <br>
            </span>
            <ul class="label-4-span57">
              <li>CC: Current value during the CC phase, in amperes (A).</li>
              <li>CV: The voltage value during the CV phase, in volts (V).</li>
              <li>IR: The internal resistance value, in ohms (Ω).</li>
              <li>
                CC and CV can be numbers, variables, or formulas, while IR only
                supports numbers.
              </li>
            </ul>
            <span class="label-4-span58">
              <br>
            </span>
            <span class="label-4-span59">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span60">
              <li>
                Utilize CCCV to charge/discharge the load. Before the load
                reaches the target voltage, charge/discharge at a fixed current
                using the CC control value. Once the load reaches the target
                voltage, charge/discharge at a fixed voltage using the CV
                control value.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image6 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i12.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i12.png" data-ll-status="loaded" width="449" height="200"><noscript><img decoding="async" class="image6" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i12.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315814">
      <div class="frame-52">
        <div class="label3">Pause</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span61">
              Control value:
              <br>
            </span>
            <span class="label-4-span62">
              There are 3 options available:
              <br>
            </span>
            <ul class="label-4-span63">
              <li>
                Normal: Normal mode, pauses the test when it reaches this step
              </li>
              <li>ACIM: Alternating Current Impedance Mode</li>
              <li>T_Chamber: Temperature Control Chamber Mode</li>
            </ul>
            <span class="label-4-span64">
              <br>
            </span>
            <span class="label-4-span65">
              Control method:
              <br>
            </span>
            <ul class="label-4-span66">
              <li>
                Upon entering this pause step, you can either pause simply,
                measure alternating current impedance, or set up the temperature
                control chamber.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image6 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i13.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i13.png" data-ll-status="loaded" width="449" height="200"><noscript><img decoding="async" class="image6" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i13.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315815">
      <div class="frame-52">
        <div class="label3">Set Variable</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span67">
              Control Values:
              <br>
            </span>
            <span class="label-4-span68">
              Three control options:
              <br>
            </span>
            <ul class="label-4-span69">
              <li>Reset: Reset the variable to 0.</li>
              <li>Increment: Increase the variable value by 1.</li>
              <li>Decrement: Decrease the variable value by 1.</li>
            </ul>
            <span class="label-4-span70">
              <br>
            </span>
            <span class="label-4-span71">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span72">
              <li>
                Provide users with the ability to operate on declared variables,
                including resetting, incrementing, and decrementing. Users can
                use these variables to set step limits or log limits, enhancing
                the flexibility of the schedule design.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label6">
          No output data, it's a control step for setting up variables in the
          schedule.
        </div>
      </div>
    </div>
    <div class="frame-1321315816">
      <div class="frame-52">
        <div class="label3">Voltage CycleV</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span73">
              Control Values:
              <br>
            </span>
            <ul class="label-4-span74">
              <li>IR: Internal resistance value, measured in Ohms.</li>
              <li>Additionally, reference a pre-set cyclic voltage file.</li>
            </ul>
            <span class="label-4-span75">
              <br>
            </span>
            <span class="label-4-span76">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span77">
              <li>
                Conduct cyclic testing on voltage, allowing for the definition
                of start voltage and target voltage by the user.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image-14008 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i14.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i14.png" data-ll-status="loaded" width="449" height="230"><noscript><img decoding="async" class="image-14008" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i14.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315817">
      <div class="frame-52">
        <div class="label3">Current CycleV</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span78">
              Control Values:
              <br>
            </span>
            <ul class="label-4-span79">
              <li>Reference a pre-set cyclic current file.</li>
            </ul>
            <span class="label-4-span80">
              <br>
            </span>
            <span class="label-4-span81">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span82">
              <li>
                Conduct cyclic testing on current, allowing for the definition
                of starting current and target current by the user.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image7 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i15.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i15.png" data-ll-status="loaded" width="449" height="280"><noscript><img decoding="async" class="image7" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i15.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315818">
      <div class="frame-52">
        <div class="label3">Power Simulation</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          <span>
            <span class="label-4-span83">
              Control Values:
              <br>
            </span>
            <ul class="label-4-span84">
              <li>Reference a power simulation file (.txt).</li>
              <li>
                Options include whether to log points repeatedly and whether
                each current value needs to log two points.
              </li>
            </ul>
            <span class="label-4-span85">
              <br>
            </span>
            <span class="label-4-span86">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span87">
              <li>
                Through the simulation file, simulate the output/input of
                current, voltage, and power values, with the file containing
                timestamps and control values.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156402">
        <img decoding="async" class="image8 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i16.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i16.png" data-ll-status="loaded" width="449" height="259"><noscript><img decoding="async" class="image8" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i16.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315799">
      <div class="frame-53">
        <div class="label3">Load Simulation</div>
      </div>
      <div class="frame-13213156394">
        <div class="label4">
          <span>
            <span class="label-4-span88">
              Control Value:
              <br>
            </span>
            <ul class="label-4-span89">
              <li>Referencing a load simulation file (.txt)</li>
              <li>
                Options to repeat log points and whether each current value
                requires logging two points are available.
              </li>
            </ul>
            <span class="label-4-span90">
              <br>
            </span>
            <span class="label-4-span91">
              Control Method:
              <br>
            </span>
            <ul class="label-4-span92">
              <li>
                Through the simulation file, simulate output/input load values
                are described. The file must include timestamps and control
                values.
              </li>
            </ul>
          </span>
        </div>
      </div>
      <div class="frame-13213156403">
        <img decoding="async" class="image8 entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i17.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i17.png" data-ll-status="loaded" width="449" height="259"><noscript><img decoding="async" class="image8" src="/wp-content/uploads/2024/09/Arbin-State-Machine-Diagram-of-Step-List-of-control-types-i17.png"></noscript>
      </div>
    </div>
  </div>
</div>
</div>
	</div>
</div>
</div>
</div>
```
