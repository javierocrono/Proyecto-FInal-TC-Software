#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from Citas import Ui_Citas_Window
import RegisCita

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Citas_Window()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.registrar)
        self.ui.btn_editar.clicked.connect(self.editar)
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