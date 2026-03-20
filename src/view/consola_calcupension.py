"""
Módulo de interfaz por consola para el sistema de cálculo pensional.

Este programa permite al usuario interactuar con el sistema de cálculo
de pensiones mediante un menú en consola.

Funcionalidades:
----------------
- Selección del tipo de pensión (Vejez, Sobreviviente, Invalidez)
- Ingreso de datos del afiliado
- Validación básica de entradas
- Cálculo de tasa de reemplazo
- Cálculo de mesada pensional
- Manejo de errores mediante excepciones personalizadas

Dependencias:
-------------
- Módulo logica_calcupension (modelo del sistema)
"""

import sys
sys.path.append("src")
from model import logica_calcupension


def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema.

    Opciones:
    ---------
    1. Pensión de Vejez
    2. Pensión de Sobreviviente
    3. Pensión de Invalidez
    4. Salir
    """
    print("\n===================================")
    print("     SISTEMA DE CÁLCULO PENSIONAL")
    print("===================================")
    print("1. Pensión de Vejez")
    print("2. Pensión de Sobreviviente")
    print("3. Pensión de Invalidez")
    print("4. Salir")


def solicitar_genero():
    """
    Solicita al usuario seleccionar el género.

    Retorna:
    --------
    str:
        "Hombre" o "Mujer"

    Raises:
    -------
    ValueError:
        Si el usuario ingresa una opción inválida.
    """
    print("\nSeleccione género:")
    print("1. Hombre")
    print("2. Mujer")

    opcion = input("Opción: ")

    if opcion == "1":
        return "Hombre"
    elif opcion == "2":
        return "Mujer"
    else:
        raise ValueError("Género inválido")


def main():
    """
    Función principal del sistema.

    Controla el flujo del programa:
    - Muestra el menú
    - Solicita datos al usuario
    - Ejecuta los cálculos
    - Maneja errores

    El programa se ejecuta en bucle hasta que el usuario decide salir.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "4":
            print("\nSaliendo del sistema...")
            break

        try:
            # =========================
            # VALIDACIÓN DE IBL
            # =========================
            ibl = float(input("\nIngrese el IBL: "))
            if ibl <= 0:
                print("Error: El IBL debe ser mayor a 0.")
                continue

            # =========================
            # VALIDACIÓN DE SEMANAS
            # =========================
            semanas = int(input("Ingrese semanas cotizadas: "))
            if semanas < 0:
                print("Error: No se permiten semanas negativas.")
                continue

            # Valores por defecto
            edad = None
            pcl = 0
            genero = None

            # =========================
            # TIPO DE PENSIÓN
            # =========================
            if opcion == "1":  # Vejez
                tipo = "Vejez"

                try:
                    genero = solicitar_genero()
                except ValueError:
                    print("Error: Género inválido.")
                    continue

                edad = int(input("Ingrese la edad: "))
                if edad < 0:
                    print("Error: La edad no puede ser negativa.")
                    continue

            elif opcion == "2":  # Sobreviviente
                tipo = "Sobreviviente"

            elif opcion == "3":  # Invalidez
                tipo = "Invalidez"

                edad = int(input("Ingrese la edad: "))
                if edad < 0:
                    print("Error: La edad no puede ser negativa.")
                    continue

                pcl = float(input("Ingrese el porcentaje de PCL: "))
                if pcl < 0:
                    print("Error: La PCL no puede ser negativa.")
                    continue

            else:
                print("Opción inválida.")
                continue

            # =========================
            # CREACIÓN DEL OBJETO
            # =========================
            solicitud = logica_calcupension.SolicitudPension(
                tipo, ibl, semanas, genero, edad, pcl
            )

            # =========================
            # CÁLCULOS (LÓGICA)
            # =========================
            tasa = logica_calcupension.CalculadoraPension.calcular_tasa_reemplazo(solicitud)

            mesada = logica_calcupension.CalculadoraPension.calcular_pension(
                tasa, ibl, tipo
            )

            # =========================
            # RESULTADO
            # =========================
            print("\n----------- RESULTADO -----------")
            print(f"Tasa de reemplazo: {round(tasa, 2)}%")
            print(f"Mesada pensional: ${round(mesada):,.0f}")
            print("---------------------------------")

        # =========================
        # MANEJO DE ERRORES
        # =========================
        except logica_calcupension.ErrorIBL:
            print("Error: El IBL debe ser mayor a 0.")

        except logica_calcupension.ErrorSemanasCotizadas:
            print("Error: No cumple con las 1300 semanas mínimas.")

        except logica_calcupension.ErrorEdadMinimaHombres:
            print("Error: Hombre menor de 62 años.")

        except logica_calcupension.ErrorEdadMinimaMujeres:
            print("Error: Mujer menor de 57 años.")

        except logica_calcupension.ErrorPCLInvalidez:
            print("Error: La PCL debe ser mayor al 50%.")

        except logica_calcupension.ErrorTipoPension:
            print("Error: Tipo de pensión inválido.")

        except logica_calcupension.ErrorGenero:
            print("Error: Género inválido.")

        except logica_calcupension.ErrorValoresNegativos:
            print("Error: No se permiten valores negativos.")

        except ValueError:
            print("Error: Entrada inválida. Verifique los datos.")


if __name__ == "__main__":
    """
    Punto de entrada del programa.

    Ejecuta la función principal del sistema de consola.
    """
    main()