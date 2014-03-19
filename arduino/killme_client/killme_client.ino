/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;
int mot = 12;

// the setup routine runs once when you press reset:
void setup() {           
  Serial.begin(115200);  
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  pinMode(mot, OUTPUT);     

}

// the loop routine runs over and over again forever:
void loop() {
  if(Serial.available() > 0 ){
    //Serial.println("");
    int dato = Serial.read();
    digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(mot, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(2000);               // wait for a second
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
    digitalWrite(mot, LOW);   // turn the LED on (HIGH is the voltage level)
  }
}
