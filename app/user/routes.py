from flask import  render_template

from . import user_blueprints


@user_blueprints.route("/usuario", methods=['GET'])
def user_index():
    return render_template('user_index.html')

@user_blueprints.route("/usuario/perfil", methods=['GET'])
def profile_index():
    return render_template('profile.html')