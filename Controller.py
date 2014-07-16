# -*- coding: utf-8 -*-

from Model import Paciente, Medico, Cita


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
    print(rut, nombres, apellidos, ficha_medica)
    nuevo = Paciente()
    nuevo.rut = rut
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.ficha_medica = ficha_medica
    nuevo.save()


def eliminarPaciente(rut):
    nuevo = Paciente()
    nuevo.rut = rut
    nuevo.delete()


def crearMedico(rut, nombres, apellidos, especialidad):
    """
    Método que crea un Medico Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    print(rut, nombres, apellidos, especialidad)
    nuevo = Medico()
    nuevo.rut = rut
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.especialidad = especialidad
    nuevo.save()


def editarMedico(rutviejo, rut, nombres, apellidos, especialidad):
    """
    Método que edita un Medico Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    nuevo = Medico()
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.especialidad = especialidad
    nuevo.save(rutviejo, rut)


def editarPaciente(rutviejo, rut, nombres, apellidos, ficha_medica):
    """
    Método que edita un Medico Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    nuevo = Paciente()
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombres = nombres
    nuevo.apellidos = apellidos
    nuevo.ficha_medica = ficha_medica
    nuevo.save(rutviejo, rut)


def eliminarMedico(rut):
    nuevo = Medico()
    nuevo.rut = rut
    nuevo.delete()


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


def editarCita(fk_paciente_rutviejo, fk_medico_rutviejo, fechavieja,
                fk_paciente_rut, fk_medico_rut, fecha, sintomas, diagnostico,
                recomendaciones, receta):
    """
    Método que edita un Medico Lo correcto sería validar
    que toda la información es correcta
    Ej:
    """
    nuevo = Cita()
    # Aquí podrían haber validaciones para el codigo
    nuevo.fk_medico_rut = fk_medico_rut
    nuevo.fecha = fecha
    nuevo.sintomas = sintomas
    nuevo.diagnostico = diagnostico
    nuevo.recomendaciones = recomendaciones
    nuevo.receta = receta
    print (fk_paciente_rutviejo, fk_medico_rutviejo,
                                      fechavieja,
                                      nuevo.fk_paciente_rut, nuevo.fk_medico_rut, nuevo.fecha,
                                      nuevo.sintomas, nuevo.diagnostico, nuevo.recomendaciones,
                                      nuevo.receta)
    nuevo.save(fk_paciente_rutviejo, fk_medico_rutviejo, fechavieja,
                fk_paciente_rut)

def obtenerNCitas(fk_paciente_rut=None, fk_medico_rut=None):
    pass
    #nuevo = Cita(rut)

def eliminarCita(fk_paciente_rut, fk_medico_rut, fecha):
    nuevo = Cita()
    nuevo.fk_paciente_rut = fk_paciente_rut
    nuevo.fk_medico_rut = fk_medico_rut
    nuevo.fecha = fecha
    print (nuevo.fk_paciente_rut, nuevo.fk_medico_rut, nuevo.fecha)
    nuevo.delete()

if __name__ == "__main__":
    pass

# -*- coding: utf-8 -*-
