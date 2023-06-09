import sys
# Hay que ejecutar esta línea antes de importar el módulo.
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
# Ahora se puede importar el módulo.
import administrador
from empleado import Empleado
from formularioRegistro import FormularioRegistro
from formularioSesion import FormularioSesion
import tkinter as tk
from tkinter import Button as bt
from PIL import Image, ImageTk, ImageDraw
from tkinter import Label as label
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from ttkthemes import ThemedTk

# tkinter.font.families() para ver las fuentes
# DarioDario7 - Nombre de usuario y contraseña para ingresar como el administrador Dario Coronel
# pip install ttkthemes - Para instalar temas especiales de tkinter
# pip install matplotlib - Para instalar la libreria de matplotlib, para realizar el grafico en el formularioPlan de productos mas vendidos

class FormularioInicio:
    def __init__(self):
        self.tema= "black"
        self.back = 'light blue'
        self.fuente='Franklin Gothic Demi Cond'
        #saddle brown #sienna4 
        self.fuenteB = 'gray20'
        self.backB = 'LightSalmon1'
        self.ventana1 = ThemedTk() #tk.Tk()
        self.ventana1.configure(bg=self.back)
        self.ventana1.geometry("900x750") # tamanno de la pantalla
        self.ventana1.geometry("+10+20") # posicion de la ventana en la pantalla
        self.ventana1.title("1 - INICIO") # titulo puesto en la ventana
        #self.ventana1.iconbitmap('c:/Users/mdari/Desktop/Ing_Prog/FrontEnd/icono.ico')
        # se fija un estilo
        style = ttk.Style(self.ventana1)
        style.theme_use(self.tema)
        # Label superior 
        self.labelSuperior = label(self.ventana1, text="SISTEMA PANADERÍA", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.pack(side='top', expand=300, anchor='center', padx=30, pady=30)
        # abrir el logo segun su ruta
        self.logo = Image.open("C:/Users/mdari/Desktop/Ing_Prog/FrontEnd/logo.png")
        # convierte la imagen en un icono
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        # pone al icono en la ventana
        self.ventana1.iconphoto(True, self.logo_tk)
        # posiciona la imagen dentro de la ventana tambien
        self.label_logo = label(self.ventana1, image=self.logo_tk, bg=self.back)
        self.label_logo.pack(side='top', anchor='center', padx=30, pady=30)
        # botón registrar - abre el formulario de registro
        self.botonRegistrar = bt(self.ventana1, text="REGISTRARSE", font=(self.fuente, 20), fg=self.fuenteB, command=self.abrirFormularioRegistro, bg=self.backB)
        # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        self.botonRegistrar.pack(side='bottom', ipadx='40', ipady='30', anchor='center', padx=30, pady=30)
        # boton sesión para abrir el formulario iniciar sesion
        self.botonSesion = bt(self.ventana1, text="INICIAR SESIÓN", font=(self.fuente, 20), fg=self.fuenteB, command=self.abrirFormularioUsuario, bg=self.backB)
        # n, ne, e, se, s, sw, w, nw, or center
        self.botonSesion.pack(side='bottom', ipadx='30', ipady='30', anchor='center', padx=30, pady=30)
        self.ventana1.mainloop() # se inicia la ventana1

    def abrirFormularioRegistro(self):
        # se oculta la ventana1
        self.ventana1.withdraw()
        # se abre el formulario de registro
        aplicacion21 = FormularioRegistro(self.ventana1)

    def abrirFormularioUsuario(self):
        # se oculta la ventana1
        self.ventana1.withdraw()
        # se abre el formulario de inicio de sesion
        aplicacion22 = FormularioSesion(self.ventana1)

# se inicia con el sistema panaderia
sistemaPanaderia = FormularioInicio()
