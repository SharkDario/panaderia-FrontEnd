import sys
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
from funciones import funciones as f
from administrador import Administrador
from datetime import datetime
import locale
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
from materiaprima import MateriaPrima
from producto import Producto
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

class FormularioPlan:
    def __init__(self, ventana, usuario):
        self.usuario = usuario
        self.tema = "blue"
        self.back = 'light blue'
        self.backB = 'SteelBlue3'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana36 = ThemedTk() #tk.Tk()
        self.ventana36.configure(bg=self.back)
        self.ventana36.title("3.6 - PLANIFICACIÓN (MP/P)")
        self.ventana36.geometry("900x750")
        self.ventana36.geometry("+10+20")

        
        
        self.labelSuperior = label(self.ventana36, text="PLANIFICACIÓN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        

        self.botonAtras = bt(self.ventana36, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana36)

        #print(self.ventana34.get_themes())
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        #SI: blue, smog, black, adapta
        #EH: kroc, plastik, winxpblue, itft1, aquativo, clam
        #NO: equilux, keramik, elegance, radiance, breeze, clearlooks, ubuntu, yaru, scidmint
        #[ 'alt', 'scidpurple', 'scidpink', 
        #'default', 'scidblue', 'classic', 'xpnative', 
        #, 'scidgrey', 'scidsand', 'scidgreen', 'arc', 'vista', 'winnative']

        self.materiaPrima()
        self.producto()
        self.fabricacion()

        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana36.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify()
        self.ventana36.destroy()

    def materiaPrima(self):
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Materia Prima")
        #nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo
        #El stock es 0 hasta que se empiecen a cargar por los remitos
        self.labelframe1 = labelF(self.pagina1, text="Registrar Nueva Materia Prima", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.labelNombre = label(self.labelframe1, text="Nombre:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre.grid(column=0, row=0, padx=4, pady=4)
        self.entradaNombre = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre.grid(column=1, row=0, padx=4, pady=4)

        self.labelDescrip = label(self.labelframe1, text="Descripción:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDescrip.grid(column=0, row=1, padx=4, pady=4)
        self.entradaDescrip = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDescrip.grid(column=1, row=1, padx=4, pady=4)

        self.labelPU = label(self.labelframe1, text="Precio unitario:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPU.grid(column=0, row=2, padx=4, pady=4)
        self.entradaPU = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaPU.grid(column=1, row=2, padx=4, pady=4)
        
        self.labelStockM = label(self.labelframe1, text="Stock mínimo:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelStockM.grid(column=0, row=4, padx=4, pady=4)
        self.entradaStockM = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaStockM.grid(column=1, row=4, padx=4, pady=4)

        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevaMateriaPrima)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevaMateriaPrima(self):
        idMateria = MateriaPrima.obtenerId((self.entradaNombre.get(), ))
        nombre = f.ingNombreMatPro(self.entradaNombre.get(), idMateria, "de la materia prima")
        descrip = self.entradaDescrip.get()
        precioU = f.ingNumPosi(self.entradaPU.get(), "El precio unitario")
        stockM = f.ingNumPosi(self.entradaStockM.get(), "El stock mínimo")
        
        entrysValidos = ((nombre!="")&(descrip!="")&(type(precioU) is not list)&(type(stockM) is not list)&(type(nombre) is not list))
        if(entrysValidos):
            #Al dar de alta una nueva materia prima su stock es 0
            nuevaMP = MateriaPrima(nombre, descrip, precioU, 0, stockM)
            mb.showinfo("¡Felicidades!", "Materia prima registrada")
        else:
            mensaje=""
            #print(dni)
            if(nombre == ""):
                mensaje += "\nEl nombre no puede estar vacío."
            if(descrip == ""):
                mensaje += "\nLa descripción no puede estar vacía."
            if(type(precioU) is list):
                mensaje += "\n"+precioU[0]
            if(type(stockM) is list):
                mensaje += "\n"+stockM[0]
            if(type(nombre) is list):
                mensaje += "\n"+nombre[0]
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDescrip.delete(0, tk.END)
        self.entradaPU.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaStockM.delete(0, tk.END)

    def producto(self):
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina2.config(width=800, height=750)
        self.cuaderno1.add(self.pagina2, text="Producto")
        #nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo
        #El stock es 0 hasta que se empiecen a cargar por los remitos
        self.labelframe2 = labelF(self.pagina2, text="Registrar Nuevo Producto", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.labelNombre2 = label(self.labelframe2, text="Nombre:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre2.grid(column=0, row=0, padx=4, pady=4)
        self.entradaNombre2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre2.grid(column=1, row=0, padx=4, pady=4)

        self.labelDescrip2 = label(self.labelframe2, text="Descripción:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDescrip2.grid(column=0, row=1, padx=4, pady=4)
        self.entradaDescrip2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDescrip2.grid(column=1, row=1, padx=4, pady=4)

        self.labelPU2 = label(self.labelframe2, text="Precio unitario:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPU2.grid(column=0, row=2, padx=4, pady=4)
        self.entradaPU2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaPU2.grid(column=1, row=2, padx=4, pady=4)
        
        self.labelStockM2 = label(self.labelframe2, text="Stock mínimo:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelStockM2.grid(column=0, row=4, padx=4, pady=4)
        self.entradaStockM2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaStockM2.grid(column=1, row=4, padx=4, pady=4)

        self.botonConfirmar2 = bt(self.labelframe2, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoProducto)
        self.botonConfirmar2.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevoProducto(self):
        idProducto = Producto.obtenerId((self.entradaNombre2.get(), ))
        nombre = f.ingNombreMatPro(self.entradaNombre2.get(), idProducto, "del producto")
        descrip = self.entradaDescrip2.get()
        precioU = f.ingNumPosi(self.entradaPU2.get(), "El precio unitario")
        stockM = f.ingNumPosi(self.entradaStockM2.get(), "El stock mínimo")
        
        entrysValidos = ((nombre!="")&(descrip!="")&(type(precioU) is not list)&(type(stockM) is not list)&(type(nombre) is not list))
        if(entrysValidos):
            #Al dar de alta un nuevo producto su stock es 0
            nuevoPro = Producto(nombre, descrip, precioU, 0, stockM)
            mb.showinfo("¡Felicidades!", "Producto registrado")
        else:
            mensaje=""
            #print(dni)
            if(nombre == ""):
                mensaje += "\nEl nombre no puede estar vacío."
            if(descrip == ""):
                mensaje += "\nLa descripción no puede estar vacía."
            if(type(precioU) is list):
                mensaje += "\n"+precioU[0]
            if(type(stockM) is list):
                mensaje += "\n"+stockM[0]
            if(type(nombre) is list):
                mensaje += "\n"+nombre[0]
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDescrip2.delete(0, tk.END)
        self.entradaPU2.delete(0, tk.END)
        self.entradaNombre2.delete(0, tk.END)
        self.entradaStockM2.delete(0, tk.END)
    

    def fabricacion(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina3.config(width=800, height=750)
        self.cuaderno1.add(self.pagina3, text="Fabricación (Añadir)")
        #nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo
        #El stock es 0 hasta que se empiecen a cargar por los remitos
        self.labelframe3 = labelF(self.pagina3, text="Añadir materia prima a producto", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        
        # Combobox creation
        # listaPro empieza siendo una lista de tuplas [("Chipa", ), ("Pan de queso", )]
        listaPro = Producto.recuperarNombres()
        # listaPro se convierte en una lista con únicamente los nombres contenidos en cada tupla ["Chipa", "Pan de queso"]
        listaPro = [x[0] for x in listaPro]

        self.comboPro = ttk.Combobox(self.labelframe3, font=(self.fuente, 20), width = 15, values=listaPro)
        # Adding combobox drop down list
        self.comboPro.set(listaPro[0])
        self.comboPro.grid(column = 0, row = 1)
        self.comboPro.bind("<<ComboboxSelected>>", self.on_selectP)

        self.textPro = tk.StringVar()
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (listaPro[0], ), "Producto")
        descripP = descripP[0]
        #print(descripP[0])
        self.textPro = descripP[0]
        self.labelPro = label(self.labelframe3, text=self.textPro, font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPro.grid(column=1, row=1, padx=4, pady=4)


        listaMat = MateriaPrima.recuperarNombres()
        listaMat = [x[0] for x in listaMat]
         
        descripMP = MateriaPrima.obtenerArti("materiasprimas", "descripcionMateriaPrima", (listaMat[0], ), "MateriaPrima")
        descripMP = descripMP[0]
        self.textMat = descripMP[0]
        self.labelMat = label(self.labelframe3, text=self.textMat, font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelMat.grid(column=1, row=2, padx=4, pady=4)

        self.comboMat = ttk.Combobox(self.labelframe3, font=(self.fuente, 20), width = 15, values=listaMat)
        # Adding combobox drop down list
        self.comboMat.set(listaMat[0])
        self.comboMat.grid(column = 0, row = 2)
        self.comboMat.bind("<<ComboboxSelected>>", self.on_selectMP)

        self.labelCant = label(self.labelframe3, text="Cantidad materia prima:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCant.grid(column=0, row=3, padx=4, pady=4)
        self.entradaCant = entry(self.labelframe3, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCant.grid(column=1, row=3, padx=4, pady=4)

        self.botonConfirmar2 = bt(self.labelframe3, text="Añadir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.annadirMPaP)
        self.botonConfirmar2.grid(column=1, row=10, padx=4, pady=4)

    def on_selectP(self, event):
        nombreP = self.comboPro.get()
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (nombreP, ), "Producto")
        descripP = descripP[0]
        self.textPro = descripP[0]
        self.labelPro.config(text=self.textPro)

    def on_selectMP(self, event):
        nombreMP = self.comboMat.get()
        descripMP = MateriaPrima.obtenerArti("materiasprimas", "descripcionMateriaPrima", (nombreMP, ), "MateriaPrima")
        descripMP = descripMP[0]
        self.textMat = descripMP[0]
        self.labelMat.config(text=self.textMat)

    def annadirMPaP(self):
        #print("1", )
        cantidad = f.ingNumPosi(self.entradaCant.get(), "La cantidad")
        
        if((type(cantidad) is not list)&(cantidad!="")):
            idMatPrima = MateriaPrima.obtenerId((self.comboMat.get(), ))
            producto = Producto.obtenerPro(self.comboPro.get())
            valorV = producto.fabricacion(idMatPrima, cantidad)
            if(valorV):
                mb.showerror("Error", f'{self.comboMat.get()} ya existe en la fabricación del producto {self.comboPro.get()}')
            else:
                mb.showinfo("¡Felicidades!", f'{self.comboMat.get()} añadido a {self.comboPro.get()}')
        else:
            mensaje=""
            #print(dni)
            if(cantidad == ""):
                mensaje += "\nLa cantidad no puede estar vacía."
            if(type(cantidad) is list):
                mensaje += "\n"+cantidad[0]
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaCant.delete(0, tk.END)

    