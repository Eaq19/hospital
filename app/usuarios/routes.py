from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.autenticacion.models import DocumentType, User, Admin, Patient, Doctor, Role
from . import user_blueprints
from .forms import CrearUsuarioForm
from datetime import datetime

# lista de usuarios
ROWS_PER_PAGE = 5

@user_blueprints.route("/usuarios", methods=['GET', 'POST'])
#@login_required
def list():
    page = request.args.get('page', 1, type=int)
    
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    
    return render_template('list_user.html', users=users.items)

@user_blueprints.route("/usuarios/delete/<int:id>", methods=['GET', 'POST'])
#@login_required
def delete(id):
    post:User = User.get_by_id(id)
    if post is not None :
        post.delete()
    page = request.args.get('page', 1, type=int)
    
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return redirect(url_for('user.list'))

# lista de citas
@user_blueprints.route("/usuarios/<int:id>", methods=['GET', 'POST'])
#@login_required
def edit(id):
    post:User = User.get_by_id(id)
    if post is not None :
        form = CrearUsuarioForm()
        types = DocumentType.get_all()
        types.insert(0, DocumentType("Tipo de documento", 0))
        listTypes=[(i.get_id(), i.get_name()) for i in types]
        roles = Role.get_all()
        roles.insert(0, Role("Tipo de documento", 0))
        listRoles=[(i.get_id(), i.get_name()) for i in roles]
        form.tipo_documento.choices = listTypes
        form.tipoUsuario.choices = listRoles
        form.nombres.data = post.get_name()
        form.apellidos.data = post.get_lastName()
        form.tipo_documento.data = post.get_documentType().get_id()
        form.num_documento.data = post.get_documentNumber()
        form.num_telefono.data = post.get_phoneNumber()
        form.fecha_nacimiento.data = post.get_birthDate()
        form.sexo.data = post.get_gender()
        form.tipoUsuario.data = post.get_type().get_id()
        form.estado.data = post.get_is_active()
        if request.method == 'POST':
            if form.validate_on_submit():
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('user.list'))

    return render_template('edit_user.html',form=form, user=post)


# lista de comentarios
@user_blueprints.route("/usuario", methods=['GET', 'POST'])
#@login_required
def create():
    form = CrearUsuarioForm()
    listTypes=[(i.get_id(), i.get_name()) for i in DocumentType.get_all()]
    listRoles=[(i.get_id(), i.get_name()) for i in Role.get_all()]
    form.tipo_documento.choices = listTypes
    form.tipoUsuario.choices = listRoles
    if form.validate_on_submit():
        if form.tipoUsuario.data == "1" :
            user = Admin(form.nombres.data, form.apellidos.data, form.password.data, form.tipo_documento.data, form.tipo_documento.data, form.fecha_nacimiento.data, form.num_telefono.data, form.sexo.data, datetime.now(), 1)
            user.save()
        elif form.tipoUsuario.data == "2" :
            user = Doctor(form.nombres.data, form.apellidos.data, form.password.data, form.tipo_documento.data, form.tipo_documento.data, form.fecha_nacimiento.data, form.num_telefono.data, form.sexo.data, datetime.now(), "General")
            user.save()
        elif form.tipoUsuario.data == "3" :
            user = Patient(form.nombres.data, form.apellidos.data, form.password.data, form.tipo_documento.data, form.tipo_documento.data, form.fecha_nacimiento.data, form.num_telefono.data, form.sexo.data, datetime.now())
            user.save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('user.list'))
    
    return render_template("create_user.html", form=form, documentTypes= DocumentType.get_all(), roles = Role.get_all())
