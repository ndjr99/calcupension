CREATE TABLE solicitudes_pension (
    id_solicitud INTEGER PRIMARY KEY NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    ingreso_base_liquidacion NUMERIC(12,2) NOT NULL,
    semanas INTEGER NOT NULL,
    genero VARCHAR(10),
    edad INTEGER,
    porcentaje_perdida_capacidad_laboral NUMERIC(5,2),
    fecha TIMESTAMP NOT NULL,
    tasa_reemplazo NUMERIC(5,2),
    mesada NUMERIC(12,2)
);