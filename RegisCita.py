#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from Registro_Cita import Ui_Registrar_CIta_Window

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Registrar_CIta_Window()
        self.ui.setupUi(self)
        self.ui.btn_ingresar.clicked.connect(self.registraCita)
        self.ui.btn_cancelar.clicked.connect(self.close)
        self.centrar()
        self.show()

    def registraCita(self):
        """
        Recoje todos los datos ingresados en la interfaz para pasarselos al
        controller. Donde este los revisara para luego agregarlos a la base de
        datos.
        Si existiese error en el ingreso de los datos mostrara un mensaje de
        error.
        """
        rut = self.ui.ledit_rut.text()

        nombres = self.ui.ledit_nombres.text()
        apellidos = self.ui.ledit_apellidos.text()
        especialidad = self.ui.ledit_especialidad.text()

        Controller.crearMedico(rut, nombres, apellidos, especialidad)
        self.close()

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