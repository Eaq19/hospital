from .models import get_user
from flask import (render_template, redirect, url_for, request, current_app)
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
from . import autenticacion_blueprints
from .forms import InciarSesionForm, CrearUsuarioForm

from .models import User

# crear_cuenta
@autenticacion_blueprints.route("/crear_cuenta", methods=['GET', 'POST'])
def crear_cuenta():

    if current_user.is_authenticated:
        return redirect(url_for('paciente.paciente_index'))

    form = CrearUsuarioForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        #user = User(len(users) + 1, nombre, apellido, password)
        #users.append(user)
        # Dejamos al usuario logueado
        #login_user(user, remember=True)
        next_page = request.args.get('next', None)

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('paciente.paciente_index')

        return redirect(next_page)
    return render_template("crear_cuenta.html", form=form)


# iniciar_sesion
@autenticacion_blueprints.route("/iniciar_sesion", methods=['GET', 'POST'])
def iniciar_sesion():
    if current_user.is_authenticated:
        return redirect(url_for('inicio.inicio'))

    form = InciarSesionForm()
    if form.validate_on_submit():
        user = get_user(form.usuario.data)
        if user is not None and user.check_password(form.password.data):
            page = None
            if user.get_type().get_id() == 1:
                page = 'administrador.administrador_index'
            elif user.get_type().get_id() == 2:
                page = 'medico.medico_index'
            elif user.get_type().get_id() == 3:
                page = 'paciente.paciente_index'
            
            login_user(user, remember=True)
            
            next_page = request.args.get('next')
            user.set_is_authenticated(True)
            
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for(page)
            print(page)
            return redirect(next_page)            
    return render_template('iniciar_sesion.html', form=form)


# logout
@autenticacion_blueprints.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('autenticacion.iniciar_sesion'))

# prueba para el login
@login_manager.user_loader
def load_user(user_id):
    for user in User.get_all():
        if user.id == int(user_id):
            return user
    return None
