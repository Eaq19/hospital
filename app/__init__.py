from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Registro de los Blueprints
    from .inicio import inicio_blueprints
    app.register_blueprint(inicio_blueprints)

    from .autenticacion import autenticacion_blueprints
    app.register_blueprint(autenticacion_blueprints)
    
    from .paciente import paciente_blueprints
    app.register_blueprint(paciente_blueprints)

    from .appointment import appointment_blueprints
    app.register_blueprint(appointment_blueprints)

    from .doctor import doctor_blueprints
    app.register_blueprint(doctor_blueprints)

    from .user import user_blueprints
    app.register_blueprint(user_blueprints)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    
    login_manager.login_view = "autenticacion.iniciar_sesion"
    login_manager.init_app(app)
    return app
