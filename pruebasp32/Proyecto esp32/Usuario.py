# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana1JOGTkG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	\n"
"	\n"
"	border-image: url(:/casa/casa real.jpg);\n"
";}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, -40, 401, 161))
        self.label.setStyleSheet(u"font: 57 italic 36pt \"Z003 [urw]\";\n"
"color: black;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 70, 251, 51))
        self.label_2.setStyleSheet(u"\n"
"font: 63 italic 20pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 150, 91, 41))
        self.label_3.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 190, 131, 51))
        self.label_4.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.UsuarioI = QLineEdit(self.centralwidget)
        self.UsuarioI.setObjectName(u"UsuarioI")
        self.UsuarioI.setGeometry(QRect(250, 160, 241, 21))
        self.UsuarioI.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"background-color: rgb(97, 97, 97);")
        self.IniciarS = QPushButton(self.centralwidget)
        self.IniciarS.setObjectName(u"IniciarS")
        self.IniciarS.setGeometry(QRect(310, 260, 121, 30))
        self.IniciarS.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 230, 231, 22))
        self.label_5.setStyleSheet(u"font: 11pt \"PibotoLt\";\n"
"color: red;")
        self.Contraseña = QLineEdit(self.centralwidget)
        self.Contraseña.setObjectName(u"Contraseña")
        self.Contraseña.setGeometry(QRect(250, 200, 241, 21))
        self.Contraseña.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"background-color: rgb(97, 97, 97);")
        self.pushButton_Salir = QPushButton(self.centralwidget)
        self.pushButton_Salir.setObjectName(u"pushButton_Salir")
        self.pushButton_Salir.setGeometry(QRect(570, 380, 121, 30))
        self.pushButton_Salir.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\"TechGuardian Homes\"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese su Usuario ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Usuario:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Contrase\u00f1a:</p></body></html>", None))
        self.IniciarS.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label_5.setText("")
        self.pushButton_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

