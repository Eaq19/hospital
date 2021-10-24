from flask import render_template, request

from app.autenticacion.models import User
from . import administrador_blueprints


@administrador_blueprints.route("/administrador", methods=['GET', 'POST'])
def administrador_index():
    return render_template('administrador_index.html')


# lista de usuarios
ROWS_PER_PAGE = 5

@administrador_blueprints.route("/usuarios", methods=['GET', 'POST'])
def usuarios_administrador():
    page = request.args.get('page', 1, type=int)
    
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    
    return render_template('usuarios_administrador.html', users=users.items)


# lista de citas
@administrador_blueprints.route("/citas", methods=['GET', 'POST'])
def citas_administrador():
    return render_template('citas_administrador.html')


# lista de comentarios
@administrador_blueprints.route("/comentarios", methods=['GET', 'POST'])
def comentarios_administrador():
    return render_template('comentarios_administrador.html')
