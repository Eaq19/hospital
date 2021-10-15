from flask import  render_template

from . import doctor_blueprints


@doctor_blueprints.route("/doctor", methods=['GET', 'POST'])
def doctor_index():
    return render_template('doctor_index.html')