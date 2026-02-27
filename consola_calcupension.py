import logica_calcupension


def mostrar_menu_principal():
    print("\n===================================")
    print("     SISTEMA DE CÁLCULO PENSIONAL")
    print("===================================")
    print("1. Pensión de Vejez")
    print("2. Pensión de Sobreviviente")
    print("3. Pensión de Invalidez")
    print("4. Salir")


def solicitar_genero():
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
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "4":
            print("\nSaliendo del sistema...")
            break

        try:
            ibl = float(input("\nIngrese el IBL: "))
            semanas = int(input("Ingrese semanas cotizadas: "))
            genero = solicitar_genero()

            edad = None
            pcl = 0

            if opcion == "1":  # Vejez
                tipo = "Vejez"
                edad = int(input("Ingrese la edad: "))

            elif opcion == "2":  # Sobreviviente
                tipo = "Sobreviviente"

            elif opcion == "3":  # Invalidez
                tipo = "Invalidez"
                edad = int(input("Ingrese la edad: "))
                pcl = float(input("Ingrese el porcentaje de PCL: "))

            else:
                print("Opción inválida.")
                continue

            tasa = logica_calcupension.calcular_tasa_reemplazo(
                tipo, ibl, semanas, genero, edad, pcl
            )

            mesada = logica_calcupension.calcular_pension(
                tasa, ibl, tipo
            )

            print("\n----------- RESULTADO -----------")
            print(f"Tasa de reemplazo: {round(tasa, 2)}%")
            print(f"Mesada pensional: ${round(mesada):,.0f}")
            print("---------------------------------")

        except logica_calcupension.error_ibl:
            print("Error: El IBL debe ser mayor a 0.")

        except logica_calcupension.error_semanas_cotizadas:
            print("Error: No cumple con las 1300 semanas mínimas.")

        except logica_calcupension.error_edad_minima_hombres:
            print("Error: Hombre menor de 62 años.")

        except logica_calcupension.error_edad_minima_mujeres:
            print("Error: Mujer menor de 57 años.")

        except logica_calcupension.error_pcl_invalidez:
            print("Error: La PCL debe ser mayor al 50%.")

        except ValueError:
            print("Error: Entrada inválida. Verifique los datos.")


if __name__ == "__main__":
    main()