from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , DateTimeField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class IngresarPersonalForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    telefono = StringField('Telefono', validators=[DataRequired('Este campo es requerido')])
    dni = IntegerField('dni',validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Agregar nuevo personal')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})

class EditarPersonalForm(FlaskForm): 
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    telefono = StringField('Telefono',validators=[DataRequired('Este campo es requerido')])
    dni = IntegerField('dni', validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Agregar nuevo personal')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})

