# Metadata

| Field | Value1 |
|------|------|
| Title | Arbin Control Scripting [Test Schedule] Language |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/arbin-control-scripting-test-schedule-language.html |
| Category | Battery Testing Software |
| Last Updated | 2024-10 |

# Overview

Arbin Battery Testing Schedule is a structured plan that outlines when and how batteries are tested to ensure their safety, performance, and compliance. It includes various testing types, frequencies, Constant Current (CC), Constant Voltage (CV), Constant Current & Voltage (CC-CV), IR, DCIR, Cycle Voltammetry, Aging, and documentation practices. By following a well-defined testing schedule, organizations can maintain battery reliability, address potential issues proactively, and extend the operational life of their battery systems.

## Automatic Configuration & Setting

Definition of Arbin Schedule is a collection of STEPs that can be RUN connected sequences, JUMP different STEP, PAUSE, RESUME, STOP, END, LOOP, REST, etc. A STEP is a control type state machine with Actions, LogLimits, StepLimits, and Transitions.

### State Descriptions

| State | Description | Action |
|-------|-------------|--------|
| Action | In this state, the system will execute the step with corresponding control type. For example, output constant current with 2A. | Execute step |
| Log Limits | In this state, the system will check if the log limit has been reached. If it does, it will trigger the system to log the data. | Check log limit |
| Step Limits | In this state, the system will check if the step limit has been reached. If it does, the system will go to the next state. Otherwise, stay in the current state. | Check step limit |
| Action | In this state, the system will transition from one step to another. | Transition to next step |

### Transition Scenarios

There are 5 different scenarios:
1. Stay at the same step.
2. Restart at the same step.
3. Go to the next step.
4. Jump to another step.
5. Finish the test.

Additional scenarios:
1. End Test
2. Unsafe

## Control Types and Functions

| Control Type | Steps | Functions | Schedule |
|--------------|-------|-----------|----------|
| Static | REST, CC, Crated, CV, CCCV, DCIR, IR | Jump, Loop, Conditional, etc. | Built-in Steps |
| Dynamic | Lua Script Steps | No Sub-Schedule | Scripting Steps |
| Complex | DCIM, IEC 61960 | Programmable | Built-in, Scripting Steps |

# Example Schedule

![ARBIN-Arbin Control Scripting-Example Schedule](https://www.arbin.com/wp-content/uploads/2024/10/ARBIN-Arbin-Control-Scripting-Example-Schedule.png)

# Notes

*Autocalibration box is sold separately.*
