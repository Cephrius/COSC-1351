#include <Servo.h>

Servo myservo1;

void setup() {
  // put your setup code here, to run once:
  myservo1.attach(12); # <----- TOP SERVO
  myservo1.writeMicroseconds(1000);
  myservo2.attach(10); # <----- BOTTOM SERVO
  myservo2.writeMicroseconds(1000);
}

void dispense(){
  myservo1.writeMicroseconds(1900);
}

void dontMove(){
  myservo1.writeMicroseconds(1470);
}



void loop()
{
 
}