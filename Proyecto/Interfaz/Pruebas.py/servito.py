from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from pathlib import Path


class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio")
        self.resize(700, 500)
        self.setMinimumSize(700, 500)
        self.setMaximumSize(700, 500)
        self.setStyleSheet("background-color: white;")

        self.label = QLabel("TechGuardian Homes", self)
        self.label.setGeometry(170, -40, 401, 161)
        self.label.setFont(QFont("Arial", 36, QFont.Bold))
        self.label.setStyleSheet("color: black;")

        self.label_user = QLabel("Usuario:", self)
        self.label_user.setGeometry(150, 150, 91, 41)
        self.label_user.setFont(QFont("Arial", 16))
        self.label_user.setStyleSheet("color: black;")

        self.label_password = QLabel("Contraseña:", self)
        self.label_password.setGeometry(110, 190, 131, 51)
        self.label_password.setFont(QFont("Arial", 16))
        self.label_password.setStyleSheet("color: black;")

        self.lineEdit_user = QLineEdit(self)
        self.lineEdit_user.setGeometry(250, 160, 241, 21)
        self.lineEdit_user.setStyleSheet("border-radius: 10px; background-color: rgb(97, 97, 97);")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(250, 200, 241, 21)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setStyleSheet("border-radius: 10px; background-color: rgb(97, 97, 97);")

        self.pushButton_login = QPushButton("Ingresar", self)
        self.pushButton_login.setGeometry(310, 260, 121, 30)
        self.pushButton_login.setStyleSheet("border-radius: 10px; background-color: rgb(132, 132, 132);")
        self.pushButton_login.clicked.connect(self.login)

        self.pushButton_exit = QPushButton("Salir", self)
        self.pushButton_exit.setGeometry(570, 380, 121, 30)
        self.pushButton_exit.setStyleSheet("border-radius: 10px; background-color: rgb(132, 132, 132);")
        self.pushButton_exit.clicked.connect(self.close)

    def login(self):
        username = self.lineEdit_user.text()
        password = self.lineEdit_password.text()

        # Aquí debes verificar si el nombre de usuario y la contraseña son válidos.
        # Por ejemplo, puedes tener una base de datos de usuarios y verificar las credenciales allí.
        # Por ahora, solo mostraré un mensaje de éxito o error.
        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso!")
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Nombre de usuario o contraseña incorrectos.")


if __name__ == '__main__':
    app = QApplication([])
    window = Inicio()
    window.show()
    app.exec()
