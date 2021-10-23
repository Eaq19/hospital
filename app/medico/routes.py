from flask import render_template

from . import medico_blueprints


@medico_blueprints.route("/medico", methods=['GET', 'POST'])
def medico_index():
    return render_template('medico_index.html')


@medico_blueprints.route("/citasMedico", methods=['GET', 'POST'])
def citas_medico():
    return render_template('citas_medico.html')


@medico_blueprints.route("/comentariosMedico", methods=['GET', 'POST'])
def comentarios_medico():
    return render_template('comentarios_medico.html')
