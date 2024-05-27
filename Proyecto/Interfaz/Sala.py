# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalaVgyVzHr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_Sala(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	\n"
"	border-image: url(:/casa/sala.jpg);\n"
"	\n"
"\n"
"	\n"
"	\n"
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
"color: black;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 0, 251, 51))
        self.label_2.setStyleSheet(u"\n"
"font: 63 italic 20pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 100, 151, 41))
        self.label_3.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.LedS1 = QPushButton(self.centralwidget)
        self.LedS1.setObjectName(u"LedS1")
        self.LedS1.setGeometry(QRect(80, 170, 121, 30))
        self.LedS1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.LedS1apagado = QPushButton(self.centralwidget)
        self.LedS1apagado.setObjectName(u"LedS1apagado")
        self.LedS1apagado.setGeometry(QRect(80, 240, 121, 30))
        self.LedS1apagado.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.pushButton_RegresarS = QPushButton(self.centralwidget)
        self.pushButton_RegresarS.setObjectName(u"pushButton_RegresarS")
        self.pushButton_RegresarS.setGeometry(QRect(560, 390, 121, 30))
        self.pushButton_RegresarS.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 110, 211, 41))
        self.label_4.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.ServoS = QPushButton(self.centralwidget)
        self.ServoS.setObjectName(u"ServoS")
        self.ServoS.setGeometry(QRect(480, 160, 121, 30))
        self.ServoS.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.ServoSCerrar = QPushButton(self.centralwidget)
        self.ServoSCerrar.setObjectName(u"ServoSCerrar")
        self.ServoSCerrar.setGeometry(QRect(480, 220, 121, 30))
        self.ServoSCerrar.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 90, 151, 41))
        self.label_6.setStyleSheet(u"\n"
"font: 63 italic 16pt \"URW Bookman [UKWN]\";\n"
"color: black;")
        self.LedS2 = QPushButton(self.centralwidget)
        self.LedS2.setObjectName(u"LedS2")
        self.LedS2.setGeometry(QRect(290, 150, 121, 30))
        self.LedS2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(132, 132, 132);\n"
"\n"
"")
        self.LedS2apagado = QPushButton(self.centralwidget)
        self.LedS2apagado.setObjectName(u"LedS2apagado")
        self.LedS2apagado.setGeometry(QRect(290, 210, 121, 30))
        self.LedS2apagado.setStyleSheet(u"border-radius: 10px;\n"
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sala de espera", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Foco 1 sala</p><p align=\"center\"><br/></p></body></html>", None))
        self.LedS1.setText(QCoreApplication.translate("MainWindow", u"Encender", None))
        self.LedS1apagado.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.pushButton_RegresarS.setText(QCoreApplication.translate("MainWindow", u"regresar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Puerta principal</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.ServoS.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.ServoSCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Foco 2 sala</p><p align=\"center\"><br/></p></body></html>", None))
        self.LedS2.setText(QCoreApplication.translate("MainWindow", u"Encender", None))
        self.LedS2apagado.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
    # retranslateUi

