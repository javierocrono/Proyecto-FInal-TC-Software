#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from Registro_Medico import Ui_Registrar_Medico_Window
import Controller
"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow):

    def __init__(self, medico=None):
        super(Principal, self).__init__()
        self.ui = Ui_Registrar_Medico_Window()
        self.ui.setupUi(self)
        self.ui.btn_ingresar.clicked.connect(self.registraMedico)
        self.ui.btn_cancelar.clicked.connect(self.close)
        self.rut = ""
        if medico is not None:
            self.rut = medico[0]
            self.ui.ledit_rut.setText(str(medico[0]))
            self.ui.ledit_nombres.setText(str(medico[1]))
            self.ui.ledit_apellidos.setText(str(medico[2]))
            self.ui.ledit_especialidad.setText(str(medico[3]))
        self.centrar()
        self.show()

    def registraMedico(self):
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
        if(rut == "" or nombres == "" or apellidos == "" or especialidad == ""):
            mensaje = "Faltan Campos de Informacion"
            errorQMessageBox = QtGui.QMessageBox()
            errorQMessageBox.setWindowTitle("Error")
            errorQMessageBox.setText(mensaje)
            errorQMessageBox.exec_()
        else:
            if self.rut == "":
                Controller.crearMedico(rut, nombres, apellidos,
                                     especialidad)
                self.close()
            else:
                Controler.editarMedico(rut, nombres, apellidos,
                                     especialidad)
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