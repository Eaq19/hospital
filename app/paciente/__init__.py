from flask import Blueprint

paciente_blueprints = Blueprint('paciente', __name__, template_folder='templates')

from . import routes