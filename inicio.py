from ensurepip import bootstrap
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def inicio():
    nombre = "Marcos"
    return render_template('inicio.html',nombre=nombre)

@app.route('/edad')
def edad():
    edad = 36
    return render_template('edad.html', edad=edad)

@app.route('/apellido')
def apellido():
    apellido = "DI LAURO"
    return render_template('apellido.html', apellido=apellido)