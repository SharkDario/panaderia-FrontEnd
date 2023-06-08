from pickle import FALSE
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
from proveedor import Proveedor
from materiaprima import MateriaPrima
from producto import Producto
from remito import Remito
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

class FormularioProduccion:
    def __init__(self, ventana, usuario):
        self.usuario = usuario
        self.tema = "itft1" #itft1 smog
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana34 = ThemedTk() #tk.Tk()
        self.ventana34.configure(bg=self.back)
        self.ventana34.title("3.4 - PRODUCCIÓN")
        self.ventana34.geometry("900x750")
        self.ventana34.geometry("+10+20")

        
        
        self.labelSuperior = label(self.ventana34, text="PRODUCCIÓN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        

        self.botonAtras = bt(self.ventana34, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana34)

        #print(self.ventana34.get_themes())
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        # produccion() es para ingresar la cantidad de productos y sumarlos al stock
        self.produccion()
        # 
        self.producto()
        self.productoSM()
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana34.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify()
        self.ventana34.destroy()
    
    def produccion(self):
        #productos
        # Combobox creation
        # listaPro empieza siendo una lista de tuplas [("Chipa", ), ("Pan de queso", )]
        listaPro = Producto.recuperarNombres()
        # listaPro se convierte en una lista con únicamente los nombres contenidos en cada tupla ["Chipa", "Pan de queso"]
        listaPro = [x[0] for x in listaPro]
        listaPro.sort(key=lambda x: x[0])

        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Producción")

        self.labelframe1 = labelF(self.pagina1, text="Producción", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.labelPro = label(self.labelframe1, text="Producto:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPro.grid(column=0, row=1, padx=4, pady=4)

        self.comboPro = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15, values=listaPro)
        # Adding combobox drop down list
        self.comboPro.set(listaPro[0])
        self.comboPro.grid(column = 1, row = 1)
        self.comboPro.bind("<<ComboboxSelected>>", self.on_selectP)
        
        self.textPro = tk.StringVar()
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (listaPro[0], ), "Producto")
        descripP = descripP[0]
        #print(descripP[0])
        self.textPro = descripP[0]
        self.labelCant = label(self.labelframe1, text=f"Cantidad ({self.textPro}):", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCant.grid(column=0, row=2, padx=4, pady=4)

        self.entradaCant = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCant.grid(column=1, row=2, padx=4, pady=4)

        self.botonConfirmar = bt(self.labelframe1, text="Producir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.cargaStockPro)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)

        self.labeltextProP = label(self.labelframe1, text=f"MATERIA PRIMA\t\t  CANTIDAD", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labeltextProP.grid(column=0, row=11, padx=4, pady=4)

        self.scrolledtextProP = st.ScrolledText(self.labelframe1, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProP.grid(column=0, row=12, padx=5, pady=10)
        self.on_selectP()

    def cargaStockPro(self):
        # Actualizar el stock de productos
        cantidad = f.ingNumPosi(self.entradaCant.get(), "La cantidad")

        #si cantidad es mayor a 0 entonces hago todo lo de abajo
       
        if(type(cantidad) is not list):
        
            nombre = self.comboPro.get()
            producto1 = Producto.obtenerPro(nombre)
            idPro = Producto.obtenerId((nombre, ))
            listaMateriaPrima = producto1.recuperarMateriasPrimas(idPro)

            MPSuficiente=True
            for datoMP in listaMateriaPrima:
                #datoMP - (idMateriaPrima, CantidadMateriaPrima)
                idMP = datoMP[0] 
                cantidadMP = datoMP[1] #cantidad por la receta
                stockMP = MateriaPrima.obtenerAtrib((idMP, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
                stockMP = stockMP[0][0]
                cantidadMPTotal = cantidad * cantidadMP # cantidad ingresada x la cantidadMP necesaria
                if(cantidadMPTotal>stockMP): #entonces no hay suficiente materia prima en stock para realizar la fabricación
                    MPSuficiente=False
                    break

            #si tengo la materia prima suficiente (con respecto a la cantidad) entonces hago todo lo de abajo
            if(MPSuficiente):
                
                for datoMP in listaMateriaPrima:
                    #datoMP - (idMateriaPrima, CantidadMateriaPrima)
                    idMP = datoMP[0]
                    cantidadMP = datoMP[1] #cantidad por la receta
                    stockMP = MateriaPrima.obtenerAtrib((idMP, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
                    stockMP = stockMP[0][0]
                    cantidadMPTotal = cantidad * cantidadMP # cantidad ingresada x la cantidadMP necesaria
                    nuevoStockMP = stockMP - cantidadMPTotal
                    MateriaPrima.modificarArti("materiasprimas", "idMateriaPrima", nuevoStockMP, idMP, "stockMateriaPrima")
                
                stockActual = Producto.obtenerAtrib((idPro, ), ("idProducto", ), "productos", "stockProducto")
                stockActual = stockActual[0][0]

                nuevoStock = stockActual + cantidad

                Producto.modificarArti("productos", "idProducto", nuevoStock, idPro, "stockProducto")
                mb.showinfo("¡Felicidades!", "Producción cargada correctamente")
            else:
                mb.showerror("Error", "Materia prima insuficiente")
        else:
            mb.showerror("Error", cantidad[0])
        self.entradaCant.delete(0, tk.END)

    def on_selectP(self, event=None):
        self.scrolledtextProP.delete('1.0', tk.END)
        nombreP = self.comboPro.get()
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (nombreP, ), "Producto")
        descripP = descripP[0]
        self.textPro = descripP[0]
        self.labelCant.config(text=f"Cantidad ({self.textPro}):")

        producto2 = Producto.obtenerPro(nombreP)
        idPro2 = Producto.obtenerId((nombreP, ))
        listaMateriaPrima2 = producto2.recuperarMateriasPrimas(idPro2)
        for idMatCant in listaMateriaPrima2:
            nombreDescrip = MateriaPrima.obtenerAtrib((idMatCant[0], ), ("idMateriaPrima", ), "materiasprimas", "nombreMateriaPrima, descripcionMateriaPrima")
            nombreDescrip = nombreDescrip[0]
            #nombre cantidad
            self.scrolledtextProP.insert(tk.END, f"{nombreDescrip[0]} ({nombreDescrip[1]})\t\t\t\t{idMatCant[1]}\n")

    def productoSM(self):
        # lista de productos con falta en el stock, con el nombre, descripcion, el stock minimo y su stock actual
        listaProductoSM = Producto.recuperarNombresStockMinimo()
        listaProductoSM.sort(key=lambda x: x[0])
        self.pagina3 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina3.config(width=800, height=750)
        self.cuaderno1.add(self.pagina3, text="Stock mínimo")
        
        self.labelframe3 = labelF(self.pagina3, text="Lista de productos con stock faltante", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.labelSM = label(self.labelframe3, text="NOMBRE\t\tSTOCK MÍNIMO\tSTOCK ACTUAL", font=(self.fuente, 15), fg=self.fuenteB, background=self.back)
        self.labelSM.grid(column=0, row=1, padx=4, pady=4)

        self.scrolledtextProSM = st.ScrolledText(self.labelframe3, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProSM.grid(column=0, row=2, padx=5, pady=10)

        #print(listaMateriaSM)
        for producto in listaProductoSM:
            #producto = (nombre, descripcion, stock minimo, stock actual)
            self.scrolledtextProSM.insert(tk.END, f"{producto[0]} ({producto[1]})\t\t  {producto[2]}\t\t{producto[3]}\n")
        self.scrolledtextProSM.configure(state='disabled')

    def producto(self):
        # lista de productos, con el nombre, descripcion, el precio unitario y su stock actual
        listaProductoN = Producto.recuperarNombresDesPUStock()
        listaProductoN.sort(key=lambda x: x[0])
        self.pagina4 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina4.config(width=800, height=750)
        self.cuaderno1.add(self.pagina4, text="Productos")
        
        self.labelframe4 = labelF(self.pagina4, text="Lista de productos", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.labelSM = label(self.labelframe4, text="NOMBRE\t\tPRECIO UNITARIO\tSTOCK ACTUAL", font=(self.fuente, 15), fg=self.fuenteB, background=self.back)
        self.labelSM.grid(column=0, row=1, padx=4, pady=4)

        self.scrolledtextProN = st.ScrolledText(self.labelframe4, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProN.grid(column=0, row=2, padx=5, pady=10)

        #print(listaMateriaSM)
        for producto in listaProductoN:
            #producto = (nombre, descripcion, precioU, stock actual)
            self.scrolledtextProN.insert(tk.END, f"{producto[0]} ({producto[1]})\t\t  {producto[2]}\t\t{producto[3]}\n")
        self.scrolledtextProN.configure(state='disabled')
