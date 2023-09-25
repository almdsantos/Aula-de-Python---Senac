#include "Servo.h"

Servo servoMotorObj;

int const potenciometroPin = 0;
int const servoMotorPin = 3;
int valPotenciometro;

void setup() {
  servoMotorObj.attach(servoMotorPin);
}

void loop(){
  valPotenciometro = analogRead(potenciometroPin);
  valPotenciometro = map(valPotenciometro, 0, 1023, 0, 360);

  servoMotorObj.write(valPotenciometro);
  delay(15);
}