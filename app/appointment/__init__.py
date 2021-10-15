from flask import Blueprint

appointment_blueprints = Blueprint('cita', __name__, template_folder='templates')

from . import routes