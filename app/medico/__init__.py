from flask import Blueprint

medico_blueprints = Blueprint('medico', __name__, template_folder='templates')

from . import routes
