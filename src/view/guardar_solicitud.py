import sys
sys.path.append("src")

import random
import datetime

from model.solicitudes import SolicitudesPension
from model.logica_calcupension import CalculadoraPension
from controller.solicitudes_controller import SolicitudesPensionController


try:
    # Leer datos de entrada de la solicitud
    solicitud = SolicitudesPension(id_solicitud=0, tipo="", ingreso_base_liquidacion=0, semanas=0, genero="", edad=0, porcentaje_perdida_capacidad_laboral=0, fecha="", tasa_reemplazo=0, mesada=0)

    solicitud.id_solicitud = random.randint(0,9999999)
    solicitud.tipo = input("Ingrese el tipo de pensión (Vejez, Invalidez, Sobreviviente): ")
    solicitud.ingreso_base_liquidacion = float(input("Ingrese el ingreso base de liquidación: "))
    solicitud.semanas = int(input("Ingrese el número de semanas cotizadas: "))
    solicitud.genero = input("Ingrese el género (Hombre, Mujer): ")
    solicitud.edad = int(input("Ingrese la edad: "))
    solicitud.porcentaje_perdida_capacidad_laboral = float(input("Ingrese el porcentaje de Pérdida de Capacidad Laboral: "))
    solicitud.fecha = datetime.date.today()
    solicitud.tasa_reemplazo = CalculadoraPension.calcular_tasa_reemplazo(solicitud)
    solicitud.mesada = CalculadoraPension.calcular_pension(solicitud.tasa_reemplazo, solicitud.ingreso_base_liquidacion, solicitud.tipo)

    # Proceso: guardar en la BD
    SolicitudesPensionController.insertar(solicitud)

    # Salida: mostrar si fue exitoso
    print("Solicitud registrada exitosamente.")
    print(f"ID de la solicitud: {solicitud.id_solicitud}")
    print(f"Tasa de reemplazo: {solicitud.tasa_reemplazo}%")
    print(f"Mesada pensional: ${solicitud.mesada:,.2f}")

except Exception as e:
    print("Ocurrió un error al grabar la solicitud:")
    print(str(e))