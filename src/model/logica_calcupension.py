class ErrorIBL(Exception):
    """Excepción para cuando el IBL no es válido."""
    pass


class ErrorSemanasCotizadas(Exception):
    """Excepción para cuando las semanas cotizadas no son suficientes."""
    pass


class ErrorEdadMinimaHombres(Exception):
    """Excepción para cuando la edad mínima de hombres no se cumple."""
    pass


class ErrorEdadMinimaMujeres(Exception):
    """Excepción para cuando la edad mínima de mujeres no se cumple."""
    pass


class ErrorPCLInvalidez(Exception):
    """Excepción para cuando la PCL no es válida para pensión de invalidez."""
    pass


class ErrorTipoPension(Exception):
    """Excepción para tipo de pensión inválido."""
    pass


class ErrorGenero(Exception):
    """Excepción para género inválido."""
    pass


class ErrorValoresNegativos(Exception):
    """Excepción para valores negativos en parámetros."""
    pass


def calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl):

    smmlv = 1_750_905

    # VALIDACIONES GENERALES
    tipos_validos = ["Vejez", "Sobreviviente", "Invalidez"]
    generos_validos = ["Hombre", "Mujer"]

    if tipo not in tipos_validos:
        raise ErrorTipoPension()

    # El género solo importa en vejez
    if tipo == "Vejez" and genero not in generos_validos:
        raise ErrorGenero()

    if semanas < 0:
        raise ErrorValoresNegativos()

    # edad puede ser None (ej: sobreviviente)
    if edad is not None and edad < 0:
        raise ErrorValoresNegativos()

    if ibl <= 0:
        raise ErrorIBL()

    if tipo == "Vejez" and semanas < 1300:
        raise ErrorSemanasCotizadas()

    if tipo == "Vejez" and genero == "Hombre" and edad is not None and edad < 62:
        raise ErrorEdadMinimaHombres()

    if tipo == "Vejez" and genero == "Mujer" and edad is not None and edad < 57:
        raise ErrorEdadMinimaMujeres()

    # PENSIÓN DE VEJEZ
    if tipo == "Vejez":

        if (genero == "Hombre" and edad >= 62) or (genero == "Mujer" and edad >= 57):

            tasa_reemplazo_base = 65.50 - (ibl / smmlv) * 0.50

            if semanas > 1300:
                incremento = (semanas - 1300) / 50 * 1.5
            else:
                incremento = 0

            tasa_total = tasa_reemplazo_base + incremento

            if tasa_total > 80:
                tasa_total = 80
            elif tasa_total < 55:
                tasa_total = 55

            return tasa_total

    # PENSIÓN DE SOBREVIVIENTE
    elif tipo == "Sobreviviente":

        tasa_reemplazo_base = 45

        if semanas > 500:
            incremento = (semanas - 500) / 50 * 2
        else:
            incremento = 0

        tasa_total = tasa_reemplazo_base + incremento

        if tasa_total > 75:
            tasa_total = 75

        return tasa_total

    # PENSIÓN DE INVALIDEZ
    elif tipo == "Invalidez":

        if pcl <= 50:
            raise ErrorPCLInvalidez()

        if pcl > 50 and pcl <= 66:

            tasa_reemplazo_base = 45

            if semanas > 500:
                incremento = (semanas - 500) / 50 * 1.5
            else:
                incremento = 0

        elif pcl > 66:

            tasa_reemplazo_base = 54

            if semanas > 500:
                incremento = (semanas - 500) / 50 * 2
            else:
                incremento = 0

        tasa_total = tasa_reemplazo_base + incremento

        if tasa_total > 75:
            tasa_total = 75
        elif tasa_total < 45:
            tasa_total = 45

        return tasa_total


def calcular_pension(tasa_total, ibl, tipo):

    smmlv = 1_750_905

    mesada = (tasa_total / 100) * ibl

    if tipo == "Vejez" and mesada < smmlv:
        mesada = smmlv

    return mesada