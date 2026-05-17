CREATE TABLE resultados_calculo (
    id_resultado INTEGER PRIMARY KEY NOT NULL,
    id_solicitud INTEGER NOT NULL,
    tasa_reemplazo NUMERIC(5,2) NOT NULL,
    mesada NUMERIC(15,2) NOT NULL,

    FOREIGN KEY(id_solicitud)
        REFERENCES solicitudes_pension(id_solicitud)
);