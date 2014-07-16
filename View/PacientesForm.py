# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PacientesForm.ui'
#
# Created: Wed Jul 16 04:41:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PacientesForm(object):
    def setupUi(self, PacientesForm):
        PacientesForm.setObjectName("PacientesForm")
        PacientesForm.resize(527, 491)
        self.widget = QtGui.QWidget(PacientesForm)
        self.widget.setGeometry(QtCore.QRect(420, 71, 90, 400))
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
        self.tblview_pacientes = QtGui.QTableView(PacientesForm)
        self.tblview_pacientes.setGeometry(QtCore.QRect(14, 71, 400, 400))
        self.tblview_pacientes.setMaximumSize(QtCore.QSize(565, 440))
        self.tblview_pacientes.setObjectName("tblview_pacientes")
        self.widget_2 = QtGui.QWidget(PacientesForm)
        self.widget_2.setGeometry(QtCore.QRect(14, 20, 400, 45))
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

        self.retranslateUi(PacientesForm)
        QtCore.QMetaObject.connectSlotsByName(PacientesForm)

    def retranslateUi(self, PacientesForm):
        PacientesForm.setWindowTitle(QtGui.QApplication.translate("PacientesForm", "Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_registrar.setText(QtGui.QApplication.translate("PacientesForm", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("PacientesForm", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("PacientesForm", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("PacientesForm", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

