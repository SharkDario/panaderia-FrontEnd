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
#DarioDario7
#pip install ttkthemes

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
        self.ventana1.geometry("900x750")
        self.ventana1.geometry("+10+20")
        self.ventana1.title("1 - INICIO")
        #self.ventana1.iconbitmap('c:/Users/mdari/Desktop/Ing_Prog/FrontEnd/icono.ico')

        style = ttk.Style(self.ventana1)
        style.theme_use(self.tema)

        self.labelSuperior = label(self.ventana1, text="SISTEMA PANADERÍA", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.pack(side='top', expand=300, anchor='center', padx=30, pady=30)
        self.logo = Image.open("C:/Users/mdari/Desktop/Ing_Prog/FrontEnd/logo.png")
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.ventana1.iconphoto(True, self.logo_tk)
        self.label_logo = label(self.ventana1, image=self.logo_tk, bg=self.back)
        self.label_logo.pack(side='top', anchor='center', padx=30, pady=30)
        self.botonRegistrar = bt(self.ventana1, text="REGISTRARSE", font=(self.fuente, 20), fg=self.fuenteB, command=self.abrirFormularioRegistro, bg=self.backB)
        # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        self.botonRegistrar.pack(side='bottom', ipadx='40', ipady='30', anchor='center', padx=30, pady=30)
        self.botonSesion = bt(self.ventana1, text="INICIAR SESIÓN", font=(self.fuente, 20), fg=self.fuenteB, command=self.abrirFormularioUsuario, bg=self.backB)
        # n, ne, e, se, s, sw, w, nw, or center
        self.botonSesion.pack(side='bottom', ipadx='30', ipady='30', anchor='center', padx=30, pady=30)
        self.ventana1.mainloop()

    def abrirFormularioRegistro(self):
        self.ventana1.withdraw()
        aplicacion21 = FormularioRegistro(self.ventana1)

    def abrirFormularioUsuario(self):
        self.ventana1.withdraw()
        aplicacion22 = FormularioSesion(self.ventana1)

sistemaPanaderia = FormularioInicio()

#estilo = ttk.Style()
#print(estilo.theme_names())
#style.theme_use('clam') 
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
#mygreen = "#d2ffd2"
#myred = "#dd0202"
#estilo.theme_create( "yummy", parent="alt", settings={
#        "Notebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
#        "Notebook.Tab": {
#            "configure": {"padding": [5, 1], "background": mygreen },
#            "map":       {"background": [("selected", myred)],
#                          "expand": [("selected", [1, 1, 1, 0])] } } } )

#style.theme_use("yummy")


"""
from tkinter import Tk, Label
from PIL import Image, ImageTk

ventana = Tk()

# Cargar la imagen
imagen = Image.open("ruta_imagen")
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un Label con la imagen
label_imagen = Label(ventana, image=imagen_tk)
label_imagen.place(x=0, y=0, relwidth=1, relheight=1)

# Agregar otros widgets encima del Label
label_texto = Label(ventana, text="Texto")
label_texto.pack()

ventana.mainloop()


def mascara(imagen):
    # Crear una máscara con bordes redondeados
    ancho, alto = imagen.size
    radio = 30  # Radio de los bordes redondeados
    mascara = Image.new('L', (ancho, alto), 0)
    dibujar = ImageDraw.Draw(mascara)
    dibujar.ellipse((0, 0, radio * 2, radio * 2), fill=255)
    dibujar.rectangle((radio, 0, ancho - radio, alto), fill=255)
    dibujar.ellipse((ancho - radio * 2, 0, ancho, radio * 2), fill=255)
    return mascara

"""