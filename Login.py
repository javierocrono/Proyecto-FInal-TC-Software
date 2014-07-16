#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('View')
from PySide import QtGui, QtCore
from PySide.QtGui import *
from LoginWindow import Ui_MainWindow
import main

"""
Inicia la aplicacion de forma clara
"""


class Principal(QtGui.QMainWindow):

    usuarios = [("JavierO", "1234"), ("Barbara", "2736"),
                ("Maria", "ladelbarrio")]

    def __init__(self, parent=None):

        super(Principal, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_aceptar.clicked.connect(self.verificar)
        self.ui.btn_cancelar.clicked.connect(self.close)
        self.centrar()

    def verificar(self):
        pass
        usuario = self.ui.ledit_usuario.text()
        password = self.ui.ledit_contrasenia.text()
        user = (usuario, password)
        print (user)
        correcto = False
        for i in (self.usuarios):
            if i == user:
                correcto = True
                break

        if correcto:
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("Login Exitoso")
            correctoQMessageBox.setText(u"Bienvenido")
            correctoQMessageBox.exec_()

            main.Principal()
            self.close()

        else:
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("ERROR")
            correctoQMessageBox.setText(u"Usuario y/o contraseña incorrecta")
            correctoQMessageBox.exec_()

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