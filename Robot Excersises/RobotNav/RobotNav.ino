#include <Servo.h>

Servo myservo1;
Servo myservo2;
void loop() {

void setup() {
  myservo1.attach(11);
  myservo1.writeMicroseconds(1000);
  myservo2.attach(12);
  myservo2.writeMicroseconds(1000);

void backright() {
  myservo1.writeMicroseconds(1500);
  myservo2.writeMicroseconds(2000);
}
void forward() {
  myservo1.writeMicroseconds(2000);
  myservo2.writeMicroseconds(1000);
}

void backward() {
  myservo1.writeMicroseconds(1000);
  myservo2.writeMicroseconds(2000);
}

void turnright() {
  myservo1.writeMicroseconds(1700);
  myservo2.writeMicroseconds(1500);
}

void dontmove() { 
  myservo1.writeMicroseconds(1515);
  myservo2.writeMicroseconds(1460);
}

void turnleft() { 
  myservo1.writeMicroseconds(1500);
  myservo2.writeMicroseconds(1000);
}

}




dontmove();
/*
  forward();
  delay(1000);
  dontmove();
  delay(1000);
  backward();
  delay(1000);
  dontmove();
  delay(5000);
  
  forward();
  delay(1000);
  dontmove();
  delay(1000);
  backward();
  delay(1000);
  dontmove();
  delay(5000);
  
  forward();
  delay(900);
  turnleft();
  delay(1200);
  forward();
  delay(900);
  dontmove();
  delay(5000);
  
  forward();
  delay(1400);
  turnleft();
  delay(725);a
  forward();
  delay(340);
  dontmove();
  delay(2000);
  backward();
  delay(300);
  backright();
  delay(745);
  backward();
  delay(1800);
  dontmove();
  delay(5000);


  forward();
  delay(1300);
  turnleft();
  delay(300);
  forward();
  delay(800);
  turnleft();
  delay(1500);
  forward();
  delay(400);
  turnright();
  delay(790);
  forward();
  delay(800);
  turnright();
  delay(400);
  forward();
  delay(1200);
  dontmove();
  delay(5000);


  forward();
  delay(1420);
  turnleft();
  delay(350);
  forward();
  delay(400);
  turnleft();
  delay(348);
  forward();
  delay(1862);
  dontmove();
  delay(5000);
*/
  
}
// Function movements  

