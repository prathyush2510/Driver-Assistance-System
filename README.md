# Driver-Assistant-System
This Repository contains all files related to Driver Assistant System Project

## What it does ??
This project consists of three inter-linked modules which are firstly, driver
drowsiness detection, followed by alcohol content detection and accident/crash
detection alongside control to constantly monitor the driver’s physiological
condition which will affect the stability of the vehicle. To implement this, a
variety of software algorithms and input extraction hardware tools have been
employed in a collaborative way. For the industrial implementation of this
project a prototype has been developed. To detect the onset of fatigue or loss of
vigilance of the driver, within the close vicinity of the driver multiple sensors
are embedded on this prototype.

## Some of the Important details to be noted:
1.The SMTP protocol which is used to send mail works only on JIO network. <br>
2.The Raspberry pi is connected to laptop using remote desktop connection app on windows 10.<br>
3.Both the laptop and raspberry pi are connected to same JIO network.<br>
4.While using the Android App , permissions such as sms and location should be enabled.<br>
5.Settings has to be changed for the email id which is used to send the alert.<br>

<h3>Hardware of the System</h3>
<img src="https://github.com/prathyush2510/Driver-Assistance-System/blob/main/images/hardware.PNG" height=500px>

<h3>Overall Prototype of the system</h3>
<img src="https://github.com/prathyush2510/Driver-Assistance-System/blob/main/images/Untitled.png">

<h3>Use of Haar Cascade Algorithm to Monitor facial interactions of the driver.</h3>
<img src="https://github.com/prathyush2510/Driver-Assistance-System/blob/main/images/face.PNG">

<h4>Alerting phase consist of 2 different modules</h4>
<h5>1 Mail <h5>
 <img src="https://github.com/prathyush2510/Driver-Assistance-System/blob/main/images/mail1.jpeg" height=400px>

<h5>2 Msg <h5>
 <img src="https://github.com/prathyush2510/Driver-Assistance-System/blob/main/images/msg.jpeg" height=400px>
 

## Publication Details
 
View here : 
https://ieeexplore.ieee.org/document/9432361

Details:
"Driver Assistance System using Raspberry Pi and Haar Cascade Classifiers," 2021 5th International Conference on Intelligent Computing and Control Systems (ICICCS), 2021
pp. 1729-1735, doi: 10.1109/ICICCS51141.2021.9432361.

Authors:
 <ul>
  <li>V. Praveen Kumar</li>
  <li>P. Aravind</li>
  <li>S. Nachammai Devi Pooja</li>
  <li>S. Prathyush</li>
  <li>S. AngelDeborah</li>
  <li>K. R. S. Chandran</li>
 </ul>
 
 
 <h1>Steps to Run the Prototype</h1>
 1.Connect the Raspbery pi to Computer. (I used Remote Desktop Connection App in Windows 10)<br>
 2.Run the Python Program.(Main.py)<br>
 3.After Detection of any of the proposed event , an alert is raised.<br>
 4.Check your Email and Phone number for Alert message. <br>
 
 
 <h3>My Teammates </h3>
 1.<a href="https://github.com/NachammaiPooja">Nachammai Pooja</a><br>
 2.<a href="https://github.com/Aravind1411">Aravind P</a><br>
 3.<a href="https://github.com/praveenkumar0211">Praveen Kumar V</a><br>
