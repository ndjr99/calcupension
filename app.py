import sys
sys.path.append("src")

from flask import Flask
from flask import render_template, request

from model.logica_calcupension import CalculadoraPension, SolicitudPension
from model.solicitudes import SolicitudesPension
from controller.solicitudes_controller import SolicitudesPensionController
import random
import datetime
from datetime import date

app = Flask(__name__)

@app.route('/')
def solicitud():
    return render_template('crear_solicitud.html')

@app.route('/guardar_solicitud')
def guardar_solicitud():
    solicitud = SolicitudPension(tipo=request.args['tipo'], ingreso_base_liquidacion=float(request.args['ingreso_base_liquidacion']), semanas=int(request.args['semanas']), genero=request.args['genero'], edad=int(request.args['edad']), porcentaje_perdida_capacidad_laboral=float(request.args['porcentaje_perdida_capacidad_laboral']))
    tasa_reemplazo = CalculadoraPension.calcular_tasa_reemplazo(solicitud)
    mesada = CalculadoraPension.calcular_pension(tasa_reemplazo, solicitud.ingreso_base_liquidacion, solicitud.tipo)

    solicitud_pension = SolicitudesPension(
            id_solicitud=random.randint(0,9999999),
            tipo=request.args['tipo'],
            ingreso_base_liquidacion=float(request.args['ingreso_base_liquidacion']),
            semanas=int(request.args['semanas']),
            genero=request.args['genero'],
            edad=int(request.args['edad']),
            porcentaje_perdida_capacidad_laboral=float(request.args['porcentaje_perdida_capacidad_laboral']),
            fecha=date.today(),
            tasa_reemplazo=tasa_reemplazo,
            mesada=mesada
        )

    # Insertar la solicitud en la base de datos
    SolicitudesPensionController.insertar(solicitud_pension)

    return render_template("guardar_solicitud.html", tasa_reemplazo=tasa_reemplazo, mesada=mesada, tipo=solicitud_pension.tipo, ingreso_base_liquidacion=solicitud_pension.ingreso_base_liquidacion, semanas=solicitud_pension.semanas, genero=solicitud_pension.genero, edad=solicitud_pension.edad, fecha=solicitud_pension.fecha, porcentaje_perdida_capacidad_laboral=solicitud_pension.porcentaje_perdida_capacidad_laboral)
app.run(debug=True)