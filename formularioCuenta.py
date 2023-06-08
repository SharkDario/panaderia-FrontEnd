import sys
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
import locale
from funciones import funciones as f
from administrador import Administrador
from datetime import datetime
#from usuario import Usuario
#import formularioInicio 
#import subprocess
from tkinter import scrolledtext as st
from tkcalendar import DateEntry
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import Entry as entry
from tkinter import Menu
from tkinter import Label as label
from tkinter import LabelFrame as labelF
from PIL import Image, ImageTk, ImageDraw
from tkinter import Button as bt
import tkinter as tk
from ttkthemes import ThemedTk
from usuario import Usuario
from empleado import Empleado
# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes

#style = ttk.Style()
#style.configure('Custom', background='red')

"""
Button: TButton
Checkbutton: TCheckbutton
Combobox: TCombobox
Entry: TEntry
Frame: TFrame
Label: TLabel
LabelFrame: TLabelFrame
Menubutton: TMenubutton
Notebook: TNotebook
PanedWindow: TPanedwindow
Progressbar: Horizontal.TProgressbar or Vertical.TProgressbar, depending on the orient option.
Radiobutton: TRadiobutton ESTE SÍ
Scale: Horizontal.TScale or Vertical.TScale, depending on the orient option.
Scrollbar: Horizontal.TScrollbar or Vertical.TScrollbar, depending on the orient option
Separator: TSeparator
Sizegrip: TSizegrip
Treeview: Treeview
"""

class FormularioCuenta:
    def __init__(self, ventana, usuario):
        self.usuario = usuario
        self.tema = "itft1" #itft1 smog
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana30 = ThemedTk() #tk.Tk()
        self.ventana30.configure(bg=self.back)
        self.ventana30.title("3.1 - CUENTA")
        self.ventana30.geometry("900x750")
        self.ventana30.geometry("+10+20")

        
        
        self.labelSuperior = label(self.ventana30, text="CUENTA", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        

        self.botonAtras = bt(self.ventana30, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana30)

        #print(self.ventana34.get_themes())
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        #se ve el perfil de la cuenta
        self.verPerfil()
        # se puede modificar atributos de la cuenta
        self.modificarPerfil()
        
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana30.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify() # vuelve a aparecer la ventana3
        self.ventana30.destroy() # se destruye la ventana30

    def modificarPerfil(self):
        # 
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Modificar perfil")
        # labelframe de modificar perfil
        self.labelframe1 = labelF(self.pagina1, text="Modificar perfil", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.labelTipo = label(self.labelframe1, text="Atributo a modificar:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipo.grid(column=0, row=1, padx=4, pady=4)
        # Combobox creation
        self.comboTipo = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15)
        # Adding combobox drop down list
        self.comboTipo['values'] = ('Nombre', 'Domicilio', 'Teléfono', 'Usuario', 'Contraseña') #valores de comboTipo
        self.comboTipo.set('Nombre') # se inserta el valor por defecto al entrar a la pagina del cuaderno
        
        self.comboTipo.grid(column = 1, row = 1)
        self.comboTipo.bind("<<ComboboxSelected>>", self.on_select) # cada vez que se selecciona comboTipo se activa on_select
        #label y entrada del valor nuevo
        self.labelVal = label(self.labelframe1, text="Valor nuevo:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelVal.grid(column=0, row=2, padx=4, pady=4)
        self.entradaVal = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaVal.grid(column=1, row=2, padx=4, pady=4)

        self.botonConfirmar = bt(self.labelframe1, text="Modificar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.modificarAtributo)
        self.botonConfirmar.grid(column=1, row=3, padx=4, pady=4)
        
    def on_select(self, event): # en el caso de que se selecciona Contraseña entonces se mostraran • al escribir
            if ((self.comboTipo.get()) == "Contraseña"):
                self.entradaVal.delete(0, tk.END)
                self.entradaVal.config(show="•")
            else:
                self.entradaVal.delete(0, tk.END)
                self.entradaVal.config(show="")

    def modificarAtributo(self):
        bande=True #para modificar atributos de persona
        tipo = self.comboTipo.get()
        if((tipo=="Nombre")|(tipo=="Domicilio")):
            tipo=tipo.lower()
            var = self.entradaVal.get() 
        elif(tipo=="Teléfono"):
            tipo="telefono"
            var = f.ingNum(self.entradaVal.get(), "El teléfono", 15) #se valida el numero de telefono
        elif(tipo=="Usuario"):
            bande=False #para modificar atributos de usuario
            tipo="usuario"
            usuarios = Usuario.recuperarNombresUser() # se recuperan los nombres de usuarios
            var = f.ingUser(self.entradaVal.get(), usuarios) # se valida el usuario, si es que ya existe en la base de datos
        else:
            bande=False
            tipo="clave" #se valida la clave q tenga 8 caracteres, un numero y una mayuscula
            var = f.ingClaveValida(self.entradaVal.get())
        # se verifica el valor de verdad
        entryValido = (type(var) is not list)&(var!="")

        if(entryValido): #si es verdadero
            if(bande): # se modifican atributos de persona (nombre, domicilio, telefono)
                self.usuario.modificarPerso("usuarios", var, tipo)
            else: # se modifican atributos de usuario (usuario, clave)
                self.usuario.modificarUser(var, tipo)
            self.insertarMensaje(True) # se inserta el mensaje, se pasa True, pq se cambio el valor de un atributo
            mb.showinfo("¡Felicidades!", "Atributo modificado")
        else:
            mensaje=""
            if(type(var) is list): #var = ["mensaje: sobre la validacion"]
                mensaje += "\n"+var[0]
            if(var == ""):
                mensaje += "\nEl valor no puede estar vacío."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaVal.delete(0, tk.END) # se elimina lo escrito en la entrada

    def insertarMensaje(self, nuevo=None):
        self.scrolledtext2.configure(state='normal')  #se configura a normal para editar el scrolledtext2
        mensaje=""
        # Con "nuevo" se actualiza el perfil
        dni = self.usuario.DNI
        if(type(self.usuario) is Administrador): # si el usuario es un objeto Administrador
            if(nuevo==True):
                self.usuario = Administrador.obtenerAdmi(dni) # se obtiene el usuario actualizado si es que se paso True como argumento
            idUser = Administrador.obtenerId((dni, )) # se obtiene su id mediante la clase Administrador
        else: # en este caso el usuario es un objeto Empleado
            if(nuevo==True): 
                self.usuario = Empleado.obtenerEmple([dni], dni) # se obtiene el usuario actualizado si es que se paso True como argumento
            idUser = Empleado.obtenerId((dni, )) # se obtiene su id mediante la clase Empleado
            fechaIni = Empleado.verFechaContratacion((idUser, )) # se obtiene la fecha de contratacion del empleado
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # se pone la fecha en la localidad en la que esta quien lo ejecuta
            fechaIni = fechaIni[0][0]
            fechaIni = fechaIni.strftime('%d de %B de %Y') # se transforma el datetime a cadena
            mensaje=f"Cargo: {self.usuario.cargo}\nFecha de contratación: {fechaIni}" # se guarda el cargo y la fecha en un mensaje
        #el mensaje completo de todos los datos del usuario
        mensaje = f"ID: {idUser}\nDNI: {self.usuario.DNI}\nCUIL/CUIT: {self.usuario.CUIL_CUIT}\nNombre: {self.usuario.nombre}\nDomicilio: {self.usuario.domicilio}\nTeléfono: {self.usuario.telefono}\nUsuario: {self.usuario.user}\n"+mensaje
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert(tk.END, mensaje) # se inserta el mensaje en el scrolledtext2 que aparece en perfil
        self.scrolledtext2.configure(state='disabled') # se desactiva la edicion

    def verPerfil(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Perfil")
        
        self.labelframe2 = labelF(self.pagina2, text="Perfil", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        #aqui se insertan los datos del usuario
        self.scrolledtext2 = st.ScrolledText(self.labelframe2, font=(self.fuente, 20), width=35, height=10)
        self.scrolledtext2.grid(column=1, row=1, padx=10, pady=10)
        # esto acciona que se vean los datos del usuario en el scrolledtext2
        self.insertarMensaje()
        
        
    def verUsuario(self):
        try: 
            self.dni2 = int(self.entradaDNI2.get())
        except Exception:
            self.dni2 = self.entradaDNI2.get()
        self.datos = (self.dni2, )
        self.listaDNIs = Empleado.obtenerDNIs()
        self.emple = Empleado.obtenerEmpleado(self.listaDNIs, self.datos, True)
        consulta = self.emple
        if consulta is not False:
            #(DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, puesto
            if(consulta[8]==1):
                puesto="Repositor"
            elif(consulta[8]==2):
                puesto="Vendedor"
            else:
                puesto="Productor"
            # mensaje que guarda los datos del usuario
            mensaje = "ID: "+str(consulta[0])+"\nDNI: "+str(consulta[1])+"\nCUIL/CUIT: "+str(consulta[2])+"\nNombre: "+consulta[3]+"\nDomicilio: "+consulta[4]+"\nTeléfono: "+str(consulta[5])+"\nUsuario: "+consulta[6]+"\nCargo: "+puesto
            self.scrolledtext2.delete("1.0", tk.END) # se elimina lo que tenga
            self.scrolledtext2.insert(tk.END, mensaje) # se inserta el mensaje con los datos del usuario
        else:
            self.entradaDNI2.delete(0, tk.END)
            #self.scrolledtext2.configure(state='normal')
            self.scrolledtext2.delete("1.0", tk.END)
            #self.scrolledtext2.configure(state='disabled')
            mb.showerror("Error", "No existe empleado con el DNI ingresado.")
    

        
