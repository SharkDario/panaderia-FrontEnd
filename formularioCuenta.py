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
        self.tema = "blue"
        self.back = 'light blue'
        self.backB = 'SteelBlue3'
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
        
        #SI: blue, smog, black, adapta
        #EH: kroc, plastik, winxpblue, itft1, aquativo, clam
        #NO: equilux, keramik, elegance, radiance, breeze, clearlooks, ubuntu, yaru, scidmint
        #[ 'alt', 'scidpurple', 'scidpink', 
        #'default', 'scidblue', 'classic', 'xpnative', 
        #, 'scidgrey', 'scidsand', 'scidgreen', 'arc', 'vista', 'winnative']
        self.verPerfil()
        self.modificarPerfil()
        
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana30.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify()
        self.ventana30.destroy()

    def modificarPerfil(self):
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Modificar perfil")
        
        self.labelframe1 = labelF(self.pagina1, text="Modificar perfil", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.labelTipo = label(self.labelframe1, text="Atributo a modificar:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipo.grid(column=0, row=1, padx=4, pady=4)
        # Combobox creation
        self.comboTipo = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15)
        # Adding combobox drop down list
        self.comboTipo['values'] = ('Nombre', 'Domicilio', 'Teléfono', 'Usuario', 'Contraseña')
        self.comboTipo.set('Nombre')
        
        self.comboTipo.grid(column = 1, row = 1)
        self.comboTipo.bind("<<ComboboxSelected>>", self.on_select)

        self.labelVal = label(self.labelframe1, text="Valor nuevo:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelVal.grid(column=0, row=2, padx=4, pady=4)
        self.entradaVal = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaVal.grid(column=1, row=2, padx=4, pady=4)

        self.botonConfirmar = bt(self.labelframe1, text="Modificar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.modificarAtributo)
        self.botonConfirmar.grid(column=1, row=3, padx=4, pady=4)
        
    def on_select(self, event):
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
            var = f.ingNum(self.entradaVal.get(), "El teléfono", 15)
        elif(tipo=="Usuario"):
            bande=False #para modificar atributos de usuario
            tipo="usuario"
            usuarios = Usuario.recuperarNombresUser()
            var = f.ingUser(self.entradaVal.get(), usuarios)
        else:
            bande=False
            tipo="clave"
            var = f.ingClaveValida(self.entradaVal.get())
        entryValido = (type(var) is not list)&(var!="")

        if(entryValido):
            if(bande):
                self.usuario.modificarPerso("usuarios", var, tipo)
            else:
                self.usuario.modificarUser(var, tipo)
            self.insertarMensaje(True)
            mb.showinfo("¡Felicidades!", "Atributo modificado")
        else:
            mensaje=""
            if(type(var) is list):
                mensaje += "\n"+var[0]
            if(var == ""):
                mensaje += "\nEl valor no puede estar vacío."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaVal.delete(0, tk.END)

    def insertarMensaje(self, nuevo=None):
        self.scrolledtext2.configure(state='normal')
        mensaje=""
        # Con "nuevo" se actualiza el perfil
        dni = self.usuario.DNI
        if(type(self.usuario) is Administrador):
            if(nuevo==True):
                self.usuario = Administrador.obtenerAdmi(dni)
            idUser = Administrador.obtenerId((dni, ))
        else:
            if(nuevo==True):
                self.usuario = Empleado.obtenerEmple([dni], dni)
            idUser = Empleado.obtenerId((dni, ))
            fechaIni = Empleado.verFechaContratacion((idUser, ))
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            fechaIni = fechaIni[0][0]
            fechaIni = fechaIni.strftime('%d de %B de %Y')
            mensaje=f"Cargo: {self.usuario.cargo}\nFecha de contratación: {fechaIni}"

        mensaje = f"ID: {idUser}\nDNI: {self.usuario.DNI}\nCUIL/CUIT: {self.usuario.CUIL_CUIT}\nNombre: {self.usuario.nombre}\nDomicilio: {self.usuario.domicilio}\nTeléfono: {self.usuario.telefono}\nUsuario: {self.usuario.user}\n"+mensaje
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert(tk.END, mensaje)
        self.scrolledtext2.configure(state='disabled')

    def verPerfil(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Perfil")
        
        self.labelframe2 = labelF(self.pagina2, text="Perfil", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.scrolledtext2 = st.ScrolledText(self.labelframe2, font=(self.fuente, 20), width=35, height=10)
        self.scrolledtext2.grid(column=1, row=1, padx=10, pady=10)

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
            mensaje = "ID: "+str(consulta[0])+"\nDNI: "+str(consulta[1])+"\nCUIL/CUIT: "+str(consulta[2])+"\nNombre: "+consulta[3]+"\nDomicilio: "+consulta[4]+"\nTeléfono: "+str(consulta[5])+"\nUsuario: "+consulta[6]+"\nCargo: "+puesto
            self.scrolledtext2.delete("1.0", tk.END)
            self.scrolledtext2.insert(tk.END, mensaje)
        else:
            self.entradaDNI2.delete(0, tk.END)
            #self.scrolledtext2.configure(state='normal')
            self.scrolledtext2.delete("1.0", tk.END)
            #self.scrolledtext2.configure(state='disabled')
            mb.showerror("Error", "No existe empleado con el DNI ingresado.")
    

        
        #subprocess.call(["python", "formularioInicio.py"])



#a#['adapta', 'alt', 'blue', 'scidpurple', 'scidpink', 'aquativo', 'itft1', 'equilux', 'elegance', 
        #'default', 'clam', 'black', 'scidblue', 'winxpblue', 'classic', 'radiance', 'scidmint', 'xpnative', 
        #'yaru', 'ubuntu', 'kroc', 'plastik', 'breeze', 'scidgrey', 'scidsand', 'scidgreen', 'clearlooks', 'smog', 'arc', 'vista', 'keramik', 'winnative']
        """
        our_themes = self.ventana34.get_themes()
        print(our_themes)
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use("adapta")

        my_menu = Menu(self.ventana34)
        self.ventana34.config(menu=my_menu)

        theme_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(menu=theme_menu)
        
 def changer(self, theme):
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(theme)

        for t in our_themes:
            theme_menu.add_command(label=t , command=self.changer(t))
        """