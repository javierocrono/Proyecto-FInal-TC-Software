#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from CitasForm import Ui_CitasForm
import RegisCita
import Controller

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QWidget):

    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_CitasForm()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.registrar)
        self.ui.btn_editar.clicked.connect(self.editar)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.renderizaTabla()
        self.load()
        self.centrar()
        self.show()

    def editar(self):
        app = RegisCita.Principal()
        app.setWindowTitle("Editar Cita")
        sys.exit(app.exec_())

    def registrar(self):
        app = RegisCita.Principal()
        sys.exit(app.exec_())

    def eliminar(self):
        pass

    def renderizaTabla(self):
        self.table = self.ui.tblview_citas
        self.table.setFixedWidth(400)
        self.table.setFixedHeight(340)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.main_layout.addWidget(self.table)

    def load(self):
            # metodo para cargar la grilla con las citas
            citas = Controller.citas()
            self.model = QtGui.QStandardItemModel(len(citas), 4)
            self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Fecha"))
            self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Sintomas"))
            self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Diagnostico"))
            self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Recomendaciones"))
            self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Receta"))
            self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Rut Paciente"))
            self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Rut Medico"))
            r = 0
            for row in citas:
                index = self.model.index(r, 0, QtCore.QModelIndex())
                self.model.setData(index, row['Fecha'])
                index = self.model.index(r, 1, QtCore.QModelIndex())
                self.model.setData(index, row['Sintomas'])
                index = self.model.index(r, 2, QtCore.QModelIndex())
                self.model.setData(index, row['Diagnostico'])
                index = self.model.index(r, 3, QtCore.QModelIndex())
                self.model.setData(index, row['Recomendaciones'])
                index = self.model.index(r, 4, QtCore.QModelIndex())
                self.model.setData(index, row['Receta'])
                index = self.model.index(r, 5, QtCore.QModelIndex())
                self.model.setData(index, row['fk_rut_paciente'])
                index = self.model.index(r, 6, QtCore.QModelIndex())
                self.model.setData(index, row['fk_rut_medico'])

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