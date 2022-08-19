DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS personal;
DROP TABLE IF EXISTS ingreso;
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    desde TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    telefono INTEGER NOT NULL
);

CREATE TABLE ingreso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingreso TIMESTAMP,
    egreso TIMESTAMP 
);
CREATE TABLE personal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    desde TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_ingreso INTEGER,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    telefono INTEGER NOT NULL,
    foreign key(id_ingreso) references ingreso(id)
);