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
        rut = None,
        nombre = "",
        apellidos = "",
        ficha_medica = ""):

            self.rut = rut
            self.nombres = nombres
            self.apellidos = apellidos
            self.ficha_medica = ficha_medica

            # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
            if rut is not None:
                self.load()
            elif nombres is not None:
                self.load(nombres = nombres)

    def load(self, nombres = None):

        conn = connect()
        query = "SELECT * FROM paciente "
        if nombres is not None:
            query += "WHERE nombres = ?"
            condition = nombres

        else:
            if self.id_curso is None:
                return
            query += " WHERE id_curso = ?"
            condition = self.id_curso
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
        query = "INSERT INTO {0} ".format(self.__tablename__)
        # La pk está definida como auto increment en el modelo
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
            return
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None