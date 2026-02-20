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
import logica_calcupension


class TestCalculoPension(unittest.TestCase):
    """
    Clase de pruebas unitarias para validar el cálculo de tasa de reemplazo
    y mesada pensional según diferentes escenarios.

    Cada método test evalúa un caso específico del sistema.
    """

    def test_normal_1(self):
        """
        Caso normal de pensión de vejez para hombre.
        - 1300 semanas cotizadas
        - Edad mínima cumplida
        - Se valida tasa calculada y mesada resultante
        """
        tipo = "Vejez"
        ibl = 3_000_000
        semanas = 1300
        genero = "Hombre"
        edad = 62
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 64.64
        mesada_esperada = 1_939_299

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_normal_2(self):
        """
        Caso normal de pensión de vejez para mujer.
        Se valida el cálculo correcto de tasa y mesada.
        """
        tipo = "Vejez"
        ibl = 5_000_000
        semanas = 1300
        genero = "Mujer"
        edad = 57
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 64.07
        mesada_esperada = 3_203_608

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_semanas_de_mas_cotizadas(self):
        """
        Caso donde el afiliado tiene semanas adicionales
        a las 1300 mínimas, generando incremento en la tasa.
        """
        tipo = "Vejez"
        ibl = 2_500_000
        semanas = 1500
        genero = "Hombre"
        edad = 62
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 70.79
        mesada_esperada = 1_769_652

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_pension_de_sobreviviente(self):
        """
        Caso de pensión de sobreviviente.
        Se valida el incremento por semanas superiores a 500.
        """
        tipo = "Sobreviviente"
        ibl = 3_500_000
        semanas = 700
        genero = "Hombre"
        edad = None
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 53.00
        mesada_esperada = 1_855_000

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_ibl_menor_al_SMMLV(self):
        """
        Caso donde la mesada calculada es inferior
        al Salario Mínimo Mensual Legal Vigente (SMMLV),
        por lo tanto debe ajustarse al mínimo.
        """
        tipo = "Vejez"
        ibl = 1_400_000
        semanas = 1400
        genero = "Mujer"
        edad = 57
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 68.10
        mesada_esperada = 1_750_905

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_mayor_a_tasa_maxima(self):
        """
        Caso donde la tasa supera el tope máximo permitido (80%).
        Se valida que el sistema aplique correctamente el límite.
        """
        tipo = "Vejez"
        ibl = 10_000_000
        semanas = 2000
        genero = "Hombre"
        edad = 62
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 80.00
        mesada_esperada = 8_000_000

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_pension_de_invalidez_baja(self):
        """
        Caso de pensión de invalidez con PCL entre 50% y 66%.
        """
        tipo = "Invalidez"
        ibl = 2_800_000
        semanas = 900
        genero = "Mujer"
        edad = 53
        pcl = 65

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 57.00
        mesada_esperada = 1_596_000

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_pension_de_invalidez_alta(self):
        """
        Caso de pensión de invalidez con PCL superior a 66%.
        """
        tipo = "Invalidez"
        ibl = 4_000_000
        semanas = 1000
        genero = "Hombre"
        edad = 55
        pcl = 70

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)
        tasa_reemplazo_esperada = 74.00
        mesada_esperada = 2_960_000

        self.assertAlmostEqual(tasa_reemplazo_calculada, tasa_reemplazo_esperada, 2)
        self.assertAlmostEqual(mesada_calculada, mesada_esperada, 0)

    def test_error_ibl(self):
        """
        Verifica que el sistema retorne error
        cuando el IBL es menor o igual a 0.
        """
        tipo = "Vejez"
        ibl = 0
        semanas = 1350
        genero = "Hombre"
        edad = 63
        pcl = 0

        with self.assertRaises(Exception):
            tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
            mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)

    def test_error_semanas_cotizadas(self):
        """
        Verifica que el sistema retorne error
        cuando no se cumplen las 1300 semanas mínimas.
        """
        tipo = "Vejez"
        ibl = 2_000_000
        semanas = 400
        genero = "Mujer"
        edad = 58
        pcl = 0

        with self.assertRaises(Exception):
                    tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
                    mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)

    def test_error_edad_minima_hombres(self):
        """
        Verifica error cuando un hombre no cumple la edad mínima (62 años).
        """
        tipo = "Vejez"
        ibl = 2_700_000
        semanas = 1300
        genero = "Hombre"
        edad = 50
        pcl = 0

        with self.assertRaises(Exception):
            tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
            mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)

    def test_error_edad_minima_mujeres(self):
        """
        Verifica error cuando una mujer no cumple la edad mínima (57 años).
        """
        tipo = "Vejez"
        ibl = 4_500_000
        semanas = 1300
        genero = "Mujer"
        edad = 45
        pcl = 0

        with self.assertRaises(Exception):
            tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
            mesada_calculada = logica_calcupension.calcular_pension(tasa_reemplazo_calculada, ibl, tipo)


if __name__ == '__main__':
    """
    Punto de entrada del archivo de pruebas.
    Ejecuta todas las pruebas unitarias definidas en la clase.
    """
    unittest.main()