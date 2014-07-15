# -*- coding: utf-8 -*-

import sqlite3


def connect():
    """Retorna una conexión con la base de datos"""
    conn = sqlite3.connect('pacientes.db')
    conn.row_factory = sqlite3.Row
    return conn


class Paciente(object):

    __tablename__ = "paciente"
    rut = None  # Primary Key
    nombres = ""
    apellidos = ""
    ficha_medica = ""

    def __init__(self,
        rut=None,
        nombres="",
        apellidos="",
        ficha_medica=""):

            self.rut = rut
            self.nombres = nombres
            self.apellidos = apellidos
            self.ficha_medica = ficha_medica

            # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
            if rut is not None:
                self.load()
            elif nombres is not None:
                self.load(nombres=nombres)

    def load(self, nombres=None):

        conn = connect()
        query = "SELECT * FROM paciente "
        if nombres is not None:
            query += "WHERE nombres = ?"
            condition = nombres

        else:
            if self.id_curso is None:
                return
            query += " WHERE rut = ?"
            condition = self.rut
        result = conn.execute(
            query, [condition])
        row = result.fetchone()
        conn.close()

        if row is not None:
            self.rut = row[0]
            self.nombres = row[1]
            self.apellidos = row[2]
            self.ficha_medica = row[3]
        else:
            self.rut = None
            print "El registro no existe"

    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.rut is None:
            self.rut = self.__insert()
        else:
            self.__update()

    def __insert(self):
        query = "INSERT INTO paciente "
        query += "(rut, nombres, apellidos, ficha_medica) "
        query += "VALUES (?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.rut,
                    self.nombres,
                    self.apellidos,
                    self.ficha_medica])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE paciente "
        query += "SET nombres = ?, "
        query += "apellidos = ?, "
        query += "ficha_medica = ?, "
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.nombres,
                    self.apellidos,
                    self.ficha_medica,
                    self.rut])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete(self):
        query = "DELETE FROM paciente "
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(query, [self.rut])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla paciente.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        pacientes = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            for row in data:
                pacientes.append(
                    Paciente(row[0], row[1], row[2], row[3]))
            return pacientes

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


class medico(object):

    __tablename__ = "medico"
    rut = None  # Primary Key
    nombres = ""
    apellidos = ""
    especialidad = ""

    def __init__(self,
        rut=None,
        nombres="",
        apellidos="",
        especielidad=""):

            self.rut = rut
            self.nombres = nombres
            self.apellidos = apellidos
            self.especialidad = especialidad

            # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
            if rut is not None:
                self.load()
            elif nombres is not None:
                self.load(nombres=nombres)

    def load(self, nombres=None):

        conn = connect()
        query = "SELECT * FROM medico "
        if nombres is not None:
            query += "WHERE nombres = ?"
            condition = nombres

        else:
            if self.id_curso is None:
                return
            query += " WHERE rut = ?"
            condition = self.rut
        result = conn.execute(
            query, [condition])
        row = result.fetchone()
        conn.close()

        if row is not None:
            self.rut = row[0]
            self.nombres = row[1]
            self.apellidos = row[2]
            self.especialidad = row[3]
        else:
            self.rut = None
            print "El registro no existe"

    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.rut is None:
            self.rut = self.__insert()
        else:
            self.__update()

    def __insert(self):
        query = "INSERT INTO medico "
        query += "(rut, nombres, apellidos, especialidad) "
        query += "VALUES (?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.rut,
                    self.nombres,
                    self.apellidos,
                    self.especialidad])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE medico "
        query += "SET nombres = ?, "
        query += "apellidos = ?, "
        query += "especialidad = ?, "
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.nombres,
                    self.apellidos,
                    self.especialidad,
                    self.rut])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete(self):
        query = "DELETE FROM paciente "
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(query, [self.rut])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla paciente.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        pacientes = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            for row in data:
                pacientes.append(
                    Paciente(row[0], row[1], row[2], row[3]))
            return pacientes

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


class Cita(object):

    __tablename__ = "cita"
    fk_paciente_rut = None
    fk_medico_rut = None
    fecha = ""
    sintomas = ""
    diagnostico = ""
    recomendaciones = ""
    receta = ""

    def __init__(
        self,
        fk_paciente_rut=None,
        fk_medico_rut=None,
        fecha="",
        sintomas="",
        diagnostico="",
        recomendaciones="",
        receta=""):
            fk_paciente_rut = fk_paciente_rut
            fk_medico_rut = fk_medico_rut
            fecha = fecha
            sintomas = sintomas
            diagnostico = diagnostico
            recomendaciones = recomendaciones
            receta = receta


