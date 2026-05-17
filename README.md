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
* **Persistencia en base de datos PostgreSQL** para el registro y consulta de solicitudes de pensión.

El sistema considera el **Salario Mínimo Mensual Legal Vigente (SMMLV)** para validar el valor mínimo de la mesada en pensión de vejez.

---

# Funcionamiento

## Prerrequisitos

Antes de ejecutar el proyecto se debe tener instalado:

* **Python 3.x**
* **Librería Kivy**: Necesaria para la interfaz gráfica. Se instala con:  
  `pip install kivy`
* **psycopg2**: Necesario para la conexión con PostgreSQL. Se instala con:  
  `pip install psycopg2`
* **PostgreSQL**: Motor de base de datos. Descargable desde https://www.postgresql.org/download/
* Acceso a una **consola de comandos** (CMD, PowerShell o Terminal de Linux)

---

## Configuración de la Base de Datos

### 1. Crear la base de datos en PostgreSQL

Conéctese a PostgreSQL y cree una base de datos:

```sql
CREATE DATABASE calcupension;
```

### 2. Configurar las credenciales de conexión

Copie el archivo de ejemplo y renómbrelo:

secret_config_sample.py → secret_config.py

Edite `secret_config.py` con sus datos de conexión:

```python
PGDATABASE = "calcupension"
PGUSER = "su_usuario"
PGPASSWORD = "su_contraseña"
PGHOST = "localhost"
PGPORT = "5432"
```

> ⚠️ El archivo `secret_config.py` está en `.gitignore`. **Nunca lo suba al repositorio.**

### 3. Crear las tablas

Las tablas se crean automáticamente al ejecutar las pruebas unitarias. También puede crearlas manualmente ejecutando el script `sql/crear-solicitudes.sql` desde su cliente de PostgreSQL (psql, pgAdmin, etc.).

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
* **Controlador (acceso a base de datos)**
* **Vista (interfaz de usuario)**
* **Pruebas**

El sistema utiliza:

* unittest para pruebas unitarias
* psycopg2 para la conexión con PostgreSQL

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
    ├── main.py
    ├── calcupension.py
    ├── calcupension.spec
    ├── secret_config_sample.py
    ├── README.md
    ├── .gitignore
    │
    ├── sql/
    │   ├── crear-solicitudes.sql
    │   ├── borrar-solicitudes.sql
    │   └── operaciones-solicitudes.sql
    │
    ├── src/
    │   ├── controller/
    │   │   └── solicitudes_controller.py
    │   ├── model/
    │   │   ├── __init__.py
    │   │   ├── logica_calcupension.py
    │   │   └── solicitudes.py
    │   └── view/
    │       ├── gui/
    │       │   └── gui_calcupension.py
    │       ├── buscar_solicitud.py
    │       ├── consola_calcupension.py
    │       └── guardar_solicitud.py
    │
    ├── docs/
    │   ├── Enlace a la entrevista con experto.docx
    │   └── Pruebas unitarias calcupension.xlsx
    │
    └── test/
        ├── __init__.py
        ├── test_calcupension.py
        └── test_solicitudes.py

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

## controller

Contiene la capa de acceso a datos:

* **SolicitudesPensionController**  
  Gestiona la conexión a PostgreSQL y provee los métodos para crear la tabla, borrarla, insertar solicitudes y buscarlas por ID.

---

## view

Contiene la interfaz de usuario tanto en consola como gráfica:

* Permite ingresar datos de forma intuitiva.
* Crea objetos SolicitudPension.
* Invoca la lógica del modelo.
* Maneja errores mediante excepciones y ventanas emergentes (**Popups**) para evitar cierres inesperados.
* Incluye vistas para guardar y buscar solicitudes en la base de datos.

---

## Carpeta test

Contiene las **pruebas unitarias**:

    test/
        test_calcupension.py
        test_solicitudes.py

Las pruebas de `test_calcupension.py` verifican:

* Cálculo correcto de pensión de vejez
* Diferencias entre hombres y mujeres
* Incrementos por semanas adicionales
* Tope máximo de tasa de reemplazo
* Pensión de sobreviviente
* Pensión de invalidez
* Manejo de excepciones

Las pruebas de `test_solicitudes.py` verifican:

* Inserción y recuperación correcta de solicitudes en la base de datos
* Integridad de los datos para los tres tipos de pensión

> ⚠️ `test_solicitudes.py` borra y recrea la tabla al inicio. Nunca lo ejecute contra una base de datos de producción.

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

Para ejecutar las pruebas de base de datos:

    python test/test_solicitudes.py

o en Windows:

    py test\test_solicitudes.py

El archivo de pruebas incluye:

    import sys
    sys.path.append("src")

Esto permite ubicar los módulos correctamente.

Si todo funciona correctamente:

    Ran 13 tests
    OK