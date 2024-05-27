# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuMbbiyg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_Menu(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	\n"
"	\n"
"	border-image: url(:/casa/Casain.jpg);\n"
"	\n"
"	\n"
"\n"
";}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 221, 41))
        self.label.setStyleSheet(u"font: 57 italic 20pt \"Z003 [urw]\";\n"
"color: white;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 0, 251, 51))
        self.label_2.setStyleSheet(u"\n"
"font: 63 italic 20pt \"URW Bookman [UKWN]\";\n"
"color: white;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 230, 231, 22))
        self.label_5.setStyleSheet(u"font: 11pt \"PibotoLt\";\n"
"color: red;")
        self.pushButton_CerrarSesion = QPushButton(self.centralwidget)
        self.pushButton_CerrarSesion.setObjectName(u"pushButton_CerrarSesion")
        self.pushButton_CerrarSesion.setGeometry(QRect(560, 390, 121, 30))
        self.pushButton_CerrarSesion.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.pushButton_Cocina = QPushButton(self.centralwidget)
        self.pushButton_Cocina.setObjectName(u"pushButton_Cocina")
        self.pushButton_Cocina.setGeometry(QRect(170, 80, 311, 61))
        self.pushButton_Cocina.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.616071 rgba(19, 237, 255, 255), stop:0.834821 rgba(255, 255, 203, 255), stop:1 rgba(87, 87, 87, 255));\n"
"\n"
"\n"
"font: 63 italic 36pt \"URW Bookman [UKWN]\";\n"
"color: black")
        self.pushButton_Habitacion = QPushButton(self.centralwidget)
        self.pushButton_Habitacion.setObjectName(u"pushButton_Habitacion")
        self.pushButton_Habitacion.setGeometry(QRect(170, 170, 311, 61))
        self.pushButton_Habitacion.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.383929 rgba(19, 251, 255, 255), stop:0.834821 rgba(255, 255, 203, 255), stop:1 rgba(87, 87, 87, 255));\n"
"\n"
"\n"
"font: 63 italic 36pt \"URW Bookman [UKWN]\";\n"
"color: black")
        self.pushButton_Garage = QPushButton(self.centralwidget)
        self.pushButton_Garage.setObjectName(u"pushButton_Garage")
        self.pushButton_Garage.setGeometry(QRect(170, 340, 311, 61))
        self.pushButton_Garage.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.383929 rgba(19, 251, 255, 255), stop:0.834821 rgba(255, 255, 203, 255), stop:1 rgba(87, 87, 87, 255));\n"
"\n"
"\n"
"font: 63 italic 36pt \"URW Bookman [UKWN]\";\n"
"color: black")
        self.pushButton_Sala = QPushButton(self.centralwidget)
        self.pushButton_Sala.setObjectName(u"pushButton_Sala")
        self.pushButton_Sala.setGeometry(QRect(170, 250, 311, 61))
        self.pushButton_Sala.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.383929 rgba(19, 251, 255, 255), stop:0.834821 rgba(255, 255, 203, 255), stop:1 rgba(87, 87, 87, 255));\n"
"\n"
"\n"
"font: 63 italic 36pt \"URW Bookman [UKWN]\";\n"
"color: black")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/casa/casa real.jpg\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\"TechGuardian Homes\"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu de inicio", None))
        self.label_5.setText("")
        self.pushButton_CerrarSesion.setText(QCoreApplication.translate("MainWindow", u"cerrar sesion", None))
        self.pushButton_Cocina.setText(QCoreApplication.translate("MainWindow", u"Cocina", None))
        self.pushButton_Habitacion.setText(QCoreApplication.translate("MainWindow", u"Habitaci\u00f3n", None))
        self.pushButton_Garage.setText(QCoreApplication.translate("MainWindow", u"Garage", None))
        self.pushButton_Sala.setText(QCoreApplication.translate("MainWindow", u"Sala", None))
    # retranslateUi

