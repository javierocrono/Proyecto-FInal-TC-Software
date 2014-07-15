from model import Paciente, Medico


def pacientes():
    return Paciente.all()


def medicos():
    return Medico.all()


def crear_paciente(rut, nombres, apellidos, ficha_medica):
    """
    Método que crea un Paciente. Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    nuevo = Paciente()
    nuevo.rut = rut
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.ficha_medica = ficha_medica
    nuevo.save()

if __name__ == "__main__":
    pass

# -*- coding: utf-8 -*-
