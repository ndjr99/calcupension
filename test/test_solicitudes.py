import unittest
import random
import sys
sys.path.append("src")

from controller.solicitudes_controller import SolicitudesPensionController
from model.solicitudes import SolicitudesPension

class TestSolicitudesPension(unittest.TestCase):

    # Test Fixture
    @classmethod
    def setUpClass(cls):
        """ Jamás ejecute las pruebas unitarias en una BD de producción porque borra todos los datos"""
        SolicitudesPensionController.borrar_tabla()
        SolicitudesPensionController.crear_tabla()
    
    def test_insertar_y_buscar_1(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo="Vejez",
            ingreso_base_liquidacion=3000000,
            semanas=1300,
            genero="Hombre",
            edad=62,
            porcentaje_perdida_capacidad_laboral=0,
            fecha="2026-06-01 12:00:00",
            tasa_reemplazo=64.64,
            mesada=1939299
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))

    def test_insertar_y_buscar_2(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo="Vejez",
            ingreso_base_liquidacion=5000000,
            semanas=1300,
            genero="Mujer",
            edad=57,
            porcentaje_perdida_capacidad_laboral=0,
            fecha="2026-06-01 12:00:00",
            tasa_reemplazo=64.07,
            mesada=3203608
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))

    def test_insertar_y_buscar_3(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo="Vejez",
            ingreso_base_liquidacion=4500000,
            semanas=1300,
            genero="Hombre",
            edad=63,
            porcentaje_perdida_capacidad_laboral=0,
            fecha="2026-06-01 12:00:00",
            tasa_reemplazo=64.21,
            mesada=2889673
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))

    def test_insertar_y_buscar_4(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo="Sobreviviente",
            ingreso_base_liquidacion=3500000,
            semanas=700,
            genero="Hombre",
            edad=0,
            porcentaje_perdida_capacidad_laboral=0,
            fecha="2026-06-01 12:00:00",
            tasa_reemplazo=53.00,
            mesada=1855000
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))

    def test_insertar_y_buscar_5(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo="Invalidez",
            ingreso_base_liquidacion=2800000,
            semanas=900,
            genero="Mujer",
            edad=53,
            porcentaje_perdida_capacidad_laboral=65,
            fecha="2026-06-01 12:00:00",
            tasa_reemplazo=57.00,
            mesada=1596000
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))
        
if __name__ == "__main__":
    unittest.main()