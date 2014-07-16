# -*- coding: utf-8 -*-

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
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()
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
            # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
            # Si la fk_id_actor viene con valor es porque se busca las peliculas
            # en las que participo.
            # Del mismo modo si fk_id_pelicula viene con algun valor es porque
            # se busca los actores de esa película.
            if fk_id_actor is not None:
                # Buscamos Peliculas
                self.load()
            elif fk_id_pelicula is not None:
                # Buscamos Actores
                self.load(fk_id_pelicula=fk_id_pelicula)

    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.fk_id_actor is not None:
            self.fk_id_actor = self.insert()
        else:
            print "else"
            self.__update()

    def insert(self):
        query = "INSERT INTO cita "
        query += "(fecha, sintomas, diagnostico, recomendaciones,"
        query += " receta, fk_rut_paciente, fk_rut_medico) "
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
                    self.fk_rut_paciente,
                    self.fk_rut_medico])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE cita SET"
        query += "(fecha, sintomas, diagnostico, recomendaciones,"
        query += " receta, fk_rut_paciente, fk_rut_medico) "
        query += "VALUES (?, ?, ?, ?, ?, ?, ?)"
        query += "WHERE rut = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.fecha,
                    self.sintomas,
                    self.diagnostico,
                    self.recomendaciones,
                    self.receta,
                    self.fk_rut_paciente,
                    self.fk_rut_medico])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def load(self, fk_id_pelicula=None):
        """
        Carga una relación especifica.
        Depende de que parametro reciba buscara actor para una pelicula o
        pelicula de un actor.
        """
        conn = connect()
        query = "SELECT * FROM actor_en_pelicula"

        if self.fk_id_actor is not None:
            query += " WHERE fk_id_actor = ?"
            condition = self.fk_id_actor
        else:
            if fk_id_pelicula is None:
                return

            query += " WHERE fk_id_pelicula = ?"
            condition = fk_id_pelicula

        result = conn.execute(
            query, [condition])
        print result
        row = result.fetchone()
        conn.close()

        if row is not None:
            self.fk_id_actor = row[0]
            self.fk_id_pelicula = row[1]
            self.personaje = row[2]
            self.descripcion = row[3]
        else:
            self.nombre = None
            print "No existe el registro"

    @classmethod
    def actoresDeLaPelicula(cls, id_pelicula):
        """
        Retorna todas los Primary Key de los actores que participan en una
        misma pelicula buscada.

        @param id_pelicula:
            Primary Key de la película a la que le buscamos los actores.
        @return data:
            Tabla con los Primary Key de los actores participantes en la
            película buscada.
        """
        query = "SELECT fk_id_actor FROM {}".format(cls.__tablename__)
        query += " WHERE fk_id_pelicula = {}".format(id_pelicula)
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            return data

        except sqlite3.Error as e:
            #print "An error occurred:", e.args[0]
            return None

    @classmethod
    def peliculasDelActor(cls, id_actor):
        """
        Retorna todas los Primary Key de las películas en las que participa el
        un mismo actor.

        @param id_actor:
            Primary Key del actor al que se le buscan las películas.
        @return data:
            Tabla con los Primary Key de las películas en las que participo el
            actor al que se le buscaban las películas.
        """
        query = "SELECT fk_id_pelicula FROM {}".format(cls.__tablename__)
        query += " WHERE fk_id_actor = {}".format(id_actor)
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            return data

        except sqlite3.Error as e:
            #print "A Ocurrido un Error!:", e.args[0]
            return None

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla actor_en_pelicula.
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
            #print "An error occurred:", e.args[0]
            return None


if __name__ == "__main__":
    pass


