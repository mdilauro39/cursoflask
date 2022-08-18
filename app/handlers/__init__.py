from collections import UserString
import json
import hashlib
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
    print(row)
    for i in row:
        if i[2] == usuario:
            return validar_contrasena(contraseña,i[4])
    return False

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

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
    personal = "SELECT * FROM personal"
    cursor.execute(personal)
    db.close()
    """Devuelve un diccionario con los datos del empleado con el id indicado
    Si el emplado no existe devuelve None

    :param id: id del empleado
    :return: diccionario con los datos del empleado
    """
    lista_personal = personal # carga todos los usuarios
    for empleado in lista_personal:
        if empleado['id'] == id:
            return empleado
    return None


def agregar_personal(datos_nuevos):
    print(datos_nuevos)
    print(datos_nuevos['nombre'])
    """
    Guarda los datos de un nuevo empleado en el archivo de personal
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO personal (nombre,apellido,contraseña,telefono) VALUES (?, ? , ? ,?)",(datos_nuevos['nombre'], datos_nuevos['apellido'],encode(datos_nuevos['contraseña']),datos_nuevos['telefono'])
            )
    db.commit()


def eliminar_personal(id):
    """
    Elimina el empleado con el id indicado
    """
    id = int(id)
    with open('app/files/personal.json', 'r') as archivo:
        lista_personal = json.load(archivo)  # carga todos los usuarios
    # Crea una lista con los empleados que no tengan el id indicado
    lista_personal = [p for p in lista_personal if p['id'] != id]
    with open('app/files/personal.json', 'w') as archivo:
        json.dump(lista_personal, archivo, indent=4)

