# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CitasForm.ui'
#
# Created: Wed Jul 16 04:49:00 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CitasForm(object):
    def setupUi(self, CitasForm):
        CitasForm.setObjectName("CitasForm")
        CitasForm.resize(531, 482)
        self.widget = QtGui.QWidget(CitasForm)
        self.widget.setGeometry(QtCore.QRect(426, 60, 90, 400))
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
        self.widget_2 = QtGui.QWidget(CitasForm)
        self.widget_2.setGeometry(QtCore.QRect(20, 9, 400, 45))
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
        self.tblview_citas = QtGui.QTableView(CitasForm)
        self.tblview_citas.setGeometry(QtCore.QRect(20, 60, 400, 400))
        self.tblview_citas.setMaximumSize(QtCore.QSize(565, 440))
        self.tblview_citas.setObjectName("tblview_citas")

        self.retranslateUi(CitasForm)
        QtCore.QMetaObject.connectSlotsByName(CitasForm)

    def retranslateUi(self, CitasForm):
        CitasForm.setWindowTitle(QtGui.QApplication.translate("CitasForm", "Citas", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_registrar.setText(QtGui.QApplication.translate("CitasForm", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("CitasForm", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("CitasForm", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("CitasForm", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

