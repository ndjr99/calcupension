class SolicitudesPension:
    def __init__(self, id_solicitud: int, tipo: str, ingreso_base_liquidacion: float, semanas: int, genero: str, edad: int, porcentaje_pcl: float, fecha: str):
        self.id_solicitud = id_solicitud
        self.tipo = tipo
        self.ingreso_base_liquidacion = ingreso_base_liquidacion
        self.semanas = semanas
        self.genero = genero
        self.edad = edad
        self.porcentaje_pcl = porcentaje_pcl
        self.fecha = fecha

    def is_equal(self, otro) -> bool:
        """ Verifica cada atributo de self contra otra instancia de esta clase y dipara una excepción si no son iguales """
        assert(self.id_solicitud == otro.id_solicitud)
        assert(self.tipo == otro.tipo)
        assert(self.ingreso_base_liquidacion == otro.ingreso_base_liquidacion)
        assert(self.semanas == otro.semanas)
        assert(self.genero == otro.genero)
        assert(self.edad == otro.edad)
        assert(self.porcentaje_pcl == otro.porcentaje_pcl)
        assert(str(self.fecha) == str(otro.fecha))
        return True