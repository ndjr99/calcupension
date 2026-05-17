import unittest
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
    
    def test_insertar_y_buscar(self):
        # Crear un objeto SolicitudesPension
        solicitud_prueba = SolicitudesPension(
            id_solicitud=10,
            tipo="Vejez",
            ingreso_base_liquidacion=1500000.00,
            semanas=1300,
            genero="Hombre",
            edad=65,
            porcentaje_pcl=0,
            fecha="2026-06-01 12:00:00"
        )

        # Insertar la solicitud en la base de datos
        SolicitudesPensionController.insertar(solicitud_prueba)

        # Buscar la solicitud en la base de datos
        solicitud_buscada = SolicitudesPensionController.buscar_solicitud(solicitud_prueba.id_solicitud)
        # Verificar que si haya traido la solicitud correcta
        self.assertTrue(solicitud_prueba.is_equal(solicitud_buscada))

if __name__ == "__main__":
    unittest.main()