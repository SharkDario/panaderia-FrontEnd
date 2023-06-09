import sys
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
from funciones import funciones as f
from administrador import Administrador
#from usuario import Usuario
#import formularioInicio 
#import subprocess
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import Entry as entry
from tkinter import Label as label
from PIL import Image, ImageTk, ImageDraw
from tkinter import Button as bt
from ttkthemes import ThemedTk
import tkinter as tk
from usuario import Usuario
# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes


class FormularioRegistro: # se define una clase que crea una ventana de formulario para el registro de administradores
    def __init__(self, ventana): # constructor de la clase
        self.tema = "black" # se inicializan variables que se utilizan para el estilo de distintos label boton entry
        self.ventana1 = ventana
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana21 = ThemedTk() # crea una instancia ThemedTk() para aplicar estilos a la ventana
        self.ventana21.configure(bg=self.back) # se configura el fondo de la ventana
        self.ventana21.geometry("900x750") #tamanno de la ventana
        self.ventana21.geometry("+10+20") # se posiciona en la pantalla
        self.ventana21.title("2.1 - REGISTRO") # titulo de la ventana
        style = ttk.Style(self.ventana21) 
        style.theme_use(self.tema) # estilo que usa la ventana
        
        #🔙 boton para ir a la ventana anterior
        self.botonAtras = bt(self.ventana21, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioInicio)
        self.botonAtras.grid(row=0, column=0, sticky='w')
        
        self.labelSuperior = label(self.ventana21, text="REGISTRO ADMIN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')

        self.labelE = label(self.ventana21, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w')

        # DNI, CUIL_CUIT, nombre, domicilio, user, clave,
        # label y entrada del DNI
        self.labelDNI = label(self.ventana21, text="DNI: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI.grid(row=2, column=0, padx=1, pady=1, sticky='w')
        self.entradaDNI = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI.grid(row=2, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del CUIL
        self.labelCUIL_CUIT = label(self.ventana21, text="CUIL/CUIT: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCUIL_CUIT.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.entradaCUIL_CUIT = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCUIL_CUIT.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del nombre
        self.labelNombre = label(self.ventana21, text="Nombre completo: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.entradaNombre = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del domicilio
        self.labelDomicilio = label(self.ventana21, text="Domicilio: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDomicilio.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.entradaDomicilio = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDomicilio.grid(row=5, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del telefono
        self.labelTel = label(self.ventana21, text="Teléfono: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTel.grid(row=6, column=0, padx=1, pady=1, sticky='w')
        self.entradaTel = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaTel.grid(row=6, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del usuario
        self.labelUser = label(self.ventana21, text="Usuario: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(row=7, column=0, padx=1, pady=1, sticky='w')
        self.entradaUser = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(row=7, column=1, padx=1, pady=1, sticky='w')
        # label y entrada de la clave
        self.labelClave = label(self.ventana21, text="Contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(row=8, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(row=8, column=1, padx=1, pady=1, sticky='w')
        # label y entrada de la clave a repetir
        self.labelClave2 = label(self.ventana21, text="Repita su contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(row=9, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave2 = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(row=9, column=1, padx=1, pady=1, sticky='w')
        # label y entrada del codigo identificador
        self.labelIden = label(self.ventana21, text="Identificación: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelIden.grid(row=10, column=0, padx=1, pady=1, sticky='w')
        self.entradaIden = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaIden.grid(row=10, column=1, padx=1, pady=1, sticky='w')
        # boton de registro para dar de alta a un nuevo administrador
        self.botonRegistro = bt(self.ventana21, text="REGISTRARSE", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.altaNuevoAdministrador)
        self.botonRegistro.grid(row=11, column=1, padx=45, pady=60, sticky='w')
        # se abre la ventana
        self.ventana21.mainloop()

    def abrirFormularioInicio(self):
        self.ventana1.deiconify() # vuelve a aparecer la ventana1
        self.ventana21.destroy() # se cierra la ventana21

    def altaNuevoAdministrador(self):
        usuarios = Usuario.recuperarNombresUser() # se recuperan los nombres de usuario
        listDni = Usuario.recuperarDNIs() # se recuperan los dnis de usuario
        #usuarios = usuarios[0]
        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI") 
        if(type(dni) is not list): # si el dni no es lista, entonces es valido
            dni = f.ingDNI(dni, listDni)
        cuil = f.ingDNI_CUIL(self.entradaCUIL_CUIT.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomicilio.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)
        user = f.ingUser(self.entradaUser.get(), usuarios)
        claveVal = f.ingClaveValida(self.entradaClave.get())
        clave = f.ingClave(self.entradaClave.get(), self.entradaClave2.get())
        iden = f.ingClave(self.entradaIden.get(), f.recuperarIden(), "El código de identificación es incorrecto")
        #print((dni is not list)&(cuil is not list)&(user is not list)&(clave is not list)&(iden is not list))
        dniCuilComparar=False
        dniCuilNoLista = (type(dni) is not list) & (type(cuil) is not list)
        if(dniCuilNoLista):
            dniCuilComparar = f.dniCuilComparar(dni, cuil) # verifica que el dni y el cuil sean validos
        entrysValidos = ((dniCuilNoLista)&(type(user) is not list)&(type(clave) is not list)&(type(iden) is not list)&(nombre!="")&(domi!="")&(dniCuilComparar)&(type(claveVal) is not list)&(type(tel) is not list))
        if(entrysValidos): # si las entradas son validas, entonces se crea un objeto administrador y se da de alta en la base de datos
            nuevoAdmi = Administrador(dni, cuil, nombre, domi, int(tel), user, clave)
            mb.showinfo("¡Felicidades!", "Administrador registrado")
        else:
            mensaje=""
            # si alguna variable es una lista, guarda un unico valor que es el mensaje
            if(type(dni) is list):
                mensaje += dni[0]
            if(type(cuil) is list):
                mensaje += "\n"+cuil[0]
            if(nombre == ""):
                mensaje += "\nEl nombre no puede estar vacío."
            if(domi == ""):
                mensaje += "\nEl domicilio no puede estar vacío."
            if(type(tel) is list):
                mensaje += "\n"+tel[0]
            if(type(user) is list):
                mensaje += "\n"+user[0]
            if(type(claveVal) is list):
                mensaje += claveVal[0]
            if(type(clave) is list):
                mensaje += "\n"+clave[0]
            if(type(iden) is list):
                mensaje += "\n"+iden[0]
            if(dniCuilComparar==False):
                mensaje += "\nEl DNI y el CUIL/CUIT no coinciden."
            # imprime el mensaje en una ventana de error
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END) # elimina todo lo que se escribio en las entradas
        self.entradaCUIL_CUIT.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaDomicilio.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaUser.delete(0, tk.END)
        self.entradaClave.delete(0, tk.END)
        self.entradaClave2.delete(0, tk.END)
        self.entradaIden.delete(0, tk.END)

