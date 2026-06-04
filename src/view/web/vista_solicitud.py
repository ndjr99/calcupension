import sys
sys.path.append("src")

from flask import Blueprint
from flask import render_template, request

from model.logica_calcupension import CalculadoraPension, SolicitudPension, ErrorIBL, ErrorSemanasCotizadas, ErrorEdadMinimaHombres, ErrorEdadMinimaMujeres, ErrorPCLInvalidez, ErrorTipoPension, ErrorGenero, ErrorValoresNegativos
from model.solicitudes import SolicitudesPension
from controller.solicitudes_controller import SolicitudesPensionController
import random
import datetime
from datetime import date

blueprint = Blueprint( "vista_usuarios", __name__, "templates")

@blueprint.route('/')
def menu_inicio():
    return render_template('menu_inicio.html')

@blueprint.route('/calcular_pension')
def calcular_pension():
    return render_template('calcular_pension.html')

@blueprint.route('/pension_calculada')
def pension_calculada():
    try:
        solicitud = SolicitudPension(
            tipo=request.args['tipo'],
            ingreso_base_liquidacion=float(request.args['ingreso_base_liquidacion']),
            semanas=int(request.args['semanas']),
            genero=request.args['genero'],
            edad=int(request.args['edad']) if request.args.get('edad') else None,
            porcentaje_perdida_capacidad_laboral=float(request.args.get('porcentaje_perdida_capacidad_laboral') or 0)
        )
        tasa_reemplazo = CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada = CalculadoraPension.calcular_pension(tasa_reemplazo, solicitud.ingreso_base_liquidacion, solicitud.tipo)

    except (ErrorIBL, ErrorSemanasCotizadas, ErrorEdadMinimaHombres,
            ErrorEdadMinimaMujeres, ErrorPCLInvalidez, ErrorTipoPension,
            ErrorGenero, ErrorValoresNegativos) as e:
        return render_template('calcular_pension.html', error=str(e))
    
    except ValueError:
        return render_template('calcular_pension.html', error="Por favor ingrese todos los datos.")

    return render_template('pension_calculada.html', tasa_reemplazo=tasa_reemplazo, mesada=mesada)

@blueprint.route('/crear_solicitud')
def crear_solicitud():
    return render_template('crear_solicitud.html')

@blueprint.route('/crear_tabla')
def crear_tabla():
    SolicitudesPensionController.crear_tabla()
    return "Tabla solicitudes_pension creada exitosamente."

@blueprint.route('/guardar_solicitud')
def guardar_solicitud():
    try:
        solicitud = SolicitudPension(
            tipo=request.args['tipo'],
            ingreso_base_liquidacion=float(request.args['ingreso_base_liquidacion']),
            semanas=int(request.args['semanas']),
            genero=request.args['genero'],
            edad=int(request.args['edad']) if request.args.get('edad') else None,
            porcentaje_perdida_capacidad_laboral=float(request.args.get('porcentaje_perdida_capacidad_laboral') or 0)
        )
        tasa_reemplazo = CalculadoraPension.calcular_tasa_reemplazo(solicitud)
        mesada = CalculadoraPension.calcular_pension(tasa_reemplazo, solicitud.ingreso_base_liquidacion, solicitud.tipo)

    except (ErrorIBL, ErrorSemanasCotizadas, ErrorEdadMinimaHombres,
            ErrorEdadMinimaMujeres, ErrorPCLInvalidez, ErrorTipoPension,
            ErrorGenero, ErrorValoresNegativos) as e:
        return render_template('crear_solicitud.html', error=str(e))
    
    except ValueError:
        return render_template('crear_solicitud.html', error="Por favor ingrese todos los datos.")

    solicitud_pension = SolicitudesPension(
        id_solicitud=random.randint(0, 9999999),
        tipo=request.args['tipo'],
        ingreso_base_liquidacion=float(request.args['ingreso_base_liquidacion']),
        semanas=int(request.args['semanas']),
        genero=request.args['genero'],
        edad=int(request.args['edad']) if request.args.get('edad') else None,
        porcentaje_perdida_capacidad_laboral=float(request.args.get('porcentaje_perdida_capacidad_laboral') or 0),
        fecha=date.today(),
        tasa_reemplazo=tasa_reemplazo,
        mesada=mesada
    )

    SolicitudesPensionController.insertar(solicitud_pension)

    return render_template("guardar_solicitud.html", id_solicitud=solicitud_pension.id_solicitud, tasa_reemplazo=tasa_reemplazo, mesada=mesada, tipo=solicitud_pension.tipo, ingreso_base_liquidacion=solicitud_pension.ingreso_base_liquidacion, semanas=solicitud_pension.semanas, genero=solicitud_pension.genero, edad=solicitud_pension.edad, fecha=solicitud_pension.fecha, porcentaje_perdida_capacidad_laboral=solicitud_pension.porcentaje_perdida_capacidad_laboral)

@blueprint.route('/buscar_solicitud')
def buscar_solicitud():
    return render_template('buscar_solicitud.html')

@blueprint.route('/solicitud_buscada')
def solicitud_buscada():
    id_solicitud = int(request.args['id_solicitud'])
    solicitud = SolicitudesPensionController.buscar_solicitud(id_solicitud)

    if solicitud:
        return render_template('solicitud_buscada.html', id_solicitud=solicitud.id_solicitud, tipo=solicitud.tipo, ingreso_base_liquidacion=solicitud.ingreso_base_liquidacion, semanas=solicitud.semanas, genero=solicitud.genero, edad=solicitud.edad, porcentaje_perdida_capacidad_laboral=solicitud.porcentaje_perdida_capacidad_laboral, fecha=solicitud.fecha, tasa_reemplazo=solicitud.tasa_reemplazo, mesada=solicitud.mesada)
    else:
        return "Solicitud no encontrada."

if __name__ == '__main__':
    blueprint.run(debug=True)