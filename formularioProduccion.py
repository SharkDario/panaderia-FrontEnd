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

        #estilo del cuaderno
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        # produccion() es para ingresar la cantidad de productos y sumarlos al stock
        self.produccion()
        # visualizar la lista de productos
        self.producto()
        # visualizar la lista de productos con stock faltante
        self.productoSM()
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana34.mainloop() #abre la ventana

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify() #se muestra la ventana3
        self.ventana34.destroy() #se cierra la ventana34
    
    def produccion(self):
        #productos
        # Combobox creation
        # listaPro empieza siendo una lista de tuplas [("Chipa", ), ("Pan de queso", )]
        listaPro = Producto.recuperarNombres()
        # listaPro se convierte en una lista con únicamente los nombres contenidos en cada tupla ["Chipa", "Pan de queso"]
        listaPro = [x[0] for x in listaPro]
        # se ordena la listaPro alfabeticamiento segun el nombre del producto
        listaPro.sort(key=lambda x: x[0])

        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Producción")
        # labelframe de la produccion
        self.labelframe1 = labelF(self.pagina1, text="Producción", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        # label y combobox del producto
        self.labelPro = label(self.labelframe1, text="Producto:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPro.grid(column=0, row=1, padx=4, pady=4)
        # el combo guarda la lista de productos
        self.comboPro = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15, values=listaPro)
        # Adding combobox drop down list
        self.comboPro.set(listaPro[0])
        self.comboPro.grid(column = 1, row = 1)
        self.comboPro.bind("<<ComboboxSelected>>", self.on_selectP) #cada vez q se selecciona se activa la funcion on_selectP
        
        self.textPro = tk.StringVar()
        # se obtiene la descripcion del producto
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (listaPro[0], ), "Producto")
        # descripP es una tupla con un valor, se convierte en un solo valor
        descripP = descripP[0]
        # en textPro se guarda la descripcion
        self.textPro = descripP[0] # en el label de cantidad se escribira Cantidad kg por ejemplo
        # label y entrada de la cantidad de materia prima
        self.labelCant = label(self.labelframe1, text=f"Cantidad ({self.textPro}):", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCant.grid(column=0, row=2, padx=4, pady=4)
        self.entradaCant = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCant.grid(column=1, row=2, padx=4, pady=4)
        # boton que al ser presionado activa cargaStockPro
        self.botonConfirmar = bt(self.labelframe1, text="Producir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.cargaStockPro)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        self.labeltextProP = label(self.labelframe1, text=f"MATERIA PRIMA\t\t  CANTIDAD", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labeltextProP.grid(column=0, row=11, padx=4, pady=4)
        #scrolledtext de la materia prima, con sus nombres, descripcion y cantidad
        self.scrolledtextProP = st.ScrolledText(self.labelframe1, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProP.grid(column=0, row=12, padx=5, pady=10)
        self.on_selectP() #acciona el metodo on_selectP()

    def cargaStockPro(self):
        # Actualizar el stock de productos
        cantidad = f.ingNumPosi(self.entradaCant.get(), "La cantidad") # se valida que la cantidad sea positiva
        # si cantidad es mayor a 0 entonces hago todo lo de abajo
        if(type(cantidad) is not list): 
            nombre = self.comboPro.get() # se obtiene el nombre del producto mediante el comboPro
            producto1 = Producto.obtenerPro(nombre) # se obtiene el producto mediante el nombre
            idPro = Producto.obtenerId((nombre, )) # se obtiene el id producto mediante el nombre
            listaMateriaPrima = producto1.recuperarMateriasPrimas(idPro) # se recuperan los nombres de las materias primas que se utilizan en el producto
            MPSuficiente=True
            for datoMP in listaMateriaPrima: # se recorre cada materia prima de la lista
                #datoMP - (idMateriaPrima, CantidadMateriaPrima)
                idMP = datoMP[0] 
                cantidadMP = datoMP[1] #cantidad por la receta
                stockMP = MateriaPrima.obtenerAtrib((idMP, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
                stockMP = stockMP[0][0] # la lista de tupla [(stockMP,)] se convierte en un valor stockMP
                cantidadMPTotal = cantidad * cantidadMP # cantidad ingresada x la cantidadMP necesaria
                if(cantidadMPTotal>stockMP): #entonces no hay suficiente materia prima en stock para realizar la fabricación
                    MPSuficiente=False
                    break

            #si tengo la materia prima suficiente (con respecto a la cantidad) entonces hago todo lo de abajo
            if(MPSuficiente):
                for datoMP in listaMateriaPrima: # se recorre cada materia prima de la lista
                    #datoMP - (idMateriaPrima, CantidadMateriaPrima)
                    idMP = datoMP[0]
                    cantidadMP = datoMP[1] #cantidad por la receta
                    stockMP = MateriaPrima.obtenerAtrib((idMP, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
                    stockMP = stockMP[0][0] # la lista de tupla [(stockMP,)] se convierte en un valor stockMP
                    cantidadMPTotal = cantidad * cantidadMP # cantidad ingresada x la cantidadMP necesaria
                    nuevoStockMP = stockMP - cantidadMPTotal # se calcula el nuevo stock de la materia prima
                    # se modifica el stock de la materia prima en la BD
                    MateriaPrima.modificarArti("materiasprimas", "idMateriaPrima", nuevoStockMP, idMP, "stockMateriaPrima")
                # se obtiene el stockActual del producto mediante el idPro
                stockActual = Producto.obtenerAtrib((idPro, ), ("idProducto", ), "productos", "stockProducto")
                stockActual = stockActual[0][0] # la lista de tupla [(stock,)] se convierte en un valor stock
                nuevoStock = stockActual + cantidad # se calcula el nuevoStock
                # se actualiza el nuevo stock del producto en la BD
                Producto.modificarArti("productos", "idProducto", nuevoStock, idPro, "stockProducto")
                mb.showinfo("¡Felicidades!", "Producción cargada correctamente")
            else:
                mb.showerror("Error", "Materia prima insuficiente")
        else:
            mb.showerror("Error", cantidad[0])
        self.entradaCant.delete(0, tk.END)

    def on_selectP(self, event=None):
        self.scrolledtextProP.delete('1.0', tk.END)
        nombreP = self.comboPro.get() # se obtiene el nombre del producto
        descripP = Producto.obtenerArti("productos", "descripcionProducto", (nombreP, ), "Producto") #se obtiene la descripcion del producto
        descripP = descripP[0]
        self.textPro = descripP[0]
        self.labelCant.config(text=f"Cantidad ({self.textPro}):") # se inserta la descripcion en el label de cantidad
        # se obtiene el producto mediante el nombre
        producto2 = Producto.obtenerPro(nombreP)
        idPro2 = Producto.obtenerId((nombreP, )) # se obtiene el id del producto mediante el nombre
        listaMateriaPrima2 = producto2.recuperarMateriasPrimas(idPro2) # se recuperan todas las materias primas mediante el id producto
        for idMatCant in listaMateriaPrima2: #idMatCant[0] - id materia prima   idMatCant[1] - cantidad
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
        #scrolledText  de los productos
        self.scrolledtextProN = st.ScrolledText(self.labelframe4, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProN.grid(column=0, row=2, padx=5, pady=10)

        # se recorre cada producto de la lista producto
        for producto in listaProductoN:
            #producto = (nombre, descripcion, precioU, stock actual)
            self.scrolledtextProN.insert(tk.END, f"{producto[0]} ({producto[1]})\t\t  {producto[2]}\t\t{producto[3]}\n")
        self.scrolledtextProN.configure(state='disabled')
