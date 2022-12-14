from app import app
from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required

from app.forms import *
from app.handlers import *


@app.route('/')  # http://localhost:5000/
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('borrar'):
        eliminar_personal(request.args.get('borrar'))
        flash('Se ha eliminado el empleado', 'success')
    return render_template('index.html', titulo="Inicio", personal=get_personal())

@app.route('/egreso/<int:id_empleado>', methods=['GET', 'POST'])
@login_required
def egreso(id_empleado):
        agregar_egreso(id_empleado)
        flash('Se ha registrado el egreso del personal', 'success')
        return redirect(url_for('index'))

@app.route('/ingresar-personal', methods=['GET', 'POST'])
@login_required
def ingresar_personal():
    personal_form = IngresarPersonalForm()
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('index'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 'nombre': personal_form.nombre.data, 'apellido': personal_form.apellido.data, 'telefono': personal_form.telefono.data, 'dni': personal_form.dni.data,'motivo':personal_form.motivo.data }
        agregar_personal(datos_nuevos)
        flash('Se ha agregado un nuevo empleado', 'success')
        return redirect(url_for('index'))
    return render_template('ingresar_personal.html', titulo="Personal", personal_form=personal_form)


@app.route('/editar-personal/<int:id_empleado>', methods=['GET', 'POST'])
@login_required
def editar_personal(id_empleado):
    personal_form = EditarPersonalForm(data=get_personal_por_id(id_empleado))
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('index'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 'nombre': personal_form.nombre.data, 'apellido': personal_form.apellido.data, 'telefono': personal_form.telefono.data, 'dni': personal_form.dni.data,'motivo':personal_form.motivo.data, 'id':id_empleado }
        editarpersonal(datos_nuevos)
        flash('Se ha editado el empleado exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('editar_personal.html', titulo="Personal", personal_form=personal_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = login_form.usuario.data
        password = login_form.password.data
        if validar_usuario(usuario, password):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

