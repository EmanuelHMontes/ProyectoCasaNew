from Habitacion import Ui_Habitacion

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from pathlib import Path
from PyQt5.QtGui import QFont, QPixmap 

class Inicio(QMainWindow, Ui_Habitacion):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inicio()
    window.show();
    sys.exit(app.exec())