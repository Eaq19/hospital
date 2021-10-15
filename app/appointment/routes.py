from flask import  render_template

from . import appointment_blueprints


@appointment_blueprints.route("/cita", methods=['GET'])
def appointment_index():
    return render_template('appointment_index.html')