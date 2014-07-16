# -*- coding: utf-8 -*-

import sys
import sqlite3


def connect():
    """Retorna una conexión con la base de datos"""
    conn = sqlite3.connect('pacientes.db')
    conn.row_factory = sqlite3.Row
    print conn
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
            if self.rut is None:
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

    def save(self, rutviejo=None, rut=None):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if rutviejo is None:
            if self.rut is not None:
                self.rut = self.__insert()
            else:
                self.__update()
        else:
            self.rut = rut
            self.__update(rutviejo)

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

    def __update(self, rutviejo=None):
        query = "UPDATE paciente "
        query += "SET rut = ?, "
        query += "nombres = ?, "
        query += "apellidos = ?, "
        query += "ficha_medica = ? "
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.rut,
                    self.nombres,
                    self.apellidos,
                    self.ficha_medica,
                    rutviejo])
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
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            return data

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


class Medico(object):

    __tablename__ = "medico"
    rut = None  # Primary Key
    nombres = ""
    apellidos = ""
    especialidad = ""

    def __init__(self,
        rut=None,
        nombres="",
        apellidos="",
        especialidad=""):

            self.rut = rut
            self.nombres = nombres
            self.apellidos = apellidos
            self.especialidad = especialidad

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
            if self.rut is None:
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

    def save(self, rutviejo=None, rut=None):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if rutviejo is None:
            if self.rut is not None:
                self.rut = self.__insert()
            else:
                self.__update()
        else:
            self.rut = rut
            self.__update(rutviejo)

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

    def __update(self, rutviejo=None):
        if rutviejo is not None:
            query = "UPDATE medico "
            query += "SET rut = ?, "
            query += "nombres = ?, "
            query += "apellidos = ?, "
            query += "especialidad = ? "
            query += "WHERE rut = ?"
            try:
                conn = connect()
                conn.execute(
                    query, [
                        self.rut,
                        self.nombres,
                        self.apellidos,
                        self.especialidad, rutviejo])
                conn.commit()
                conn.close()
                return True
            except sqlite3.Error as e:
                print "An error occurred:", e.args[0]
                return False

    def delete(self):
        query = "DELETE FROM medico "
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
        en la tabla medico.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            return data

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
            self.fk_paciente_rut = fk_paciente_rut
            self.fk_medico_rut = fk_medico_rut
            self.fecha = fecha
            self.sintomas = sintomas
            self.diagnostico = diagnostico
            self.recomendaciones = recomendaciones
            self.receta = receta
            if self.fk_paciente_rut is not None:
                self.load()
            elif self.fk_medico_rut is not None:
                self.load(fk_medico_rut=self.fk_medico_rut)

    def save(self, fk_paciente_rutviejo=None, fk_medico_rutviejo=None,
                fechavieja=None, fk_paciente_rut=None):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.fk_paciente_rut is not None:
            self.fk_paciente_rut = self.insert()
        else:
            self.fk_paciente_rut = fk_paciente_rut
            self.__update(fk_paciente_rutviejo, fk_medico_rutviejo,
                    fechavieja)

    def insert(self):
        query = "INSERT INTO cita "
        query += "(fecha, sintomas, diagnostico, recomendaciones,"
        query += " receta, fk_paciente_rut, fk_medico_rut) "
        query += "VALUES (?, ?, ?, ?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.fecha,
                    self.sintomas,
                    self.diagnostico,
                    self.recomendaciones,
                    self.receta,
                    self.fk_paciente_rut,
                    self.fk_medico_rut])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self, fk_paciente_rutviejo, fk_medico_rutviejo,
                    fechavieja):
        print (fk_paciente_rutviejo, fk_medico_rutviejo,
                    fechavieja, self.fk_paciente_rut, self.fk_medico_rut)
        query = "UPDATE cita SET"
        query += " fecha = ?, sintomas = ?, diagnostico = ?, "
        query += "recomendaciones = ?,"
        query += " receta = ?, fk_paciente_rut = ?, fk_medico_rut = ? "
        query += "WHERE fk_paciente_rut = ? AND fk_medico_rut = ? AND fecha = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.fecha,
                    self.sintomas,
                    self.diagnostico,
                    self.recomendaciones,
                    self.receta,
                    self.fk_paciente_rut,
                    self.fk_medico_rut,
                    fk_paciente_rutviejo, fk_medico_rutviejo,
                    fechavieja])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def load(self, fk_id_pelicula=None):
        conn = connect()
        query = "SELECT * FROM actor_en_pelicula"

        if self.fk_id_actor is not None:
            query += " WHERE fk_paciente_rut = ?"
            condition = self.fk_id_actor
        else:
            if fk_id_pelicula is None:
                return

            query += " WHERE fk_medico_rut = ?"
            condition = fk_id_pelicula

        result = conn.execute(
            query, [condition])
        print result
        row = result.fetchone()
        conn.close()

        if row is not None:
            self.fecha = row[2]
            self.sintomas = row[2]
            self.diagnostico = row[2]
            self.recomendaciones = row[2]
            self.receta = row[3]
            self.fk_paciente_rut = row[5]
            self.fk_medico_rut = row[6]
        else:
            self.nombre = None
            print "No existe el registro"

    def delete(self):
        query = "DELETE FROM cita "
        query += "WHERE fk_paciente_rut = ? AND"
        query += " fk_medico_rut = ? AND"
        query += " fecha = ? "
        try:
            conn = connect()
            print "hola"
            print (self.fk_paciente_rut, self.fk_medico_rut, self.fecha)
            conn.execute(query, [self.fk_paciente_rut, self.fk_medico_rut,
                            self.fecha])
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
        de la tabla citas.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            return data

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


if __name__ == "__main__":
    pass


