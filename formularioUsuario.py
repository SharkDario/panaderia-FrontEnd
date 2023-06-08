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
import tkinter as tk
from ttkthemes import ThemedTk
from usuario import Usuario
from formularioRH import FormularioRH
from formularioPlan import FormularioPlan
from formularioCuenta import FormularioCuenta
from formularioCompras import FormularioCompras
from formularioProduccion import FormularioProduccion
from formularioVentas import FormularioVentas
# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes


class FormularioUsuario:
    def __init__(self, ventana, usuario):
        self.ventana22 = ventana
        self.usuario = usuario
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ThemedTk()
        self.ventana3.configure(bg=self.back)
        self.ventana3.geometry("900x750")
        self.ventana3.geometry("+10+20")
        self.ventana3.title("3 - USUARIO")
        #🔙
        style = ttk.Style(self.ventana3)
        style.theme_use("blue")
        self.botonAtras = bt(self.ventana3, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioSesion)
        self.botonAtras.grid(row=0, column=0, sticky='w')
        #print(usuario)
        #print(type(usuario))
        tipo="administrador"
        try:
            tipo = self.usuario.cargo
            #print(tipo)
        except Exception:
            tipo = "administrador"

        self.labelSuperior = label(self.ventana3, text=f"¡Hola, {self.usuario.nombre}! ({tipo})", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')

        self.labelE = label(self.ventana3, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w')

        

        self.botonCuenta = bt(self.ventana3, text="CUENTA", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioCuenta)
        self.botonCuenta.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        #-Stock Producto
        if((tipo=="administrador")|(tipo=="vendedor")):
            self.botonVenta = bt(self.ventana3, text="VENTAS        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioVentas)
            self.botonVenta.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        #8 11 14 17
        #+Stock Materia Prima
        if((tipo=="administrador")|(tipo=="repositor")):
            self.botonRepo = bt(self.ventana3, text="COMPRAS        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioCompras)
            self.botonRepo.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        #-Stock Materia Prima +StockProducto
        if((tipo=="administrador")|(tipo=="productor")):
            self.botonPro = bt(self.ventana3, text="PRODUCCIÓN        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioPro)
            self.botonPro.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        
        if(tipo=="administrador"):
            self.botonRH = bt(self.ventana3, text="RECURSOS HUMANOS  ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioRH)
            self.botonRH.grid(row=6, column=1, padx=10, pady=10, sticky='w')

            self.botonPlan = bt(self.ventana3, text="PLANIFICACIÓN (MP/P)  ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioPlan)
            self.botonPlan.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        self.ventana3.mainloop()

    def abrirFormularioSesion(self):
        self.ventana22.deiconify()
        self.ventana3.destroy()
        #self.ventana21.withdraw()
        #C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\
        #subprocess.call(["python", "C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\formularioInicio.py"])

    def abrirFormularioCuenta(self):
        self.ventana3.withdraw()
        aplicacion30 = FormularioCuenta(self.ventana3, self.usuario)

    def abrirFormularioVentas(self):
        self.ventana3.withdraw()
        aplicacion31 = FormularioVentas(self.ventana3, self.usuario)

    def abrirFormularioCompras(self):
        self.ventana3.withdraw()
        aplicacion32 = FormularioCompras(self.ventana3, self.usuario)

    def abrirFormularioPro(self):
        self.ventana3.withdraw()
        aplicacion33 = FormularioProduccion(self.ventana3, self.usuario)

    def abrirFormularioRH(self):
        self.ventana3.withdraw()
        aplicacion34 = FormularioRH(self.ventana3, self.usuario)

    def abrirFormularioPlan(self):
        self.ventana3.withdraw()
        aplicacion35 = FormularioPlan(self.ventana3, self.usuario)

        
        

    

        
        #subprocess.call(["python", "formularioInicio.py"])



#aplicacion1 = FormularioRegistro()

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



"""