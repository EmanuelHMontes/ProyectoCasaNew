import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPixmap
import serial

# Define los números de pin para los LEDs
LED_PIN_1 = 2
LED_PIN_2 = 4

# Configura la comunicación serial
ser = serial.Serial("/dev/ttyUSB0", 9600)

class Inicio(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Crear botones y conectar señales
        self.LedC = QPushButton("Encender LED", self)
        self.LedC.setGeometry(50, 50, 200, 50)
        self.LedC.clicked.connect(self.encenderLED)

        self.LedCapagado = QPushButton("Apagar LED", self)
        self.LedCapagado.setGeometry(50, 120, 200, 50)
        self.LedCapagado.clicked.connect(self.apagarLED)

        self.ServoC = QPushButton("Mover Servo 0°", self)
        self.ServoC.setGeometry(50, 190, 200, 50)
        self.ServoC.clicked.connect(self.moverServo0)

        self.ServoCCerrar = QPushButton("Mover Servo 90°", self)
        self.ServoCCerrar.setGeometry(50, 260, 200, 50)
        self.ServoCCerrar.clicked.connect(self.moverServo90)

        # Agrega la imagen de fondo
        self.label_background = QLabel(self)
        self.label_background.setScaledContents(True)  
        self.label_background.setGeometry(0, 0, 700, 500)  
        self.label_background.lower()  

    def resizeEvent(self, event):
        # Redimensiona la imagen de fondo para que coincida con las dimensiones de la ventana principal
        pixmap = QPixmap("/home/Emanuel/Desktop/Proyecto/cocina.jpg") 
        self.label_background.setPixmap(pixmap.scaled(self.size()))  

    def encenderLED(self):
        # Envía el comando para encender el primer LED a través del puerto serie
        ser.write(b'1')

    def apagarLED(self):
        # Envía el comando para apagar el primer LED a través del puerto serie
        ser.write(b'0')

    def moverServo0(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'a')

    def moverServo90(self):
        # Envía el comando para mover el servo a 90 grados
        ser.write(b'b')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inicio()
    window.setGeometry(100, 100, 300, 400)
    window.show()
    sys.exit(app.exec())

