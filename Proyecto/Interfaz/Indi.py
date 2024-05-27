import RPi.GPIO as GPIO
import time
import threading

# Define los pines GPIO para los LEDs y el servo motor
LED_PIN_1 = 17
LED_PIN_2 = 27
LED_PIN_3 = 4
LED_PIN_4 = 22
LED_PIN_5 = 10
SERVO_PIN = 9
# Configura los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(LED_PIN_4, GPIO.OUT)
GPIO.setup(LED_PIN_5, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configura el pin PWM para el servo motor
pwm = GPIO.PWM(SERVO_PIN, 50)  # Frecuencia PWM de 50 Hz
pwm.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%

class ControlaTodo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.led_states = [False, False, False, False, False]  # Estados de los cinco LEDs
        self.servo_state = False  # Estado del servo motor
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            # Enciende o apaga los LEDs según sus estados
            GPIO.output(LED_PIN_1, GPIO.HIGH if self.led_states[0] else GPIO.LOW)
            GPIO.output(LED_PIN_2, GPIO.HIGH if self.led_states[1] else GPIO.LOW)
            GPIO.output(LED_PIN_3, GPIO.HIGH if self.led_states[2] else GPIO.LOW)
            GPIO.output(LED_PIN_4, GPIO.HIGH if self.led_states[3] else GPIO.LOW)
            GPIO.output(LED_PIN_5, GPIO.HIGH if self.led_states[4] else GPIO.LOW)
            # Controla el servo motor
            if self.servo_state:
                set_angle(50)
            else:
                set_angle(0)
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

def set_angle(angle):
    duty = angle / 18 + 2  # Calcula el ciclo de trabajo necesario para el ángulo deseado
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def main():
    led_thread = ControlaTodo()
    led_thread.start()

    try:
        while True:
            command = input("Introduce 'on1', 'on2', 'on3', 'on4', 'on5' para encender cada LED respectivamente, 'off1', 'off2', 'off3', 'off4', 'off5' para apagarlos, 'ons1' para encender el servo, 'offs1' para apagar el servo, o 'exit' para salir: ")
            if command.startswith("on"):
                if command == "on":
                    led_thread.servo_state = True
                else:
                    led_thread.led_states[int(command[-1]) - 1] = True
            elif command.startswith("off"):
                if command == "off":
                    led_thread.servo_state = False
                else:
                    led_thread.led_states[int(command[-1]) - 1] = False
            elif command.startswith("ons"):
                led_thread.servo_state = True
            elif command.startswith("offs"):
                led_thread.servo_state = False
            elif command == "exit":
                break
    finally:
        led_thread.stop()
        led_thread.join()
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
