# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created: Sat Jul 12 16:45:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Inicio_Window(object):
    def setupUi(self, Inicio_Window):
        Inicio_Window.setObjectName("Inicio_Window")
        Inicio_Window.resize(376, 333)
        self.centralwidget = QtGui.QWidget(Inicio_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl = QtGui.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(60, 30, 271, 17))
        self.lbl.setObjectName("lbl")
        self.btn_pacientes = QtGui.QPushButton(self.centralwidget)
        self.btn_pacientes.setGeometry(QtCore.QRect(130, 90, 98, 27))
        self.btn_pacientes.setObjectName("btn_pacientes")
        self.btn_medicos = QtGui.QPushButton(self.centralwidget)
        self.btn_medicos.setGeometry(QtCore.QRect(130, 160, 98, 27))
        self.btn_medicos.setObjectName("btn_medicos")
        self.btn_citas = QtGui.QPushButton(self.centralwidget)
        self.btn_citas.setGeometry(QtCore.QRect(130, 230, 98, 27))
        self.btn_citas.setObjectName("btn_citas")
        Inicio_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Inicio_Window)
        self.statusbar.setObjectName("statusbar")
        Inicio_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Inicio_Window)
        QtCore.QMetaObject.connectSlotsByName(Inicio_Window)

    def retranslateUi(self, Inicio_Window):
        Inicio_Window.setWindowTitle(QtGui.QApplication.translate("Inicio_Window", "Administracion de Pacientes App", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("Inicio_Window", "Sistema de Administracion de Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_pacientes.setText(QtGui.QApplication.translate("Inicio_Window", "Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_medicos.setText(QtGui.QApplication.translate("Inicio_Window", "Medicos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_citas.setText(QtGui.QApplication.translate("Inicio_Window", "Citas", None, QtGui.QApplication.UnicodeUTF8))

