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
from cliente import Cliente
from producto import Producto
from factura import Factura
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

class FormularioVentas: # Define la clase
    def __init__(self, ventana, usuario): # Define el método de inicializacion de la clase
        self.usuario = usuario # 
        self.tema = "itft1" #itft1 smog
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana33 = ThemedTk() #tk.Tk()
        self.ventana33.configure(bg=self.back)
        self.ventana33.title("3.4 - VENTAS")
        self.ventana33.geometry("900x750")
        self.ventana33.geometry("+10+20")
        self.listaPagos = ["EFECTIVO", "TARJETA DE CREDITO", "TARJETA DE DEBITO", "TRANSFERENCIA"] # Crea lista de opciones
        
        # Crea widget con título #VENTAS"
        self.labelSuperior = label(self.ventana33, text="VENTAS", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w') # Le da ubicación
        
        # Se crea un botón, se configura y se especifica el comando a ejecutar cuando se clickea
        self.botonAtras = bt(self.ventana33, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w') # Se ubica
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
        # Llama métodos
        self.registrarCliente() 
        self.clienteVerEliminar()
        self.factura()
        self.verFactura()
        self.producto()
        self.productoSM()

        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10) # Ubica el cuaderno
        self.ventana33.mainloop() # Inicia el bucle para que la pantalla se muestre y responda hasta que se cierre

   

    def volverFormularioUsuario(self): #Define método que se encarga de volver la formulario anterior, restaurandolo y destruyendo la ventana actual
        self.ventana3.deiconify()
        self.ventana33.destroy()

    def verFactura(self): # Define método
        self.pagina6 = ttk.Frame(self.cuaderno1) # Crea marco y lo asigna a la variable. Este marco es una pestaña del cuaderno
        #900x750
        self.pagina6.config(width=800, height=750) # Configuraciones
        self.cuaderno1.add(self.pagina6, text="Información de Factura:") # Agrega el marco como pestaña al cuaderno 
        #self.listaNumF = []
        # Crea un marco dentro de otro marco, que se utiliza como contenedos para organizar elementos relacionados a info de factura.
        self.labelframe6 = labelF(self.pagina6, text="Información de Factura:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe6.grid(column=0, row=0, padx=5, pady=10) # Ubicación

        # Se crea una etiqueta dentro del marco, que muestra "Tipo de factura"
        self.labelTipoF = label(self.labelframe6, text='Tipo de factura:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipoF.grid(column=0, row=1, padx=4, pady=4) # Se ubica
        # Se crea un cuadro 
        self.comboTipoF = ttk.Combobox(self.labelframe6, font=(self.fuente, 20), width = 15, values=["A", "B", "C"])
        # Adding combobox drop down list
        self.comboTipoF.set("A")
        self.comboTipoF.grid(column = 1, row = 1)
        self.comboTipoF.bind("<<ComboboxSelected>>", self.on_selectTipoF)

        self.labelNum = label(self.labelframe6, text="Número de factura:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNum.grid(column=0, row=2, padx=4, pady=4)
        self.comboNum = ttk.Combobox(self.labelframe6, font=(self.fuente, 20), width = 15)
        # Adding combobox drop down list
        #self.comboNum.set("A")
        self.comboNum.grid(column = 1, row = 2)
        self.comboNum.bind("<<ComboboxSelected>>", self.on_selectFactura)
        #self.comboNum.bind("<<ComboboxSelected>>", self.)

        self.scrolledtextFact = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=26, height=10)
        self.scrolledtextFact.grid(column=0, row=3, padx=10, pady=10)
        self.scrolledtextCli = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=24, height=10)
        self.scrolledtextCli.grid(column=1, row=3, padx=10, pady=10)
        self.scrolledtextVen = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=24, height=10)
        self.scrolledtextVen.grid(column=2, row=3, padx=10, pady=10)

        self.on_selectP2()

        self.on_selectTipoF()
        self.on_selectFactura()

    def on_selectTipoF(self, event=None):
        idTipoF = self.comboTipoF.current()+1
        self.listaNumF = Factura.recuperarNumeros(idTipoF)
        #print(self.listaNumF)
        # Convierte las listas de tuplas en listas normales
        self.listaNumF = [x[0] for x in self.listaNumF]
        # Ordena la lista de numeros
        self.listaNumF = sorted(self.listaNumF)
        #print(self.listaNumF)
        self.comboNum.config(values=self.listaNumF)
        self.comboNum.set(self.listaNumF[0])
        self.on_selectFactura()
        
    def on_selectFactura(self, event=None):
        tipoF = self.comboTipoF.current()+1
        numero = self.comboNum.get()
        self.scrolledtextFact.config(state="normal")
        self.scrolledtextCli.config(state="normal")
        self.scrolledtextVen.config(state="normal")
        #numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario
        fact1 = Factura.obtenerFactura(numero, tipoF)
        idFact1 = Factura.obtenerId((numero, tipoF))
        fact1Detalle = Factura.obtenerDetalle(idFact1)
        #print(fact1.idCliente)
        #print(fact1.idUsuario)
        cliF1DNI = Cliente.obtenerAtrib("clientes", "DNI", (int(fact1.idCliente), ), ("idCliente", ))
        #print(cliF1DNI)
        cliF1 = Cliente.obtenerCliente(cliF1DNI)
        admi=""
        try:
            userF1DNI = Administrador.obtenerAtrib("usuarios", "DNI", (int(fact1.idUsuario), ), ("idUsuario", ))
            userF1 = Administrador.obtenerAdmi(userF1DNI)
            admi=" (ADMIN)"
        except Exception:
            listaDNI = Empleado.obtenerDNIs()
            listaDNI = listaDNI[0]
            userF1DNI = Empleado.obtenerAtrib("usuarios", "DNI", (int(fact1.idUsuario), ), ("idUsuario", ))
            userF1 = Empleado.obtenerEmpleado(listaDNI, userF1DNI)
        mensajeD="DETALLE\n"
       
        for detalle in fact1Detalle:
            #idDetalleF, cantidad, precioUnitario, idFactura, idProducto
            idPro=detalle[4]
            producNom = Producto.obtenerAtrib((idPro, ), ("idProducto", ), "productos", "nombreProducto")
            producNom = producNom[0][0]
            cant = detalle[1]
            precioU = float(detalle[2])
            mensajeD+=f"{cant} - {producNom} - PU: ${precioU} - T: ${cant*precioU}\n"

        mensajeF = f"FACTURA\nNúmero: {fact1.numeroFactura}\nFecha de emisión: {fact1.fechaEmisionFactura}\nTipo de factura: {self.comboTipoF.get()}\nPrecio total: ${fact1.precioTotal}\nMedio de pago: {self.listaPagos[fact1.idMedioPago-1]}\n{mensajeD}\n"
        #self.DNI = self.nombre = nombre self.CUIL_CUIT = CUIL_CUIT self.domicilio = domicilio self.telefono
        mensajeC = f"CLIENTE\nNombre: {cliF1.nombre}\nDNI: {cliF1.DNI}\nCUIL/CUIT: {cliF1.CUIL_CUIT}\nDomicilio: {cliF1.domicilio}\nTeléfono: {cliF1.telefono}"
        mensajeV = f"VENDEDOR{admi}\nNombre: {userF1.nombre}\nDNI: {userF1.DNI}\nCUIL/CUIT: {userF1.CUIL_CUIT}\nDomicilio: {userF1.domicilio}\nTeléfono: {userF1.telefono}"
        self.scrolledtextFact.delete("1.0", tk.END)
        self.scrolledtextCli.delete("1.0", tk.END)
        self.scrolledtextVen.delete("1.0", tk.END)
        self.scrolledtextFact.insert(tk.END, mensajeF)
        self.scrolledtextCli.insert(tk.END, mensajeC)
        self.scrolledtextVen.insert(tk.END, mensajeV)
        self.scrolledtextFact.config(state="disabled")
        self.scrolledtextCli.config(state="disabled")
        self.scrolledtextVen.config(state="disabled")

    def registrarCliente(self):
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Registrar Cliente")
        
        self.labelframe1 = labelF(self.pagina1, text="Registrar Cliente", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
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

        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoCliente)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevoCliente(self):

        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI")
        cuil = f.ingDNI_CUIL(self.entradaCUIL.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomi.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)

        #fecha = datetime.strptime(self.entradaFecha.get(), '%m/%d/%y') #datetime.strptime("5-26-2023", '%m-%d-%Y')
        #Esto es para verificar si el DNI ya existe en las tablas de Clientes
        idCliente = Cliente.obtenerId((dni,))
        
        dniCuilComparar = f.dniCuilComparar(dni, cuil)
        entrysValidos = ((nombre!="")&(domi!="")&(dniCuilComparar)&(type(tel) is not list)&(idCliente==-1))
        if(entrysValidos):
            #nombreCliente, CUIL_CUIT,	DNI, telefonoCliente, domicilioCliente,
            nuevoCliente = Cliente(nombre, cuil, dni, int(tel), domi)
            mb.showinfo("¡Felicidades!", "Cliente registrado")
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
            if(idCliente!=-1):
                mensaje += "\nEl DNI ya existe en la base de datos."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END)
        self.entradaCUIL.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaDomi.delete(0, tk.END)
        
    
    def factura(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina2.config(width=800, height=750)
        self.cuaderno1.add(self.pagina2, text="Cargar Factura")
        
        # idRemito:                 numeroRemito fechaEmisionRemito idProveedor 
        # remito
        self.labelframe2 = labelF(self.pagina2, text="Factura", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.labelNum = label(self.labelframe2, text="Número de factura:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNum.grid(column=0, row=1, padx=4, pady=4)
        self.entradaNum = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNum.grid(column=1, row=1, padx=4, pady=4)

        self.labelFechaEmi = label(self.labelframe2, text='Fecha de emisión:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFechaEmi.grid(column=0, row=2, padx=4, pady=4)
        self.entradaFechaEmi = DateEntry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFechaEmi.grid(column=1, row=2, padx=4, pady=4)

        self.labelTipoF = label(self.labelframe2, text='Tipo de factura:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipoF.grid(column=0, row=3, padx=4, pady=4)
        self.comboTipoF = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=["A", "B", "C"])
        # Adding combobox drop down list
        self.comboTipoF.set("A")
        self.comboTipoF.grid(column = 1, row = 3)

        self.labelTipoMP = label(self.labelframe2, text='Medio de pago:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipoMP.grid(column=0, row=4, padx=4, pady=4)
        self.comboTipoMP = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=self.listaPagos)
        # Adding combobox drop down list
        self.comboTipoMP.set("EFECTIVO")
        self.comboTipoMP.grid(column = 1, row = 4)

        self.listaNom = Cliente.recuperarNombres()
        self.listaDNI = Cliente.recuperarDNIs()

        # Convierte las listas de tuplas en listas normales
        self.listaNom = [x[0] for x in self.listaNom]
        self.listaDNI = [x[0] for x in self.listaDNI]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        ordenado = sorted(zip(self.listaNom, self.listaDNI))

        # Desempaquetar la lista ordenada en dos listas separadas
        self.listaNom, self.listaDNI = map(list, zip(*ordenado))
        
        self.labelCli = label(self.labelframe2, text="Cliente:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCli.grid(column=0, row=5, padx=4, pady=4)

        self.comboCli = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=self.listaNom)
        # Adding combobox drop down list
        self.comboCli.set(self.listaNom[0])
        self.comboCli.grid(column = 1, row = 5)
        self.comboCli.bind("<<ComboboxSelected>>", self.on_selectC)
        
        self.textCli = self.listaDNI[0]
        self.labelCliDni = label(self.labelframe2, text=f"DNI: {self.textCli}", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCliDni.grid(column=2, row=5, padx=4, pady=4)
        # remito
        # idDetalleRemitoProveedor: cantidad fechaEntregaProducto idRemito idMateriaPrima idTipoEstadoMateriaPrima
        # idTipoEstadoMateriaPrima: descripcionEstadoMateriaPrima
        # detalleRemito
        
        self.listaDetalles = []
        self.labelDetalle = label(self.labelframe2, text="Detalle", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDetalle.grid(column=0, row=6, padx=4, pady=4, sticky='w')

        #idDetalleFactura	cantidad	precioUnitario	idFactura	idProducto

        listaPro = Producto.recuperarNombres()
        listaPro = [x[0] for x in listaPro]
        
        listaPro = sorted(listaPro)
         
        descripPro = Producto.obtenerArti("productos", "descripcionProducto", (listaPro[0], ), "Producto")
        descripPro = descripPro[0]
        self.textP = descripPro[0]
        precioUPro = Producto.obtenerArti("productos", "precioUnitarioProducto", (listaPro[0], ), "Producto")
        self.textLabelPu = precioUPro[0][0]
        self.labelP = label(self.labelframe2, text=self.textP, font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelP.grid(column=1, row=7, padx=4, pady=4)

        self.comboProduc = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=listaPro)
        # Adding combobox drop down list
        self.comboProduc.set(listaPro[0])
        self.comboProduc.grid(column = 0, row = 7)
        self.comboProduc.bind("<<ComboboxSelected>>", self.on_selectP)

        self.labelPU1 = label(self.labelframe2, text=f"Precio unitario:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPU1.grid(column=0, row=8, padx=4, pady=4)
        self.labelPU = label(self.labelframe2, text=f"{self.textLabelPu}", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelPU.grid(column=1, row=8, padx=4, pady=4)
        #self.entradaPU = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        #self.entradaPU.grid(column=1, row=8, padx=4, pady=4)

        self.labelCant = label(self.labelframe2, text="Cantidad:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCant.grid(column=0, row=9, padx=4, pady=4)
        self.entradaCant = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCant.grid(column=1, row=9, padx=4, pady=4)

        self.botonAnnadirPro = bt(self.labelframe2, text="Añadir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.annadirPro)
        self.botonAnnadirPro.grid(column=2, row=9, padx=4, pady=4)

        self.scrolledtextPro = st.ScrolledText(self.labelframe2, font=(self.fuente, 15), width=30, height=5)
        self.scrolledtextPro.grid(column=0, row=10, padx=4, pady=4)
        # detalleFactura

        self.botonCargarF = bt(self.labelframe2, text="Cargar Factura", font=(self.fuente, 30), fg=self.fuenteB, background=self.backB, command=self.cargarFactura)
        self.botonCargarF.grid(column=1, row=10, padx=4, pady=4)
        
    def on_selectP(self, event):
        nombreP = self.comboProduc.get()
        descripPro = Producto.obtenerArti("productos", "descripcionProducto", (nombreP, ), "Producto")
        descripPro = descripPro[0]
        self.textP = descripPro[0]
        precioUPro = Producto.obtenerArti("productos", "precioUnitarioProducto", (nombreP, ), "Producto")
        self.textLabelPu = precioUPro[0][0]

        self.labelP.config(text=self.textP)
        self.labelPU.config(text=f"{self.textLabelPu}")

    
    def annadirPro(self):
        #idMP = MateriaPrima.obtenerId((self.comboMat.get(), ))
        idP = Producto.obtenerId((self.comboProduc.get(), ))
        descrip = self.textP
        precioU = self.textLabelPu
        cant = f.ingNumPosi(self.entradaCant.get(), "La cantidad")
        stockP = Producto.obtenerAtrib((idP, ), ("idProducto", ), "productos", "stockProducto")
        stockP = stockP[0][0]
        if(type(cant) is not list):
            if(cant<=stockP):
                # 	idDetalleFactura:	cantidad	precioUnitario	idFactura	idProducto	
                precioU = float(precioU)
                datos = (cant, precioU, idP)
                # creamos una lista de tuplas con cada detalle que tendrá el remito para cuando lo creemos
                self.listaDetalles.append(datos)
                self.scrolledtextPro.insert(tk.END, f"{self.comboProduc.get()} {descrip} - PU: ${precioU} - {cant}\n")
            else:
                mb.showerror("Error", "La cantidad de productos en stock es menor a la solicitada.")
        else:
            mb.showerror("Error", cant[0])
    
# PRECIO TOTAL 
    def cargarFactura(self):
        numFactura = f.ingNumPosi(self.entradaNum.get(), "El número de factura")
        mensajeNR="El número de factura junto al tipo de factura ya existe en la base de datos."
        idTipoF = self.comboTipoF.current()+1
        
        idFactura = Factura.obtenerId((numFactura, idTipoF))
        if(idFactura==-1):
            mensajeNR=""

        entryValido = (self.listaDetalles!=[])&(type(numFactura) is not list)&(mensajeNR=="")
        if(entryValido):
            fechaEmision = datetime.strptime(self.entradaFechaEmi.get(), '%m/%d/%y') # se convierte la fecha de str a datetime
            medioP = self.comboTipoMP.current()+1 # se obtiene el id de medio de pago (1-2-3-4)
            if(type(self.usuario) is Administrador): # si el objeto self.usuario es administrador se llama a la clase Administrador
                idUser = Administrador.obtenerId((self.usuario.DNI, )) # para obtener el id del administrador
            else: # sino se llama a la clase Empleado para obtener el id del empleado
                idUser = Empleado.obtenerId((self.usuario.DNI, ))
            idCli = Cliente.obtenerId((self.textCli, )) # se obtiene el id del cliente
            #numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario
            # se crea un objeto Factura que se guarda en la tabla factura en la base de datos
            # el precio total es 0, hasta que se actualice por calcular segun los detalles
            factura = Factura(numFactura, fechaEmision, idTipoF, 0, medioP, idCli, idUser)
            # se obtiene el id de la factura dada de alta
            idFactura = Factura.obtenerId((numFactura, idTipoF))
            # se inicia el acumulador
            precioTotal=0
            for detalle in self.listaDetalles: # por cada detalle en la lista de detalles
                #datos = (cant, precioU, idP) en detalle
                #cantidad, precioUnitario, idFactura, idProducto) en detalleFactura
                cant = detalle[0]
                precioU = detalle[1]
                idP = detalle[2]
                # se da de alta un detalle en la tabla detallefactura en la BD con el ID de la factura en cuestion
                factura.detalleFactura(cant, precioU, idFactura, idP)
                precioTotal += cant*precioU
                # actualización del stock de productos
                stockActual = Producto.obtenerAtrib((idP, ), ("idProducto", ), "productos", "stockProducto") # se obtienne el stock actual
                stockActual = stockActual[0][0] # la lista de una tupla de un valor, se convierte en una variable float que guarda ese valor
                nuevoStock = stockActual - cant # se resta del stock actual la cantidad del detalle
                Producto.modificarArti("productos", "idProducto", nuevoStock, idP, "stockProducto") # se actualiza el stock del producto
            # se actualiza el precio total de la factura
            factura.actualizarTotal(precioTotal, idFactura)
            mb.showinfo("¡Felicidades!", f"Factura cargada correctamente (PRECIO TOTAL: ${precioTotal})")
            self.listaDetalles.clear() # se limpia la listaDetalles
            self.entradaNum.delete(0, tk.END) # se elimina lo ingresado en la entradaNum
            self.scrolledtextPro.delete("1.0", tk.END) # se limpia el scrolledtext de los detalles
        else:
            mensaje=""
            if(type(numFactura) is list):
                mensaje += f"{numFactura[0]}\n"
            if(self.listaDetalles==[]):
                mensaje += f"El detalle factura no puede estar vacío."
            if(mensajeNR!=""):
                mensaje += mensajeNR
            mb.showerror("Error", mensaje)

    """
    def on_selectMP(self, event):
        nombreMP = self.comboMat.get()
        #descripMP = MateriaPrima.obtenerArti("materiasprimas", "descripcionMateriaPrima", (nombreMP, ), "MateriaPrima")
        descripMP = descripMP[0]
        self.textMat = descripMP[0]
        self.labelMat.config(text=self.textMat)

    def on_selectP(self, event):
        indice = self.comboProv.current()
        
        self.textProv = self.listaDNI[indice]
        self.labelProv.config(text=f"DNI: {self.textProv}")
    """
    
    def on_selectC(self, event):
        indice = self.comboCli.current()
        
        self.textCli = self.listaDNI[indice]
        self.labelCliDni.config(text=f"DNI: {self.textCli}")

    #consulta(cone, dDatos, cadenaT, tabla, atributoS)
    #select nombreMateriaPrima from materiasprimas where stockMinimoMateriaPrima<stockMateriaPrima
        
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
        # se ordenan los productos alfabeticamente
        listaProductoN.sort(key=lambda x: x[0])
        self.pagina4 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina4.config(width=800, height=750)
        self.cuaderno1.add(self.pagina4, text="Productos") #titulo del cuaderno
        #titulo del frame
        self.labelframe4 = labelF(self.pagina4, text="Lista de productos", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        # NOMBRE - PRECIO UNITARIO - STOCK ACTUAL
        self.labelSM = label(self.labelframe4, text="NOMBRE\t\tPRECIO UNITARIO\tSTOCK ACTUAL", font=(self.fuente, 15), fg=self.fuenteB, background=self.back)
        self.labelSM.grid(column=0, row=1, padx=4, pady=4)
        #scrolledtext donde se insertaran los datos de todos los productos de la tabla producto
        self.scrolledtextProN = st.ScrolledText(self.labelframe4, font=(self.fuente, 15), width=40, height=15)
        self.scrolledtextProN.grid(column=0, row=2, padx=5, pady=10)
        # se recorre cada producto de la lista de productos
        for producto in listaProductoN:
            #producto = (nombre, descripcion, precioU, stock actual)
            # Se inserta en el scrolledtext cada dato del producto y se realiza un salto de linea para el siguiente
            self.scrolledtextProN.insert(tk.END, f"{producto[0]} ({producto[1]})\t\t  {producto[2]}\t\t{producto[3]}\n")
        self.scrolledtextProN.configure(state='disabled')

    def clienteVerEliminar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.pagina5.config(width=800, height=750)
        self.cuaderno1.add(self.pagina5, text="Ver Cliente")

        self.labelframe5 = labelF(self.pagina5, text="Información de Cliente", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.listaNom2 = Cliente.recuperarNombres()
        self.listaDNI2 = Cliente.recuperarDNIs()

        # Convierte las listas de tuplas en listas normales
        self.listaNom2 = [x[0] for x in self.listaNom2]
        self.listaDNI2 = [x[0] for x in self.listaDNI2]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        ordenado = sorted(zip(self.listaNom2, self.listaDNI2))

        # Desempaquetar la lista ordenada en dos listas separadas
        self.listaNom2, self.listaDNI2 = map(list, zip(*ordenado))
        
        self.labelProve2 = label(self.labelframe5, text="Cliente:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProve2.grid(column=0, row=1, padx=4, pady=4)

        self.comboProv2 = ttk.Combobox(self.labelframe5, font=(self.fuente, 20), width = 15, values=self.listaNom2)
        # Adding combobox drop down list
        self.comboProv2.set(self.listaNom2[0])
        self.comboProv2.grid(column = 1, row = 1)
        self.comboProv2.bind("<<ComboboxSelected>>", self.on_selectP2)
        
        self.textProv2 = self.listaDNI2[0]
        self.labelProv2 = label(self.labelframe5, text=f"DNI: {self.textProv2}", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelProv2.grid(column=2, row=1, padx=4, pady=4)

        self.scrolledtext2 = st.ScrolledText(self.labelframe5, font=(self.fuente, 20), width=20, height=10)
        self.scrolledtext2.grid(column=0, row=2, padx=10, pady=10)
        self.on_selectP2()

        self.botonEliminar = bt(self.labelframe5, text="Dar de baja", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.bajaCliente)
        self.botonEliminar.grid(column=1, row=2, padx=4, pady=4)

    def bajaCliente(self):
        indice = self.comboProv2.current()
        dniEli = self.listaDNI2[indice]
        self.listaNom2.pop(indice)
        self.listaDNI2.remove(dniEli) 
        self.comboProv2.config(values=self.listaNom2)
        idProv = Cliente.obtenerId((dniEli, ))
        Cliente.bajaCliente(idProv)
        mb.showinfo("¡Felicidades!", "Cliente dado de baja")
        
    def on_selectP2(self, event=None):
        indice = self.comboProv2.current()
        self.scrolledtext2.config(state="normal")
        self.textProv2 = self.listaDNI2[indice]
        self.labelProv2.config(text=f"DNI: {self.textProv2}")
        cli1 = Cliente.obtenerCliente(int(self.textProv2))
        mensaje = f"DNI: {cli1.DNI}\nCUIL/CUIT: {cli1.CUIL_CUIT}\nNombre: {cli1.nombre}\nDomicilio: {cli1.domicilio}\nTeléfono: {cli1.telefono}\n"
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert(tk.END, mensaje)
        self.scrolledtext2.config(state="disabled")
