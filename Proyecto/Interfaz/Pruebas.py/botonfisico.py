import RPi.GPIO as GPIO
import time

LED_PIN = 17
BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    button_state = GPIO.input(BUTTON_PIN)
    if button_state == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)  # Ajusta el tiempo de espera según sea necesario
