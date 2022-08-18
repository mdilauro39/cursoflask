import sqlite3
import hashlib

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
password = "admin"
h = hashlib.sha256()
h.update(password.encode('utf-8'))

cur.execute("INSERT INTO usuario (nombre,apellido,contraseña,telefono) VALUES (?, ? , ? ,?)",
            ('admin', 'admin',h.hexdigest(),'56465456')
            )
connection.commit()
connection.close()