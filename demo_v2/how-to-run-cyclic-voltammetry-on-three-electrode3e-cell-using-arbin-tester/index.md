# Source

- URL: https://www.arbin.com/how-to-run-cyclic-voltammetry-on-three-electrode3e-cell-using-arbin-tester.html

# Content

#  How to run cyclic voltammetry on three-electrode(3E) cell using Arbin Tester
October 21, 2025
# I. Introduction to 3E cell
In a battery with 2 electrode, when you measure the battery voltage, you measure the potential difference between the cathode and anode of the battery. In this case, you only see the total difference in potentials and do not know how much each electrode contribute to this difference. You would not know which electrode you need to change the material to improve the performance of the battery.
This causes the analysis process become much more difficult and sometimes it is blindly guessing. 3E cells are introduced in battery material research where you can study the electrochemical reactions on each electrode separately.
![how to run cyclic voltammetry on three electrode3e cell using arbin tester 1](https://www.arbin.com/wp-content/uploads/2025/10/how-to-run-cyclic-voltammetry-on-three-electrode3e-cell-using-arbin-tester-1.png)
In the most common case, the 3E cell include working electrode (W), counter electrode (C), and reference electrode (R). The material on R and C electrode are normally fixed, meanwhile, the researcher put the material they want to study on working electrode (W).
The current will flow between working electrode and counter electrode, however, the voltage is measured between the working electrode and the reference electrode.
Because practically there’s no current flow through the reference electrode, all the change of voltage is only contributed by what is happening on the working electrode. By doing this, the working electrode W is studied separately from the counter electrode.
In some cases, people also want to measure the voltage between Working electrode and Counter electrode concurrently. In this case, Arbin instruments are also capable of conducting the test.
# II Apply Arbin Instruments’ machine to measure 3E cell.
## 1. Hardware connection
![apply arbin instruments machine to measure 3e cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20560'%3E%3C/svg%3E)
Figure 1: Terminal connections for battery testing using Arbin System
A typical Arbin system socket have 4 wire: red, white, black, green wires. They are respectively I+, V+, I-, V-. You can see in the above diagram second voltage connectors which will be mentioned later.
**a. When anodic current is positive**
![positive anodic current](https://www.arbin.com/wp-content/uploads/2025/10/positive-anodic-current.png)
Figure 2:Positive anodic current
In this connection, the red wire (I+) is connected to the working electrode, the black wire (I-) is connected to the counter electrode. This will provide current to flow from the W to the C.
The white wire is connected to W and the green wire is connected to R, this will measure the voltage between W and R.
### b. When anodic current is negative
![negative anodic current](https://www.arbin.com/wp-content/uploads/2025/10/negative-anodic-current.png)
Figure 3: Negative anodic current
You do not need to change the cable connections compared to Figure 2. The Arbin system allows current control in both directions. In the MITS software, simply enter a negative current value to make the current flow from the counter electrode to the working electrode.
![negative anodic current 2](https://www.arbin.com/wp-content/uploads/2025/10/negative-anodic-current-2.png)
Figure 4: Negative anodic current
There is still another way of negative anodic current connection as the diagram above (Figure 4). In this case, the cell must have 2 reference electrode.
### c. Auxiliary voltage connector
If you want to measure the voltage between the C and W, you can use auxiliary voltage connector as shown in figure 1. You can connect the read alligator clip to C, the black alligator clip to W.
When you connect Arbin main system to the battery, you also need to connect Auxiliary voltage to Arbin system through ethernet cable. The red and black cable of the Auxiliary is connected to the battery as shown in the picture below.
![auxiliary voltage connector](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201966%20990'%3E%3C/svg%3E)
## 2. Software configuration
If you are not measuring voltage between W and C, you do not have to care about the mapping file. However, if you are, then in the mapping file, please remember to map the auxiliary channel to the IV channel correctly.
In the example below, we are mapping Auxiliary voltage channel 1 to IV channel 1. This IV channel 1 and Aux Voltage channel 1 are used to connect to the 3E battery.
![aux voltage channel 1 are used to connect to the 3e battery](https://www.arbin.com/wp-content/uploads/2025/10/aux-voltage-channel-1-are-used-to-connect-to-the-3e-battery.png)
After the connection, you can follow this article to run cyclic voltammetry on Arbin software: [How to run cyclic voltammetry(CV) using Arbin Tester](https://www.arbin.com/how-to-run-cyclic-voltammetry-on-three-electrode3e-cell-using-arbin-tester.html)
Posted in [Application Notes](https://www.arbin.com/category/application-notes), [Latest News](https://www.arbin.com/category/latest-news)
[ ![Arbin Team](https://secure.gravatar.com/avatar/1fbb2cb48e39ebefa1c1ce89417a209646a543accdad521cbdd22b968d3a6b95?s=300&d=mm&r=g)](https://www.arbin.com)
###  [ Arbin Team ](https://www.arbin.com)
  * [ Visit author's facebook profile ](https://www.facebook.com/ArbinInstruments/)
  * [ Visit author's linkedin profile ](https://www.linkedin.com/company/arbin-instruments/)
  * [ Visit author's youtube profile ](https://www.youtube.com/channel/UCw-WJk0lBTGXPdSac4Xx8CA)

Posts navigation
[← Arbin at The Battery Show North America 2025 — Empowering the Future of Energy Innovation](https://www.arbin.com/arbin-at-the-battery-show-north-america-2025-empowering-the-future-of-energy-innovation.html)
[Driving Battery Innovation: Arbin at The Battery Show India 2025 →](https://www.arbin.com/driving-battery-innovation-arbin-at-the-battery-show-india-2025.html)
