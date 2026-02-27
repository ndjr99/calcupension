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

def calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl):
    """
    Calcula la tasa de reemplazo pensional según el tipo de pensión.

    Parámetros:
    -----------
    tipo : str
        Tipo de pensión. Puede ser:
        - "Vejez"
        - "Sobreviviente"
        - "Invalidez"

    ibl : float
        Ingreso Base de Liquidación (IBL) del afiliado.
        Debe ser mayor a 0.

    semanas : int
        Número total de semanas cotizadas.

    genero : str
        Género del afiliado. Puede ser:
        - "Hombre"
        - "Mujer"

    edad : int
        Edad actual del afiliado.

    pcl : float
        Porcentaje de Pérdida de Capacidad Laboral.
        Solo aplica para pensión por invalidez.

    Retorna:
    --------
    float:
        Tasa de reemplazo calculada (en porcentaje).

    str:
        Mensaje de error si no se cumplen los requisitos mínimos.
    
    Descripción:
    ------------
    - Para pensión de vejez:
        * Requiere mínimo 1300 semanas.
        * Edad mínima: 62 años (Hombre) o 57 años (Mujer).
        * La tasa base se calcula con fórmula dependiente del IBL.
        * Se incrementa por semanas adicionales.
        * Tiene límites entre 55% y 80%.

    - Para pensión de sobreviviente:
        * Tasa base del 45%.
        * Incremento por semanas superiores a 500.
        * Tope máximo del 75%.

    - Para pensión de invalidez:
        * Depende del porcentaje de pérdida de capacidad laboral (PCL).
        * PCL entre 50% y 66% → tasa base 45%.
        * PCL mayor a 66% → tasa base 54%.
        * Incremento por semanas superiores a 500.
        * Límite entre 45% y 75%.
    """

    smmlv = 1_750_905

    if ibl <= 0:
        raise error_ibl()

    if tipo == "Vejez" and semanas < 1300:
        raise error_semanas_cotizadas()

    if tipo == "Vejez" and genero == "Hombre" and edad < 62:
        raise error_edad_minima_hombres()

    if tipo == "Vejez" and genero == "Mujer" and edad < 57:
        raise error_edad_minima_mujeres()

    if tipo == "Vejez":
        if (genero == "Hombre" and edad >= 62) or (genero == "Mujer" and edad >= 57):
            
            r = 65.50 - (ibl / smmlv) * 0.50
            if semanas > 1300:
                incremento = (semanas - 1300) / 50 * 1.5
            else:
                incremento = 0
            tasa_total = r + incremento
            if tasa_total > 80:
                tasa_total = 80
            elif tasa_total < 55:
                tasa_total = 55

            return tasa_total
    
    elif tipo == "Sobreviviente":
        r = 45
        if semanas > 500:
            incremento = (semanas - 500) / 50 * 2
        else:
            incremento = 0
        tasa_total = r + incremento
        if tasa_total > 75:
            tasa_total = 75

        return tasa_total
    
    elif tipo == "Invalidez":
        if pcl <= 50:
            raise error_pcl_invalidez()

        if pcl > 50 and pcl <= 66:
            r = 45
            if semanas > 500:
                incremento = (semanas - 500) / 50 * 1.5
            else:
                incremento = 0

        elif pcl > 66:
            r = 54
            if semanas > 500:
                incremento = (semanas - 500) / 50 * 2
            else:
                incremento = 0
        tasa_total = r + incremento
        if tasa_total > 75:
            tasa_total = 75
        elif tasa_total < 45:
            tasa_total = 45

        return tasa_total


def calcular_pension(tasa_total, ibl, tipo):
    """
    Calcula el valor de la mesada pensional.

    Parámetros:
    -----------
    tasa_total : float
        Tasa de reemplazo calculada (porcentaje).

    ibl : float
        Ingreso Base de Liquidación.

    tipo : str
        Tipo de pensión ("Vejez", "Sobreviviente", "Invalidez").

    Retorna:
    --------
    float:
        Valor de la mesada pensional.

    Descripción:
    ------------
    - La mesada se calcula aplicando la tasa de reemplazo al IBL.
    - En pensión de vejez, si el valor calculado es inferior al
      salario mínimo mensual legal vigente (SMMLV),
      se ajusta al valor del SMMLV.
    """

    smmlv = 1_750_905
    mesada = (tasa_total / 100) * ibl
    if tipo == "Vejez" and mesada < smmlv:
        mesada = smmlv
    return mesada