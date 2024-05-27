import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPixmap
import RPi.GPIO as GPIO
from Cocinota import Ui_Cocina
import time

# Define los números de pin para el LED y el servo motor
LED_PIN = 17
SERVO_PIN = 9

# Configura los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Inicializa el PWM para el servo motor
pwm = GPIO.PWM(SERVO_PIN, 50)  # Frecuencia PWM de 50 Hz
pwm.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%

class Inicio(QMainWindow, Ui_Cocina):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Conecta los botones a las funciones correspondientes
        self.LedC.clicked.connect(self.encenderLED)
        self.LedCapagado.clicked.connect(self.apagarLED)
        self.ServoC.clicked.connect(self.abrirServo)
        self.ServoCCerrar.clicked.connect(self.cerrarServo)

        # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # Escala la imagen para que se ajuste al tamaño del QLabel
        self.label_background.setGeometry(0, 0, 700, 500)  # Establece las dimensiones del QLabel
        self.label_background.lower()  # Coloca la imagen de fondo en la capa inferior

    def resizeEvent(self, event):
        # Redimensiona la imagen de fondo para que coincida con las dimensiones de la ventana principal
        pixmap = QPixmap("/home/Emanuel/Desktop/Proyecto/cocina.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def encenderLED(self):
        # Enciende el LED
        GPIO.output(LED_PIN, GPIO.HIGH)

    def apagarLED(self):
        # Apaga el LED
        GPIO.output(LED_PIN, GPIO.LOW)

    def abrirServo(self):
        # Gira el servo a 90 grados
        set_angle(180)

    def cerrarServo(self):
        # Vuelve el servo a 0 grados
        set_angle(0)

def set_angle(angle):
    duty = angle / 18 + 2  # Calcula el ciclo de trabajo necesario para el ángulo deseado
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Ajusta este tiempo según sea necesario para el movimiento completo
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec())
