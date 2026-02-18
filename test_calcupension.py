import unittest
import logica_calcupension

class TestCalculoPension(unittest.TestCase):
    def test_normal_1(self):
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
        tipo = "Vejez"
        ibl = 0
        semanas = 1350
        genero = "Hombre"
        edad = 63
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        

        self.assertEqual(tasa_reemplazo_calculada, "Error: el IBL debe ser mayor a 0")

    def test_error_semanas_cotizadas(self):
        tipo = "Vejez"
        ibl = 2_000_000
        semanas = 400
        genero = "Mujer"
        edad = 58
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        

        self.assertEqual(tasa_reemplazo_calculada, "Error: las semanas cotizadas deeben ser mayores o iguales a 1300")

    def test_error_edad_minima_hombres(self):
        tipo = "Vejez"
        ibl = 2_700_000
        semanas = 1300
        genero = "Hombre"
        edad = 50
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        

        self.assertEqual(tasa_reemplazo_calculada, "Error: debe tener al menos 62 años para pensionarse")

    def test_error_edad_minima_mujeres(self):
        tipo = "Vejez"
        ibl = 4_500_000
        semanas = 1300
        genero = "Mujer"
        edad = 45
        pcl = 0

        tasa_reemplazo_calculada = logica_calcupension.calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl)
        

        self.assertEqual(tasa_reemplazo_calculada, "Error: debe tener al menos 57 años para pensionarse")

if __name__ == '__main__':        
    unittest.main()