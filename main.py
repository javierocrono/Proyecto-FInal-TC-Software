#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from Inicio import Ui_Inicio_Window
import AdminMedicos
import AdminPacientes
import AdminCitas

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow, Ui_Inicio_Window):

    def __init__(self, parent=None):

        super(Principal, self).__init__(parent)
        self.ui = Ui_Inicio_Window()
        self.ui.setupUi(self)
        self.ui.btn_medicos.clicked.connect(self.adminMedicos)
        self.ui.btn_pacientes.clicked.connect(self.adminPacientes)
        self.ui.btn_citas.clicked.connect(self.adminCitas)
        self.centrar()
        self.show()

    def adminMedicos(self):
        app = AdminMedicos.Principal()
        sys.exit(app.exec_())

    def adminPacientes(self):
        app = AdminPacientes.Principal()
        sys.exit(app.exec_())

    def adminCitas(self):
        app = AdminCitas.Principal()
        sys.exit(app.exec_())

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
    sys.exit(app.exec_())

if __name__ == '__main__':

    run()