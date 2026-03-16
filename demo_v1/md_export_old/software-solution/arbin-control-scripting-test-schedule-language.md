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
