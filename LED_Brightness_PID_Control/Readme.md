# Components used:
| Name   | 
|----------|
| NodeMCU ESP8266 |
| KY-018 |
| White LED | 
| Jumper wires | 

# Procedure:
First Generate a step response for the system:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/6beb5dbb-e0ed-41a1-bb5d-83fff4fe60bd)

## 1. Saving the sensor value for the step response using PuTTY or RealTerm:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/f4db8974-6fe5-418c-8f70-60b302dcb682)
#### Starting UART communication using RealTerm:
Ref: https://miscircuitos.com/plot-real-time-signal-coming-arduino/
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/616df685-c2bc-49b8-90c5-5178efd5d9ba)

#### We open the Capture tab and select the appropriate settings:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/f00efcc0-77a0-4799-85d4-cfe4435ff868)

#### The data is saved in the designated location and file:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/22fbc7a9-ee52-47a6-afe0-b07c26001fb2)
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/13cfce42-2a39-496a-a306-c2f627dc5167)

### 2. Finding the approximate curve manually (initial guess):
We can model this setup as a 1st order with dead time  (PT1-elemet + Time Shift), 

![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/be702169-3e4f-4ff9-a358-87783ba899f1)

  Thus there are three important constants: <br />
	> **Gain K** (Rise in Output Value by Rise in Input Value)<br />
		>> **K** = (151-1003)/(1024-0) = -0.832<br /><br />
	> **Time Constant Tau** ( It takes 5 Tau to go from initial point to 90% steady state value.)<br />
		||5*Tau = 1003 - (1003-151)*0.9 = 236.2  <br />
		||5*Tau = 20ms (from data)<br />
		 || **Tau** = 4ms<br /><br />
	|**Dead Time T** = 0ms (from data)<br />
	
	
## 3. Simulating the initla model in MatLab and Comparing it with the experimental data:
### Generating the Transfer Function in with above calculated constants:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/76da910f-9e64-4c9d-b33a-6cb9b9c88bdd)

### Modeling on Simulink:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/58deb3d6-c40b-4814-bee4-54d456cfcb82)

#### Scope:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/b063786f-7a06-48a3-97c8-1d90aa974e33)


### Comparing the data with experimental:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/5c5f320e-fdb0-4fa6-a3dd-9e7b974cf24c)

	
## 4. Using non-linear Curve fitting using Python SciPy Library:
Ref: https://www.youtube.com/watch?v=1H-SdMuJXTk&t=237s
	
### We find following constant with least square method:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/a2e0e538-4717-4743-b96e-165b21fbd1f1)

### the new constants in the Simulink Model:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/529810db-7a3d-4fbb-b71b-9638c98afa9a)
	
### New Curve vs Experimental Data
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/f2ca99a8-2499-4f58-a450-608199cfb48d)

		
## 5. PID Tuning:
### Creating a PID Model in Simulink:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/0a5c7ced-d7b6-4ae4-b351-23c5641d8e9c)

### Tuning the Plant using PID Controller Block:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/16aa0490-4b0d-43c9-90cd-9dc463a91318)

### Block with new values for Controller Parameter:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/66b80a9c-fbe3-49fd-b5bc-515ce8c9a6b5)
		
#### Result:
![image](https://github.com/haris-mujeeb/Digital-Control-Projects/assets/57053470/8de5d8f5-6d84-4724-8d5f-dce54cae89ee)

