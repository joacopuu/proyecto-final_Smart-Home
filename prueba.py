# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Smart_HomekkpqJG.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 50, 501, 80))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 15, 81, 31))
        self.lcd_temperatura = QLCDNumber(self.groupBox)
        self.lcd_temperatura.setObjectName(u"lcd_temperatura")
        self.lcd_temperatura.setGeometry(QRect(10, 40, 91, 31))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 20, 81, 31))
        self.label_ciclo = QLabel(self.groupBox)
        self.label_ciclo.setObjectName(u"label_ciclo")
        self.label_ciclo.setEnabled(True)
        self.label_ciclo.setGeometry(QRect(180, 40, 81, 31))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 20, 81, 31))
        self.label_alarma_estado = QLabel(self.groupBox)
        self.label_alarma_estado.setObjectName(u"label_alarma_estado")
        self.label_alarma_estado.setGeometry(QRect(370, 40, 81, 31))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(100, 140, 501, 331))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 20, 91, 31))
        self.btn_luces_on = QPushButton(self.groupBox_2)
        self.btn_luces_on.setObjectName(u"btn_luces_on")
        self.btn_luces_on.setGeometry(QRect(20, 70, 101, 101))
        self.btn_luces_off = QPushButton(self.groupBox_2)
        self.btn_luces_off.setObjectName(u"btn_luces_off")
        self.btn_luces_off.setGeometry(QRect(130, 70, 101, 101))
        self.label_luces_estado = QLabel(self.groupBox_2)
        self.label_luces_estado.setObjectName(u"label_luces_estado")
        self.label_luces_estado.setGeometry(QRect(90, 40, 91, 31))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 20, 71, 31))
        self.label_vent_estado = QLabel(self.groupBox_2)
        self.label_vent_estado.setObjectName(u"label_vent_estado")
        self.label_vent_estado.setGeometry(QRect(350, 40, 91, 31))
        self.btn_vent_on = QPushButton(self.groupBox_2)
        self.btn_vent_on.setObjectName(u"btn_vent_on")
        self.btn_vent_on.setGeometry(QRect(280, 70, 101, 101))
        self.btn_vent_off = QPushButton(self.groupBox_2)
        self.btn_vent_off.setObjectName(u"btn_vent_off")
        self.btn_vent_off.setGeometry(QRect(390, 70, 101, 101))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 180, 81, 31))
        self.btn_alarma_on = QPushButton(self.groupBox_2)
        self.btn_alarma_on.setObjectName(u"btn_alarma_on")
        self.btn_alarma_on.setGeometry(QRect(140, 210, 101, 101))
        self.btn_alarma_off = QPushButton(self.groupBox_2)
        self.btn_alarma_off.setObjectName(u"btn_alarma_off")
        self.btn_alarma_off.setGeometry(QRect(260, 210, 101, 101))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuSmart_Home = QMenu(self.menubar)
        self.menuSmart_Home.setObjectName(u"menuSmart_Home")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSmart_Home.menuAction())

        self.retranslateUi(MainWindow)
        self.btn_luces_on.clicked.connect(MainWindow.prender_luz)
        self.btn_luces_off.clicked.connect(MainWindow.apagar_luz)
        self.btn_vent_on.clicked.connect(MainWindow.prender_vent)
        self.btn_vent_off.clicked.connect(MainWindow.apagar_vent)
        self.btn_alarma_on.clicked.connect(MainWindow.prender_alarma)
        self.btn_alarma_off.clicked.connect(MainWindow.apagar_vent)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Monitoreo en Tiempo Real", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ciclo Diurno", None))
        self.label_ciclo.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Alarma:", None))
        self.label_alarma_estado.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Controles Manuales", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Luces de la Casa", None))
        self.btn_luces_on.setText(QCoreApplication.translate("MainWindow", u"Prender", None))
        self.btn_luces_off.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label_luces_estado.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ventiladores", None))
        self.label_vent_estado.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.btn_vent_on.setText(QCoreApplication.translate("MainWindow", u"Prender", None))
        self.btn_vent_off.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Alarma (Casa)", None))
        self.btn_alarma_on.setText(QCoreApplication.translate("MainWindow", u"Prender", None))
        self.btn_alarma_off.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.menuSmart_Home.setTitle(QCoreApplication.translate("MainWindow", u"Smart Home", None))
    # retranslateUi

