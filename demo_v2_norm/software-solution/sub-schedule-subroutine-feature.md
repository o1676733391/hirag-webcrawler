# Metadata

| Field | Value1 |
|------|------|
| Title | Sub-Schedule (Subroutine) Feature |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/sub-schedule-subroutine-feature.html |
| Category | Software Solutions |
| Last Updated | |

# Overview

The Sub-Schedule feature introduces an innovative method that enhances modularity, improves maintainability, and strengthens information hiding in programming approaches. This feature allows for a simpler, more efficient, and flexible development experience, making it easier to tackle complex projects.

# Key Features

| Feature | Description |
| Modular Testing Routines | Create reusable testing routines that can be easily integrated into the main schedule, avoiding redundancy and maintaining organized schedules. |
| Flexibility | Modify Sub-Schedules quickly without overhauling the entire main schedule, essential for R&D environments. |
| Streamline Test Design | Reuse commonly performed test sequences to create new battery test recipes faster and more efficiently. |
| Enhanced Version Control | Maintain organization and oversight of test variations by isolating and reusing critical components within tests. |
| Simplified Workflow | Integrate previously validated test segments into new tests, enabling smoother test creation. |
| Simplified Managed Tests | Reuse test sequences to create new battery test recipes efficiently. |
| Reusability | Easily integrate validated test segments into new tests, maintaining accuracy in complex battery testing protocols. |
| Adaptability | Quickly create new battery test recipes by reusing test sequences. |

# Limitations

| Limitation | Description |
| NOT Schedule | Sub-Schedule cannot convert to a main Schedule and cannot run as a main schedule or independent schedule. |
| Schedule NOT A SubSchedule | Main schedule cannot act as a sub-schedule and cannot run as a step of another main schedule. |
| Maximum Subroutines | The total of Sub Schedule and Main Schedule Steps must be less than or equal to 500. |
| NOT Nested Sub-Schedule | Sub-Schedule cannot reference other schedules or Sub-Schedules to form a nested structure. |
| Multiple Reference | Many schedules can reference one or multiple sub-schedules, with default global settings from the running schedule that can be overwritten in sub-schedules. |
| Carbon Copy | Changes in Sub-Schedule subsequences will not reflect in previous references and must be forcefully updated. |

# Sub-Schedule Editor

The Sub Schedule folder in the Schedule Editor allows for the creation of Sub Schedules in the same manner as creating a Schedule.

# Managed Sub-Schedule

## Assignment

Instructions on how to assign a sub-schedule.

## Monitor Test (Monitor & Control)

Channel View in the Monitor & Control window will indicate whether the test is in a SubSchedule step.

## Data Query

A new field, "Sub_Step_ID," will be added to the database Event_Table, Resume_Table, and other related tables for users to view corresponding data when querying results.

## Viewing Data

When exporting data to Excel or CSV files, a new column for SubSch Step has been added.

# Notes
