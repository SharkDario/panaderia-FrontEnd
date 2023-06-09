import sys
#from FrontEnd.formularioUsuario import FormularioUsuario
# Hay que ejecutar esta línea antes de importar el módulo.
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
# Ahora se puede importar el módulo.
from administrador import Administrador
from empleado import Empleado
from usuario import Usuario
from formularioUsuario import FormularioUsuario
from funciones import funciones as f
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import Entry as entry
from tkinter import Label as label
from PIL import Image, ImageTk, ImageDraw
from tkinter import Button as bt
from ttkthemes import ThemedTk
import tkinter as tk

# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes

class FormularioSesion:
    def __init__(self, ventana):
        self.tema = "black"
        self.ventana1 = ventana
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente = 'Franklin Gothic Demi Cond'
        self.ventana22 = ThemedTk()
        self.ventana22.configure(bg=self.back)
        self.ventana22.geometry("900x750") #tamanno de la ventana
        self.ventana22.geometry("+10+20") #posicion en la pantalla
        self.ventana22.title("2.2 - SESION") #titulo de la ventana
        style = ttk.Style(self.ventana22) # estilo
        style.theme_use(self.tema)
        # boton para ir al formulario anterior
        self.botonAtras = bt(self.ventana22, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioInicio)
        self.botonAtras.grid(row=0, column=0, sticky='w')

        self.labelSuperior = label(self.ventana22, text="INICIAR SESIÓN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')

        self.labelE = label(self.ventana22, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w')
        # label y entrada de usuario
        self.labelUser = label(self.ventana22, text="Usuario: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(row=2, column=0, padx=1, pady=1, sticky='w')
        self.entradaUser = entry(self.ventana22, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(row=2, column=1, padx=1, pady=1, sticky='w')
        # label y entrada de clave
        self.labelClave = label(self.ventana22, text="Contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave = entry(self.ventana22, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        # label y entrada de clave a repetir
        self.labelClave2 = label(self.ventana22, text="Repita su contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave2 = entry(self.ventana22, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        # boton que acciona iniciarSesionAdmiEmple
        self.botonIniciarS = bt(self.ventana22, text="INICIAR SESIÓN", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.iniciarSesionAdminEmple)
        # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        self.botonIniciarS.grid(row=5, column=1, padx=45, pady=60, sticky='w') # se posiciona el boton
        # se abre la ventana
        self.ventana22.mainloop()

    def abrirFormularioInicio(self):
        self.ventana1.deiconify() # Hace visible la ventana1 (formulario de inicio)
        self.ventana22.destroy() # Destruye la ventana22 (formulario actual)

    def abrirFormularioUsuario(self, tipo):
        self.ventana22.withdraw()   # Oculta la ventana22 (formulario actual)
        aplicacion3 = FormularioUsuario(self.ventana22, tipo)   # Crea una instancia de FormularioUsuario con la ventana22 y el tipo de usuario especificado

    def iniciarSesionAdminEmple(self):
        usuarios = Usuario.recuperarNombresUser()  # Recupera los nombres de usuario almacenados
        #usuarios = usuarios[0] 
        user = self.entradaUser.get() # Obtiene el valor ingresado en el campo de usuario
        clave = f.ingClave(self.entradaClave.get(), self.entradaClave2.get())  # Obtiene y encripta la clave ingresada
        entryValido = (type(clave) is not list) # Verifica si la clave ingresada es válida
        mensaje=""  # Variable para almacenar mensajes de error
        bandeIS = False   # Bandera para indicar si se inicia sesión correctamente
        if(entryValido): # Si la clave ingresada es valida
            usuarioIng = Usuario.iniciarSesion(user, clave) # Intenta iniciar sesión con el usuario y clave proporcionados
            if(usuarioIng!=[]): #si la lista no esta vacia
                #aqui volvemos a la lista de 1 tupla, en solo 1 tupla
                usuarioIng = usuarioIng[0]    # Selecciona la primera tupla de la lista
                #print(usuarioIng)
                tipo=usuarioIng[8] # Obtiene el tipo de usuario (Administrador o Empleado) 
                if(tipo==1): #Administrador
                    userOld = Administrador.obtenerAdmi(usuarioIng[1])  # Obtiene los datos del administrador
                else: #Empleado
                    listDNI = Empleado.obtenerDNIs()   # Obtiene la lista de DNIs de los empleados
                    userOld = Empleado.obtenerEmpleado(listDNI, (usuarioIng[1], )) #Obtiene los datos del empleado
                mb.showinfo("¡Felicidades!", f"Bienvenid@ {usuarioIng[3]}")  # Muestra un mensaje de bienvenida
                bandeIS=True # Cambia la bandera a True para indicar inicio de sesión exitoso
            else:
                mensaje += "\nUsuario y/o contraseña incorrectos."
        self.entradaUser.delete(0, tk.END)   # Borra el contenido del campo de usuario
        self.entradaClave.delete(0, tk.END)   # Borra el contenido del campo clave
        self.entradaClave2.delete(0, tk.END)    # Borra el contenido del campo de confirmación de clave
        if(bandeIS):
            #Aqui inicia sesion correctamente
            #directamente con userOld verificaremos que modulos puede usar en el formularioUsuario
            #utilizando un try except para ver si tiene el atributo idTipoEmpleado
            self.abrirFormularioUsuario(userOld)   # Abre el formulario de usuario con los datos del usuario logueado
        else:
            if(type(clave) is list): #si la clave esta en la lista
                mensaje += "\n"+clave[0] # Agrega el mensaje de error relacionado a la clave
            mb.showerror("Error", mensaje)   # Muestra un mensaje de error
            #self.entradaUser.delete(0, tk.END)
            #self.entradaClave.delete(0, tk.EN D)
            #self.entradaClave2.delete(0, tk.END)


