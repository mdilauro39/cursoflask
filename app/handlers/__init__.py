from collections import UserString
import datetime
import json
import hashlib
from sqlite3 import Timestamp
from app.dbasedb import get_db

def encode(contrasena):
    return hashlib.sha256(str(contrasena).encode('utf8')).hexdigest()


def validar_contrasena(contraseña, contraseña_hash):
    # Si la contraseña ingresada es igual a la almacenada en el archivo devuelve True
    return encode(contraseña) == contraseña_hash


def validar_usuario(usuario, contraseña):
    db = get_db()
    cursor = db.cursor()
    consulta = "SELECT * FROM usuario"
    cursor.execute(consulta)
    row = cursor.fetchall()
    """
    Valida que el usuario y la contraseña sean correctos

    :param usuario: nombre de usuario
    :param contrasena: contraseña
    :return: True si el usuario y la contraseña son correctos, False en caso contrario    
    """
    # Si el usuario y la contraseña ingresados son iguales a los almacenados en el archivo devuelve True
    for i in row:
        if i[2] == usuario:
            return validar_contrasena(contraseña,i[4])
    return False

def get_personal():
    db = get_db()
    cursor = db.cursor()
    consulta = "SELECT * FROM personal"
    cursor.execute(consulta)
    row = cursor.fetchall()
    return row
    """Devuelve una lista de diccionarios con los datos de los empleados

    :return: lista de diccionarios con los datos de los empleados
    """


def get_personal_por_id(id):
    db = get_db()
    cursor = db.cursor()
    personal = "SELECT * FROM personal WHERE id=?"
    cursor.execute(personal,(id,))
    row = cursor.fetchall()
   
    """Devuelve un diccionario con los datos del empleado con el id indicado
    Si el emplado no existe devuelve None

    :param id: id del empleado
    :return: diccionario con los datos del empleado
    """
    lista_personal = cursor # carga todos los usuarios
    for empleado in lista_personal:
        if empleado[0] == id:
            return empleado
    return None


def agregar_personal(datos_nuevos):
    """
    Guarda los datos de un nuevo empleado en el archivo de personal
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO personal (nombre,apellido,telefono,dni,motivo) VALUES (?, ? , ? ,?,?)",(datos_nuevos['nombre'], datos_nuevos['apellido'],datos_nuevos['telefono'],datos_nuevos['dni'],datos_nuevos['motivo']))
    db.commit()


def eliminar_personal(id):
    print(id)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM personal WHERE id=?",(id,))
    db.commit()

def agregar_egreso(datos_nuevos):
    """
    Guarda los datos de un nuevo empleado en el archivo de personal
    """
    db = get_db()
    cursor = db.cursor()
    egreso = datetime.datetime.now()
    cursor.execute("UPDATE personal SET egreso = ? WHERE id = ?",(egreso,datos_nuevos))
    db.commit()

def editarpersonal(datos_nuevos):
    """
    Guarda los datos de un nuevo empleado en el archivo de personal
    """
    db = get_db()
    cursor = db.cursor()
    print(datos_nuevos)
    cursor.execute("UPDATE personal SET nombre = ? apellido = ? telefono = ? dni = ? motivo = ? WHERE id = ?",(datos_nuevos),)
    db.commit()
   

