# CALCUPENSION

Sistema de cálculo pensional desarrollado en **Python** que permite calcular la **tasa de reemplazo** y la **mesada pensional** según el tipo de pensión.

---

# Fork del proyecto por:

* Jose Manuel Jaramillo Valencia
* Miguel Angel Salazar

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
* **Interfaz Gráfica Amigable** desarrollada en Kivy con manejo de errores mediante Popups.

El sistema considera el **Salario Mínimo Mensual Legal Vigente (SMMLV)** para validar el valor mínimo de la mesada en pensión de vejez.

---

# Funcionamiento

## Prerrequisitos

Antes de ejecutar el proyecto se debe tener instalado:

* **Python 3.x**
* **Librería Kivy**: Necesaria para la interfaz gráfica. Se instala con:  
  `pip install kivy`
* Acceso a una **consola de comandos** (CMD, PowerShell o Terminal de Linux)

---

## Ejecución

### 💻 Interfaz Gráfica (Recomendado)
Para ejecutar la interfaz gráfica desde la línea de comandos, ubíquese en la **carpeta raíz del proyecto** y ejecute:

    python main.py

### ⌨️ Versión de Consola
Para ejecutar la versión original por consola, ejecute alguno de los siguientes comandos:

    python src/view/consola_calcupension.py

o en Windows:

    py src/view/consola_calcupension.py

El sistema mostrará un menú interactivo para ingresar los datos solicitados.

---

# 📱 Versión Móvil (Android)

La aplicación ha sido compilada exitosamente para Android utilizando **Buildozer**.

* **Descarga**: Puede descargar el archivo **.apk** directamente desde la sección de **[Releases](https://github.com/Salas18/calcupension_/releases)** de este repositorio.
* **Instalación**: Una vez descargado, permita la instalación desde fuentes desconocidas en los ajustes de seguridad de su dispositivo móvil.

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

## Carpeta src y Raíz

Contiene el **código fuente de la aplicación**:

    calcupension/
    │
    ├─ main.py                # Punto de entrada para la GUI y Android
    ├─ src/
    │  ├─ model/
    │  │  └─ logica_calcupension.py
    │  └─ view/
    │     └─ consola_calcupension.py
    └─ source/view/           # Archivos de interfaz gráfica Kivy (Clean Code)

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

Contiene la interfaz de usuario tanto en consola como gráfica:

* Permite ingresar datos de forma intuitiva.
* Crea objetos SolicitudPension.
* Invoca la lógica del modelo.
* Maneja errores mediante excepciones y ventanas emergentes (**Popups**) para evitar cierres inesperados.

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
