# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro_Paciente.ui'
#
# Created: Wed Jul 16 04:35:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Registro_Paciente_Window(object):
    def setupUi(self, Registro_Paciente_Window):
        Registro_Paciente_Window.setObjectName("Registro_Paciente_Window")
        Registro_Paciente_Window.resize(347, 349)
        self.centralwidget = QtGui.QWidget(Registro_Paciente_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtGui.QLabel(self.centralwidget)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_1 = QtGui.QLabel(self.widget_2)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 0, 0, 1, 1)
        self.ledit_apellidos = QtGui.QLineEdit(self.widget_2)
        self.ledit_apellidos.setObjectName("ledit_apellidos")
        self.gridLayout.addWidget(self.ledit_apellidos, 2, 1, 1, 1)
        self.ledit_rut = QtGui.QLineEdit(self.widget_2)
        self.ledit_rut.setObjectName("ledit_rut")
        self.gridLayout.addWidget(self.ledit_rut, 0, 1, 1, 1)
        self.ledit_nombres = QtGui.QLineEdit(self.widget_2)
        self.ledit_nombres.setObjectName("ledit_nombres")
        self.gridLayout.addWidget(self.ledit_nombres, 1, 1, 1, 1)
        self.ledit_ficha_medica = QtGui.QLineEdit(self.widget_2)
        self.ledit_ficha_medica.setObjectName("ledit_ficha_medica")
        self.gridLayout.addWidget(self.ledit_ficha_medica, 3, 1, 1, 1)
        self.lbl_4 = QtGui.QLabel(self.widget_2)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 3, 0, 1, 1)
        self.lbl_3 = QtGui.QLabel(self.widget_2)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 2, 0, 1, 1)
        self.lbl_2 = QtGui.QLabel(self.widget_2)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_ingresar = QtGui.QPushButton(self.widget)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.horizontalLayout.addWidget(self.btn_ingresar)
        self.btn_cancelar = QtGui.QPushButton(self.widget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.verticalLayout.addWidget(self.widget)
        Registro_Paciente_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Registro_Paciente_Window)
        self.statusbar.setObjectName("statusbar")
        Registro_Paciente_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Registro_Paciente_Window)
        QtCore.QMetaObject.connectSlotsByName(Registro_Paciente_Window)

    def retranslateUi(self, Registro_Paciente_Window):
        Registro_Paciente_Window.setWindowTitle(QtGui.QApplication.translate("Registro_Paciente_Window", "Registrar Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Ingresar Datos en cada campo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_1.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Rut      ", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_4.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Ficha Medica", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_3.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_2.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Registro_Paciente_Window", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

