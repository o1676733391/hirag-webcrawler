# Source

- URL: https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html

# Content

#  Arbin APIs Performance  
Test Results
All commands are executed 1000 times except for the command involving control channel operation, which is executed only 100 times, and the test results are shown in the table below:
##  Local
### Environment
  * Client and server are both on the same PC
  * Mits 10.4.14.16 and ArbinCTI 1.0.70
  * MCU: LBT21084, 8Ch
  * Each command is executed on one channel only

![ARBIN-AAF-ArbinAPIs-local](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-ArbinAPIs-local.png)
##  Wi-Fi
### Experiment Setup Environment
  * Local area network (Wi-Fi)
  * Two computers: IP192.168.1.54(Client) and IP192.168.1.107(Server)
  * Mits 10.4.14.16 and ArbinCTI 1.0.70
  * MCU: LBT21084, 8Ch
  * Each command is executed on one channel only

![ARBIN-AAF-ArbinAPIs-wifi](https://www.arbin.com/wp-content/uploads/2024/09/ARBIN-AAF-ArbinAPIs-wifi.png)
##  Definition
### [Max Response Time](https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html)
The maximum time duration between Sending Command to CTI and Receiving CTI feedback(confirmation)​
### [Min Response Time](https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html)
The minimum time duration between Sending Command to CTI and Receiving CTI feedback(confirmation)​
### [Average Response Time](https://www.arbin.com/software-solution/arbin-apis-performance-test-results.html)
The averagetime duration between Sending Command to CTI and Receiving CTI feedback(confirmation)
Timeout​
Description
Time(s)​
Note​
Connection Timeout
If a timeout is set, a connection timeout error code is returned if a network connection is not received within the time period. 
-
Network connection timeout needs to be set manually, the default is busy waiting for results 
Login Timeout
If the client does not call the PostUserLogin interface to log in within the specified time, the server will disconnect from the network. 
/
WinDaq has no login timeout.
Active Timeout
If the client does not call any interface within the specified time, the server will disconnect from the network. 
/
WinDaq has no active timeout.
Post Get Meta Variables
A timeout error code will be returned if the Feedback is not received within the specified time. 
3
Post UpLoad File
Upload file(Block)   
  
A timeout error code will be returned if the Feedback is not received within the specified time. 
1.5
Remaining commands
/
/
For **Get Channel Data** command, the user can get the data very quickly, but the data may not change, the data change according to the log of IV channel or MCU refresh every 3 seconds.
##  APIs Performance
Command
Description
Avg (ms)
99 PCT
95 PCT
90 PCT
PostAssignFile
Assign files to IV channels
15.76
19.91
17.95
17.19
PostAssignSchedule
Assign files to IV channels
21.37
23.43
22.79
22.50
PostCheckFileEx
Check if the file exists
2.59
37.25
2.96
2.60
PostConvertToAnonymousOrNamedTO
TestObject to anonymous or non-anonymous
15.82
16.58
16.37
16.30
PostGetChannelInfoEx*
Get TestObject data for IV channel
0.12
0.31
0.22
0.17
PostGetChannelsDataMinimalistMode*
Getting IV channel data with only current and voltage 
0.11
0.30
0.19
0.15
PostGetChannelsData*
Getting IV channel data
0.12
0.44
0.22
0.17
PostGetMetaVariables*
Get meta-variables for IV channels
1.36
2.99
2.24
2.01
PostGetResumeData
Get Resume data for IV channel from database
22.59
26.29
24.78
24.15
PostGetStartData
Get the initial data needed before Start
10.27
13.26
11.96
11.39
PostGetServerSoftwareVersionNumber
Get the software version number of the server
0.90
2.24
1.36
1.26
PostGetStringLimitLength
Get the string limit length, such as: Test Name
0.93
4.18
1.38
1.24
PostJumpChanne
Control IV channel jump to other step
17.90
19.63
18.96
18.71
PostResumeChannelEx
Resume IV channel
118.88
134.78
125.95
124.71
PostResumeChannel
Resume IV channel
121.41
137.65
130.98
128.67
PostSetMetaVariable
Update a meta-variable of the IV channel
0.93
3.42
1.36
1.26
PostStartChannelEx
Start IV channel
49.97
56.37
54.22
53.41
PostStartChannel
Start IV channel
51.76
58.57
56.27
55.38
PostStopChannel
Stop IV channel
17.66
18.93
18.55
18.39
PostUpdateMetaVariableAdvanced
Batch update of meta-variables for IV channels
1.15
4.59
1.67
1.52
PostUpdateParameters
Update parameters, e.g. TestObject parameters
15.88
16.83
16.42
16.34
PostUserLogin
User login
2.10
5.08
3.14
2.85
PostBrowseDirectory
Get a list of files and folders in a Directory
9.56
34.15
12.15
10.40
PostDeleteFile
Delete file
16.15
22.06
16.76
16.66
PostDownLoadFile
Download file
1.51
3.95
2.13
1.93
PostNewFolder
New Directory
15.94
16.81
16.48
16.39
PostNewOrDelete
Delete file or new Directory
15.93
16.74
16.49
16.41
PostUpLoadFile
Upload file(Block)
23.47
29.84
27.49
26.57
PostUpLoadFile
Upload file
15.76
19.91
17.95
17.19
*99% Percentiles (PCT) of client request and response time in milliseconds have proven our integration with other systems will be robust and high performance.

## Table-like Div HTML (Original)

```html
<div class="fl-col fl-node-m84jqhcst17a fl-col-bg-color specification-table" data-node="m84jqhcst17a">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-thkpf4mx8ic7 align-center" data-node="thkpf4mx8ic7">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>
<div class="definition-table">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Timeout​</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Description</div>
      </div>
      <div class="frame-1321315640">
        <div class="label2">Time(s)​</div>
      </div>
      <div class="frame-1321315641">
        <div class="label2">Note​</div>
      </div>
    </div>
    <div class="frame-1321315797">
      <div class="frame-52">
        <div class="label3">Connection Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If a timeout is set, a connection timeout error code is returned if a
          network connection is not received within the time period.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">-</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">
          Network connection timeout needs to be set manually, the default is busy
          waiting for results
        </div>
      </div>
    </div>
    <div class="frame-1321315805">
      <div class="frame-52">
        <div class="label3">Login Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If the client does not call the PostUserLogin interface to log in within
          the specified time, the server will disconnect from the network.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">WinDaq has no login timeout.</div>
      </div>
    </div>
    <div class="frame-1321315806">
      <div class="frame-52">
        <div class="label3">Active Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If the client does not call any interface within the specified time, the
          server will disconnect from the network.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">WinDaq has no active timeout.</div>
      </div>
    </div>
    <div class="frame-1321315807">
      <div class="frame-52">
        <div class="label3">Post Get Meta Variables</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          A timeout error code will be returned if the Feedback is not received
          within the specified time.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">3</div>
      </div>
      <div class="frame-13213156412"></div>
    </div>
    <div class="frame-1321315808">
      <div class="frame-52">
        <div class="label3">Post UpLoad File</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Upload file(Block)
          <br>
          <br>
          A timeout error code will be returned if the Feedback is not received
          within the specified time.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">1.5</div>
      </div>
      <div class="frame-13213156412"></div>
    </div>
    <div class="frame-1321315809">
      <div class="frame-52">
        <div class="label3">Remaining commands</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412"></div>
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
<div class="definition-table">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Timeout​</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Description</div>
      </div>
      <div class="frame-1321315640">
        <div class="label2">Time(s)​</div>
      </div>
      <div class="frame-1321315641">
        <div class="label2">Note​</div>
      </div>
    </div>
    <div class="frame-1321315797">
      <div class="frame-52">
        <div class="label3">Connection Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If a timeout is set, a connection timeout error code is returned if a
          network connection is not received within the time period.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">-</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">
          Network connection timeout needs to be set manually, the default is busy
          waiting for results
        </div>
      </div>
    </div>
    <div class="frame-1321315805">
      <div class="frame-52">
        <div class="label3">Login Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If the client does not call the PostUserLogin interface to log in within
          the specified time, the server will disconnect from the network.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">WinDaq has no login timeout.</div>
      </div>
    </div>
    <div class="frame-1321315806">
      <div class="frame-52">
        <div class="label3">Active Timeout</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          If the client does not call any interface within the specified time, the
          server will disconnect from the network.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412">
        <div class="label4">WinDaq has no active timeout.</div>
      </div>
    </div>
    <div class="frame-1321315807">
      <div class="frame-52">
        <div class="label3">Post Get Meta Variables</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          A timeout error code will be returned if the Feedback is not received
          within the specified time.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">3</div>
      </div>
      <div class="frame-13213156412"></div>
    </div>
    <div class="frame-1321315808">
      <div class="frame-52">
        <div class="label3">Post UpLoad File</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Upload file(Block)
          <br>
          <br>
          A timeout error code will be returned if the Feedback is not received
          within the specified time.
        </div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">1.5</div>
      </div>
      <div class="frame-13213156412"></div>
    </div>
    <div class="frame-1321315809">
      <div class="frame-52">
        <div class="label3">Remaining commands</div>
      </div>
      <div class="frame-13213156392">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156402">
        <div class="label4">/</div>
      </div>
      <div class="frame-13213156412"></div>
    </div>
  </div>
</div>
```

```html
<div class="fl-col fl-node-6yn783geqwsi fl-col-bg-color specification-table" data-node="6yn783geqwsi">
	<div class="fl-col-content fl-node-content">
<div class="fl-module fl-module-html fl-node-1cutp679ym4r" data-node="1cutp679ym4r">
	<div class="fl-module-content fl-node-content">
		<div class="fl-html">
	<style></style>

<div class="api-performance-table ">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Command</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Description</div>
      </div>
      <div class="frame-1321315829">
        <div class="frame-1321315642">
          <div class="label2">Avg (ms)</div>
        </div>
        <div class="frame-1321315640">
          <div class="label2">99 PCT</div>
        </div>
        <div class="frame-1321315643">
          <div class="label2">95 PCT</div>
        </div>
        <div class="frame-1321315641">
          <div class="label2">90 PCT</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315839">
      <div class="frame-52">
        <div class="label3">PostAssignFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Assign files to IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.91</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">17.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">17.19</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315811">
      <div class="frame-52">
        <div class="label3">PostAssignSchedule</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Assign files to IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">21.37</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">23.43</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">22.79</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">22.50</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315812">
      <div class="frame-52">
        <div class="label3">PostCheckFileEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Check if the file exists</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">2.59</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">37.25</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.60</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315813">
      <div class="frame-52">
        <div class="label3">PostConvertToAnonymousOrNamedTO</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">TestObject to anonymous or non-anonymous</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.82</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.58</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.37</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.30</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315814">
      <div class="frame-52">
        <div class="label3">PostGetChannelInfoEx*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get TestObject data for IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.12</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.31</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.17</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315815">
      <div class="frame-52">
        <div class="label3">PostGetChannelsDataMinimalistMode*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Getting IV channel data with only current and voltage
        </div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.11</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.30</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.19</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.15</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315816">
      <div class="frame-52">
        <div class="label3">PostGetChannelsData*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Getting IV channel data</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.12</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.44</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.17</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315817">
      <div class="frame-52">
        <div class="label3">PostGetMetaVariables*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get meta-variables for IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">2.99</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.24</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.01</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315818">
      <div class="frame-52">
        <div class="label3">PostGetResumeData</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get Resume data for IV channel from database</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">22.59</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">26.29</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">24.78</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">24.15</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315819">
      <div class="frame-52">
        <div class="label3">PostGetStartData</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the initial data needed before Start</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">10.27</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">13.26</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">11.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">11.39</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315820">
      <div class="frame-52">
        <div class="label3">PostGetServerSoftwareVersionNumber</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the software version number of the server</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.90</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">2.24</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.26</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315821">
      <div class="frame-52">
        <div class="label3">PostGetStringLimitLength</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the string limit length, such as: Test Name</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">4.18</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.38</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.24</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315822">
      <div class="frame-52">
        <div class="label3">PostJumpChanne</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Control IV channel jump to other step</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">17.90</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.63</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">18.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">18.71</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315823">
      <div class="frame-52">
        <div class="label3">PostResumeChannelEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Resume IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">118.88</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">134.78</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">125.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">124.71</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315824">
      <div class="frame-52">
        <div class="label3">PostResumeChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Resume IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">121.41</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">137.65</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">130.98</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">128.67</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315825">
      <div class="frame-52">
        <div class="label3">PostSetMetaVariable</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Update a meta-variable of the IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">3.42</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.26</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315826">
      <div class="frame-52">
        <div class="label3">PostStartChannelEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Start IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">49.97</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">56.37</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">54.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">53.41</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315827">
      <div class="frame-52">
        <div class="label3">PostStartChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Start IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">51.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">58.57</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">56.27</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">55.38</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315828">
      <div class="frame-52">
        <div class="label3">PostStopChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Stop IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">17.66</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">18.93</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">18.55</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">18.39</div>
        </div>
      </div>
    </div>
    <div class="frame-13213158293">
      <div class="frame-52">
        <div class="label3">PostUpdateMetaVariableAdvanced</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Batch update of meta-variables for IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.15</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">4.59</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.67</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.52</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315830">
      <div class="frame-52">
        <div class="label3">PostUpdateParameters</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Update parameters, e.g. TestObject parameters</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.88</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.83</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.42</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.34</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315831">
      <div class="frame-52">
        <div class="label3">PostUserLogin</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">User login</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">2.10</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">5.08</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">3.14</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.85</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315832">
      <div class="frame-52">
        <div class="label3">PostBrowseDirectory</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get a list of files and folders in a Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">9.56</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">34.15</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">12.15</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">10.40</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315833">
      <div class="frame-52">
        <div class="label3">PostDeleteFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Delete file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">16.15</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">22.06</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.76</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.66</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315834">
      <div class="frame-52">
        <div class="label3">PostDownLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Download file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.51</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">3.95</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.13</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.93</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315835">
      <div class="frame-52">
        <div class="label3">PostNewFolder</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">New Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.94</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.81</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.48</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.39</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315836">
      <div class="frame-52">
        <div class="label3">PostNewOrDelete</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Delete file or new Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.74</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.49</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.41</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315837">
      <div class="frame-52">
        <div class="label3">PostUpLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Upload file(Block)</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">23.47</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">29.84</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">27.49</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">26.57</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315838">
      <div class="frame-52">
        <div class="label3">PostUpLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Upload file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.91</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">17.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">17.19</div>
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
<div class="api-performance-table ">
  <div class="frame-1321315669">
    <div class="frame-1321315804">
      <div class="frame-5">
        <div class="label">Command</div>
      </div>
      <div class="frame-1321315639">
        <div class="label2">Description</div>
      </div>
      <div class="frame-1321315829">
        <div class="frame-1321315642">
          <div class="label2">Avg (ms)</div>
        </div>
        <div class="frame-1321315640">
          <div class="label2">99 PCT</div>
        </div>
        <div class="frame-1321315643">
          <div class="label2">95 PCT</div>
        </div>
        <div class="frame-1321315641">
          <div class="label2">90 PCT</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315839">
      <div class="frame-52">
        <div class="label3">PostAssignFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Assign files to IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.91</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">17.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">17.19</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315811">
      <div class="frame-52">
        <div class="label3">PostAssignSchedule</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Assign files to IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">21.37</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">23.43</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">22.79</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">22.50</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315812">
      <div class="frame-52">
        <div class="label3">PostCheckFileEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Check if the file exists</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">2.59</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">37.25</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.60</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315813">
      <div class="frame-52">
        <div class="label3">PostConvertToAnonymousOrNamedTO</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">TestObject to anonymous or non-anonymous</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.82</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.58</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.37</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.30</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315814">
      <div class="frame-52">
        <div class="label3">PostGetChannelInfoEx*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get TestObject data for IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.12</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.31</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.17</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315815">
      <div class="frame-52">
        <div class="label3">PostGetChannelsDataMinimalistMode*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">
          Getting IV channel data with only current and voltage
        </div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.11</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.30</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.19</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.15</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315816">
      <div class="frame-52">
        <div class="label3">PostGetChannelsData*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Getting IV channel data</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.12</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">0.44</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">0.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">0.17</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315817">
      <div class="frame-52">
        <div class="label3">PostGetMetaVariables*</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get meta-variables for IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">2.99</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.24</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.01</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315818">
      <div class="frame-52">
        <div class="label3">PostGetResumeData</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get Resume data for IV channel from database</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">22.59</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">26.29</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">24.78</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">24.15</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315819">
      <div class="frame-52">
        <div class="label3">PostGetStartData</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the initial data needed before Start</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">10.27</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">13.26</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">11.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">11.39</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315820">
      <div class="frame-52">
        <div class="label3">PostGetServerSoftwareVersionNumber</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the software version number of the server</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.90</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">2.24</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.26</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315821">
      <div class="frame-52">
        <div class="label3">PostGetStringLimitLength</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get the string limit length, such as: Test Name</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">4.18</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.38</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.24</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315822">
      <div class="frame-52">
        <div class="label3">PostJumpChanne</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Control IV channel jump to other step</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">17.90</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.63</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">18.96</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">18.71</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315823">
      <div class="frame-52">
        <div class="label3">PostResumeChannelEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Resume IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">118.88</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">134.78</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">125.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">124.71</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315824">
      <div class="frame-52">
        <div class="label3">PostResumeChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Resume IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">121.41</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">137.65</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">130.98</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">128.67</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315825">
      <div class="frame-52">
        <div class="label3">PostSetMetaVariable</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Update a meta-variable of the IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">0.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">3.42</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.36</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.26</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315826">
      <div class="frame-52">
        <div class="label3">PostStartChannelEx</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Start IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">49.97</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">56.37</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">54.22</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">53.41</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315827">
      <div class="frame-52">
        <div class="label3">PostStartChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Start IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">51.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">58.57</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">56.27</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">55.38</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315828">
      <div class="frame-52">
        <div class="label3">PostStopChannel</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Stop IV channel</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">17.66</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">18.93</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">18.55</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">18.39</div>
        </div>
      </div>
    </div>
    <div class="frame-13213158293">
      <div class="frame-52">
        <div class="label3">PostUpdateMetaVariableAdvanced</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Batch update of meta-variables for IV channels</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.15</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">4.59</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">1.67</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.52</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315830">
      <div class="frame-52">
        <div class="label3">PostUpdateParameters</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Update parameters, e.g. TestObject parameters</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.88</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.83</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.42</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.34</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315831">
      <div class="frame-52">
        <div class="label3">PostUserLogin</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">User login</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">2.10</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">5.08</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">3.14</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">2.85</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315832">
      <div class="frame-52">
        <div class="label3">PostBrowseDirectory</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Get a list of files and folders in a Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">9.56</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">34.15</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">12.15</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">10.40</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315833">
      <div class="frame-52">
        <div class="label3">PostDeleteFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Delete file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">16.15</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">22.06</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.76</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.66</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315834">
      <div class="frame-52">
        <div class="label3">PostDownLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Download file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">1.51</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">3.95</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">2.13</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">1.93</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315835">
      <div class="frame-52">
        <div class="label3">PostNewFolder</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">New Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.94</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.81</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.48</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.39</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315836">
      <div class="frame-52">
        <div class="label3">PostNewOrDelete</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Delete file or new Directory</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.93</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">16.74</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">16.49</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">16.41</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315837">
      <div class="frame-52">
        <div class="label3">PostUpLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Upload file(Block)</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">23.47</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">29.84</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">27.49</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">26.57</div>
        </div>
      </div>
    </div>
    <div class="frame-1321315838">
      <div class="frame-52">
        <div class="label3">PostUpLoadFile</div>
      </div>
      <div class="frame-1321315639">
        <div class="label4">Upload file</div>
      </div>
      <div class="frame-13213158292">
        <div class="frame-1321315642">
          <div class="label4">15.76</div>
        </div>
        <div class="frame-13213156402">
          <div class="label4">19.91</div>
        </div>
        <div class="frame-1321315643">
          <div class="label4">17.95</div>
        </div>
        <div class="frame-13213156412">
          <div class="label4">17.19</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
