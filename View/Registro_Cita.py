# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro_Cita.ui'
#
# Created: Sat Jul 12 16:44:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Registrar_CIta_Window(object):
    def setupUi(self, Registrar_CIta_Window):
        Registrar_CIta_Window.setObjectName("Registrar_CIta_Window")
        Registrar_CIta_Window.resize(279, 357)
        self.centralwidget = QtGui.QWidget(Registrar_CIta_Window)
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
        self.ledit_rutpaciente = QtGui.QLineEdit(self.widget_2)
        self.ledit_rutpaciente.setObjectName("ledit_rutpaciente")
        self.gridLayout.addWidget(self.ledit_rutpaciente, 0, 1, 1, 1)
        self.lbl_2 = QtGui.QLabel(self.widget_2)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 1, 0, 1, 1)
        self.ledit_rutmedico = QtGui.QLineEdit(self.widget_2)
        self.ledit_rutmedico.setObjectName("ledit_rutmedico")
        self.gridLayout.addWidget(self.ledit_rutmedico, 1, 1, 1, 1)
        self.lbl_3 = QtGui.QLabel(self.widget_2)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 2, 0, 1, 1)
        self.ledit_fecha = QtGui.QLineEdit(self.widget_2)
        self.ledit_fecha.setObjectName("ledit_fecha")
        self.gridLayout.addWidget(self.ledit_fecha, 2, 1, 1, 1)
        self.lbl_4 = QtGui.QLabel(self.widget_2)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 3, 0, 1, 1)
        self.ledit_sintomas = QtGui.QLineEdit(self.widget_2)
        self.ledit_sintomas.setObjectName("ledit_sintomas")
        self.gridLayout.addWidget(self.ledit_sintomas, 3, 1, 1, 1)
        self.lbl_5 = QtGui.QLabel(self.widget_2)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 4, 0, 1, 1)
        self.ledit_diagnostico = QtGui.QLineEdit(self.widget_2)
        self.ledit_diagnostico.setObjectName("ledit_diagnostico")
        self.gridLayout.addWidget(self.ledit_diagnostico, 4, 1, 1, 1)
        self.lbl_6 = QtGui.QLabel(self.widget_2)
        self.lbl_6.setObjectName("lbl_6")
        self.gridLayout.addWidget(self.lbl_6, 5, 0, 1, 1)
        self.ledit_recomendaciones = QtGui.QLineEdit(self.widget_2)
        self.ledit_recomendaciones.setObjectName("ledit_recomendaciones")
        self.gridLayout.addWidget(self.ledit_recomendaciones, 5, 1, 1, 1)
        self.lbl_7 = QtGui.QLabel(self.widget_2)
        self.lbl_7.setObjectName("lbl_7")
        self.gridLayout.addWidget(self.lbl_7, 6, 0, 1, 1)
        self.ledit_receta = QtGui.QLineEdit(self.widget_2)
        self.ledit_receta.setObjectName("ledit_receta")
        self.gridLayout.addWidget(self.ledit_receta, 6, 1, 1, 1)
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
        Registrar_CIta_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Registrar_CIta_Window)
        self.statusbar.setObjectName("statusbar")
        Registrar_CIta_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Registrar_CIta_Window)
        QtCore.QMetaObject.connectSlotsByName(Registrar_CIta_Window)

    def retranslateUi(self, Registrar_CIta_Window):
        Registrar_CIta_Window.setWindowTitle(QtGui.QApplication.translate("Registrar_CIta_Window", "Registrar Cita", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Ingresar Datos en cada campo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_1.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Rut Paciente   ", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_2.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Rut Medico", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_3.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_4.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Sintomas", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_5.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Diagnostico", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_6.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Recomendaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_7.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Receta", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Registrar_CIta_Window", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

