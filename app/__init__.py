from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    login_manager.init_app(app)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

    # Registro de los Blueprints
    from .inicio import inicio_blueprints
    app.register_blueprint(inicio_blueprints)

    from .autenticacion import autenticacion_blueprints
    app.register_blueprint(autenticacion_blueprints)

    return app
