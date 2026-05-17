-- Traer todas las solicitudes de pensión
SELECT id_solicitud,
       tipo,
       ingreso_base_liquidacion,
       semanas,
       genero,
       edad,
       porcentaje_pcl,
       fecha
FROM public.solicitudes_pension
LIMIT 1000;

-- Insertar una solicitud de pensión
INSERT INTO solicitudes_pension (id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_pcl, fecha)
VALUES (1, 'Vejez', 5000000, 1300, 'Hombre', 65, NULL, '2026-06-01 10:00:00');

-- Buscar la solicitud de pensión con el id 1
SELECT id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_pcl, fecha
from solicitudes_pension
where id_solicitud = 1;

-- Insertar otra solicitud de pensión con id 2
insert into solicitudes_pension (id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_pcl, fecha)
Values (2, 'Invalidez', 3000000, 800, 'Mujer', 45, 70.0, '2026-06-02 11:30:00');

-- Buscar la solicitud de pensión con el id 2
SELECT id_solicitud, tipo, ingreso_base_liquidacion, semanas, genero, edad, porcentaje_pcl, fecha
from solicitudes_pension
where id_solicitud = 2;