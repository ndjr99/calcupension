class error_ibl(Exception):
    """Excepción para cuando el IBL no es válido."""
    pass


class error_semanas_cotizadas(Exception):
    """Excepción para cuando las semanas cotizadas no son suficientes."""
    pass


class error_edad_minima_hombres(Exception):
    """Excepción para cuando la edad mínima de hombres no se cumple."""
    pass


class error_edad_minima_mujeres(Exception):
    """Excepción para cuando la edad mínima de mujeres no se cumple."""
    pass


class error_pcl_invalidez(Exception):
    """Excepción para cuando la PCL no es válida para pensión de invalidez."""
    pass


class error_tipo_pension(Exception):
    """Excepción para tipo de pensión inválido."""
    pass


class error_genero(Exception):
    """Excepción para género inválido."""
    pass


class error_valores_negativos(Exception):
    """Excepción para valores negativos en parámetros."""
    pass


def calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl):

    smmlv = 1_750_905

    # VALIDACIONES GENERALES
    tipos_validos = ["Vejez", "Sobreviviente", "Invalidez"]
    generos_validos = ["Hombre", "Mujer"]

    if tipo not in tipos_validos:
        raise error_tipo_pension()

    # El género solo importa en vejez
    if tipo == "Vejez" and genero not in generos_validos:
        raise error_genero()

    if semanas < 0:
        raise error_valores_negativos()

    # edad puede ser None (ej: sobreviviente)
    if edad is not None and edad < 0:
        raise error_valores_negativos()

    if ibl <= 0:
        raise error_ibl()

    if tipo == "Vejez" and semanas < 1300:
        raise error_semanas_cotizadas()

    if tipo == "Vejez" and genero == "Hombre" and edad is not None and edad < 62:
        raise error_edad_minima_hombres()

    if tipo == "Vejez" and genero == "Mujer" and edad is not None and edad < 57:
        raise error_edad_minima_mujeres()

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
            raise error_pcl_invalidez()

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