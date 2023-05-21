Components used:
| Name   |      function      |  Cool |
|----------|:-------------:|------:|
| NodeMCU ESP8266 | microcontroller | $1600 |
| KY-018 | Photoresistor Module | $12 |
| White LED |  |    $1 |


Generate a step response for the system:





We save the value for the step response:

	

	
	
Starting UART communication using RealTerm:
	Ref: https://miscircuitos.com/plot-real-time-signal-coming-arduino/




We open the Capture tab and select the appropriate settings:



The data is saved in the designated location and file:



Finding the approximate curve manually (initial guess):
	We can model this setup as a 1st order with dead time  (PT1-elemet + Time Shift)

  Thus there are three important constants:
	Gain K	(151-1003)/(1024-0) = -0.832 	Rise in Output Value by Rise in Input Value
	Time Constant Tau	1003 - (1003-151)*0.9 = 236.2 	It takes 5 Tau to go from initial point to 90% steady state value.
		5*Tau = 20ms (from data)
		Tau = 4ms
	Dead Time T	0ms	
	
	
Generating the Transfer Function:




Modeling on Simulink:



Scope:




Comparing the data with experimental:


	
	
Using non-linear Curve fitting with python:
	Ref: https://www.youtube.com/watch?v=1H-SdMuJXTk&t=237s
	
	We find following constant with least square method:

		
	Using the new constants in the Simulink Model:

		
	New Curve vs Experimental Data

		
		
		
PID Tuning:
	Creating a PID Model in Simulink:

	
	Tuning the Plant using PID Controller Block:

		
		
	Updating Block with new values for Controller Parameter:

		
		
	Result:






![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/4b4e40ac-1bb3-4274-a9b0-087ba1ac2195)

