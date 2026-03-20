class ErrorIBL(Exception):
    """
    Excepción personalizada para indicar que el IBL es inválido.
    Se lanza cuando el ingreso base de liquidación es menor o igual a cero.
    """

    def __init__(self, ibl):
        """
        Parámetros:
        -----------
        ibl : float
            Ingreso Base de Liquidación ingresado.
        """
        super().__init__(f"ErrorIBL: IBL inválido ({ibl}). Debe ser mayor que 0.")


class ErrorSemanasCotizadas(Exception):
    """
    Excepción personalizada para indicar que las semanas cotizadas son insuficientes.
    """

    def __init__(self, semanas):
        """
        Parámetros:
        -----------
        semanas : int
            Número de semanas cotizadas.
        """
        super().__init__(f"ErrorSemanasCotizadas: semanas insuficientes ({semanas}).")


class ErrorEdadMinimaHombres(Exception):
    """
    Excepción personalizada para indicar que la edad mínima de hombres no se cumple.
    """

    def __init__(self, edad):
        """
        Parámetros:
        -----------
        edad : int
            Edad del afiliado.
        """
        super().__init__(f"ErrorEdadMinimaHombres: edad inválida ({edad}).")


class ErrorEdadMinimaMujeres(Exception):
    """
    Excepción personalizada para indicar que la edad mínima de mujeres no se cumple.
    """

    def __init__(self, edad):
        """
        Parámetros:
        -----------
        edad : int
            Edad del afiliado.
        """
        super().__init__(f"ErrorEdadMinimaMujeres: edad inválida ({edad}).")


class ErrorPCLInvalidez(Exception):
    """
    Excepción personalizada para indicar que la PCL no es válida.
    """

    def __init__(self, pcl):
        """
        Parámetros:
        -----------
        pcl : float
            Porcentaje de pérdida de capacidad laboral.
        """
        super().__init__(f"ErrorPCLInvalidez: PCL inválido ({pcl}).")


class ErrorTipoPension(Exception):
    """
    Excepción personalizada para indicar que el tipo de pensión es inválido.
    """

    def __init__(self, tipo):
        tipos_validos = ["Vejez", "Sobreviviente", "Invalidez"]
        super().__init__(f"Tipo inválido: {tipo}. Valores válidos: {tipos_validos}")


class ErrorGenero(Exception):
    """
    Excepción personalizada para indicar que el género es inválido.
    """

    def __init__(self, genero):
        generos_validos = ["Hombre", "Mujer"]
        super().__init__(f"Género inválido: {genero}. Valores válidos: {generos_validos}")


class ErrorValoresNegativos(Exception):
    """
    Excepción personalizada para indicar valores negativos en parámetros.
    """

    def __init__(self, valor, nombre):
        super().__init__(f"{nombre} negativo: {valor}")


class SolicitudPension:
    """
    Representa una solicitud de cálculo de pensión.

    Agrupa todos los parámetros necesarios para evitar funciones con muchos argumentos
    (solución al issue de clean code).
    """

    def __init__(self, tipo, ibl, semanas, genero, edad, pcl):
        self.tipo = tipo
        self.ibl = ibl
        self.semanas = semanas
        self.genero = genero
        self.edad = edad
        self.pcl = pcl


class CalculadoraPension:
    """
    Clase para realizar cálculos pensionales.

    Encapsula la lógica de validación y cálculo, siguiendo el principio
    de responsabilidad única y el estilo del profesor.
    """

    def calcular_tasa_reemplazo(solicitud: SolicitudPension):
        """
        Calcula la tasa de reemplazo pensional según el tipo de pensión.

        Parámetros:
        -----------
        solicitud : SolicitudPension
            Objeto con todos los datos del afiliado.

        Retorna:
        --------
        float:
            Tasa de reemplazo calculada (en porcentaje).

        Descripción:
        ------------
        - Vejez: requiere edad y semanas mínimas.
        - Sobreviviente: tasa base con incremento por semanas.
        - Invalidez: depende del PCL.
        """

        smmlv = 1_750_905

        CalculadoraPension.check_tipo(solicitud.tipo)
        CalculadoraPension.check_valores(solicitud)
        CalculadoraPension.check_ibl(solicitud.ibl)

        if solicitud.tipo == "Vejez":
            CalculadoraPension.check_semanas(solicitud.semanas)
            CalculadoraPension.check_edad(solicitud.genero, solicitud.edad)

        if solicitud.tipo == "Invalidez":
            CalculadoraPension.check_pcl(solicitud.pcl)

        if solicitud.tipo == "Vejez":

            tasa_reemplazo_base = 65.50 - (solicitud.ibl / smmlv) * 0.50

            if solicitud.semanas > 1300:
                incremento = (solicitud.semanas - 1300) / 50 * 1.5
            else:
                incremento = 0

            tasa_total = tasa_reemplazo_base + incremento

            if tasa_total > 80:
                tasa_total = 80
            elif tasa_total < 55:
                tasa_total = 55

            return tasa_total

        elif solicitud.tipo == "Sobreviviente":

            tasa_reemplazo_base = 45

            if solicitud.semanas > 500:
                incremento = (solicitud.semanas - 500) / 50 * 2
            else:
                incremento = 0

            tasa_total = tasa_reemplazo_base + incremento

            if tasa_total > 75:
                tasa_total = 75

            return tasa_total

        elif solicitud.tipo == "Invalidez":

            if solicitud.pcl <= 66:
                tasa_reemplazo_base = 45

                if solicitud.semanas > 500:
                    incremento = (solicitud.semanas - 500) / 50 * 1.5
                else:
                    incremento = 0
            else:
                tasa_reemplazo_base = 54

                if solicitud.semanas > 500:
                    incremento = (solicitud.semanas - 500) / 50 * 2
                else:
                    incremento = 0

            tasa_total = tasa_reemplazo_base + incremento

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
        ibl : float
        tipo : str

        Retorna:
        --------
        float:
            Valor de la mesada pensional.
        """

        smmlv = 1_750_905

        mesada = (tasa_total / 100) * ibl

        if tipo == "Vejez" and mesada < smmlv:
            mesada = smmlv

        return mesada

    def check_tipo(tipo):
        tipos_validos = ["Vejez", "Sobreviviente", "Invalidez"]
        if tipo not in tipos_validos:
            raise ErrorTipoPension(tipo)

    def check_valores(solicitud):
        if solicitud.semanas < 0:
            raise ErrorValoresNegativos(solicitud.semanas, "semanas")

        if solicitud.edad is not None and solicitud.edad < 0:
            raise ErrorValoresNegativos(solicitud.edad, "edad")

    def check_ibl(ibl):
        if ibl <= 0:
            raise ErrorIBL(ibl)

    def check_semanas(semanas):
        if semanas < 1300:
            raise ErrorSemanasCotizadas(semanas)

    def check_edad(genero, edad):
        if genero == "Hombre" and edad < 62:
            raise ErrorEdadMinimaHombres(edad)

        if genero == "Mujer" and edad < 57:
            raise ErrorEdadMinimaMujeres(edad)

    def check_pcl(pcl):
        if pcl <= 50:
            raise ErrorPCLInvalidez(pcl)