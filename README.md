# CALCUPENSION
SISTEMA DE CÁLCULO PENSIONAL

Este proyecto implementa un sistema en Python para calcular la tasa de reemplazo y la mesada pensional según el tipo de pensión.

El sistema incluye:
- Cálculo de tasa de reemplazo
- Cálculo de mesada pensional
- Validaciones obligatorias
- Excepciones personalizadas
- Pruebas unitarias automatizadas

ESTRUCTURA DEL PROYECTO

El proyecto está compuesto por:
- logica_calcupension.py → Contiene la lógica del cálculo
- test_calcupension.py → Contiene las pruebas unitarias
- README.md → Documentación del sistema

TIPOS DE PENSIÓN SOPORTADOS

El sistema permite calcular:
- Pensión de Vejez
- Pensión de Sobreviviente
- Pensión de Invalidez

EXCEPCIONES PERSONALIZADAS

El sistema valida reglas del negocio mediante excepciones propias:

- error_ibl
Se genera cuando el IBL es menor o igual a 0.

- error_semanas_cotizadas
Se genera cuando no se cumplen las 1300 semanas mínimas para pensión de vejez.

- error_edad_minima_hombres
Se genera cuando un hombre tiene menos de 62 años.

- error_edad_minima_mujeres
Se genera cuando una mujer tiene menos de 57 años.

- error_pcl_invalidez
Se genera cuando la PCL es menor o igual a 50% en pensión de invalidez.

FUNCIÓN: calcular_tasa_reemplazo()

Parámetros:
- tipo: Tipo de pensión ("Vejez", "Sobreviviente", "Invalidez")
- ibl: Ingreso Base de Liquidación
- semanas: Semanas cotizadas
- genero: "Hombre" o "Mujer"
- edad: Edad del afiliado
- pcl: Porcentaje de pérdida de capacidad laboral

Retorna:
Tasa de reemplazo en porcentaje

REGLAS DEL CÁLCULO

SALARIO MÍNIMO USADO EN EL SISTEMA:
SMMLV = 1.750.905

PENSIÓN DE VEJEZ

Requisitos:
- Mínimo 1300 semanas
- Edad mínima:
- Hombre: 62 años
- Mujer: 57 años

Fórmula base:
r = 65.50 - (IBL / SMMLV) * 0.50

Incremento:
1.5% por cada 50 semanas adicionales a 1300

Límites:
- Mínimo 55%
- Máximo 80%

PENSIÓN DE SOBREVIVIENTE

Requisitos:
- Tasa base: 45%
- Incremento: 2% por cada 50 semanas superiores a 500
- Tope máximo: 75%

PENSIÓN DE INVALIDEZ

Requisitos:
- PCL debe ser mayor al 50%
- Si 50% < PCL ≤ 66%:
- Base 45%
- Incremento 1.5% por cada 50 semanas superiores a 500
- Si PCL > 66%:
- Base 54%
- Incremento 2% por cada 50 semanas superiores a 500

Límites:
- Mínimo 45%
- Máximo 75%

FUNCIÓN: calcular_pension()

Parámetros:
- tasa_total: Tasa de reemplazo en porcentaje
- ibl: Ingreso Base de Liquidación
- tipo: Tipo de pensión

Cálculo:
mesada = (tasa_total / 100) * ibl

Regla especial:
Si es pensión de vejez y la mesada es menor al SMMLV, se ajusta al salario mínimo.

PRUEBAS UNITARIAS

El sistema incluye pruebas automáticas con unittest que validan:

- Casos normales de pensión de vejez (hombre y mujer)
- Incremento por semanas adicionales
- Aplicación del salario mínimo
- Tope máximo del 80%
- Pensión de sobreviviente
- Invalidez baja y alta
- Validación de errores

Para ejecutar las pruebas:
python test_calcupension.py
o
python -m unittest

Si todo funciona correctamente aparecerá:

Ran 13 tests
OK
