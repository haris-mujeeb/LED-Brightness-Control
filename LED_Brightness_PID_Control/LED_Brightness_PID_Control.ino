const int digitalPin = 13;
const int analogPin = A0;
int sensorValue =0;

void setup() { 
  // initialize digital pin 13 as an output.
  Serial.begin(9600);
  pinMode(digitalPin, OUTPUT);
  pinMode(analogPin, INPUT);

} 

// the loop function runs over and over again forever
void loop() {
  digitalWrite(digitalPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  Serial.println(sensorValue);

  for (int i = 0; i<300; i++){
    sensorValue = analogRead(analogPin);
//    Serial.print("sensor = ");
    Serial.print(i);
    Serial.print(",");
    Serial.println(sensorValue);
    delay(10);
  }
  
  digitalWrite(digitalPin, LOW);    // turn the LED off by making the voltage LOW
  for (int i = 0; i<300; i++){
    sensorValue = analogRead(analogPin);
//    Serial.print("sensor = ");
    Serial.print(i);
    Serial.print(",");
    Serial.println(sensorValue);
    delay(10);
  }
}
