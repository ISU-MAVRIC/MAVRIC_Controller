//MAVRIC CONTROLLER

// Import the Arduino Servo library
#include <Servo.h> 
#include <SyRenSimplified.h>
#include <PID_v1.h>

//Define Variables we'll be connecting to
double setPoint, input, rawOutput;
double rawInput, output;

//Specify the links and initial tuning parameters
//Input range 102-1023
PID myPID(&input, &rawOutput, &setPoint,1.2,0,0, DIRECT);

//String dataString;

SyRenSimplified SR(Serial2);


// Create a Servo object for each servo
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
// TO ADD SERVOS:
//   Servo servo7;

// Common servo setup values
int minPulse = 600;   // minimum servo position, us (microseconds)
int maxPulse = 2400;  // maximum servo position, us

// User input for servo and position
int userInput[3];    // raw input from serial buffer, 3 bytes
int startbyte;       // start byte, begin reading input
int servo;           // which servo
int pos;             // servo angle
int i;               // iterator

// LED on Pin 13 for digital on/off demo
int ledPin = 13;
int pinState = LOW;
// Variables for button switches
//int angle = 900;
int change = 2;

void setup() 
{ 
  // Attach each Servo object to a digital pin
  servo1.attach(8, minPulse, maxPulse);
  servo2.attach(3, minPulse, maxPulse);
  servo3.attach(4, minPulse, maxPulse);
  servo4.attach(5, minPulse, maxPulse);
  servo5.attach(6, minPulse, maxPulse);
  servo6.attach(7, minPulse, maxPulse);
  // TO ADD SERVOS:
  //   servo5.attach(PIN, minPulse, maxPulse);
  //   etc...

  // LED on Pin 13 for digital on/off demo
  pinMode(ledPin, OUTPUT);

  // Open the serial connection, 9600 baud
  Serial.begin(9600);
  Serial2.begin(9600);
  //initialize the variables we're linked to
  rawInput = analogRead(0);
  setPoint = 300;
  
  //turn the PID on
  myPID.SetOutputLimits(-127,127);
  myPID.SetMode(AUTOMATIC);
} 

void loop() 
{ 
  // Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 2) {
    // Read the first byte
    startbyte = Serial.read();
    // If it's really the startbyte (255) ...
    if (startbyte == 255) {
      // ... then get the next two bytes
      for (i=0;i<2;i++) {
        userInput[i] = Serial.read();
      }
      servo = userInput[0];
      pos = userInput[1];
      // Packet error checking
      if (pos == 255) { servo = 255; }

      // Assign new position to appropriate servo
      switch (servo) {
        case 1:   ///Left motor---Motor.setSpeed(pos) cases 1,3,5
          servo1.write(pos);    // move servo1 to 'pos'
          delay(20);
          break;
        case 2:  ///Right motor---Motor.setSpeed(pos)cases 2,4,6
          servo2.write(pos);
          delay(20);
          break;
        case 3:
          servo3.write(pos);
          delay(20);
          break;
        case 4:
          servo4.write(pos);
          delay(20);
          break;
        case 5:
          servo5.write(pos);
          delay(20);
          break;
        case 6:
          servo6.write(pos);
          delay(20);
          break;
   // TO ADD SERVOS:
   //     case 6:
   //       servo5.write(pos);
   //       break;
   // etc...
        case 50:
          //Controls the movement of the arm & end effector back and forward 
          if (pos == 180) {
            setPoint = setPoint + change; //Increment
          }
          if (pos == 90) {
            setPoint = setPoint - change; // Decrement
          }
          
          rawInput = analogRead(0);
          input = map(rawInput, 102, 1023, 0, 1023);
          myPID.Compute();
          SR.motor((int) rawOutput);
          break;
          
          
          
        // LED on Pin 13 for digtal on/off demo
        case 99:
          if (pos == 180) {
            if (pinState == LOW) { pinState = HIGH; }
            else { pinState = LOW; }
          }
          if (pos == 0) {
            pinState = LOW;
          }
          digitalWrite(ledPin, pinState);
          break;
      }
    }
  }
}
