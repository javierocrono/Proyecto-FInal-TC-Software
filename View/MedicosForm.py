# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MedicosForm.ui'
#
# Created: Tue Jul 15 22:44:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MedicosForm(object):
    def setupUi(self, MedicosForm):
        MedicosForm.setObjectName("MedicosForm")
        MedicosForm.resize(531, 482)
        self.tblview_medicos = QtGui.QTableView(MedicosForm)
        self.tblview_medicos.setGeometry(QtCore.QRect(20, 61, 400, 400))
        self.tblview_medicos.setMaximumSize(QtCore.QSize(565, 440))
        self.tblview_medicos.setObjectName("tblview_medicos")
        self.widget_2 = QtGui.QWidget(MedicosForm)
        self.widget_2.setGeometry(QtCore.QRect(20, 10, 400, 45))
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
        self.widget = QtGui.QWidget(MedicosForm)
        self.widget.setGeometry(QtCore.QRect(426, 61, 90, 400))
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

        self.retranslateUi(MedicosForm)
        QtCore.QMetaObject.connectSlotsByName(MedicosForm)

    def retranslateUi(self, MedicosForm):
        MedicosForm.setWindowTitle(QtGui.QApplication.translate("MedicosForm", "Medicos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("MedicosForm", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_registrar.setText(QtGui.QApplication.translate("MedicosForm", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("MedicosForm", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("MedicosForm", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

