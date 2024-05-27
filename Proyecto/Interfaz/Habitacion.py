# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HabitacionUnvYqt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore



class Ui_Habitacion(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	border-image: url(:/casa/Habitacion.jpg);\n"
"	\n"
"\n"
";}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 221, 41))
        self.label.setStyleSheet(u"font: 57 italic 20pt \"Z003 [urw]\";\n"
"color: black;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 0, 251, 51))
        self.label_2.setStyleSheet(u"\n"
"font: 63 italic 20pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 150, 161, 41))
        self.label_3.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.LedH = QPushButton(self.centralwidget)
        self.LedH.setObjectName(u"LedH")
        self.LedH.setGeometry(QRect(50, 180, 121, 30))
        self.LedH.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 230, 231, 22))
        self.label_5.setStyleSheet(u"font: 11pt \"PibotoLt\";\n"
"color: red;")
        self.LedHapagado = QPushButton(self.centralwidget)
        self.LedHapagado.setObjectName(u"LedHapagado")
        self.LedHapagado.setGeometry(QRect(50, 220, 121, 30))
        self.LedHapagado.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.pushButton_RegresarH = QPushButton(self.centralwidget)
        self.pushButton_RegresarH.setObjectName(u"pushButton_RegresarH")
        self.pushButton_RegresarH.setGeometry(QRect(560, 390, 121, 30))
        self.pushButton_RegresarH.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 130, 211, 41))
        self.label_4.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.ServoH = QPushButton(self.centralwidget)
        self.ServoH.setObjectName(u"ServoH")
        self.ServoH.setGeometry(QRect(500, 180, 121, 30))
        self.ServoH.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.ServoHCerrar = QPushButton(self.centralwidget)
        self.ServoHCerrar.setObjectName(u"ServoHCerrar")
        self.ServoHCerrar.setGeometry(QRect(500, 230, 121, 30))
        self.ServoHCerrar.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Habitacion", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Foco Habitacion</p><p align=\"center\"><br/></p></body></html>", None))
        self.LedH.setText(QCoreApplication.translate("MainWindow", u"Encender", None))
        self.label_5.setText("")
        self.LedHapagado.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.pushButton_RegresarH.setText(QCoreApplication.translate("MainWindow", u"regresar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Puerta Habitacion</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.ServoH.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.ServoHCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
    # retranslateUi

