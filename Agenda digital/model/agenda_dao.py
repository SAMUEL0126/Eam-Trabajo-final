from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE agenda(
        id_persona VARCHAR(50),
        Nombre VARCHAR(100),
        Correo VARCHAR(100),
        Telefono VARCHAR(100),
        PRIMARY KEY(id_persona)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada en la base de datos'
        messagebox.showinfo(titulo,mensaje)
    
def borrar_tabla():
     conexion = ConexionDB()
     
     sql = 'DROP TABLE agenda'
     try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla ya esta creada en la base de datos'
        messagebox.showinfo(titulo,mensaje)
     except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo,mensaje)