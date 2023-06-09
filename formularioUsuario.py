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


class FormularioUsuario: # Se define la clase 
    def __init__(self, ventana, usuario): # Se inicializan los atributos de la clase ventana y usuario
        self.ventana22 = ventana # Se definen algunas variables de configuración.
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
        # Se crea un botón y se asigna una función a ejecutar cuando se presione el botón
        self.botonAtras = bt(self.ventana3, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioSesion)
        # Se utiliza método grid() para darle ubicación
        self.botonAtras.grid(row=0, column=0, sticky='w')
        #print(usuario)
        #print(type(usuario))
        # Se define una variable tipo con valor inicial "administrador"
        tipo="administrador"
        try:
            tipo = self.usuario.cargo # Se intenta acceder al atributo cargo del objeto. Si existe, se asigna el valor a tipo
            #print(tipo)
        except Exception:
            tipo = "administrador" # Si ocurre una excepción, se captura y se asigna "administrador a tipo"

        # Se crea una etiqueta en la ventana. Se configura el texto y el tipo de usuario, se establece la fuente, el color del texto y el color de fondo    
        self.labelSuperior = label(self.ventana3, text=f"¡Hola, {self.usuario.nombre}! ({tipo})", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w') # Se le da ubicación
        # Se crea una etiqueta en la ventana. Se establece fuente, color de texto y color de fondo.
        self.labelE = label(self.ventana3, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w') # Se le da ubicación

        
        # Se crea un botón con el texto "CUENTA". Se configura fuente, color de fondo, color de texto y se le asigna una función
        self.botonCuenta = bt(self.ventana3, text="CUENTA", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioCuenta)
        self.botonCuenta.grid(row=2, column=1, padx=10, pady=10, sticky='w') #Se ubica el boton
        #-Stock Producto
        if((tipo=="administrador")|(tipo=="vendedor")):
            self.botonVenta = bt(self.ventana3, text="VENTAS        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioVentas)
            self.botonVenta.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        #8 11 14 17
        #+Stock Materia Prima
        if((tipo=="administrador")|(tipo=="repositor")): #Verifica tipo de usuario
            # Si es V, se crea un botón con el texto "VENTAS" y se realizan configuraciones y se le asigna una funcion a ejecutar
            self.botonRepo = bt(self.ventana3, text="COMPRAS        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioCompras)
            self.botonRepo.grid(row=4, column=1, padx=10, pady=10, sticky='w') # Se ubica el botón
        #-Stock Materia Prima +StockProducto
        if((tipo=="administrador")|(tipo=="productor")): #Verifica tipo de usuario
            # Si es V, se crea un botón "PRODUCCIÓN", se realiza configuraciones y se le asigna una funcion a ejecutar
            self.botonPro = bt(self.ventana3, text="PRODUCCIÓN        ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioPro)
            self.botonPro.grid(row=5, column=1, padx=10, pady=10, sticky='w') # Se ubica el botón
        
        if(tipo=="administrador"): #Verifica tipo de usuario
            # Si es V, se crean botones "RECURSOS HUMANOS" y "PLANIFICACIÓN (MP/P)", se realizacon configuraciones y se les asigna una función a ejecutar
            self.botonRH = bt(self.ventana3, text="RECURSOS HUMANOS  ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioRH)
            self.botonRH.grid(row=6, column=1, padx=10, pady=10, sticky='w') # Se les da posición

            self.botonPlan = bt(self.ventana3, text="PLANIFICACIÓN (MP/P)  ", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioPlan)
            self.botonPlan.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        self.ventana3.mainloop() # Inicia un bucle de la interfaz que hace que la ventana permanezca abierta

    def abrirFormularioSesion(self): # Método que se encarga de abrir el formulario de sesión
        self.ventana22.deiconify() # Hace visible la ventana 22
        self.ventana3.destroy() # Destruye la ventana 3
        #self.ventana21.withdraw()
        #C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\
        #subprocess.call(["python", "C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\formularioInicio.py"])

    def abrirFormularioCuenta(self): # Método que abre formulario de cuenta
        self.ventana3.withdraw() # Retira visibilidad de la ventana 3
        aplicacion30 = FormularioCuenta(self.ventana3, self.usuario) # Crea una instancia de FormularioCuenta pasando ventana 3 y el objeto usuario

    def abrirFormularioVentas(self): # Abre formulario de ventas 
        self.ventana3.withdraw() # Retira visibilidad de ventana 3
        aplicacion31 = FormularioVentas(self.ventana3, self.usuario) # Crea una instancia de FormularioVentas pansado ventana 3 y objeto usuario

    def abrirFormularioCompras(self): # Abre formulario de compras
        self.ventana3.withdraw() #Retira visibilidad de ventana 3
        aplicacion32 = FormularioCompras(self.ventana3, self.usuario) # Crea una instancia de FormularioCompras pasando ventana 3 y usuario como argumento

    def abrirFormularioPro(self): # Abre formulario de producción
        self.ventana3.withdraw() # Retira visibilidad de ventana 3
        aplicacion33 = FormularioProduccion(self.ventana3, self.usuario) # Crea una instancia de FormularioProducción pasando ventana 3 y usuario

    def abrirFormularioRH(self): # Abre formulario de RR.HH. 
        self.ventana3.withdraw() # Retira la visibilidad de ventana 3
        aplicacion34 = FormularioRH(self.ventana3, self.usuario) # Crea una instancia de FormularioRH pasando ventana 3 y usuario

    def abrirFormularioPlan(self): # Abre formulario de planificación
        self.ventana3.withdraw() # Retira la visibilidad de ventana 3
        aplicacion35 = FormularioPlan(self.ventana3, self.usuario) # Crea una instancia de FormularioPlan pasando ventana 3 y usuario

        
        

    

        
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
