from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from Usuario import Ui_MainWindow as Ui_LoginWindow
from Menu import Ui_Menu as Ui_MenuWindow
from Cocinota import Ui_Cocina
from Habitacion import Ui_Habitacion
from Sala import Ui_Sala
from Garage import Ui_Garage
#import RPi.GPIO as GPIO
import time
import serial
import sys

# Pines
LED_PINC = 2
SERVO_PINC = 18
LED_PINH = 4
SERVO_PINH = 19
LED_PINS = 16
LED_PINS2 = 17
SERVO_PINS = 21
LED_PING = 5
SERVO_PING = 22

# Configura los pines GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PINC, GPIO.OUT)
# GPIO.setup(SERVO_PINC, GPIO.OUT)
# GPIO.setup(LED_PING, GPIO.OUT)
# GPIO.setup(SERVO_PING, GPIO.OUT)
# GPIO.setup(LED_PINH, GPIO.OUT)
# GPIO.setup(SERVO_PINH, GPIO.OUT)
# GPIO.setup(LED_PINS, GPIO.OUT)
# GPIO.setup(LED_PINS2, GPIO.OUT)
# GPIO.setup(SERVO_PINS, GPIO.OUT)

# Configura la comunicación serial
ser = serial.Serial("COM5", 9600)

# # pwm servos
# pwm_c = None
# pwm_h = None
# pwm_g = None
# pwm_s = None

# try:
#     pwm_c = GPIO.PWM(SERVO_PINC, 50)  # Frecuencia PWM de 50 Hz
#     pwm_c.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%
#     pwm_h = GPIO.PWM(SERVO_PINH, 50)  # Frecuencia PWM de 50 Hz
#     pwm_h.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%
#     pwm_g = GPIO.PWM(SERVO_PING, 50)  # Frecuencia PWM de 50 Hz
#     pwm_g.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%
#     pwm_s = GPIO.PWM(SERVO_PINS, 50)  # Frecuencia PWM de 50 Hz
#     pwm_s.start(0)  # Inicializa el PWM con un ciclo de trabajo del 0%
# except Exception as e:
#     print("Error en pwm:", e)

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.IniciarS.clicked.connect(self.login)

        # Configurar el campo de contraseña para que los caracteres escritos no sean visibles
        self.Contraseña.setEchoMode(QLineEdit.Password)

        # Lista de usuarios y contraseñas
        self.usuarios = {
            "Emanuel": "spiderman",
            "Hugo": "goku",
            "Itza": "uwu",
            "Diego": "bocho",
            "Omar": "dados"
        }

        # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc

    def resizeEvent(self, event):
         # imagen de fondo coincida con la prinicipal 
         pixmap = QPixmap("C:\\Users\\emanu\\Desktop\\pruebasp32\\Proyecto esp32\\imag\\Casa real.jpg")  # Nueva ruta de la imagen de fondo
         self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def login(self):
        username = self.UsuarioI.text()
        password = self.Contraseña.text()

        # Verificar si el nombre de usuario y la contraseña son válidos
        if username in self.usuarios and self.usuarios[username] == password:
            QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso!")
            self.menu_window = MenuWindow()
            self.menu_window.show()
            self.hide()  # Ocultar la ventana de inicio de sesión
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Nombre de usuario o contraseña incorrectos.")

class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Conectar la señal clicked del botón pushButton_Cocina a la función abrirCocinota
        self.pushButton_Cocina.clicked.connect(self.abrirCocinota)
        self.pushButton_Habitacion.clicked.connect(self.abrirHabitacion)
        self.pushButton_Sala.clicked.connect(self.abrirSala)
        self.pushButton_Garage.clicked.connect(self.abrirGarage)
        self.pushButton_CerrarSesion.clicked.connect(self.cerrarSesion)  # Conectar el botón de cerrar sesión

        # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc

    def resizeEvent(self, event):
        # imagen de fondo coincida con la prinicipal 
        pixmap = QPixmap("C:\\Users\\emanu\\Desktop\\pruebasp32\\Proyecto esp32\\imag\\Casain.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def abrirCocinota(self):
        self.cocinota_window = CocinotaWindow()
        self.cocinota_window.show()
        self.hide()  # Ocultar la ventana de Menú

    def abrirHabitacion(self):
        self.Habitacion_window = HabitacionWindow()
        self.Habitacion_window.show()
        self.hide()  # Ocultar la ventana de Menú

    def abrirSala(self):
        self.Sala_window = SalaWindow()
        self.Sala_window.show()
        self.hide()  # Ocultar la ventana de Menú

    def abrirGarage(self):
        self.Garage_window = GarageWindow()
        self.Garage_window.show()
        self.hide()  # Ocultar la ventana de Menú

    def cerrarSesion(self):  # para cerrar sesión
        reply = QMessageBox.question(self, 'Cerrar Sesión', '¿Estás seguro de que quieres cerrar sesión?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            login_window.show()

class CocinotaWindow(QMainWindow, Ui_Cocina):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Conectar la señal clicked del botón pushButton_RegresarC a la función regresarAMenu
        self.pushButton_RegresarC.clicked.connect(self.regresarAMenu)

        self.LedC.clicked.connect(self.encenderLED)
        # Apagar led
        self.LedCapagado.clicked.connect(self.apagarLED)
        self.ServoC.clicked.connect(self.abrirServo)
        self.ServoCCerrar.clicked.connect(self.cerrarServo)


        # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc

    def resizeEvent(self, event):
        # imagen de fondo coincida con la prinicipal 
        pixmap = QPixmap("/home/Emanuel/Desktop/Casa/ProyectoCasa/Proyecto/imag/cocina.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def encenderLED(self):
        # Envía el comando para encender el LED a través del puerto serie
        ser.write(b'1')

    def apagarLED(self):
         # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'2')

    def abrirServo(self):
              # Envía el comando para mover el servo a 90 grados
        ser.write(b'b')

    def cerrarServo(self):
       # Envía el comando para mover el servo a 0 grados
        ser.write(b'a')

    def regresarAMenu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()  # Cierra la ventana actual

class HabitacionWindow(QMainWindow, Ui_Habitacion):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Conectar la señal clicked del botón pushButton_RegresarC a la función regresarAMenu
        self.pushButton_RegresarH.clicked.connect(self.regresarAMenu)

        self.LedH.clicked.connect(self.encenderLED)
        # Apagar led
        self.LedHapagado.clicked.connect(self.apagarLED)

        self.ServoH.clicked.connect(self.abrirServo)
        self.ServoHCerrar.clicked.connect(self.cerrarServo)


          # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc

    def resizeEvent(self, event):
        # imagen de fondo coincida con la prinicipal 
        pixmap = QPixmap("/home/Emanuel/Desktop/Casa/ProyectoCasa/Proyecto/imag/Habitacion.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def encenderLED(self):
        # Envía el comando para encender el LED a través del puerto serie
        ser.write(b'3')

    def apagarLED(self):
        # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'4')

    def abrirServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'c')


    def cerrarServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'd')

    def regresarAMenu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()  # Cierra la ventana actual

class SalaWindow(QMainWindow, Ui_Sala):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Conectar la señal clicked del botón pushButton_RegresarC a la función regresarAMenu
        self.pushButton_RegresarS.clicked.connect(self.regresarAMenu)

          # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc

        self.LedS1.clicked.connect(self.encenderLED)
        self.LedS2.clicked.connect(self.encenderLED2)
        # Apagar led
        self.LedS1apagado.clicked.connect(self.apagarLED)
        self.LedS2apagado.clicked.connect(self.apagarLED2)

        self.ServoS.clicked.connect(self.abrirServo)
        self.ServoSCerrar.clicked.connect(self.cerrarServo)
        

    def resizeEvent(self, event):
        # imagen de fondo coincida con la prinicipal 
        pixmap = QPixmap("/home/Emanuel/Desktop/Casa/ProyectoCasa/Proyecto/imag/sala.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def encenderLED(self):
        # Envía el comando para encender el LED a través del puerto serie
        ser.write(b'5')

    def apagarLED(self):
         # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'6')

    def encenderLED2(self):
        # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'7')


    def apagarLED2(self):
        # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'8')

    def abrirServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'e')


    def cerrarServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'f')


    def regresarAMenu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()  # Cierra la ventana actual

class GarageWindow(QMainWindow, Ui_Garage):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Conectar la señal clicked del botón pushButton_RegresarC a la función regresarAMenu
        self.pushButton_RegresarG.clicked.connect(self.regresarAMenu)

          # Agrega la imagen de fondo
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setScaledContents(True)  # para ajustar imagen a la ventana 
        self.label_background.setGeometry(0, 0, 700, 500)  # Dimencion de la ventana
        self.label_background.lower()  # Imagen de fondo para no tapar botones etc


        self.LedG.clicked.connect(self.encenderLED)
        # Apagar led
        self.LedGapagado.clicked.connect(self.apagarLED)

        self.ServoG.clicked.connect(self.abrirServo)
        self.ServoGCerrar.clicked.connect(self.cerrarServo)

    def resizeEvent(self, event):
        # imagen de fondo coincida con la prinicipal 
        pixmap = QPixmap("/home/Emanuel/Desktop/Casa/ProyectoCasa/Proyecto/imag/garage.jpg")  # Ruta de la imagen de fondo
        self.label_background.setPixmap(pixmap.scaled(self.size()))  # Escala la imagen para que se ajuste al tamaño de la ventana

    def encenderLED(self):
         # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'9')

    def apagarLED(self):
        # Envía el comando para apagar el LED a través del puerto serie
        ser.write(b'0')

    def abrirServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'g')


    def cerrarServo(self):
        # Envía el comando para mover el servo a 0 grados
        ser.write(b'h')


    def regresarAMenu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()  # Cierra la ventana actual

# def set_angle(angle, pwm):
#     duty = angle / 18 + 2  # Calcula el ciclo de trabajo necesario para el ángulo deseado
#     GPIO.output(SERVO_PINC, True)
#     pwm.ChangeDutyCycle(duty)
#     time.sleep(1)  # Ajusta este tiempo según sea necesario para el movimiento completo
#     GPIO.output(SERVO_PINC, False)
#     pwm.ChangeDutyCycle(0)

if __name__ == '__main__':
    app = QApplication([])

    # Crear la ventana de inicio y mostrarla
    login_window = LoginWindow()
    login_window.show()

    # Conectar la señal clicked del botón pushButton_Salir a la función exitApp
    login_window.pushButton_Salir.clicked.connect(app.quit)

    sys.exit(app.exec())
