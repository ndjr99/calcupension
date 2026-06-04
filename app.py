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

from view.web import vista_solicitud

app = Flask(__name__)

app.register_blueprint( vista_solicitud.blueprint )

if __name__ == '__main__':
    app.run(debug=True)
