from collections import UserString
import json
import hashlib
from app.dbasedb import get_db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def encode(contrasena):
    return hashlib.sha256(str(contrasena).encode('utf8')).hexdigest()


def validar_contrasena(contraseña, contraseña_hash):
    # Si la contraseña ingresada es igual a la almacenada en el archivo devuelve True
    return encode(contraseña) == contraseña_hash


def validar_usuario(usuario, contraseña):
    conn = query_db("SELECT * FROM usuario")
    """
    Valida que el usuario y la contraseña sean correctos

    :param usuario: nombre de usuario
    :param contrasena: contraseña
    :return: True si el usuario y la contraseña son correctos, False en caso contrario    
    """
    # Si el usuario y la contraseña ingresados son iguales a los almacenados en el archivo devuelve True
     
    if usuario in conn:  # si el usuario existe
        return validar_contrasena(contraseña, usuario[contraseña])
    else:
        return False

def get_personal():
    conn = get_db_connection()
    personal = conn.execute('SELECT * FROM personal').fetchall()
    conn.close()
    """Devuelve una lista de diccionarios con los datos de los empleados

    :return: lista de diccionarios con los datos de los empleados
    """

    lista_personal = personal # carga todos los usuarios
    return lista_personal


def get_personal_por_id(id):
    conn = get_db_connection()
    personal = conn.execute('SELECT * FROM personal').fetchall()
    conn.close()
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
    """
    Guarda los datos de un nuevo empleado en el archivo de personal
    """
    with open('app/files/personal.json', 'r') as archivo:
        lista_personal = json.load(archivo)  # carga todos los usuarios
    # Obtener el último id, si no hay ningún empleado, el id es 1
    if not lista_personal:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_personal, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_personal.append(datos_nuevos)
    with open('app/files/personal.json', 'w') as archivo:
        json.dump(lista_personal, archivo, indent=4)


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

