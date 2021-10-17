from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
from autenticacion.models import User
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Registro de los Blueprints
    from .inicio import inicio_blueprints
    app.register_blueprint(inicio_blueprints)

    from .autenticacion import autenticacion_blueprints
    app.register_blueprint(autenticacion_blueprints)
    
    from .paciente import paciente_blueprints
    app.register_blueprint(paciente_blueprints)

    from .administrador import administrador_blueprints
    app.register_blueprint(administrador_blueprints)
    
    from .medico import medico_blueprints
    app.register_blueprint(medico_blueprints)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/hospital'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    login_manager.login_view = "autenticacion.iniciar_sesion"
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

def app_context():
        db.create_all()
        return app