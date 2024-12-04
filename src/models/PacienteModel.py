from database.db import get_connection
from .entities.Paciente import Paciente


class PacienteModel:

    @classmethod
    def get_pacientes(self):
        try:
            connection = get_connection()
            pacientes = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT nui, nui_terapeuta, nombre, apellido, edad, direccion, estado FROM paciente ORDER BY apellido ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    paciente = Paciente(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    pacientes.append(paciente.to_JSON())
            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paciente(self, nui):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT nui, nui_terapeuta, nombre, apellido, edad, direccion, estado FROM paciente WHERE nui = %s", (nui,))
                row = cursor.fetchone()
                paciente = None
                if row != None:
                    paciente = Paciente(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    paciente = paciente.to_JSON()
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO paciente (nui, nui_terapeuta, nombre, apellido, edad, direccion, estado) VALUES (%s,%s, %s, %s, %s, %s, %s)", (
                    paciente.nui, paciente.nui_terapeuta, paciente.nombre, paciente.apellido, paciente.edad, paciente.direccion, paciente.estado))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE paciente SET nui_terapeuta = %s, nombre = %s, apellido = %s, edad = %s, direccion = %s, estado = %s WHERE nui = %s", (
                    paciente.nui_terapeuta, paciente.nombre, paciente.apellido, paciente.edad, paciente.direccion, paciente.estado, paciente.nui))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM paciente WHERE nui = %s", (paciente.nui,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)