import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.solicitudes import SolicitudesPension
import secret_config

class SolicitudesPensionController:

    def crear_tabla():
        cursor = SolicitudesPensionController.obtener_cursor()
        # Lee el contenido del archivo sql/crear-solicitudes.sql y lo guarda en la variable sql
        with open("sql/crear-solicitudes.sql", "r") as archivo:
            sql = archivo.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = SolicitudesPensionController.obtener_cursor()
        # Lee el contenido del archivo sql/borrar-solicitudes.sql y lo guarda en la variable sql
        with open("sql/borrar-solicitudes.sql", "r") as archivo:
            sql = archivo.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def obtener_cursor():
        """ Crea un objeto cursor para poder ejecutar SQL en la base de datos. """
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        cursor = connection.cursor()
        return cursor

    def insertar(solicitud: SolicitudesPension):
        cursor = SolicitudesPensionController.obtener_cursor()
        consulta = f""" INSERT INTO solicitudes_pension (id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_perdida_capacidad_laboral, fecha, tasa_reemplazo, mesada)
        VALUES ({solicitud.id_solicitud}, '{solicitud.tipo}', {solicitud.ingreso_base_liquidacion}, {solicitud.semanas}, '{solicitud.genero}', {solicitud.edad}, {solicitud.porcentaje_perdida_capacidad_laboral}, '{solicitud.fecha}', {solicitud.tasa_reemplazo}, {solicitud.mesada}); """
        
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar_solicitud(id_solicitud: int) -> SolicitudesPension:
        """ Busca una solicitud de pensión en la tabla y la carga en una instancia de la clase SolicitudesPension. """
        # Conectar a la BD
        cursor = SolicitudesPensionController.obtener_cursor()
        # Ejecutamos el sql para traer una fila
        consulta = f""" SELECT id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_perdida_capacidad_laboral, fecha, tasa_reemplazo, mesada
            FROM solicitudes_pension WHERE id_solicitud = {id_solicitud}; """
        cursor.execute(consulta)
        
        # La fila retorna la carga en la instancia de la clase SolicitudesPension
        fila = cursor.fetchone()
        solicitud = SolicitudesPension(id_solicitud=fila[0], tipo=fila[1], ingreso_base_liquidacion=fila[2], semanas=fila[3], genero=fila[4], edad=fila[5], porcentaje_perdida_capacidad_laboral=float(fila[6]), fecha=fila[7], tasa_reemplazo=float(fila[8]), mesada=float(fila[9]))
        return solicitud