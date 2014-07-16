# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created: Wed Jul 16 10:28:41 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 228)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 140, 211, 51))
        self.widget.setObjectName("widget")
        self.btn_aceptar = QtGui.QPushButton(self.widget)
        self.btn_aceptar.setGeometry(QtCore.QRect(10, 10, 81, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_cancelar = QtGui.QPushButton(self.widget)
        self.btn_cancelar.setGeometry(QtCore.QRect(120, 10, 81, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(40, 30, 331, 101))
        self.widget_2.setObjectName("widget_2")
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 71, 17))
        self.label.setObjectName("label")
        self.ledit_contrasenia = QtGui.QLineEdit(self.widget_2)
        self.ledit_contrasenia.setGeometry(QtCore.QRect(120, 60, 181, 27))
        self.ledit_contrasenia.setObjectName("ledit_contrasenia")
        self.ledit_usuario = QtGui.QLineEdit(self.widget_2)
        self.ledit_usuario.setGeometry(QtCore.QRect(120, 10, 181, 27))
        self.ledit_usuario.setObjectName("ledit_usuario")
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 81, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Login Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("MainWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("MainWindow", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))

