"""
Módulo de pruebas unitarias para el sistema de cálculo pensional.

Este archivo contiene pruebas automatizadas para verificar el correcto funcionamiento de:

- calcular_tasa_reemplazo()
- calcular_pension()

Las pruebas cubren:

- Casos normales de pensión de vejez
- Incremento por semanas adicionales
- Pensión de sobreviviente
- Pensión de invalidez (baja y alta)
- Aplicación del salario mínimo
- Tope máximo de tasa de reemplazo
- Casos de error por validaciones
"""

import unittest
import sys
sys.path.append("src")
from model import logica_calcupension


class TestCalculoPension(unittest.TestCase):
    """
    Clase de pruebas unitarias para validar el cálculo de tasa de reemplazo
    y mesada pensional según diferentes escenarios.

    Cada método test evalúa un caso específico del sistema.
    """

    def test_normal_1(self):
        """
        Caso normal de pensión de vejez para hombre.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 3_000_000, 1300, "Hombre", 62, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada: float = logica_calcupension.CalculadoraPension.calcular_pension(
            tasa, solicitud.ingreso_base_liquidacion, solicitud.tipo
        )

        self.assertAlmostEqual(tasa, 64.64, 2)
        self.assertAlmostEqual(mesada, 1_939_299, 0)

    def test_normal_2(self):
        """
        Caso normal de pensión de vejez para mujer.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 5_000_000, 1300, "Mujer", 57, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada: float = logica_calcupension.CalculadoraPension.calcular_pension(
            tasa, solicitud.ingreso_base_liquidacion, solicitud.tipo
        )

        self.assertAlmostEqual(tasa, 64.07, 2)
        self.assertAlmostEqual(mesada, 3_203_608, 0)

    def test_normal_3(self):
        """
        Caso normal de pensión de vejez para hombre.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 4_500_000, 1300, "Hombre", 63, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada: float = logica_calcupension.CalculadoraPension.calcular_pension(
            tasa, solicitud.ingreso_base_liquidacion, solicitud.tipo
        )

        self.assertAlmostEqual(tasa, 64.21, 2)
        self.assertAlmostEqual(mesada, 2_889_673, 0)

    def test_semanas_de_mas_cotizadas(self):
        """
        Caso donde el afiliado tiene semanas adicionales.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 2_500_000, 1500, "Hombre", 62, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada: float = logica_calcupension.CalculadoraPension.calcular_pension(
            tasa, solicitud.ingreso_base_liquidacion, solicitud.tipo
        )

        self.assertAlmostEqual(tasa, 70.79, 2)
        self.assertAlmostEqual(mesada, 1_769_652, 0)

    def test_pension_de_sobreviviente(self):
        """
        Caso de pensión de sobreviviente.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Sobreviviente", 3_500_000, 700, "Hombre", None, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

        self.assertAlmostEqual(tasa, 53.00, 2)

    def test_ibl_menor_al_SMMLV(self):
        """
        Caso donde la mesada es menor al SMMLV.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 1_400_000, 1400, "Mujer", 57, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada: float = logica_calcupension.CalculadoraPension.calcular_pension(
            tasa, solicitud.ingreso_base_liquidacion, solicitud.tipo
        )

        self.assertAlmostEqual(tasa, 68.10, 2)
        self.assertAlmostEqual(mesada, 1_750_905, 0)

    def test_mayor_a_tasa_maxima(self):
        """
        Caso donde la tasa supera el 80%.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 10_000_000, 2000, "Hombre", 62, 0
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

        self.assertAlmostEqual(tasa, 80.00, 2)

    def test_pension_de_invalidez_baja(self):
        """
        Caso de invalidez con PCL bajo.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Invalidez", 2_800_000, 900, "Mujer", 53, 65
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

        self.assertAlmostEqual(tasa, 57.00, 2)

    def test_pension_de_invalidez_alta(self):
        """
        Caso de invalidez con PCL alto.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Invalidez", 4_000_000, 1000, "Hombre", 55, 70
        )

        tasa: float = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

        self.assertAlmostEqual(tasa, 74.00, 2)

    def test_error_ibl(self):
        """
        Error por IBL inválido.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 0, 1350, "Hombre", 63, 0
        )

        with self.assertRaises(logica_calcupension.ErrorIBL):
            logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

    def test_error_semanas_cotizadas(self):
        """
        Error por semanas insuficientes.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 2_000_000, 400, "Mujer", 58, 0
        )

        with self.assertRaises(logica_calcupension.ErrorSemanasCotizadas):
            logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

    def test_error_edad_minima_hombres(self):
        """
        Error por edad mínima hombre.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 2_700_000, 1300, "Hombre", 50, 0
        )

        with self.assertRaises(logica_calcupension.ErrorEdadMinimaHombres):
            logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

    def test_error_edad_minima_mujeres(self):
        """
        Error por edad mínima mujer.
        """
        solicitud: logica_calcupension.SolicitudPension = logica_calcupension.SolicitudPension(
            "Vejez", 4_500_000, 1300, "Mujer", 45, 0
        )

        with self.assertRaises(logica_calcupension.ErrorEdadMinimaMujeres):
            logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)


if __name__ == '__main__':
    """
    Punto de entrada del archivo de pruebas.
    Ejecuta todas las pruebas unitarias definidas en la clase.
    """
    unittest.main()