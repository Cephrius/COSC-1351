Servo myservo1;
Servo myservo2;

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
  myservo2.writeMicroseconds(1490);
}

void turnleft() { 
  myservo1.writeMicroseconds(1500);
  myservo2.writeMicroseconds(1000);
}

}

void loop() {


dontmove();

  // Challenge 3
  forward();
  delay(900);
  turnleft();
  delay(1200);
  forward();
  delay(900);
  dontmove();
  delay(5000);

}