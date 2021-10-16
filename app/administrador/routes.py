from flask import  render_template

from . import administrador_blueprints


@administrador_blueprints.route("/administrador", methods=['GET', 'POST'])
def administrador_index():
    return render_template('administrador_index.html')
