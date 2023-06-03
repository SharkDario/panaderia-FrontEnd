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

class FormularioCompras:
    def __init__(self, ventana, usuario):
        self.usuario = usuario
        self.tema = "blue"
        self.back = 'light blue'
        self.backB = 'SteelBlue3'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana33 = ThemedTk() #tk.Tk()
        self.ventana33.configure(bg=self.back)
        self.ventana33.title("3.3 - COMPRAS")
        self.ventana33.geometry("900x750")
        self.ventana33.geometry("+10+20")

        
        
        self.labelSuperior = label(self.ventana33, text="COMPRAS", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        

        self.botonAtras = bt(self.ventana33, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana33)

        #print(self.ventana34.get_themes())
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        #SI: blue, smog, black, adapta
        #EH: kroc, plastik, winxpblue, itft1, aquativo, clam
        #NO: equilux, keramik, elegance, radiance, breeze, clearlooks, ubuntu, yaru, scidmint
        #[ 'alt', 'scidpurple', 'scidpink', 
        #'default', 'scidblue', 'classic', 'xpnative', 
        #, 'scidgrey', 'scidsand', 'scidgreen', 'arc', 'vista', 'winnative']

        self.registrarProveedor()
        self.remito()
        self.materiaPrimaSM()
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana33.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify()
        self.ventana33.destroy()

    def registrarProveedor(self):
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Registrar Proveedor")
        
        self.labelframe1 = labelF(self.pagina1, text="Registrar Proveedor", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        #self.labelFecha = label(self.labelframe1, text='Fecha de contratación:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        #self.labelFecha.grid(column=0, row=0, padx=4, pady=4)
        #self.entradaFecha = DateEntry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        #self.entradaFecha.grid(column=1, row=0, padx=4, pady=4)

        self.labelDNI = label(self.labelframe1, text="DNI:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI.grid(column=0, row=1, padx=4, pady=4)
        self.entradaDNI = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI.grid(column=1, row=1, padx=4, pady=4)

        self.labelCUIL = label(self.labelframe1, text="CUIL/CUIT:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCUIL.grid(column=0, row=2, padx=4, pady=4)
        self.entradaCUIL = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCUIL.grid(column=1, row=2, padx=4, pady=4)

        self.labelNombre = label(self.labelframe1, text="Nombre:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre.grid(column=0, row=3, padx=4, pady=4)
        self.entradaNombre = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre.grid(column=1, row=3, padx=4, pady=4)

        self.labelDomi = label(self.labelframe1, text="Domicilio:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDomi.grid(column=0, row=4, padx=4, pady=4)
        self.entradaDomi = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDomi.grid(column=1, row=4, padx=4, pady=4)

        self.labelTel = label(self.labelframe1, text="Teléfono:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTel.grid(column=0, row=5, padx=4, pady=4)
        self.entradaTel = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaTel.grid(column=1, row=5, padx=4, pady=4)

        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoProveedor)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevoProveedor(self):

        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI")
        cuil = f.ingDNI_CUIL(self.entradaCUIL.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomi.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)

        #fecha = datetime.strptime(self.entradaFecha.get(), '%m/%d/%y') #datetime.strptime("5-26-2023", '%m-%d-%Y')
        #Esto es para verificar si el DNI ya existe en las tablas de Proveedores
        idProveedor = Proveedor.obtenerId((dni,))
        
        dniCuilComparar = f.dniCuilComparar(dni, cuil)
        entrysValidos = ((nombre!="")&(domi!="")&(dniCuilComparar)&(type(tel) is not list)&(idProveedor==-1))
        if(entrysValidos):
            #nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor
            nuevoProveedor = Proveedor(nombre, cuil, dni, domi, int(tel))
            mb.showinfo("¡Felicidades!", "Proveedor registrado")
        else:
            mensaje=""
            #print(dni)
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
            if(dniCuilComparar==False):
                mensaje += "\nEl DNI y el CUIL/CUIT no coinciden."
            if(idProveedor!=-1):
                mensaje += "\nEl DNI ya existe en la base de datos."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END)
        self.entradaCUIL.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaDomi.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)

    def remito(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina2.config(width=800, height=750)
        self.cuaderno1.add(self.pagina2, text="Cargar Remito")
        
        # idRemito:                 numeroRemito fechaEmisionRemito idProveedor 
        # remito
        self.labelframe2 = labelF(self.pagina2, text="Remito", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.labelNum = label(self.labelframe2, text="Número de remito:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNum.grid(column=0, row=1, padx=4, pady=4)
        self.entradaNum = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNum.grid(column=1, row=1, padx=4, pady=4)

        self.labelFechaEmi = label(self.labelframe2, text='Fecha de emisión:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFechaEmi.grid(column=0, row=2, padx=4, pady=4)
        self.entradaFechaEmi = DateEntry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFechaEmi.grid(column=1, row=2, padx=4, pady=4)

        self.listaNom = Proveedor.recuperarNombres()
        self.listaDNI = Proveedor.recuperarDNIs()

        # Convierte las listas de tuplas en listas normales
        self.listaNom = [x[0] for x in self.listaNom]
        self.listaDNI = [x[0] for x in self.listaDNI]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        ordenado = sorted(zip(self.listaNom, self.listaDNI))

        # Desempaquetar la lista ordenada en dos listas separadas
        self.listaNom, self.listaDNI = map(list, zip(*ordenado))
        
        self.labelProve = label(self.labelframe2, text="Proveedor:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProve.grid(column=0, row=3, padx=4, pady=4)

        self.comboProv = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=self.listaNom)
        # Adding combobox drop down list
        self.comboProv.set(self.listaNom[0])
        self.comboProv.grid(column = 1, row = 3)
        self.comboProv.bind("<<ComboboxSelected>>", self.on_selectP)
        
        self.textProv = self.listaDNI[0]
        self.labelProv = label(self.labelframe2, text=f"DNI: {self.textProv}", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProv.grid(column=2, row=3, padx=4, pady=4)
        # remito
        # idDetalleRemitoProveedor: cantidad fechaEntregaProducto idRemito idMateriaPrima idTipoEstadoMateriaPrima
        # idTipoEstadoMateriaPrima: descripcionEstadoMateriaPrima
        # detalleRemito
        self.listaDetalles = []
        self.labelDetalle = label(self.labelframe2, text="Detalle", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDetalle.grid(column=0, row=4, padx=4, pady=4, sticky='w')

        listaMat = MateriaPrima.recuperarNombres()
        listaMat = [x[0] for x in listaMat]
         
        descripMP = MateriaPrima.obtenerArti("materiasprimas", "descripcionMateriaPrima", (listaMat[0], ), "MateriaPrima")
        descripMP = descripMP[0]
        self.textMat = descripMP[0]
        self.labelMat = label(self.labelframe2, text=self.textMat, font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelMat.grid(column=1, row=5, padx=4, pady=4)

        self.comboMat = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=listaMat)
        # Adding combobox drop down list
        self.comboMat.set(listaMat[0])
        self.comboMat.grid(column = 0, row = 5)
        self.comboMat.bind("<<ComboboxSelected>>", self.on_selectMP)

        self.labelCant = label(self.labelframe2, text="Cantidad:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCant.grid(column=0, row=6, padx=4, pady=4)
        self.entradaCant = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCant.grid(column=1, row=6, padx=4, pady=4)

        self.labelFechaEnt = label(self.labelframe2, text='Fecha de entrega:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFechaEnt.grid(column=0, row=7, padx=4, pady=4)
        self.entradaFechaEnt = DateEntry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFechaEnt.grid(column=1, row=7, padx=4, pady=4)
        # lista descripción
        listaD = ["integro", "defectuoso"]
        self.labelDescrip = label(self.labelframe2, text="Descripción de estado:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDescrip.grid(column=0, row=8, padx=4, pady=4)
        self.comboDescrip = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=listaD)
        # Adding combobox drop down list
        self.comboDescrip.grid(column = 1, row = 8)
        self.comboDescrip.set(listaD[0])

        self.botonAnnadirMat = bt(self.labelframe2, text="Añadir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.annadirSTMat)
        self.botonAnnadirMat.grid(column=2, row=8, padx=4, pady=4)

        self.scrolledtextMat = st.ScrolledText(self.labelframe2, font=(self.fuente, 15), width=25, height=5)
        self.scrolledtextMat.grid(column=0, row=9, padx=4, pady=4)
        # detalleRemito

        self.botonCargarR = bt(self.labelframe2, text="Cargar Remito", font=(self.fuente, 30), fg=self.fuenteB, background=self.backB, command=self.cargarRemito)
        self.botonCargarR.grid(column=1, row=9, padx=4, pady=4)

    def annadirSTMat(self):
        idMP = MateriaPrima.obtenerId((self.comboMat.get(), ))
        idTEMP = self.comboDescrip.current()+1
        fechaE = datetime.strptime(self.entradaFechaEnt.get(), '%m/%d/%y')
        cant = f.ingNumPosi(self.entradaCant.get(), "La cantidad")
        if(type(cant) is not list):
            # idDetalleRemitoProveedor: cantidad fechaEntregaProducto idRemito idMateriaPrima idTipoEstadoMateriaPrima
            datos = (cant, fechaE, idMP, idTEMP)
            # creamos una lista de tuplas con cada detalle que tendrá el remito para cuando lo creemos
            self.listaDetalles.append(datos)
            self.scrolledtextMat.insert(tk.END, f"{self.comboMat.get()} - {cant} - {self.entradaFechaEnt.get()} - {self.comboDescrip.get()}\n")
        else:
            mb.showerror("Error", cant[0])

    def cargarRemito(self):
        numRemito = f.ingNumPosi(self.entradaNum.get(), "El número de remito")
        mensajeNR="El número de remito ya existe en la base de datos."
        try:
            idRemito = Remito.obtenerId((numRemito,))
            if(idRemito==-1):
                mensajeNR=""
        except Exception:
            mensajeNR=""

        entryValido = (self.listaDetalles!=[])&(type(numRemito) is not list)&(mensajeNR=="")
        if(entryValido):
            print("")
            fechaEmision = datetime.strptime(self.entradaFechaEmi.get(), '%m/%d/%y')
            #self.textProv almacena el DNI del proveedor seleccionado
            idProv = Proveedor.obtenerId((self.textProv, ))
            remito = Remito(numRemito, fechaEmision, idProv)
            idRemito = Remito.obtenerId((numRemito, ))
            for detalle in self.listaDetalles:
                #datos = (cant, fechaE, idMP, idTEMP)
                remito.detalleRemito(detalle[0], detalle[1], idRemito, detalle[2], detalle[3])
                #Cannot add or update a child row: a foreign key constraint fails 
                #(`panaderia`.`detalleremitoproveedor`, CONSTRAINT `detalleremitoproveedor_ibfk_3` FOREIGN KEY 
                #(`idTipoEstadoMateriaPrima`) REFERENCES `tipoestadomateriaprima` (`idTipoEstadoMateriaPrima`) ON DE)
            mb.showinfo("¡Felicidades!", "Remito cargado correctamente")
            self.listaDetalles.clear()
            self.entradaNum.delete(0, tk.END)
            self.scrolledtextMat.delete("1.0", tk.END)
        else:
            mensaje=""
            if(type(numRemito) is list):
                mensaje += f"{numRemito[0]}\n"
            if(self.listaDetalles==[]):
                mensaje += f"El detalle remito no puede estar vacío."
            if(mensajeNR!=""):
                mensaje += mensajeNR
            mb.showerror("Error", mensaje)

    def on_selectMP(self, event):
        nombreMP = self.comboMat.get()
        descripMP = MateriaPrima.obtenerArti("materiasprimas", "descripcionMateriaPrima", (nombreMP, ), "MateriaPrima")
        descripMP = descripMP[0]
        self.textMat = descripMP[0]
        self.labelMat.config(text=self.textMat)

    def on_selectP(self, event):
        indice = self.comboProv.current()
        
        self.textProv = self.listaDNI[indice]
        self.labelProv.config(text=f"DNI: {self.textProv}")

    #consulta(cone, dDatos, cadenaT, tabla, atributoS)
    #select nombreMateriaPrima from materiasprimas where stockMinimoMateriaPrima<stockMateriaPrima
    
    def materiaPrimaSM(self):
        # lista de materia prima con falta en el stock, con el nombre, descripcion, el stock minimo y su stock actual
        listaMateriaSM = MateriaPrima.recuperarNombresStockMinimo()

        self.pagina3 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina3.config(width=800, height=750)
        self.cuaderno1.add(self.pagina3, text="Stock mínimo")
        
        self.labelframe3 = labelF(self.pagina3, text="Lista de materia prima con stock faltante", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.labelSM = label(self.labelframe3, text="NOMBRE\t\tSTOCK MÍNIMO\tSTOCK ACTUAL", font=(self.fuente, 15), fg=self.fuenteB, background=self.back)
        self.labelSM.grid(column=0, row=1, padx=4, pady=4)

        self.scrolledtextMatSM = st.ScrolledText(self.labelframe3, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextMatSM.grid(column=0, row=2, padx=5, pady=10)

        #print(listaMateriaSM)
        for materia in listaMateriaSM:
            #print(materia)
            #materia = (nombre, descripcion, stock minimo, stock actual)
            self.scrolledtextMatSM.insert(tk.END, f"{materia[0]} ({materia[1]})\t\t  {materia[2]}\t\t{materia[3]}\n")
        self.scrolledtextMatSM.configure(state='disabled')