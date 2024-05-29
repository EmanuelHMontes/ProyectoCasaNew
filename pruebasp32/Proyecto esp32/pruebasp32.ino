#include <ESP32Servo.h>

#define LED_PINC 2   // LED cocina
#define LED_PINH 4   // LED habitacion
#define LED_PINS1 16  // LED1 salaF1
#define LED_PINS2 17  // LED2 salaF2
#define LED_PING 5   // LED garage
#define SERVO_PINC 18  // Pin para servomotor de cocina
#define SERVO_PINH 19  // Pin para servomotor de habitacion
#define SERVO_PINS 21  // Pin para servomotor de sala
#define SERVO_PING 22  // Pin para servomotor DE GARAGE

Servo PuertaCocina; // Crear un objeto de tipo Servo para el primer servo
Servo PuertaHabitacion; 
Servo PuertaPrincipal;
Servo PuertaGarage;

void setup() {
    Serial.begin(9600);
    pinMode(LED_PINC, OUTPUT);
    pinMode(LED_PINH, OUTPUT);
    pinMode(LED_PINS1, OUTPUT);
    pinMode(LED_PINS2, OUTPUT);
    pinMode(LED_PING, OUTPUT);
    pinMode(SERVO_PINC, OUTPUT);
    pinMode(SERVO_PINH, OUTPUT);
    pinMode(SERVO_PINS, OUTPUT);
    pinMode(SERVO_PING, OUTPUT);

    PuertaCocina.attach(SERVO_PINC); // junatar PuertaCocina con el pin del SERVO_PINC
    PuertaHabitacion.attach(SERVO_PINH); // Adjuntar el objeto myServo2 al pin del segundo servo
    PuertaPrincipal.attach(SERVO_PINS);
    PuertaGarage.attach(SERVO_PING);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        if (command == '1') {
            digitalWrite(LED_PINC, HIGH);
            Serial.println("LED 1 Encendido");
        } else if (command == '2') {
            digitalWrite(LED_PINC, LOW);
            Serial.println("LED 1 Apagado");
        } else if (command == '3') {
            digitalWrite(LED_PINH, HIGH);
            Serial.println("LED 2 Encendido");
        } else if (command == '4') {
            digitalWrite(LED_PINH, LOW);
            Serial.println("LED 2 Apagado");
        } else if (command == '5') {
            digitalWrite(LED_PINS1, HIGH);
            Serial.println("LED 3 Encendido");
        } else if (command == '6') {
            digitalWrite(LED_PINS1, LOW);
            Serial.println("LED 3 Apagado");
        } else if (command == '7') {
            digitalWrite(LED_PINS2, HIGH);
            Serial.println("LED 4 Encendido");
        } else if (command == '8') {
            digitalWrite(LED_PINS2, LOW);
            Serial.println("LED 4 Apagado");
        } else if (command == '9') {
            digitalWrite(LED_PING, HIGH);
            Serial.println("LED 5 Encendido");
        } else if (command == '0') {
            digitalWrite(LED_PING, LOW);
            Serial.println("LED 5 Apagado");
        } else if (command == 'a') {
            PuertaCocina.write(0); // Mover el primer servo a la posición 0 grados
            Serial.println("Servo 1 movido a 0 grados");
        } else if (command == 'b') {
            PuertaCocina.write(90); // Mover el primer servo a la posición 90 grados
            Serial.println("Servo 1 movido a 90 grados");
        } else if (command == 'c') {
            PuertaHabitacion.write(0); // Mover el segundo servo a la posición 0 grados
            Serial.println("Servo 2 movido a 0 grados");
        } else if (command == 'd') {
            PuertaHabitacion.write(90); // Mover el segundo servo a la posición 90 grados
            Serial.println("Servo 2 movido a 90 grados");
        } else if (command == 'e') {
            PuertaPrincipal.write(0); // Mover el tercer servo a la posición 0 grados
            Serial.println("Servo 3 movido a 0 grados");
        } else if (command == 'f') {
            PuertaPrincipal.write(90); // Mover el tercer servo a la posición 90 grados
            Serial.println("Servo 3 movido a 90 grados");
        } else if (command == 'g') {
            PuertaGarage.write(0); // Mover el cuarto servo a la posición 0 grados
            Serial.println("Servo 4 movido a 0 grados");
        } else if (command == 'h') {
            PuertaGarage.write(90); // Mover el cuarto servo a la posición 90 grados
            Serial.println("Servo 4 movido a 90 grados");
        }
    }
}
