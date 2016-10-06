import sqlite3
don= sqlite3.connect('personas.db')

don.execute("CREATE TABLE Familia (id integer primary key AUTOINCREMENT, nombre text)")
don.execute("CREATE TABLE Persona (id integer primary key AUTOINCREMENT, Familia id integer, nombre text, apellido text, edad integer)")

don.commit()

don.close()