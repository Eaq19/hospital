from flask import render_template

from . import paciente_blueprints


@paciente_blueprints.route("/paciente", methods=['GET', 'POST'])
def paciente_index():
    return render_template('paciente_index.html')


@paciente_blueprints.route("/citasPaciente", methods=['GET', 'POST'])
def citas_paciente():
    return render_template('citas_paciente.html')


@paciente_blueprints.route("/comentariosPaciente", methods=['GET', 'POST'])
def comentarios_paciente():
    return render_template('comentarios_paciente.html')
