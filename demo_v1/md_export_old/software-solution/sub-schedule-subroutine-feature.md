# Source

- URL: https://www.arbin.com/software-solution/sub-schedule-subroutine-feature.html

# Content

#  Sub-Schedule (Subroutine) Feature
![ARBIN-ACL-Sub-Schedule-Subroutine-Feature.png](https://www.arbin.com/images/layout/ARBIN-ACL-Sub-Schedule-Subroutine-Feature.png)
##  Introduction Sub-Schedule
Our current programming approach relies on traditional scheduling methods, but it lacks modularity and is difficult to maintain.
Now, we are introducing an innovative sub-Schedule method that significantly enhances modularity, improves maintainability, and strengthens information hiding.
With this cutting-edge approach, you'll enjoy a simpler, more efficient, and flexible development experience, making it easier to tackle complex projects!
We have integrated the concepts of encapsulation and reusability into our Schedule and Sub-Schedule methods, delivering a **powerful solution** that enhances efficiency and flexibility in your development process.

Only one-layer Sub-Schedule is supported
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
##  Limitations
### NOT Schedule
Sub-Schedule cannot convert to main Schedule and cannot run as main schedule or independent schedule.
### Schedule NOT A SubSchedule
Main schedule cannot acts a sub-schedule and cannot run as step of another main schedule
### Maximum Subroutines
Only allowing Sub Schedule and Main Schedule Steps together must be less than or equal to 500
### NOT Nested Sub-Schedule
Sub-Schedule cannot reference other schedule or Sub-Schedule to form a nested
### Multiple Reference
Many schedules can reference to one or multiple sub-schedules and default global setting from running schedule and allow to overwrite in sub-schedules
### Carbon Copy
Sub-Schedule subsequence change will **NOT** reflect to previous reference, and must **FORCE** update
## Sub-Schedule Editor

We have a Sub Schedule folder in the Schedule Editor. The way to create a Sub Schedule is the same as creating a Schedule
## Managed Sub-Schedule
### Assignment
Here is how you assign sub schedule

### Monitor Test (Monitor & Control)
Channel View in the Monitor & Control window will also show whether the test is in a SubSchedule step.

### Data Query
A new field in SQL will be added, "Sub_Step_ID" to the database Event_Table, Resume_Table, and other related database tables so that users may view the corresponding data when querying results.

### Viewing Data
When exporting data to Excel or CSV file, a new column for SubSch Step has been added.
