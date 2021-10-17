from flask import render_template

from . import administrador_blueprints


@administrador_blueprints.route("/administrador", methods=['GET', 'POST'])
def administrador_index():
    return render_template('administrador_index.html')


@administrador_blueprints.route("/citas", methods=['GET', 'POST'])
def citas_administrador():
    return render_template('citas_administrador.html')


@administrador_blueprints.route("/comentarios", methods=['GET', 'POST'])
def comentarios_administrador():
    return render_template('comentarios_administrador.html')


@administrador_blueprints.route("/usuarios", methods=['GET', 'POST'])
def usuarios_administrador():
    return render_template('usuarios_administrador.html')
