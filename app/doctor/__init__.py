from flask import Blueprint

doctor_blueprints = Blueprint('doctor', __name__, template_folder='templates')

from . import routes