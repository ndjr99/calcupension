# CALCUPENSION

Sistema de cálculo pensional desarrollado en **Python** que permite calcular la **tasa de reemplazo** y la **mesada pensional** según el tipo de pensión.

---

# Autores del proyecto:

* Francisco Gómez Gutiérrez
* Nelson David Jiménez Ruiz

---

# Descripción

CALCUPENSION es una aplicación que permite calcular la **tasa de reemplazo** y el **valor de la mesada pensional** de acuerdo con diferentes tipos de prestación del sistema pensional.

El sistema permite calcular:

* Pensión de Vejez
* Pensión de Sobreviviente
* Pensión de Invalidez

A partir de información como:

* IBL (Ingreso Base de Liquidación)
* Semanas cotizadas
* Edad
* Género
* PCL (Porcentaje de pérdida de capacidad laboral)

El sistema calcula:

* La **tasa de reemplazo**
* La **mesada pensional estimada**

El proyecto implementa:

* **Programación Orientada a Objetos (POO)**
* Validaciones de reglas de negocio mediante **excepciones personalizadas**
* **Pruebas unitarias automatizadas**

El sistema considera el **Salario Mínimo Mensual Legal Vigente (SMMLV)** para validar el valor mínimo de la mesada en pensión de vejez.

---

# Funcionamiento

## Prerrequisitos

Antes de ejecutar el proyecto se debe tener instalado:

* **Python 3.x**
* Acceso a una **consola de comandos** (CMD o PowerShell)

No se requieren bibliotecas externas adicionales.

---

## Ejecución

Para ejecutar el programa **por fuera del entorno de desarrollo**, siga los siguientes pasos:

1. Abra una consola de comandos.
2. Ubíquese en la **carpeta raíz del proyecto**.

Ejecute alguno de los siguientes comandos:

    python src/view/consola_calcupension.py

o en Windows:

    py src/view/consola_calcupension.py

El sistema mostrará un menú interactivo:

    ===================================
         SISTEMA DE CÁLCULO PENSIONAL
    ===================================
    1. Pensión de Vejez
    2. Pensión de Sobreviviente
    3. Pensión de Invalidez
    4. Salir

El usuario deberá ingresar los datos solicitados para realizar el cálculo.

Al finalizar, el sistema mostrará:

* Tasa de reemplazo
* Valor de la mesada pensional

Ejemplo de salida:

    ----------- RESULTADO -----------
    Tasa de reemplazo: 65.5%
    Mesada pensional: $1,900,000
    ---------------------------------

---

# Desarrollo

El proyecto está desarrollado en **Python** siguiendo una estructura modular y orientada a objetos, separando:

* **Modelo (lógica del negocio)**
* **Vista (interfaz de usuario)**
* **Pruebas**

El sistema utiliza:

* unittest para pruebas unitarias

También implementa:

* Encapsulamiento de datos mediante clases
* Validaciones centralizadas
* Excepciones personalizadas
* Separación por capas

---

# Organización de los módulos

## Carpeta src

Contiene el **código fuente de la aplicación**:

    src/
    │
    ├─ model/
    │   logica_calcupension.py
    │
    ├─ view/
        consola_calcupension.py

---

## model

Contiene la lógica del sistema, incluyendo:

### Clases principales:

* SolicitudPension  
  Representa los datos de entrada del afiliado.

* CalculadoraPension  
  Contiene los métodos para:
  - Calcular tasa de reemplazo  
  - Calcular mesada pensional  
  - Validar reglas del sistema  

También incluye:

* Excepciones personalizadas
* Métodos de validación (check_*)

---

## view

Contiene la interfaz de usuario en consola:

* Permite ingresar datos
* Crea objetos SolicitudPension
* Invoca la lógica del modelo
* Maneja errores mediante excepciones

---

## Carpeta test

Contiene las **pruebas unitarias**:

    test/
        test_calcupension.py

Las pruebas verifican:

* Cálculo correcto de pensión de vejez
* Diferencias entre hombres y mujeres
* Incrementos por semanas adicionales
* Tope máximo de tasa de reemplazo
* Pensión de sobreviviente
* Pensión de invalidez
* Manejo de excepciones

---

# Importante sobre los módulos

Cada carpeta debe contener:

    __init__.py

Esto permite que Python reconozca las carpetas como módulos.

---

# Uso

## Ejecutar pruebas unitarias

Desde la carpeta raíz:

    python test/test_calcupension.py

o en Windows:

    py test\test_calcupension.py

El archivo de pruebas incluye:

    import sys
    sys.path.append("src")

Esto permite ubicar los módulos correctamente.

Si todo funciona correctamente:

    Ran 13 tests
    OK