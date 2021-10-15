from flask import  render_template

from . import paciente_blueprints


@paciente_blueprints.route("/paciente", methods=['GET', 'POST'])
def paciente_index():
    return render_template('paciente_index.html')