#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from MedicosForm import Ui_MedicosForm
import RegisMedico
import Controller

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QWidget, Ui_MedicosForm):

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.ui = Ui_MedicosForm()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.registrar)
        self.ui.btn_editar.clicked.connect(self.editar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_refrescar.clicked.connect(self.load)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.renderizaTabla()
        self.load()
        self.centrar()
        self.show()

    def editar(self):
        index = self.ui.tblview_medicos.currentIndex()  # obtiene la fila
                                                        #seleccionada
        if index.row() == -1:
            mensaje = "Seleccione un Medico para Editar"
            errorQMessageBox = QtGui.QMessageBox()
            errorQMessageBox.setWindowTitle("Error")
            errorQMessageBox.setText(mensaje)
            errorQMessageBox.exec_()
        else:
            medico = list()
            model = self.ui.tblview_medicos.model()
            medico.append(model.index(index.row(), 0, QtCore.QModelIndex()).data())
            medico.append(model.index(index.row(), 1, QtCore.QModelIndex()).data())
            medico.append(model.index(index.row(), 2, QtCore.QModelIndex()).data())
            medico.append(model.index(index.row(), 3, QtCore.QModelIndex()).data())
        app = RegisMedico.Principal(medico)
        app.setWindowTitle("Editar Paciente")
        sys.exit(app.exec_())

    def registrar(self):
        app = RegisMedico.Principal()
        sys.exit(app.exec_())

    def eliminar(self):
        index = self.ui.tblview_medicos.currentIndex()  # obtiene la fila
                                                        #seleccionada
        if index.row() == -1:
            mensaje = "Seleccione un Medico para borrar"
            errorQMessageBox = QtGui.QMessageBox()
            errorQMessageBox.setWindowTitle("Error")
            errorQMessageBox.setText(mensaje)
            errorQMessageBox.exec_()
        else:
            model = self.ui.tblview_medicos.model()
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            Controller.eliminarMedico(rut)

    def renderizaTabla(self):
        self.table = self.ui.tblview_medicos
        self.table.setFixedWidth(450)
        self.table.setFixedHeight(340)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.main_layout.addWidget(self.table)

    def load(self):
            # metodo para cargar la grilla con los medicos
            medicos = Controller.medicos()
            self.model = QtGui.QStandardItemModel(len(medicos), 5)
            self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
            self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem
                                               (u"Nombres"))
            self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem
                                               (u"Apellidos"))
            self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem
                                               (u"Especialidad"))
            self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem
                                               (u"N Horas Medicas"))
            r = 0
            for row in medicos:
                fk_rut_medico = row['rut']
                index = self.model.index(r, 0, QtCore.QModelIndex())
                self.model.setData(index, row['Rut'])
                index = self.model.index(r, 1, QtCore.QModelIndex())
                self.model.setData(index, row['Nombres'])
                index = self.model.index(r, 2, QtCore.QModelIndex())
                self.model.setData(index, row['Apellidos'])
                index = self.model.index(r, 3, QtCore.QModelIndex())
                self.model.setData(index, row['Especialidad'])
                index = self.model.index(r, 4, QtCore.QModelIndex())
                self.model.setData(index, Controller.obtenerNCitas(fk_rut_medico))
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