# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        | Sub-Schedule (Subroutine) Feature                   |
| Page Type    | Software                                            |
| Source URL   | https://www.arbin.com/software-solution/sub-schedule-subroutine-feature.html |
| Category     | Software Solutions                                  |
| Last Updated |                                                     |

# Overview

The Sub-Schedule feature enhances modularity and maintainability in programming by allowing the creation of reusable testing routines that can be integrated into main schedules.

# Key Features

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Modular testing routines     | Create reusable testing routines that can be easily integrated into main schedules. |
| Flexibility                 | Modify Sub-Schedules without overhauling the entire main schedule.         |
| Streamline test design      | Reuse test sequences to create new battery test recipes efficiently.       |
| Enhanced version control    | Isolate and reuse critical components within tests for consistency.        |
| Simplified workflow         | Integrate validated test segments into new tests for smoother creation.    |
| Simplified managed tests    | Reduce repetitive setup by reusing common test sequences.                  |
| Reusability                 | Integrate validated segments into new tests while maintaining accuracy.    |
| Adaptability                | Quickly create new battery test recipes by reusing sequences.              |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
|           |       |      |       |

## Hardware Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
|           |       |      |       |

## Measurement Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
|           |       |      |       |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
|           |       |      |       |

## General Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum subroutines | 500 | steps | Combined Sub-Schedule and Main Schedule steps must be ≤ 500. |
| Nested Sub-Schedule | Not allowed | | Sub-Schedules cannot reference other schedules. |
| Multiple reference | Allowed | | Many schedules can reference one or multiple sub-schedules. |
| Carbon copy behavior | Not reflected | | Changes in Sub-Schedule subsequence do not reflect in previous references. |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |
|-----------|-------------|----------------|
|           |             |                |

# Software Integration

| Software | Description | Capability |
|----------|-------------|------------|
|          |             |            |

# System Architecture / Infrastructure

| Component | Description |
|-----------|-------------|
| Sub-Schedule Editor | A folder in the Schedule Editor for creating Sub-Schedules. |

# Accessories / Optional Modules

| Module | Description | Link |
|--------|-------------|------|
|        |             |      |

# Related Products / Systems

| Product | Description | Link |
|---------|-------------|------|
|         |             |      |

# Notes

* Sub-Schedule cannot convert to main Schedule and cannot run as a main schedule or independent schedule.
* Main schedule cannot act as a sub-schedule and cannot run as a step of another main schedule.
* Sub-Schedule subsequence change will **NOT** reflect to previous reference, and must **FORCE** update.
* A new field "Sub_Step_ID" will be added to the database for data queries.
* When exporting data, a new column for SubSch Step has been added.
