# Source

- URL: https://www.arbin.com/software-solution/arbin-control-scripting-test-schedule-language.html

# Content

#  Arbin Control Scripting  [Test Schedule] Language
Arbin Battery Testing Schedule is a structured plan that outlines when and how batteries are tested to ensure their safety, performance, and compliance. It includes various testing types, frequencies, Constant Current (CC), Constant Voltage (CV), Constant Current & Voltage (CC-CV), IR, DCIR, Cycle Voltammetry, Aging, and documentation practices.
By following a well-defined testing schedule, organizations can maintain battery reliability, address potential issues proactively, and extend the operational life of their battery systems.
![ARBIN-Arbin Control Scripting \[Test Schedule\] Language](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Arbin-Control-Scripting-Test-Schedule-Language-1.jpg)
##  Automatic Configuration & Setting
Definition of [Arbin] **Schedule** is a collection of **STEPs** can be **RUN** connected sequences, **JUMP** different **STEP** , **PAUSE** , **RESUME** , **STOP** , **END** , **LOOP** , **REST** , etc.
And STEP is a **control type** state machine with Actions, LogLimits, StepLimits, and Transitions.
![ARBIN-Automatic Configuration & Setting i1](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-Automatic-Configuration-Setting-i1.png)
![ARBIN-Automatic Configuration & Setting i1](https://www.arbin.com/wp-content/uploads/2024/10/ARBIN-Automatic-Configuration-Setting-i1.png)
![ARBIN-Automatic Configuration & Setting i2](https://www.arbin.com/wp-content/uploads/2024/10/ARBIN-Automatic-Configuration-Setting-i2.png)
State
Description
Action
In this state, the system will execute the step with corresponding control type. For example, output constant current with 2A. 
Log Limits
In this state, the system will check if the log limit has been reached. If it does, it will trigger the system to log the data. 
Step Limits
In this state, the system will check if the step limit has been reached. If it does, the system will go to the next state. Otherwise, stay in the current state. 
Action
In this state, the system will transition from one step to another. 
![](https://www.arbin.com/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png)
Transition
There are 5 different scenarios:   
  

  1. Stay at the same step.
  2. Restart at the same step
  3. Go to the next step.
  4. Jump to another step.
  5. Finish the test.

  1. End Test
  2. Unsafe

Control Types
Steps
Functions
Schedule
Static
REST,CC, Crated, CV,CCCV, DCIR, IR
Jump, Loop, Conditional, etc.
Built-in Steps
Dynamic
Lua Script Steps
No Sub-Schedule
Scripting Steps
Complex
DCIM, IEC 61960
Programmable
Built-in, Scripting Steps
Schedule contains the above elements and operation. We provide extremely flexible ways to manage and control Arbin Testing Systems.
### Example Schedule
![ARBIN-Arbin Control Scripting-Example Schedule](https://www.arbin.com/wp-content/uploads/2024/10/ARBIN-Arbin-Control-Scripting-Example-Schedule.png)

## Table-like Div HTML (Original)

```html
<div class="fl-col fl-node-g5da4rlv6b01 fl-col-bg-color specification-table" data-node="g5da4rlv6b01">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-s8rm3y6hvoc4" data-node="s8rm3y6hvoc4">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>
<div class="schedules-table1">
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
          In this state, the system will check if the log limit has been reached.
          If it does, it will trigger the system to log the data.
        </div>
      </div>
    </div>
    <div class="frame-1321315801">
      <div class="frame-52">
        <div class="label3">Step Limits</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          In this state, the system will check if the step limit has been reached.
          If it does, the system will go to the next state. Otherwise, stay in the
          current state.
        </div>
      </div>
    </div>
    <div class="frame-1321315800">
      <div class="frame-52">
        <div class="label3">Action</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          In this state, the system will transition from one step to another.
        </div>
        <img decoding="async" class="image entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png" data-ll-status="loaded" width="969" height="269"><noscript><img decoding="async" class="image" src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315799">
      <div class="frame-53">
        <div class="label3">Transition</div>
      </div>
      <div class="frame-13213156394">
        <div class="label5">
          <span>
            <span class="label-5-span">
              There are 5 different scenarios:
              <br>
              <br>
            </span>
            <ol class="label-5-span2">
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
<div class="schedules-table1">
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
          In this state, the system will check if the log limit has been reached.
          If it does, it will trigger the system to log the data.
        </div>
      </div>
    </div>
    <div class="frame-1321315801">
      <div class="frame-52">
        <div class="label3">Step Limits</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          In this state, the system will check if the step limit has been reached.
          If it does, the system will go to the next state. Otherwise, stay in the
          current state.
        </div>
      </div>
    </div>
    <div class="frame-1321315800">
      <div class="frame-52">
        <div class="label3">Action</div>
      </div>
      <div class="frame-13213156393">
        <div class="label4">
          In this state, the system will transition from one step to another.
        </div>
        <img decoding="async" class="image entered lazyloaded" src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png" data-lazy-src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png" data-ll-status="loaded" width="969" height="269"><noscript><img decoding="async" class="image" src="/wp-content/uploads/2024/09/Arbin-SS-ACL-Schedules-table-1.png"></noscript>
      </div>
    </div>
    <div class="frame-1321315799">
      <div class="frame-53">
        <div class="label3">Transition</div>
      </div>
      <div class="frame-13213156394">
        <div class="label5">
          <span>
            <span class="label-5-span">
              There are 5 different scenarios:
              <br>
              <br>
            </span>
            <ol class="label-5-span2">
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
```

```html
<div id="test-schedule-table2" class="fl-module fl-module-html fl-node-1fts9kx8d0jw" data-node="1fts9kx8d0jw">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>

<div class="schedules-table2">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Control Types</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Steps</div>
      </div>
      <div class="frame-1321315640">
        <div class="label2">Functions</div>
      </div>
      <div class="frame-1321315641">
        <div class="label2">Schedule</div>
      </div>
    </div>
    <div class="frame-1321315797">
      <div class="frame-52">
        <div class="label3">Static</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">REST,CC, Crated, CV,CCCV, DCIR, IR</div>
      </div>
      <div class="frame-1321315640">
        <div class="label4">Jump, Loop, Conditional, etc.</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">Built-in Steps</div>
      </div>
    </div>
    <div class="frame-1321315802">
      <div class="frame-52">
        <div class="label3">Dynamic</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Lua Script Steps</div>
      </div>
      <div class="frame-1321315640">
        <div class="label4">No Sub-Schedule</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">Scripting Steps</div>
      </div>
    </div>
    <div class="frame-1321315803">
      <div class="frame-53">
        <div class="label3">Complex</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">DCIM, IEC 61960</div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">Programmable</div>
      </div>
      <div class="frame-13213156413">
        <div class="label4">Built-in, Scripting Steps</div>
      </div>
    </div>
  </div>

</div>
</div>
	</div>
</div>
```

```html
<div class="schedules-table2">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Control Types</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Steps</div>
      </div>
      <div class="frame-1321315640">
        <div class="label2">Functions</div>
      </div>
      <div class="frame-1321315641">
        <div class="label2">Schedule</div>
      </div>
    </div>
    <div class="frame-1321315797">
      <div class="frame-52">
        <div class="label3">Static</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">REST,CC, Crated, CV,CCCV, DCIR, IR</div>
      </div>
      <div class="frame-1321315640">
        <div class="label4">Jump, Loop, Conditional, etc.</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">Built-in Steps</div>
      </div>
    </div>
    <div class="frame-1321315802">
      <div class="frame-52">
        <div class="label3">Dynamic</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Lua Script Steps</div>
      </div>
      <div class="frame-1321315640">
        <div class="label4">No Sub-Schedule</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">Scripting Steps</div>
      </div>
    </div>
    <div class="frame-1321315803">
      <div class="frame-53">
        <div class="label3">Complex</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">DCIM, IEC 61960</div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">Programmable</div>
      </div>
      <div class="frame-13213156413">
        <div class="label4">Built-in, Scripting Steps</div>
      </div>
    </div>
  </div>

</div>
```
