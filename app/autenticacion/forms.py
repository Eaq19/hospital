from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators
from wtforms.validators import DataRequired, Email, Length

class InciarSesionForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    ingresar = SubmitField('Iniciar Sesión')
    
class CrearUsuarioForm(FlaskForm):
    nombres = StringField('Nombre', validators=[DataRequired()])
    
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    re_password = PasswordField('Re-Ingrese Password', validators=[DataRequired()])
    
    tipo_documento = SelectField('Tipo Documento', choices=[('TI', 'Tarjeta de identidad'), 
                                                            ('CC', 'Cédula de ciudadanía'), ('PAS', 'Pasaporte')])
    
    num_documento = StringField('Número de documento', validators=[DataRequired()])
    
    fecha_nacimiento = DateField('Fecha de nacimiento', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    
    num_telefono = StringField('Número de teléfono', validators=[DataRequired()])
    
    estado = SelectField('ESTADO', choices=[('A','Activo')])
    
    guardar = SubmitField('Guardar')
    
