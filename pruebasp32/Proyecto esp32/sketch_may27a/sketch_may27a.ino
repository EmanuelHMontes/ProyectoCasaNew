#include <Arduino.h>

const int LED_PIN_1 = 2;
const int LED_PIN_2 = 4;

void setup() {
  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '0') {
      digitalWrite(LED_PIN_1, LOW);
    } else if (command == '1') {
      digitalWrite(LED_PIN_1, HIGH);
    } else if (command == '2') {
      digitalWrite(LED_PIN_2, LOW);
    } else if (command == '3') {
      digitalWrite(LED_PIN_2, HIGH);
    }
  }
}
