from flask import Flask


def create_app():
    app = Flask(__name__)
    
    # Registro de los Blueprints
    from .inicio import inicio_bp
    app.register_blueprint(inicio_bp)
    
    return app
