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
from factura import Factura
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
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
        self.tema = "itft1" #itft1 smog
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
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
        self.productoVerEliminar()
        self.materiaPVerEliminar()
        self.verProductosMasV()

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
        listaPro = sorted(listaPro)

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
        listaMat = sorted(listaMat)
         
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

    def productoVerEliminar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.pagina5.config(width=800, height=750)
        self.cuaderno1.add(self.pagina5, text="Ver Producto")

        self.labelframe5 = labelF(self.pagina5, text="Información de Producto", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.listaNom2 = Producto.recuperarNombres()
        
        self.listaNom2 = [x[0] for x in self.listaNom2]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        self.listaNom2 = sorted(self.listaNom2)
        
        self.labelProve2 = label(self.labelframe5, text="Producto:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProve2.grid(column=0, row=1, padx=4, pady=4)

        self.comboProv2 = ttk.Combobox(self.labelframe5, font=(self.fuente, 20), width = 15, values=self.listaNom2)
        # Adding combobox drop down list
        self.comboProv2.set(self.listaNom2[0])
        self.comboProv2.grid(column = 1, row = 1)
        self.comboProv2.bind("<<ComboboxSelected>>", self.on_selectP2)

        self.scrolledtext2 = st.ScrolledText(self.labelframe5, font=(self.fuente, 20), width=20, height=10)
        self.scrolledtext2.grid(column=0, row=2, padx=10, pady=10)
        self.on_selectP2()

        self.botonEliminar = bt(self.labelframe5, text="Dar de baja", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.bajaProducto)
        self.botonEliminar.grid(column=1, row=2, padx=4, pady=4)

    def bajaProducto(self):
        indice = self.comboProv2.current()
        nombre = self.comboProv2.get()
        self.listaNom2.pop(indice)
        self.comboProv2.config(values=self.listaNom2)
        idProv = Producto.obtenerId((nombre, ))
        Producto.bajaProducto(idProv)
        mb.showinfo("¡Felicidades!", "Producto dado de baja")

    def on_selectP2(self, event=None):
        indice = self.comboProv2.current()
        self.scrolledtext2.config(state="normal")
        
        produc1 = Producto.obtenerPro(self.comboProv2.get())
        #self.nombre = nombre
        #self.descripcion = descripcion
        #self.precioU = precioUnitario
        #self.stock = stock
        #self.stockM
        mensaje = f"Nombre: {produc1.nombre}\nUnidad de medida: {produc1.descripcion}\nPrecio unitario: {produc1.precioU}\nStock actual: {produc1.stock}\nStock mínimo: {produc1.stockM}"
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert(tk.END, mensaje)
        self.scrolledtext2.config(state="disabled")

    
    def materiaPVerEliminar(self):
        self.pagina6 = ttk.Frame(self.cuaderno1)
        self.pagina6.config(width=800, height=750)
        self.cuaderno1.add(self.pagina6, text="Ver Materia Prima")
        #labelframe5 -> 6
        self.labelframe6 = labelF(self.pagina6, text="Información de Materia Prima", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe6.grid(column=0, row=0, padx=5, pady=10)
        #listaNom2 -> 3
        self.listaNom3 = MateriaPrima.recuperarNombres()
        
        self.listaNom3 = [x[0] for x in self.listaNom3]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        self.listaNom3 = sorted(self.listaNom3)
        #labelProve2 -> 3
        self.labelProve3 = label(self.labelframe6, text="Materia prima:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProve3.grid(column=0, row=1, padx=4, pady=4)
        #comboProv2 -> 3
        self.comboProv3 = ttk.Combobox(self.labelframe6, font=(self.fuente, 20), width = 15, values=self.listaNom3)
        # Adding combobox drop down list
        self.comboProv3.set(self.listaNom3[0])
        self.comboProv3.grid(column = 1, row = 1)
        self.comboProv3.bind("<<ComboboxSelected>>", self.on_selectP3)
        #scrolledtext2 -> 3
        self.scrolledtext3 = st.ScrolledText(self.labelframe6, font=(self.fuente, 20), width=20, height=10)
        self.scrolledtext3.grid(column=0, row=2, padx=10, pady=10)
        self.on_selectP3()

        self.botonEliminar = bt(self.labelframe6, text="Dar de baja", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.bajaCliente)
        self.botonEliminar.grid(column=1, row=2, padx=4, pady=4)

    def bajaCliente(self):
        indice = self.comboProv3.current()
        nombre = self.comboProv3.get()
        self.listaNom3.pop(indice)
        self.comboProv3.config(values=self.listaNom3)
        idProv = MateriaPrima.obtenerId((nombre, ))
        MateriaPrima.bajaMateriaP(idProv)
        mb.showinfo("¡Felicidades!", "Materia prima dada de baja")

    def on_selectP3(self, event=None):
        indice = self.comboProv3.current()
        self.scrolledtext3.config(state="normal")
        
        mat1 = MateriaPrima.obtenerMat(self.comboProv3.get())
        
        mensaje = f"Nombre: {mat1.nombre}\nUnidad de medida: {mat1.descripcion}\nPrecio unitario: {mat1.precioU}\nStock actual: {mat1.stock}\nStock mínimo: {mat1.stockM}"
        self.scrolledtext3.delete("1.0", tk.END)
        self.scrolledtext3.insert(tk.END, mensaje)
        self.scrolledtext3.config(state="disabled")
    
    def verProductosMasV(self):
        self.pagina7 = ttk.Frame(self.cuaderno1)
        self.pagina7.config(width=800, height=750)
        self.cuaderno1.add(self.pagina7, text="Ver Productos Más Vendidos")
        self.labelframe7 = labelF(self.pagina7, text="Información Productos Más Vendidos", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe7.grid(column=0, row=0, padx=5, pady=10)

        self.labelFInicio = label(self.labelframe7, text='Fecha de inicio:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFInicio.grid(column=0, row=0, padx=4, pady=4)
        self.entradaFInicio = DateEntry(self.labelframe7, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFInicio.grid(column=1, row=0, padx=4, pady=4)

        self.labelFFin = label(self.labelframe7, text='Fecha de fin:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFFin.grid(column=0, row=1, padx=4, pady=4)
        self.entradaFFin = DateEntry(self.labelframe7, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFFin.grid(column=1, row=1, padx=4, pady=4)

        self.botonConsultar = bt(self.labelframe7, text="Consultar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.calcularProductosMasV)
        self.botonConsultar.grid(column=1, row=10, padx=4, pady=4)

    def calcularProductosMasV(self):
        fechaIni=datetime.strptime(self.entradaFInicio.get(), '%m/%d/%y')
        fechaFin=datetime.strptime(self.entradaFFin.get(), '%m/%d/%y')
        if(fechaIni <= fechaFin): #si es válida la fecha
            facturas = Factura.recuperarFechaEspecifica(fechaIni, fechaFin)
            #[(fact1),(fact2)]
            #idFactura numeroFactura fechaEmisionFactura idTipoFactura precioTotal idMedioPago idCliente idUsuario
            #print(facturas)
            nombresProductos=[]
            cantidades=[]
            for factu in facturas:
                factuDetalle=Factura.obtenerDetalle(factu[0])
                for detalle in factuDetalle:
                    #idDetalleF, cantidad, precioUnitario, idFactura, idProducto
                    idPro = detalle[4]
                    nombreP = Producto.obtenerAtrib((idPro, ), ("idProducto", ), "productos", "nombreProducto")
                    nombreP = nombreP[0][0]
                    nombresProductos.append(nombreP)
                    cantidades.append(detalle[1])
            #print(nombresProductos)
            #print(cantidades)
            # Creamos un diccionario para almacenar las cantidades acumuladas
            productosCantidades = {}
            # Recorremos las listas y acumulamos las cantidades
            for nombre, cant in zip(nombresProductos, cantidades):
                if nombre not in productosCantidades: # Si el nombre no está en el diccionario entonces lo agregamos con su cantidad inicial
                    productosCantidades[nombre] = cant
                else: # Si no, entonces quiere decir que esta en el diccionario, por lo tanto acumulamos
                    productosCantidades[nombre] += cant

            # Convertimos el diccionario a dos listas otra vez
            nombresProductos = list(productosCantidades.keys())
            cantidades = list(productosCantidades.values())
            # Generamos los colores para cada barra
            colores = plt.cm.viridis(np.linspace(0, 1, len(nombresProductos)))
            # Creamos las barras
            plt.bar(nombresProductos, cantidades, color=colores)
            plt.xlabel('Productos')
            plt.ylabel('Cantidad vendida')
            plt.title(f'Venta de productos entre {self.entradaFInicio.get()} y {self.entradaFFin.get()}')

            plt.show()
        else:
            mb.showerror("Error", "La fecha de inicio debe ser antes o igual a la fecha de fin.")

            # Mostrar el resultado
                #for id, cantidad in cantidades_acumuladas.items():
                #print(f"idProduc: {id}, cantidad: {cantidad}")