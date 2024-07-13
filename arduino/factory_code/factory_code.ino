////Integrated Control CODE
//Control Fan Motor
//Control Water Level
//Team 2: 
//Date: November 16th, 2022
//Description:  This sketch turns the Fan Motor ON and OFF based on measured temperature and set UCL and LCL
//It also prints the analog read value from the thermistor
//This sketch monitors and controls the water level in the Chemical Bath and Reservoir
//At the same time where it monitors the water leveland temperature, it displays the values and data onto the LCD screen

//importing the library to be used for the LCD screen
#include <Wire.h>  


  // set the LCD address to 0x27 for a 16 chars and 2 line display 

/*********************************************************/ 

//variables
int fan = 8; //initializing the led variable to write to whatever is connected to pin 8
int led = 9; //initializing the led variable to write to whatever is connected to pin 9
int pump = 10; //initializing the led variable to write to whatever is connected to pin 10

//setting up the pins to be used as ouputs
void setup() {
  pinMode(fan, OUTPUT); //digital pin 8 controls Fan Motor
  pinMode(led, OUTPUT); //digital pin 9 controls LED Heater
  pinMode(pump, OUTPUT); //digital pin 10 controls Mini-Pump
  Serial.begin(9600);  //set up to print out text to monitor

/*
//******************** LCD **************************************
  lcd.init();  //initialize the lcd 

  lcd.backlight();  //open the backlight  

  lcd.setCursor ( 0, 0 );            // go to the top left corner 
  lcd.print("  Houston Christian  "); // write this string on the top row 
  lcd.setCursor ( 0, 1 );            // go to the 2nd row 
  lcd.print("     University     "); // pad string with spaces for centering 
  lcd.setCursor ( 7, 2 );            // go to the third row 
  lcd.print("i = "); // pad with spaces for centering  
  lcd.setCursor ( 7, 3 );            // go to the fourth row 
  lcd.print("x = "); // pad with spaces for centering 
*/
}
//main loop
void loop() {
  H2OV();
  delay(2000);
  thermy();
  delay(300);

}


//Making a seperate function to control the water pump
void H2OV() {
  int H2Oval = analogRead(3);// read water sensor analog input pin 5
  //lcd.setCursor (0, 2 );            // go to the third row
  //lcd.print("Water Level: "); lcd.print(H2Oval);  //
  Serial.print("Water Level: "); Serial.println(H2Oval);
  // if the water gets to a low water value, 170, then turn on the pump
  if (H2Oval < 170) {
    digitalWrite(pump, HIGH);
  }
  // if the water gets to a high water value, 180, then turn off the pump
  else if (H2Oval > 180) {
    digitalWrite(pump, LOW);
  }
  delay(100);  
}

//Making a seperate function to control the led and fan
void thermy() {
  int val = analogRead(0); // read thermister analog input pin 4
  
  //lcd.setCursor ( 0, 0 );            // go to the top left corner
  //lcd.print("Analog value =   "); lcd.print(val) // write this string on the top row
  Serial.print("Analog value = ");
  Serial.print(val);

  //lcd.setCursor ( 0, 1 );            // go to the 2nd row
  //lcd.print("Temperature = "); lcd.print(int((val/7.1)-.77));    //write this on the second row
  Serial.print("    Temperature = ");
  Serial.println(int((val/7.1)-.77)); // our temperature equation to convert
                                     // the analogRead value to fahrenheit

  //if the value that is recieved by thermistor gets to a certain high value, 576,
  //the turn off the led and turn on the fan
  if (val > 20) {
    digitalWrite(fan,HIGH);
    digitalWrite(led, LOW);
  }
  //else if the value that the thermistor recieves gets to a certain low value, 535,
  //turn on the led and turn off the fan
  else if (val = 0) {
    digitalWrite(fan, LOW);
    digitalWrite(led, HIGH);
  }
}
