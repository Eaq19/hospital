from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators
from wtforms.validators import DataRequired, Email, Length
    
class CrearUsuarioForm(FlaskForm):
    nombres = StringField('Nombre', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    re_password = PasswordField('Re-Ingrese Password', validators=[DataRequired()])
    tipo_documento = SelectField('Tipo Documento', coerce=int)
    num_documento = StringField('Número de documento', validators=[DataRequired()])
    num_telefono = StringField('Número de telefono', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de nacimiento', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    tipoUsuario = SelectField('Rol', coerce=int)
    
    estado = SelectField('Estado', choices=[(True,'Activo'), (False,'Desactivado')], coerce=bool)
    
    guardar = SubmitField('Guardar')
    
