# Metadata

| Field | Value |
|------|------|
| Title | Arbin Control Scripting [Test Schedule] Language |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/arbin-control-scripting-test-schedule-language.html |
| Category | Battery Testing |
| Last Updated | 2024-09 |

# Overview

Arbin Battery Testing Schedule is a structured plan that outlines when and how batteries are tested to ensure their safety, performance, and compliance. It includes various testing types, frequencies, Constant Current (CC), Constant Voltage (CV), Constant Current & Voltage (CC-CV), IR, DCIR, Cycle Voltammetry, Aging, and documentation practices. By following a well-defined testing schedule, organizations can maintain battery reliability, address potential issues proactively, and extend the operational life of their battery systems.

# Key Features

| Feature | Description |
|---------|-------------|
| Testing Types | Constant Current (CC), Constant Voltage (CV), Constant Current & Voltage (CC-CV), IR, DCIR, Cycle Voltammetry, Aging |
| Schedule Management | Extremely flexible ways to manage and control Arbin Testing Systems |

# Automatic Configuration & Setting

Definition of Arbin Schedule is a collection of STEPs that can be RUN connected sequences, JUMP different STEP, PAUSE, RESUME, STOP, END, LOOP, REST, etc. A STEP is a control type state machine with Actions, LogLimits, StepLimits, and Transitions.

## Control Types

| Control Type | Description |
|--------------|-------------|
| Static | REST, CC, Crated, CV, CCCV, DCIR, IR |
| Dynamic | Lua Script Steps |
| Complex | DCIM, IEC 61960 |

## State Descriptions

| State | Description |
|-------|-------------|
| Action | In this state, the system will execute the step with corresponding control type. For example, output constant current with 2A. |
| Log Limits | In this state, the system will check if the log limit has been reached. If it does, it will trigger the system to log the data. |
| Step Limits | In this state, the system will check if the step limit has been reached. If it does, the system will go to the next state. Otherwise, stay in the current state. |
| Transition | In this state, the system will transition from one step to another. |

## Transition Scenarios

| Scenario | Description |
|----------|-------------|
| 1 | Stay at the same step. |
| 2 | Restart at the same step. |
| 3 | Go to the next step. |
| 4 | Jump to another step. |
| 5 | Finish the test. |

# Example Schedule

*No specific example schedule provided in the source document.*

# Notes

*Images and diagrams referenced in the document are not included in the markdown.*
