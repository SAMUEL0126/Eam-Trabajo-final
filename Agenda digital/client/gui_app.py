import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu,width = 300 , height = 300)
    menu_inicio = tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro de la BD')
    menu_inicio.add_command(label='Eliminar Registro de la BD')
    menu_inicio.add_command(label='Salir de la BD',command=root.destroy)
    barra_menu.add_cascade(label='Consulta')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    
    
    
class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width = 500, height = 500)
        self.root = root
        self.pack()
        self.config (bg = 'silver')
        self.campo_nombre()
        
    def campo_nombre(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self,text = 'Nombre:')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0 , column = 0, padx=10,pady = 10)
        
        self.label_Cedula = tk.Label(self,text = 'Identificacion:')
        self.label_Cedula.config(font = ('Arial', 12, 'bold'))
        self.label_Cedula.grid(row = 1 , column = 0,padx=10,pady = 10)
        
        self.label_Correo= tk.Label(self,text = 'Correo Electronico:')
        self.label_Correo.config(font = ('Arial', 12, 'bold'))
        self.label_Correo.grid(row = 2 , column = 0,padx=10,pady = 10)
        
        self.label_Telefono = tk.Label(self,text = 'Numero de Telefono:')
        self.label_Telefono.config(font = ('Arial', 12, 'bold'))
        self.label_Telefono.grid(row = 3 , column = 0)
        
        #Entrys de cada campo 
        self.entry_Nombre = tk.Entry(self)
        self.entry_Nombre.config(width = 50, height = 50)
        self.entry_Nombre.grid(row = 0 , column = 1)
        
        self.entry_Cedula = tk.Entry(self)
        self.entry_Cedula.grid(row = 0 , column = 1)
        
        self.entry_Correo= tk.Entry(self)
        self.entry_Correo.grid(row = 0 , column = 1)
        
        self.entry_Telefono = tk.Entry(self)
        self.entry_Telefono.grid(row = 0 , column = 1)
        
      