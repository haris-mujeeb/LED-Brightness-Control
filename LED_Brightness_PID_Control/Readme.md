# Components used:
| Name   | Function |  
|----------|:-------------:|
| NodeMCU ESP8266 | Microcontroller | 
| KY-018 | Photoresistor Module | 
| White LED |  |
| Jumper wires |  |

# Procedure:
First Generate a step response for the system:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/6beb5dbb-e0ed-41a1-bb5d-83fff4fe60bd)

## Saving the sensor value for the step response using PuTTY or RealTerm:
	![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/f4db8974-6fe5-418c-8f70-60b302dcb682)
#### Starting UART communication using RealTerm:
	Ref: https://miscircuitos.com/plot-real-time-signal-coming-arduino/
	![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/616df685-c2bc-49b8-90c5-5178efd5d9ba)

	We open the Capture tab and select the appropriate settings:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/f00efcc0-77a0-4799-85d4-cfe4435ff868)



The data is saved in the designated location and file:
	![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/22fbc7a9-ee52-47a6-afe0-b07c26001fb2)
	![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/13cfce42-2a39-496a-a306-c2f627dc5167)


Finding the approximate curve manually (initial guess):
	We can model this setup as a 1st order with dead time  (PT1-elemet + Time Shift)
			![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/be702169-3e4f-4ff9-a358-87783ba899f1)

  Thus there are three important constants:
	Gain K (Rise in Output Value by Rise in Input Value)
		K = (151-1003)/(1024-0) = -0.832
	Time Constant Tau ( It takes 5 Tau to go from initial point to 90% steady state value.)
		5*Tau = 1003 - (1003-151)*0.9 = 236.2  
		5*Tau = 20ms (from data)
		  Tau = 4ms
	Dead Time T = 0ms (from data)
	
	
Simulating the initla model in MatLab and Comparing it with the experimental data:
	Generating the Transfer Function in with above calculated constants:
		![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/76da910f-9e64-4c9d-b33a-6cb9b9c88bdd)

	Modeling on Simulink:
		![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/58deb3d6-c40b-4814-bee4-54d456cfcb82)

		Scope:
		![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/b063786f-7a06-48a3-97c8-1d90aa974e33)


	Comparing the data with experimental:
		![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/5c5f320e-fdb0-4fa6-a3dd-9e7b974cf24c)

	
Using non-linear Curve fitting using Python SciPy Library:
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

