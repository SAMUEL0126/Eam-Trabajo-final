import tkinter as tk
from tkinter import ttk
from model.agenda_dao import crear_tabla , borrar_tabla
from model.agenda_dao import Agenda , guardar , listar
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu,width = 300 , height = 300)
    menu_inicio = tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro de la BD',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro de la BD',command=borrar_tabla)
    menu_inicio.add_command(label='Salir de la BD',command=root.destroy)
    barra_menu.add_cascade(label='Consulta')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    
    
    
class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width = 500, height = 500)
        self.root = root
        self.pack()
        
        self.config (bg = 'White')
        self.campo_nombre()
        self.deshabilitar_campos()
        self.tabla_Sgenda()
        
    def campo_nombre(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self,text = 'Nombre:')
        self.label_nombre.config(font = ('Arial', 12, 'bold'),bg='white')
        self.label_nombre.grid(row = 0 , column = 0, padx=10,pady = 10)
        
        self.label_Cedula = tk.Label(self,text = 'Identificacion:')
        self.label_Cedula.config(font = ('Arial', 12, 'bold'),bg='white')
        self.label_Cedula.grid(row = 1 , column = 0,padx=10,pady = 10)
        
        self.label_Correo= tk.Label(self,text = 'Correo Electronico:')
        self.label_Correo.config(font = ('Arial', 12, 'bold'),bg='white')
        self.label_Correo.grid(row = 2 , column = 0,padx=10,pady = 10)
        
        self.label_Telefono = tk.Label(self,text = 'Numero de Telefono:')
        self.label_Telefono.config(font = ('Arial', 12, 'bold'),bg='white')
        self.label_Telefono.grid(row = 3 , column = 0,padx=10,pady = 10)
        
        #Entrys de cada campo 
        self.mi_nombre = tk.StringVar()
        self.entry_Nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_Nombre.config(width = 50,font = ('Arial', 12, 'bold'))
        self.entry_Nombre.grid(row = 0 , column = 1,padx=10,pady = 10,columnspan=2)
        
        self.mi_cedula = tk.StringVar()
        self.entry_Cedula = tk.Entry(self, textvariable=self.mi_cedula)
        self.entry_Cedula.config(width = 50,font = ('Arial', 12, 'bold'))
        self.entry_Cedula.grid(row = 1 , column = 1,padx=10,pady = 10,columnspan=2)
        
        self.mi_correo = tk.StringVar()
        self.entry_Correo = tk.Entry(self, textvariable=self.mi_correo)
        self.entry_Correo.config(width = 50,font = ('Arial', 12, 'bold'))
        self.entry_Correo.grid(row = 2 , column = 1,padx=10,pady = 10,columnspan=2)
        
        self.mi_telefono = tk.StringVar()
        self.entry_Telefono = tk.Entry(self, textvariable=self.mi_telefono)
        self.entry_Telefono.config(width = 50,font = ('Arial', 12, 'bold'))
        self.entry_Telefono.grid(row = 3 , column = 1,padx=10,pady = 10,columnspan=2)
        
        
        self.boton_nuevoC = tk.Button(self, text="Nuevo Contaacto", command=self.Habilitar_Campos)
        self.boton_nuevoC.config(width=20,font=('Arial',12,'bold'),fg='white',bg = '#158645',cursor= 'hand2',activebackground='lime')
        self.boton_nuevoC.grid(row=3,column=0,padx=10,pady = 10)
        
        
        self.boton_Guardar = tk.Button(self, text="Guardar Contaacto",command=self.guardar_datos)
        self.boton_Guardar.config(width=20,font=('Arial',12,'bold'),fg='white',bg = '#1658A2',cursor= 'hand2',activebackground='#3586DF')
        self.boton_Guardar.grid(row=3,column=1,padx=10,pady = 10)
        
        
        self.boton_Cancelar = tk.Button(self, text="Cancaelar",command=self.deshabilitar_campos)
        self.boton_Cancelar.config(width=20,font=('Arial',12,'bold'),fg='white', bg = '#BD152E',cursor= 'hand2', activebackground='#E15370')
        self.boton_Cancelar.grid(row=3,column=2,padx=10,pady = 10)

        
    def Habilitar_Campos(self):
        
        self.mi_nombre.set('')
        self.mi_correo.set('')
        self.mi_cedula.set('')
        self.mi_telefono.set('')
        
        self.entry_Cedula.config(state='normal')
        self.entry_Correo.config(state='normal')
        self.entry_Nombre.config(state='normal')
        self.entry_Telefono.config(state='normal')
        
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    
    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_correo.set('')
        self.mi_cedula.set('')
        self.mi_telefono.set('')
        
        
        self.entry_Cedula.config(state='disabled')
        self.entry_Correo.config(state='disabled')
        self.entry_Nombre.config(state='disabled')
        self.entry_Telefono.config(state='disabled')
        
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
        
    def guardar_datos(self):
        
        agenda = Agenda(
           self.mi_nombre.get(),
           self.mi_correo.get(),
           self.mi_cedula.get(),
           self.mi_telefono.get()
        )
        
        guardar(agenda)
        
        self.deshabilitar_campos()
        
    def tabla_Sgenda(self):
        
        self.lista_agenda = listar()
        self.lista_agenda.reverse()
        
        
        
        self.tabla = ttk.Treeview(self,columns=('Nombre','Identificacion','Correo','Telefono'))
        
        self.tabla.grid(row=4,column=0,columnspan=4) 
        
        self.tabla.heading('#0',text='ID')        
        self.tabla.heading('#1',text='NOMBRE')  
        self.tabla.heading('#2',text='CORREO')  
        self.tabla.heading('#3',text='TELEFONO')       
        
        for i in self.label_nombre:
            self.tabla.insert('',0,text=i[0],values=(i[1],i[2],i[3]))
        
           
        self.boton_Editar = tk.Button(self, text="Editar",)
        self.boton_Editar.config(width=20,font=('Arial',12,'bold'),fg='white',bg = '#158645',cursor= 'hand2',activebackground='lime')
        self.boton_Editar.grid(row=5,column=0,padx=10,pady = 10)
        
        
           
        self.boton_Eliminar = tk.Button(self, text="Eliminar",)
        self.boton_Eliminar.config(width=20,font=('Arial',12,'bold'),fg='white', bg = '#BD152E',cursor= 'hand2', activebackground='#E15370')
        self.boton_Eliminar.grid(row=5,column=1,padx=10,pady = 10)