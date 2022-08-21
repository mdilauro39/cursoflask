DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS personal;
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATE DEFAULT (datetime('now','localtime')),
    desde TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    telefono INTEGER NOT NULL
);

CREATE TABLE personal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    timestamp DATE DEFAULT (datetime('now','localtime')),
    telefono INTEGER NOT NULL,
    dni INTEGER NOT NULL,
    ingreso timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    egreso timestamp,
    motivo TEXT NOT NULL 
);

