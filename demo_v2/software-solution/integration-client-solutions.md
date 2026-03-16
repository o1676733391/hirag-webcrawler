# Source

- URL: https://www.arbin.com/software-solution/integration-client-solutions.html

# Content

#  Integration Client  
Solutions
![ARBIN-AAF-Integration-Client-Solutions](https://www.arbin.com/wp-content/uploads/2024/10/ARBIN-AAF-Integration-Client-Solutions.png)
Table of Contents

##  Introduction
While the Arbin Console offers a user-friendly interface for monitoring and managing battery testing experiments, we understand that advanced users may desire more granular control over their Arbin machines.
To cater to this need, we've developed three additional solutions, provide greater flexibility and customization for users seeking advanced functionality
Video Player
<https://www.arbin.com/wp-content/uploads/2025/05/API-integration-f8.mp4>
![](https://www.arbin.com/wp-content/uploads/2025/03/API-integration-video-bg-f4.png)
00:00
00:00
02:11
[Use Up/Down Arrow keys to increase or decrease volume.](javascript:void\(0\);)
### 1. Arbin Intelligent Client, or ArbinClient
### 2. Arbin Web Services
![Arbin Datastore Overview](https://www.arbin.com/wp-content/uploads/2025/02/Arbin-Datastore-Overview.png)
##  ArbinClient: Advanced Successor to Arbin CTI
[ ](https://www.arbin.com/software-solution/integration-client-solutions.html)
Arbin Intelligent Client (ArbinClient) is a significant upgrade from its predecessors and built upon the Data Acquisition Service (DAS), which is a core component of MITS 11
[ ](https://www.arbin.com/software-solution/integration-client-solutions.html)
ArbinClient offers a streamlined and user-friendly API that simplifies the control and management of Arbin machines, reducing development time and minimizing command latency.
### [Granular Control and Scripting Capabilities](https://www.arbin.com/software-solution/integration-client-solutions.html)
ArbinClient empowers users with precise management of various experiment parameters and settings. Its support for Python and C# scripting enables automated testing and the creation of complex experiment sequences.
### [Faster Development](https://www.arbin.com/software-solution/integration-client-solutions.html)
The intuitive API of ArbinClient facilitates rapid integration, allowing developers to create custom applications and workflows with minimal effort. This accelerates development cycles and reduces time-to-market.
### [Hardware-in-Loop (HIL) Integration](https://www.arbin.com/software-solution/integration-client-solutions.html)
Adjusts the experiment schedule based on real-time measurements, enabling more dynamic and responsive testing.
### [Downward Compatibility](https://www.arbin.com/software-solution/integration-client-solutions.html)
ArbinClient is designed to be compatible with MITS 10. If you're still using MITS 10, ArbinClient can call the built-in Arbin CTI interface, ensuring seamless communication and functionality. This allows you to benefit from ArbinClient's advanced features without the immediate need to upgrade to MITS 11.
![ARBIN-AAF-AIClient- Advanced Successor to Arbin CTI](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-AIClient-Advanced-Successor-to-Arbin-CTI.png)
##  Arbin Web Services
[ ](https://www.arbin.com/software-solution/integration-client-solutions.html)
As the tech landscape shifts towards web-based and cloud-based solutions, Arbin is at the forefront of innovation.
[ ](https://www.arbin.com/software-solution/integration-client-solutions.html)
We're excited to announce the development of a cutting-edge API gateway designed to streamline HTTP request management and routing to our Arbin Data Acquisition Server (DAS).
Our new API gateway is a cornerstone of Arbin's next-generation backend infrastructure. It offers a robust solution for:
### [Real-time data presentation](https://www.arbin.com/software-solution/integration-client-solutions.html)
Access and visualize data in real-time, enabling immediate insights and analysis.
### [Flexible programming](https://www.arbin.com/software-solution/integration-client-solutions.html)
Leverage your preferred programming language to interact with the API, ensuring maximum compatibility and customization.
### [Enhanced efficiency](https://www.arbin.com/software-solution/integration-client-solutions.html)
Streamline the data flow between your applications and the DAS, improving overall system performance.
![API integration v10](https://www.arbin.com/wp-content/uploads/2025/03/API-integration-v10.gif)
To complement our API gateway, we're also developing a dedicated web application for End-of-Line testing.  
This intuitive tool will simplify the end-of-line testing process and automate the generation of essential reports.
Module
Purpose
Methods
Authentication
Authenticates the user and establishes a connection to the DAS backend. 
/ArbinEOL/Login
Test Profile Management
Creates, manages, and executes test profiles.
/ArbinEOL/GetTestObjects   
/ArbinEOL/GetSchedules   
/ArbinEOL/GetEOLVariables 
Test Execution and Monitoring
Controls the operational state of channels during a test and monitors test progress. 
/ArbinEOL/GetEOLChannelsData   
/ArbinEOL/StartTest   
/ArbinEOL/GetCANConfig 
Test Reporting
Generates and manages test reports.
/ArbinEOL/GetAllTestsRecords   
/ArbinEOL/GetTestsRecordByTestID   
/ArbinEOL/GetTestsRecordsByResult 
##  Arbin APIs Performance Test Results
All commands are executed 1000 times except for the command involving control channel operation, which is executed only 100 times, and the test results are shown in the table below:

## Table-like Div HTML (Original)

```html
<div class="fl-col fl-node-h7k9d4ac1r38 fl-col-bg-color specification-table" data-node="h7k9d4ac1r38">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-nbuai0ld78et" data-node="nbuai0ld78et">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>

<div class="web-service-table">
  <div class="frame-1321315669">
    <div class="frame-1321315797">
      <div class="frame-5">
        <div class="label">Module</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Purpose</div>
      </div>
      <div class="frame-1321315640">
        <div class="label">Methods</div>
      </div>
    </div>
    <div class="frame-1321315807">
      <div class="frame-52">
        <div class="label3">Authentication</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Authenticates the user and establishes a connection to the DAS backend.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label5">/ArbinEOL/Login</div>
      </div>
    </div>
    <div class="frame-1321315804">
      <div class="frame-52">
        <div class="label6">Test Profile Management</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">Creates, manages, and executes test profiles.</div>
      </div>
      <div class="frame-13213156402">
        <div class="label7">
          /ArbinEOL/GetTestObjects
          <br>
          /ArbinEOL/GetSchedules
          <br>
          /ArbinEOL/GetEOLVariables
        </div>
      </div>
    </div>
    <div class="frame-1321315805">
      <div class="frame-52">
        <div class="label6">Test Execution and Monitoring</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          Controls the operational state of channels during a test and monitors
          test progress.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label7">
          /ArbinEOL/GetEOLChannelsData
          <br>
          /ArbinEOL/StartTest
          <br>
          /ArbinEOL/GetCANConfig
        </div>
      </div>
    </div>
    <div class="frame-1321315806">
      <div class="frame-53">
        <div class="label6">Test Reporting</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">Generates and manages test reports.</div>
      </div>
      <div class="frame-13213156403">
        <div class="label7">
          /ArbinEOL/GetAllTestsRecords
          <br>
          /ArbinEOL/GetTestsRecordByTestID
          <br>
          /ArbinEOL/GetTestsRecordsByResult
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
<div class="web-service-table">
  <div class="frame-1321315669">
    <div class="frame-1321315797">
      <div class="frame-5">
        <div class="label">Module</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Purpose</div>
      </div>
      <div class="frame-1321315640">
        <div class="label">Methods</div>
      </div>
    </div>
    <div class="frame-1321315807">
      <div class="frame-52">
        <div class="label3">Authentication</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Authenticates the user and establishes a connection to the DAS backend.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label5">/ArbinEOL/Login</div>
      </div>
    </div>
    <div class="frame-1321315804">
      <div class="frame-52">
        <div class="label6">Test Profile Management</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">Creates, manages, and executes test profiles.</div>
      </div>
      <div class="frame-13213156402">
        <div class="label7">
          /ArbinEOL/GetTestObjects
          <br>
          /ArbinEOL/GetSchedules
          <br>
          /ArbinEOL/GetEOLVariables
        </div>
      </div>
    </div>
    <div class="frame-1321315805">
      <div class="frame-52">
        <div class="label6">Test Execution and Monitoring</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">
          Controls the operational state of channels during a test and monitors
          test progress.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label7">
          /ArbinEOL/GetEOLChannelsData
          <br>
          /ArbinEOL/StartTest
          <br>
          /ArbinEOL/GetCANConfig
        </div>
      </div>
    </div>
    <div class="frame-1321315806">
      <div class="frame-53">
        <div class="label6">Test Reporting</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">Generates and manages test reports.</div>
      </div>
      <div class="frame-13213156403">
        <div class="label7">
          /ArbinEOL/GetAllTestsRecords
          <br>
          /ArbinEOL/GetTestsRecordByTestID
          <br>
          /ArbinEOL/GetTestsRecordsByResult
        </div>
      </div>
    </div>
  </div>
</div>
```
