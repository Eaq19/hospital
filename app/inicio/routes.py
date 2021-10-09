from flask import  render_template

from . import inicio_bp


@inicio_bp.route("/")
def inicio():
    return render_template('inicio.html')
