#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from PacientesForm import Ui_PacientesForm
import RegisPaciente
import Controller

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QWidget):

    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_PacientesForm()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.registrar)
        self.ui.btn_editar.clicked.connect(self.editar)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.renderizaTabla()
        #self.load()
        self.centrar()
        self.show()

    def editar(self):
        app = RegisPaciente.Principal()
        app.setWindowTitle("Editar Paciente")
        sys.exit(app.exec_())

    def registrar(self):
        app = RegisPaciente.Principal()
        sys.exit(app.exec_())

    def eliminar(self):
        pass

    def renderizaTabla(self):
        self.table = self.ui.tblview_pacientes
        self.table.setFixedWidth(400)
        self.table.setFixedHeight(340)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.main_layout.addWidget(self.table)

    def load(self):
            # metodo para cargar la grilla con los pacientes
            pacientes = Controller.pacientes()
            self.model = QtGui.QStandardItemModel(len(pacientes), 4)
            self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
            self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
            self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellidos"))
            self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Especialidad"))
            r = 0
            for row in pacientes:
                index = self.model.index(r, 0, QtCore.QModelIndex())
                self.model.setData(index, row['Rut'])
                index = self.model.index(r, 1, QtCore.QModelIndex())
                self.model.setData(index, row['Nombres'])
                index = self.model.index(r, 2, QtCore.QModelIndex())
                self.model.setData(index, row['Apellidos'])
                index = self.model.index(r, 3, QtCore.QModelIndex())
                self.model.setData(index, row['Especialidad'])
                r = r + 1
            self.table.setModel(self.model)

    def centrar(self):
            """Centra la ventana actual."""
            qr = self.frameGeometry()
            cp = QtGui.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())


def run():

    app = QtGui.QApplication(sys.argv)
    form = Principal()
    form.show()
    app.exec_()

if __name__ == '__main__':

    run()