from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('inicio.html',nombre="marcos")

@app.route('/nombre')
def nombre():
    return render_template()

@app.route('/apellido')
def apellido():
    return render_template()