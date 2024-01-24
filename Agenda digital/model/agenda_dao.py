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

class Agenda:
    def __init__(self,nombre,correo,telefono,Identificacion):
        self.Identificacion = Identificacion
        self.nombre = nombre 
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Agenda[{self.nombre},{self.correo},{self.telefono},{self.Identificacion}]'
    

def guardar(agenda):
    conexion = ConexionDB()
    sql = f"""INSERT INTO agenda (nombre,correo,telefono,Identificacion)
    VALUES('{agenda.nombre}','{agenda.correo}','{agenda.telefono}','{agenda.Idenficacion}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "La tabla Agenda no esta creada en la base de datos"
        messagebox.showerror(titulo,mensaje)
    
def listar():
    conexion = ConexionDB()
    lista_Agenda = []
    sql = 'SELECT * FROM agenda'
    
    try:
        conexion.cursor.execute(sql)
        lista_Agenda = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo,mensaje)
        
    return lista_Agenda

def editar(agenda,identificacion):
    conexion = ConexionDB()
    
    sql = f"""UPDATE agenda
    SET nombre = '{agenda.nombre}',correo = '{agenda.correo}',
    telefono = '{agenda.telefono}', cedula = '{agenda.cedula}'
    WHERE identificacion = {identificacion}
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicicon de datos'
        mensaje = 'No se apodido editar este registro'
        messagebox.showerror(titulo,mensaje)
        
        
def eliminar(identificacion):
    
    conexion = ConexionDB()
    sql = f'DELETE FROM agenda WHERE identificacion = {identificacion}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo,mensaje)