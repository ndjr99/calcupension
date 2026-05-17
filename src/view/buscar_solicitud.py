import sys
sys.path.append("src")

from datetime import date

from model.solicitudes import SolicitudesPension
from controller.solicitudes_controller import SolicitudesPensionController

try:
    id_solicitud = int(input("Ingrese el ID de la solicitud a buscar: "))
    solicitud = SolicitudesPensionController.buscar_solicitud(id_solicitud)

    if solicitud is None:
        print("No se encontró una solicitud con ese ID.")
    else:
        print("\nInformación de la solicitud:")
        print(f"ID de solicitud: {solicitud.id_solicitud}")
        print(f"Tipo de pensión: {solicitud.tipo}")
        print(f"Ingreso base de liquidación: {solicitud.ingreso_base_liquidacion}")
        print(f"Semanas cotizadas: {solicitud.semanas}")
        print(f"Género: {solicitud.genero}")
        print(f"Edad: {solicitud.edad}")
        print(f"Porcentaje de pérdida de capacidad laboral: {solicitud.porcentaje_perdida_capacidad_laboral}%")
        print(f"Fecha de solicitud: {solicitud.fecha}")
        print(f"Tasa de reemplazo: {solicitud.tasa_reemplazo}%")
        print(f"Mesada pensional: ${solicitud.mesada:,.2f}")

except Exception as e:
    print("Ocurrió un error al buscar la solicitud:")
    print(str(e))