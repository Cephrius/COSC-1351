#include <Servo.h>

Servo myservo1;

void setup() {
  // put your setup code here, to run once:
  myservo1.attach(9);
  
}

void loop(){
  myservo1.writeMicroseconds(1000);
  delay(500);

}