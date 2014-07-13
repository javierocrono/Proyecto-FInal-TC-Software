# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Medicos.ui'
#
# Created: Sat Jul 12 16:44:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Medicos_Window(object):
    def setupUi(self, Medicos_Window):
        Medicos_Window.setObjectName("Medicos_Window")
        Medicos_Window.resize(514, 491)
        self.centralwidget = QtGui.QWidget(Medicos_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ledit_buscar = QtGui.QLineEdit(self.widget_2)
        self.ledit_buscar.setObjectName("ledit_buscar")
        self.horizontalLayout.addWidget(self.ledit_buscar)
        self.btn_buscar = QtGui.QPushButton(self.widget_2)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(90, 400))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_registrar = QtGui.QPushButton(self.widget)
        self.btn_registrar.setObjectName("btn_registrar")
        self.gridLayout.addWidget(self.btn_registrar, 0, 0, 1, 1)
        self.btn_editar = QtGui.QPushButton(self.widget)
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 1, 0, 1, 1)
        self.btn_eliminar = QtGui.QPushButton(self.widget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)
        self.tblview_medicos = QtGui.QTableView(self.centralwidget)
        self.tblview_medicos.setMaximumSize(QtCore.QSize(565, 440))
        self.tblview_medicos.setObjectName("tblview_medicos")
        self.gridLayout_2.addWidget(self.tblview_medicos, 1, 0, 1, 1)
        Medicos_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Medicos_Window)
        self.statusbar.setObjectName("statusbar")
        Medicos_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Medicos_Window)
        QtCore.QMetaObject.connectSlotsByName(Medicos_Window)

    def retranslateUi(self, Medicos_Window):
        Medicos_Window.setWindowTitle(QtGui.QApplication.translate("Medicos_Window", "Medicos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Medicos_Window", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_registrar.setText(QtGui.QApplication.translate("Medicos_Window", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Medicos_Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Medicos_Window", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

