class SolicitudesPension:
    def __init__(self, id_solicitud: int, tipo: str, ingreso_base_liquidacion: float, semanas: int, genero: str, edad: int, porcentaje_perdida_capacidad_laboral: float, fecha: str, tasa_reemplazo: float = 0, mesada: float = 0):
        self.id_solicitud = id_solicitud
        self.tipo = tipo
        self.ingreso_base_liquidacion = ingreso_base_liquidacion
        self.semanas = semanas
        self.genero = genero
        self.edad = edad
        self.porcentaje_perdida_capacidad_laboral = porcentaje_perdida_capacidad_laboral
        self.fecha = fecha
        self.tasa_reemplazo = tasa_reemplazo
        self.mesada = mesada

    def is_equal(self, otro) -> bool:
        """ Verifica cada atributo de self contra otra instancia de esta clase y dipara una excepción si no son iguales """
        assert(self.id_solicitud == otro.id_solicitud)
        assert(self.tipo == otro.tipo)
        assert(self.ingreso_base_liquidacion == otro.ingreso_base_liquidacion)
        assert(self.semanas == otro.semanas)
        assert(self.genero == otro.genero)
        assert(self.edad == otro.edad)
        assert(self.porcentaje_perdida_capacidad_laboral == otro.porcentaje_perdida_capacidad_laboral)
        assert(str(self.fecha) == str(otro.fecha))
        assert(round(self.tasa_reemplazo, 2) == round(otro.tasa_reemplazo, 2))
        assert(self.mesada == otro.mesada)
        return True