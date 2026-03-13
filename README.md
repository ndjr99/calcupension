# CALCUPENSION

Sistema de cálculo pensional desarrollado en **Python** que permite calcular la **tasa de reemplazo** y la **mesada pensional** según el tipo de pensión.

Este proyecto fue modificado en un **fork por BillVelasquez**.

---

# ¿Quién hizo esto?

Autores del proyecto:

* Francisco Gómez Gutiérrez
* Nelson David Jiménez Ruiz

---

# ¿Qué es y para qué es?

CALCUPENSION es una aplicación que permite calcular el valor de una pensión de acuerdo con diferentes tipos de prestación del sistema pensional.

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

El proyecto también incluye validaciones de reglas de negocio mediante **excepciones personalizadas** y **pruebas unitarias automatizadas**.

---

# ¿Cómo lo hago funcionar?

## Prerrequisitos

Antes de ejecutar el proyecto se debe tener instalado:

* **Python 3.x**
* Acceso a una **consola de comandos** (CMD o PowerShell)

No se requieren bibliotecas externas adicionales.

---

## Ejecución

Para ejecutar el programa **por fuera del entorno de desarrollo**, siga los siguientes pasos.

1. Abra una consola de comandos.
2. Ubíquese en la **carpeta raíz del proyecto**.

Ejecute el siguiente comando:

```
py src/view/consola_calcupension.py
```

El sistema mostrará un menú interactivo:

```
===================================
     SISTEMA DE CÁLCULO PENSIONAL
===================================
1. Pensión de Vejez
2. Pensión de Sobreviviente
3. Pensión de Invalidez
4. Salir
```

El usuario deberá ingresar los datos solicitados para realizar el cálculo.

Al finalizar, el sistema mostrará:

* Tasa de reemplazo
* Valor de la mesada pensional

Ejemplo de salida:

```
----------- RESULTADO -----------
Tasa de reemplazo: 65.5%
Mesada pensional: $1,900,000
---------------------------------
```

---

# ¿Cómo está hecho?

El proyecto está desarrollado en **Python** siguiendo una estructura modular separando:

* **Lógica del negocio**
* **Interfaz de usuario**
* **Pruebas**

El sistema utiliza la biblioteca estándar de Python:

* `unittest` para pruebas unitarias.

También implementa:

* Validaciones de reglas del negocio
* Excepciones personalizadas
* Separación por capas de la aplicación.

---

# Organización de los módulos

## Carpeta src

Contiene el **código fuente de la aplicación** organizado por capas.

```
src/
│
├─ model/
│   logica_calcupension.py
│
├─ view/
│   consola_calcupension.py
```

### model

Contiene la **lógica del cálculo pensional**, incluyendo:

* cálculo de tasa de reemplazo
* cálculo de mesada pensional
* validaciones del sistema
* excepciones personalizadas

### view

Contiene la **interfaz de consola** que permite al usuario interactuar con el sistema.

---

## Carpeta tests

Contiene las **pruebas unitarias** del sistema.

```
tests/
test_calcupension.py
```

Las pruebas verifican:

* cálculo correcto de pensión de vejez
* cálculo para hombres y mujeres
* incrementos por semanas adicionales
* tope máximo de tasa de reemplazo
* pensión de sobreviviente
* pensión de invalidez
* validaciones de errores

---

# Importante sobre los módulos

Cada carpeta de código fuente debe contener un archivo:

```
__init__.py
```

Este archivo permite que **Python reconozca la carpeta como un módulo** y permite realizar importaciones entre los distintos componentes del proyecto.

---

# Uso

## Ejecutar pruebas unitarias

Para ejecutar las pruebas desde la **carpeta raíz del proyecto**, utilice:

```
py tests\test_calcupension.py
```

Para poder ejecutar las pruebas desde la carpeta raíz, el módulo de pruebas incluye las siguientes líneas al inicio:

```
import sys
sys.path.append("src")
```

Esto permite indicar a Python la **ruta donde se encuentran los módulos del proyecto**.

Si todas las pruebas pasan correctamente aparecerá un resultado similar a:

```
Ran 13 tests
OK
```
