# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Citas.ui'
#
# Created: Sat Jul 12 16:44:30 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Citas_Window(object):
    def setupUi(self, Citas_Window):
        Citas_Window.setObjectName("Citas_Window")
        Citas_Window.resize(514, 491)
        self.centralwidget = QtGui.QWidget(Citas_Window)
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
        self.tblview_citas = QtGui.QTableView(self.centralwidget)
        self.tblview_citas.setMaximumSize(QtCore.QSize(565, 440))
        self.tblview_citas.setObjectName("tblview_citas")
        self.gridLayout_2.addWidget(self.tblview_citas, 1, 0, 1, 1)
        Citas_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Citas_Window)
        self.statusbar.setObjectName("statusbar")
        Citas_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Citas_Window)
        QtCore.QMetaObject.connectSlotsByName(Citas_Window)

    def retranslateUi(self, Citas_Window):
        Citas_Window.setWindowTitle(QtGui.QApplication.translate("Citas_Window", "Citas", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Citas_Window", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_registrar.setText(QtGui.QApplication.translate("Citas_Window", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Citas_Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Citas_Window", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

