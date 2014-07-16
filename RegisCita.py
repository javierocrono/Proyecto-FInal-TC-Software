#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from Registro_Cita import Ui_Registrar_CIta_Window
import Controller

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow):

    def __init__(self, citas=None):
        super(Principal, self).__init__()
        self.ui = Ui_Registrar_CIta_Window()
        self.ui.setupUi(self)
        self.ui.btn_ingresar.clicked.connect(self.registraCita)
        self.ui.btn_cancelar.clicked.connect(self.close)
        self.fk_paciente_rutviejo = ""
        self.fk_medico_rutviejo = ""
        self.fechavieja = ""
        if citas is not None:
            self.fk_paciente_rutviejo = citas[5]
            self.fk_medico_rutviejo = citas[6]
            self.fechavieja = citas[0]
            self.ui.ledit_rutpaciente.setText(str(citas[5]))
            self.ui.ledit_rutmedico.setText(str(citas[6]))
            self.ui.ledit_fecha.setText(str(citas[0]))
            self.ui.ledit_sintomas.setText(str(citas[1]))
            self.ui.ledit_diagnostico.setText(str(citas[2]))
            self.ui.ledit_recomendaciones.setText(str(citas[3]))
            self.ui.ledit_receta.setText(str(citas[4]))
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
        fk_paciente_rut = self.ui.ledit_rutpaciente.text()
        fk_medico_rut = self.ui.ledit_rutmedico.text()
        fecha = self.ui.ledit_fecha.text()
        sintomas = self.ui.ledit_sintomas.text()
        diagnostico = self.ui.ledit_diagnostico.text()
        recomendaciones = self.ui.ledit_recomendaciones.text()
        receta = self.ui.ledit_receta.text()
        if(fk_paciente_rut == "" or fk_medico_rut == "" or fecha == ""
            or sintomas == ""):

            mensaje = "Faltan Campos de Informacion"
            errorQMessageBox = QtGui.QMessageBox()
            errorQMessageBox.setWindowTitle("Error")
            errorQMessageBox.setText(mensaje)
            errorQMessageBox.exec_()
        else:
            if self.fechavieja == "":
                Controller.crearCita(fk_paciente_rut, fk_medico_rut, fecha,
                                     sintomas, diagnostico, recomendaciones,
                                     receta)
                self.close()
            else:
                print (self.fk_paciente_rutviejo,
                                      self.fk_medico_rutviejo,
                                      self.fechavieja,
                                      fk_paciente_rut, fk_medico_rut, fecha,
                                      sintomas, diagnostico, recomendaciones,
                                      receta)
                Controller.editarCita(self.fk_paciente_rutviejo,
                                      self.fk_medico_rutviejo,
                                      self.fechavieja,
                                      fk_paciente_rut, fk_medico_rut, fecha,
                                      sintomas, diagnostico, recomendaciones,
                                      receta)
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