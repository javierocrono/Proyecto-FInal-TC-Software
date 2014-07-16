# -*- coding: utf-8 -*-

import sys
sys.path.append('Model')
from model import Paciente, Medico, Cita


def pacientes():
    return Paciente.all()


def medicos():
    return Medico.all()


def citas():
    return Cita.all()


def crearPaciente(rut, nombres, apellidos, ficha_medica):
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


def crearMedico(rut, nombres, apellidos, especialidad):
    """
    Método que crea un Medico Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    nuevo = Medico()
    nuevo.rut = rut
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.especialidad = especialidad
    nuevo.save()


def crearCita(fk_paciente_rut, fk_medico_rut, fecha, sintomas, diagnostico,
              recomendaciones, receta):
    """
    Crea una nueva cita"
    """
    nuevo = Cita()
    nuevo.fk_medico_rut = fk_medico_rut
    nuevo.fk_paciente_rut = fk_paciente_rut
    nuevo.fecha = fecha
    nuevo.sintomas = sintomas
    nuevo.diagnostico = diagnostico
    nuevo.recomendaciones = recomendaciones
    nuevo.receta = receta
    nuevo.save()

if __name__ == "__main__":
    pass

# -*- coding: utf-8 -*-
