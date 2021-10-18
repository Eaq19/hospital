from flask import  render_template

from . import medico_blueprints


@medico_blueprints.route("/medico", methods=['GET', 'POST'])
def medico_index():
    return render_template('medico_index.html')
