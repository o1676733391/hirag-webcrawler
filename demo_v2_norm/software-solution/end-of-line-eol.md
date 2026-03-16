# Metadata

| Field | Value1 |
|------|------|
| Title | End-Of-Line (EOL) Testing Solution |
| Page Type | Software |
| Source URL | https://www.arbin.com/software-solution/end-of-line-eol.html |
| Category | Testing Solutions |
| Last Updated | 2024-10 |

# Overview

Ensure every battery performs to your highest standard with the End of Line (EOL) feature, now integrated in our trusted MITS software. The best batteries, made better.

# Key Features

| Feature | Description |
| --- | --- |
| Comprehensive Customizable Criteria Checks | Define your own battery performance criteria using logical expressions and equations. Tailor the checks to meet the specific needs of your production line. |
| Precision and Flexibility | From basic checks to complex multi-step validations, our system ensures that every battery is thoroughly tested to your exact specifications. |
| Seamless Integration with Schedule Files | Combine the EOL feature with our schedule file to create continuous end-of-line testing protocols. This allows for streamlined operations and consistent quality assurance across all production stages. |
| Automated Testing | Simplify your workflow by automating EOL testing, reducing the need for manual intervention and minimizing errors. |
| Real-Time Monitoring & Comprehensive Reporting | Stay informed with our real-time monitoring page, which provides live updates on the testing process. Quickly identify any potential issues as they arise. |
| Detailed Post-Test Reports | After testing, receive a comprehensive report covering all the criteria checks and any potential failures. These reports provide invaluable insights for improving your production process and ensuring product quality. |

# Test Profile

The EOL (End-Of-Line) profile is a structured framework designed to guide the testing process at the final stage of product production. This profile defines the steps required for EOL testing, including the schedules or scripts to be executed, the criteria that must be verified for acceptance, and the specific minimum and maximum values, along with their tolerance levels.

# Creating an EOL Profile

## Input Basic Information

Users begin by providing the essential details for the EOL profile, including the label (name), test object, and a description of the test. Additionally, there is an option to utilize CAN BMS during the testing process.

## Input Additional Test Inputs

Users can specify custom additional test inputs, which appear as variables within the test profile. These variables can be configured by providing a name, selecting a type (e.g., float, string), setting a default value, assigning a unit, and choosing whether to display this variable in the report. If the variable is no longer needed, users can delete it.

## Create Global Criteria

Global criteria in the EOL profile allow users to define conditions and checks that the EOL engine will monitor throughout the testing process. Each criterion includes a "Whens" section, where the conditions are specified, and a "Checks" section, where the criteria to be verified after conditions are met are detailed. Users can configure the system to continue or stop the current test or halt all tests if a check fails.

# Condition Expression Wizard

The Condition Expression Wizard allows users to easily create or edit condition expressions in a user-friendly environment. When you click on the expression field, a wizard pops up, providing an intuitive editor to define conditions with ease. You can access a range of predefined meta variables (MV_UDs), functions, auxiliary values, and user-customized additional inputs from the toolbar at the top of the editor. The editor also features a smart search bar, allowing you to quickly find the elements you need. Additionally, as you type, the editor offers suggestions and reminders of related variables. It will even detect and alert you to any errors in your input, helping you correct mistakes on the spot.

# Add New Conditions

You can define the relationships between various conditions using "AND" and "OR" logic. By clicking the green add button under a condition, you can add a sub-condition that is automatically connected with "AND," linking it directly to the parent condition. On the other hand, the orange add button allows you to introduce a completely new condition, which will be connected using "OR," enabling you to build complex and flexible logical expressions.

# Select the Schedule and Create Criteria for the Schedule

Finally, users can select a specific schedule for the test and create criteria tailored to that schedule, further customizing the EOL testing process to meet specific requirements.

## Schedule Selection

Users can choose a schedule file from the dropdown menu and assign it a file alias for easy reference.

## Schedule Details

The detailed steps within the selected schedule file are displayed on the right side of the interface.

## MV_UDs Configuration

All MV_UDs configurations can be viewed by clicking the "MV_UDs Config" button.

## Defining Criteria

Similar to global criteria, users can define criteria specific to the chosen schedule using the same intuitive editor as the global editor.

# Test Criteria Engine

Our Criteria Engine is the backbone of our End-of-Line (EOL) testing process, meticulously designed to ensure every product meets the highest standards of quality. When an EOL Test Run is initiated, a specific profile and test object barcode are selected, and the test is carried out on a designated channel. The process may involve executing a series of tests. These tests are evaluated against both schedule-specific and global criteria, ensuring comprehensive coverage. Each criterion is assessed multiple times throughout the test, ensuring precise and accurate results. Our evaluation process is designed to leave no room for error—if a single failure is detected, the entire test is immediately flagged, allowing for swift identification and resolution of any issues. Upon completion, the test results are determined based on the combined outcomes of all criteria, ensuring that only products meeting all necessary conditions pass. With its flexible structure and robust evaluation framework, the Criteria Engine plays a crucial role in upholding the highest levels of quality control, making it an indispensable part of the EOL testing process.

# Test Report

The EOL Test Report is a comprehensive summary that encapsulates the results of an End-of-Line (EOL) testing process. This report provides a detailed overview of the test, including the EOL Test Name, Test Run ID, and the Test Object Barcode. It also captures key timestamps for the start and end of the test, as well as the overall test result, ensuring full transparency and traceability. The core of the report is the Test Summary table, which itemizes each test conducted during the EOL process. For each test, the report details the Test ID, Test Name, Description, Acceptance Criteria, Measurement, and Unit. The final result for each test is clearly marked, allowing for quick identification of any issues or areas that need attention. One of the standout features of this report is its flexible export options. Users can easily export the report to various destinations, including cloud storage, remote servers, FTP servers, and more, providing versatile ways to share and store the test data securely.

# Notes

*Autocalibration box is sold separately.*
**EIS testing device is sold separately.**
