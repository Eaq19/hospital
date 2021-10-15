from flask import Blueprint

user_blueprints = Blueprint('usuario', __name__, template_folder='templates')

from . import routes