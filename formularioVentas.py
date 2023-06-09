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
        # Agrega una lista desplegable de ComboBox
        #self.comboNum.set("A")
        self.comboNum.grid(column = 1, row = 2)
        self.comboNum.bind("<<ComboboxSelected>>", self.on_selectFactura) #se utiliza para enlazar un evento de selección de ComboBox a una función específica llamada on_selectFactura.
        #self.comboNum.bind("<<ComboboxSelected>>", self.)

        self.scrolledtextFact = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=26, height=10)
        self.scrolledtextFact.grid(column=0, row=3, padx=10, pady=10)
        self.scrolledtextCli = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=24, height=10)
        self.scrolledtextCli.grid(column=1, row=3, padx=10, pady=10)
        self.scrolledtextVen = st.ScrolledText(self.labelframe6, font=(self.fuente, 15), width=24, height=10)
        self.scrolledtextVen.grid(column=2, row=3, padx=10, pady=10)

        self.on_selectP2()  # Llamar a la función on_selectP2()

        self.on_selectTipoF() # Llamar a la función on_selectTipoF()
        self.on_selectFactura() # Llamar a la función on_selectFactura()

    def on_selectTipoF(self, event=None):  # Definición de la función on_selectTipoF con un parámetro event opcional
        idTipoF = self.comboTipoF.current()+1 # Obtiene el índice del elemento seleccionado en comboTipoF y le suma 1 para obtener el idTipoF correspondiente
        self.listaNumF = Factura.recuperarNumeros(idTipoF) # Recupera una lista de números asociados al idTipoF utilizando el método recuperarNumeros de la clase Factura
        #print(self.listaNumF)  
        # Convierte las listas de tuplas en listas normales
        self.listaNumF = [x[0] for x in self.listaNumF]
        # Ordena la lista de numeros
        self.listaNumF = sorted(self.listaNumF) 
        #print(self.listaNumF)
        self.comboNum.config(values=self.listaNumF) # Configura los valores del ComboBox comboNum con la lista de números
        self.comboNum.set(self.listaNumF[0]) # Establece el valor seleccionado en comboNum como el primer número de la lista
        self.on_selectFactura() # Llama a la función on_selectFactura
        
    def on_selectFactura(self, event=None):  # Definición de la función on_selectFactura con un parámetro event opcional
        tipoF = self.comboTipoF.current()+1  # Obtiene el índice del elemento seleccionado en comboTipoF y le suma 1 para obtener el tipoF correspondiente
        numero = self.comboNum.get()   # Obtiene el valor seleccionado en comboNum y lo asigna a la variable numero
        self.scrolledtextFact.config(state="normal") # Configura el estado del widget scrolledtextFact como "normal" para permitir la edición
        self.scrolledtextCli.config(state="normal") # Configura el estado del widget scrolledtextCli como "normal" para permitir la edición
        self.scrolledtextVen.config(state="normal") # Configura el estado del widget scrolledtextVen como "normal" para permitir la edición
        #numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario
        fact1 = Factura.obtenerFactura(numero, tipoF)  # Obtiene la factura correspondiente al número y tipo de factura especificados
        idFact1 = Factura.obtenerId((numero, tipoF)) # Obtiene el ID de la factura a partir del número y tipo de factura
        fact1Detalle = Factura.obtenerDetalle(idFact1) # Obtiene el ID de la factura a partir del número y tipo de factura
        #print(fact1.idCliente)
        #print(fact1.idUsuario)
        cliF1DNI = Cliente.obtenerAtrib("clientes", "DNI", (int(fact1.idCliente), ), ("idCliente", ))  # Obtiene el DNI del cliente mediante el metodo obtenerAtrib utilizando su ID
    #print(cliF1DNI)  # Imprime el DNI del cliente (comentado)
        #print(cliF1DNI)
        cliF1 = Cliente.obtenerCliente(cliF1DNI) # Obtiene los datos del cliente a partir de su DNI
        admi="" # Variable para almacenar el indicador de administrador
        try:
            userF1DNI = Administrador.obtenerAtrib("usuarios", "DNI", (int(fact1.idUsuario), ), ("idUsuario", )) # Obtiene el DNI del usuario administrador utilizando su ID
            userF1 = Administrador.obtenerAdmi(userF1DNI) # Obtiene los datos del administrador a partir de su DNI
            admi=" (ADMIN)" # Agrega el indicador de administrador a la variable admi
        except Exception:
            listaDNI = Empleado.obtenerDNIs() # Obtiene una lista de DNIs de los empleados
            listaDNI = listaDNI[0]   # Selecciona el primer elemento de la lista de DNIs
            userF1DNI = Empleado.obtenerAtrib("usuarios", "DNI", (int(fact1.idUsuario), ), ("idUsuario", ))  # Obtiene el DNI del empleado utilizando su ID de usuario con el metodo de obtenerAtrib
            userF1 = Empleado.obtenerEmpleado(listaDNI, userF1DNI)  # Obtiene los datos del empleado pasando como paramentros la lista de DNI's y el DNI del usuario
        mensajeD="DETALLE\n"
       
        for detalle in fact1Detalle:  # Itera sobre los elementos de fact1Detalle
            #idDetalleF, cantidad, precioUnitario, idFactura, idProducto  
            idPro=detalle[4]  # Obtiene el ID del producto del detalle actual
            producNom = Producto.obtenerAtrib((idPro, ), ("idProducto", ), "productos", "nombreProducto") # Obtiene el nombre del producto utilizando su ID
            producNom = producNom[0][0]  # Obtiene el nombre del producto del resultado obtenido
            cant = detalle[1] # Obtiene la cantidad del detalle actual
            precioU = float(detalle[2]) # Obtiene el precio unitario del detalle actual y lo convierte a un valor flotante
            mensajeD+=f"{cant} - {producNom} - PU: ${precioU} - T: ${cant*precioU}\n"  # Agrega una línea de detalle al mensajeD concatenando la cantidad, el nombre del producto, el precio unitario y el total
        mensajeF = f"FACTURA\nNúmero: {fact1.numeroFactura}\nFecha de emisión: {fact1.fechaEmisionFactura}\nTipo de factura: {self.comboTipoF.get()}\nPrecio total: ${fact1.precioTotal}\nMedio de pago: {self.listaPagos[fact1.idMedioPago-1]}\n{mensajeD}\n"  # Crea el mensaje de la factura con los valores obtenidos y el mensajeD generado anteriormente
        #self.DNI = self.nombre = nombre self.CUIL_CUIT = CUIL_CUIT self.domicilio = domicilio self.telefono
        mensajeC = f"CLIENTE\nNombre: {cliF1.nombre}\nDNI: {cliF1.DNI}\nCUIL/CUIT: {cliF1.CUIL_CUIT}\nDomicilio: {cliF1.domicilio}\nTeléfono: {cliF1.telefono}" # Crea el mensaje para el cliente con los valores obtenidos de cliF1
        mensajeV = f"VENDEDOR{admi}\nNombre: {userF1.nombre}\nDNI: {userF1.DNI}\nCUIL/CUIT: {userF1.CUIL_CUIT}\nDomicilio: {userF1.domicilio}\nTeléfono: {userF1.telefono}" # Crea el mensaje del vendedor (o administrador) con los valores obtenidos de userF1 y admi
        self.scrolledtextFact.delete("1.0", tk.END)  # Borra el contenido existente en scrolledtextFact desde el inicio hasta el final
        self.scrolledtextCli.delete("1.0", tk.END)  # Borra el contenido existente en scrolledtextCli desde el inicio hasta el final
        self.scrolledtextVen.delete("1.0", tk.END)  # Borra el contenido existente en scrolledtextVen desde el inicio hasta el final
        self.scrolledtextFact.insert(tk.END, mensajeF)  # Inserta el mensajeF en scrolledtextFact al final del texto
        self.scrolledtextCli.insert(tk.END, mensajeC)  # Inserta el mensajeC en scrolledtextCli al final del texto
        self.scrolledtextVen.insert(tk.END, mensajeV)  # Inserta el mensajeV en scrolledtextVen al final del texto
        self.scrolledtextFact.config(state="disabled")  # Configura el estado de scrolledtextFact como "disabled" para evitar la edición
        self.scrolledtextCli.config(state="disabled")  # Configura el estado de scrolledtextCli como "disabled" para evitar la edición
        self.scrolledtextVen.config(state="disabled")  # Configura el estado de scrolledtextVen como "disabled" para evitar la edición


    def registrarCliente(self):  #define un método llamado registrarCliente que pertenece a una clase 
        #el parámetro self es necesario para que el método pueda acceder a los atributos y métodos de esa instancia específica.
        self.pagina1 = ttk.Frame(self.cuaderno1)  # Crea un marco (frame) dentro del cuaderno1
        #900x750
        self.pagina1.config(width=800, height=750) # Configura el ancho y alto de la página1
        self.cuaderno1.add(self.pagina1, text="Registrar Cliente") # Agrega la página1 al cuaderno1 con el texto "Registrar Cliente"
        
        self.labelframe1 = labelF(self.pagina1, text="Registrar Cliente", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)  # Crea un marco de etiqueta (label frame) en la página1 con el texto "Registrar Cliente" y otras configuraciones
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10) # Ubica el labelframe en la columna 0 y fila 0 de la página1 con un espacio de padding

        #self.labelFecha = label(self.labelframe1, text='Fecha de contratación:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        #self.labelFecha.grid(column=0, row=0, padx=4, pady=4)
        #self.entradaFecha = DateEntry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        #self.entradaFecha.grid(column=1, row=0, padx=4, pady=4)
           
        # Crea etiquetas y entradas para DNI, CUIL/CUIT, Nombre, Domicilio y Teléfono
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

        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoCliente) # Crea un botón de confirmación con el texto "Registrar" y una función de comando altaNuevoCliente
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4) # Ubica el botón de confirmación 
    

    def altaNuevoCliente(self): #metodo que registra un nuevo cliente en la base de datos después de validar los datos ingresados por el usuario.
         # Obtiene los valores ingresados por el usuario en los campos correspondientes
        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI")
        cuil = f.ingDNI_CUIL(self.entradaCUIL.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomi.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)

        #fecha = datetime.strptime(self.entradaFecha.get(), '%m/%d/%y') #datetime.strptime("5-26-2023", '%m-%d-%Y')
        #Esto es para verificar si el DNI ya existe en las tablas de Clientes
        idCliente = Cliente.obtenerId((dni,))
        
        dniCuilComparar = f.dniCuilComparar(dni, cuil)  #Verifica que el DNI y el CUIL/CUIT coincidan
        entrysValidos = ((nombre!="")&(domi!="")&(dniCuilComparar)&(type(tel) is not list)&(idCliente==-1)) # Verifica la validez de los valores ingresados
        if(entrysValidos):
            #nombreCliente, CUIL_CUIT,	DNI, telefonoCliente, domicilioCliente,
             # Crea una nueva instancia de la clase Cliente con los valores ingresados
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
            mb.showerror("Error", mensaje) # Muestra un mensaje de error con los detalles
        # Limpia los campos de entrada de datos
        self.entradaDNI.delete(0, tk.END)
        self.entradaCUIL.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaDomi.delete(0, tk.END)
        
    
    def factura(self):
        self.pagina2 = ttk.Frame(self.cuaderno1) # Crea un nuevo marco en el cuaderno
        #900x750
        self.pagina2.config(width=800, height=750) # Configura el ancho y alto del marco
        self.cuaderno1.add(self.pagina2, text="Cargar Factura") # Agrega el marco al cuaderno con el texto "Cargar Factura"
        
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
        self.comboTipoF = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=["A", "B", "C"]) #Crea un cuadro combinado (Combobox) en el labelframe2 con valores predeterminados en el cuadro combinado son "A", "B" y "C"
        # Agrega una lista desplegable de ComboBox
        self.comboTipoF.set("A") # Establece el valor predeterminado del cuadro combinado en "A".
        self.comboTipoF.grid(column = 1, row = 3)

        self.labelTipoMP = label(self.labelframe2, text='Medio de pago:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back) #Crea una etiqueta con el texto "Medio de pago:" y otros atributos, y lo asigna a la variable self.labelTipoMP.
        self.labelTipoMP.grid(column=0, row=4, padx=4, pady=4)
        self.comboTipoMP = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=self.listaPagos) #Crea un cuadro combinado (Combobox) para que el usuario pueda seleccionar el medio de pago, utilizando los valores proporcionados en la lista self.listaPagos. Lo asigna a la variable self.comboTipoMP.
        #  Agrega una lista desplegable de ComboBox
        self.comboTipoMP.set("EFECTIVO")    #Establece el valor predeterminado del cuadro combinado en "EFECTIVO".
        self.comboTipoMP.grid(column = 1, row = 4) #Coloca el cuadro combinado en la cuadrícula de la interfaz gráfica en la columna 1 y fila 4.

        self.listaNom = Cliente.recuperarNombres()  #Llama al método recuperarNombres() de la clase Cliente para obtener una lista de nombres de clientes
        self.listaDNI = Cliente.recuperarDNIs() #Llama al método recuperarDNIs() de la clase Cliente para obtener una lista de DNIs de clientes

        # Convierte las listas de tuplas en listas normales
        self.listaNom = [x[0] for x in self.listaNom]
        self.listaDNI = [x[0] for x in self.listaDNI]

        # Empaquetar las dos listas utilizando zip y ordenarlas por el primer elemento de cada par (listaNom)
        ordenado = sorted(zip(self.listaNom, self.listaDNI))

        # Desempaquetar la lista ordenada en dos listas separadas
        self.listaNom, self.listaDNI = map(list, zip(*ordenado))
        
        self.labelCli = label(self.labelframe2, text="Cliente:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCli.grid(column=0, row=5, padx=4, pady=4)

        self.comboCli = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=self.listaNom)  #Crea un objeto ttk.Combobox en el marco self.labelframe2 con la fuente y el ancho especificados. El contenido del cuadro combinado se establece con los valores de la lista self.listaNom.
        # Agrega una lista desplegable de ComboBox
        self.comboCli.set(self.listaNom[0]) #Establece el valor predeterminado del cuadro combinado self.comboCli con el primer elemento de la lista self.listaNom.
        self.comboCli.grid(column = 1, row = 5)
        self.comboCli.bind("<<ComboboxSelected>>", self.on_selectC) 
        #Asocia el evento ComboboxSelected del cuadro combinado self.comboCli al método self.on_selectC.
        #Esto significa que cuando se seleccione un elemento del cuadro combinado, se llamará al método self.on_selectC.
        
        self.textCli = self.listaDNI[0] # Asigna el primer elemento de la lista self.listaDNI a la variable self.textCli.
        self.labelCliDni = label(self.labelframe2, text=f"DNI: {self.textCli}", font=(self.fuente, 20), fg=self.fuenteB, background=self.back) #Crea un widget de etiqueta (Label) en el marco self.labelframe2 con el texto "DNI: {self.textCli}"
        self.labelCliDni.grid(column=2, row=5, padx=4, pady=4) 
        # remito
        # idDetalleRemitoProveedor: cantidad fechaEntregaProducto idRemito idMateriaPrima idTipoEstadoMateriaPrima
        # idTipoEstadoMateriaPrima: descripcionEstadoMateriaPrima
        # detalleRemito
        
        self.listaDetalles = [] # Inicializa una lista vacía llamada self.listaDetalles.
        self.labelDetalle = label(self.labelframe2, text="Detalle", font=(self.fuente, 20), fg=self.fuenteB, background=self.back) # Crea un widget de etiqueta (Label) en el marco self.labelframe2 con el texto "Detalle"
        self.labelDetalle.grid(column=0, row=6, padx=4, pady=4, sticky='w')

        #idDetalleFactura	cantidad	precioUnitario	idFactura	idProducto

        listaPro = Producto.recuperarNombres() #Se llama a la función recuperarNombres() de la clase Producto para obtener una lista de nombres de productos. 
        listaPro = [x[0] for x in listaPro] #ue contiene solo los primeros elementos de cada tupla en listaPro, lo que es equivalente a extraer solo los nombres de los productos.
        
        listaPro = sorted(listaPro) # Ordena la lista listaPro en orden alfabético.
         
        descripPro = Producto.obtenerArti("productos", "descripcionProducto", (listaPro[0], ), "Producto") #Llama a la función obtenerArti() de la clase Producto para obtener la descripción del primer producto de la lista listaPro
        descripPro = descripPro[0] # resultado se asigna a descripPro
        self.textP = descripPro[0] # asigna el primer elemento de descripPro a self.textP
        precioUPro = Producto.obtenerArti("productos", "precioUnitarioProducto", (listaPro[0], ), "Producto") # Llama a la función obtenerArti() nuevamente para obtener el precio unitario del primer producto de la lista listaPro y guarda en la variable
        self.textLabelPu = precioUPro[0][0] #asigna el primer elemento de precioUPro[0] a self.textLabelPu.
        self.labelP = label(self.labelframe2, text=self.textP, font=(self.fuente, 20), fg=self.fuenteB, background=self.back) #Crea un widget de etiqueta (Label) en el marco self.labelframe2 con el texto almacenado en self.textP
        self.labelP.grid(column=1, row=7, padx=4, pady=4)

        self.comboProduc = ttk.Combobox(self.labelframe2, font=(self.fuente, 20), width = 15, values=listaPro)
        # Agrega una lista desplegable de ComboBox
        self.comboProduc.set(listaPro[0])
        self.comboProduc.grid(column = 0, row = 7)
        self.comboProduc.bind("<<ComboboxSelected>>", self.on_selectP) # selecciona un elemento en el combobox, se activa el evento "ComboboxSelected" y se llama a la función on_selectP

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

        self.botonAnnadirPro = bt(self.labelframe2, text="Añadir", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.annadirPro) #crean un botón con el texto "Añadir" y lo asignan a la variable botonAnnadirPro
        #cuando el botón se presione, se ejecutará la función annadirPro.
        self.botonAnnadirPro.grid(column=2, row=9, padx=4, pady=4)

        self.scrolledtextPro = st.ScrolledText(self.labelframe2, font=(self.fuente, 15), width=30, height=5)
        self.scrolledtextPro.grid(column=0, row=10, padx=4, pady=4)
        # detalleFactura

        self.botonCargarF = bt(self.labelframe2, text="Cargar Factura", font=(self.fuente, 30), fg=self.fuenteB, background=self.backB, command=self.cargarFactura)
        #crea un botón con el texto "Cargar Factura" y lo asigna a la variable botonCargarF cuando el botón se presione, se ejecutará la función
        self.botonCargarF.grid(column=1, row=10, padx=4, pady=4)
        
    #se ejecuta cuando se selecciona un elemento del ComboBox de productos, el event representa el evento que se desancadeno al presionar el boton
    def on_selectP(self, event):
        nombreP = self.comboProduc.get()  # Obtiene el nombre seleccionado del ComboBox de productos
        descripPro = Producto.obtenerArti("productos", "descripcionProducto", (nombreP, ), "Producto")
        descripPro = descripPro[0]  # Obtiene la descripción del producto seleccionado
        self.textP = descripPro[0]  # Almacena la descripción en la variable de instancia 'textP'
        precioUPro = Producto.obtenerArti("productos", "precioUnitarioProducto", (nombreP, ), "Producto")
        self.textLabelPu = precioUPro[0][0]  # Almacena el precio unitario en la variable de instancia 'textLabelPu'

        self.labelP.config(text=self.textP)  # Actualiza el texto del label 'labelP' con la descripción del producto
        self.labelPU.config(text=f"{self.textLabelPu}")  # Actualiza el texto del label 'labelPU' con el precio unitario del producto

    def annadirPro(self):
        # Obtener el ID del producto seleccionado
        idP = Producto.obtenerId((self.comboProduc.get(), ))
        # Obtener la descripción del producto
        descrip = self.textP
        # Obtener el precio unitario del producto
        precioU = self.textLabelPu
        # Obtener la cantidad ingresada
        cant = f.ingNumPosi(self.entradaCant.get(), "La cantidad")
        # Obtener el stock del producto
        stockP = Producto.obtenerAtrib((idP, ), ("idProducto", ), "productos", "stockProducto")
        stockP = stockP[0][0]
        # Verificar si la cantidad ingresada es un número válido
        if(type(cant) is not list):
            # Verificar si la cantidad solicitada es menor o igual al stock disponible
            if(cant<=stockP):
                # Convertir el precio unitario a tipo float
                precioU = float(precioU)
                # Crear una tupla con los datos del detalle (cantidad, precio unitario, ID del producto)
                datos = (cant, precioU, idP)
                # Agregar los datos del detalle a la lista de detalles
                self.listaDetalles.append(datos)
                # Insertar el texto del producto, descripción, precio unitario y cantidad en el ScrolledText
                self.scrolledtextPro.insert(tk.END, f"{self.comboProduc.get()} {descrip} - PU: ${precioU} - {cant}\n")
            else:
                # Mostrar un mensaje de error si la cantidad solicitada es mayor al stock disponible
                mb.showerror("Error", "La cantidad de productos en stock es menor a la solicitada.")
        else:
            # Mostrar un mensaje de error si la cantidad ingresada no es válida
            mb.showerror("Error", cant[0])


# PRECIO TOTAL 
    def cargarFactura(self):
        # Obtener el número de factura ingresado
        numFactura = f.ingNumPosi(self.entradaNum.get(), "El número de factura")
        # Mensaje de error si el número de factura junto al tipo de factura ya existe en la base de datos
        mensajeNR = "El número de factura junto al tipo de factura ya existe en la base de datos."
        # Obtener el ID del tipo de factura seleccionado
        idTipoF = self.comboTipoF.current() + 1
        # Obtener el ID de la factura usando el número de factura y el ID del tipo de factura
        idFactura = Factura.obtenerId((numFactura, idTipoF))
        # Verificar si la factura ya existe en la base de datos
        if idFactura == -1:
            mensajeNR = ""
        # Verificar si los datos de entrada son válidos
        entryValido = (self.listaDetalles != []) & (type(numFactura) is not list) & (mensajeNR == "")
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
            if type(numFactura) is list:
                # Verificar si el número de factura es una lista (indicando un error en la entrada)
                mensaje += f"{numFactura[0]}\n"
            if self.listaDetalles == []:
                # Verificar si el detalle de la factura está vacío
                mensaje += f"El detalle de la factura no puede estar vacío."
            if mensajeNR != "":
                # Verificar si hay un mensaje de error relacionado con el número de factura y tipo de factura existentes en la base de datos
                mensaje += mensajeNR
            # Mostrar un cuadro de diálogo de error con el mensaje de error acumulado
            mb.showerror("Error", mensaje)
        
    def on_selectC(self, event):
        indice = self.comboCli.current()
        # Obtener el índice seleccionado en el comboCli

        self.textCli = self.listaDNI[indice]
        # Obtener el DNI correspondiente al índice seleccionado en la listaDNI

        self.labelCliDni.config(text=f"DNI: {self.textCli}")
        # Actualizar el texto del labelCliDni con el nuevo valor de DNI obtenido

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
        # Itera sobre cada producto en la lista listaProductoSM
        for producto in listaProductoSM:
            self.scrolledtextProSM.insert(tk.END, f"{producto[0]} ({producto[1]})\t\t  {producto[2]}\t\t{producto[3]}\n")
            # Inserta una línea de texto en el ScrolledText scrolledtextProSM con información del producto.
            # Utiliza los elementos del producto (nombre, descripción, stock mínimo, stock actual) para formatear el texto.
        self.scrolledtextProSM.configure(state='disabled')
        # Configura el estado del ScrolledText scrolledtextProSM como 'disabled', lo que impide la edición del texto.

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
        # Método para dar de baja a un cliente
        indice = self.comboProv2.current()
        # Obtiene el índice seleccionado en el combobox comboProv2
        dniEli = self.listaDNI2[indice]
        # Obtiene el DNI del cliente a eliminar usando el índice
        self.listaNom2.pop(indice)
        # Elimina el nombre del cliente de la lista listaNom2 en el índice dado
        self.listaDNI2.remove(dniEli)
        # Elimina el DNI del cliente de la lista listaDNI2
        self.comboProv2.config(values=self.listaNom2)
        # Actualiza los valores del combobox comboProv2 con la lista de nombres actualizada
        idProv = Cliente.obtenerId((dniEli,))
        # Obtiene el ID del cliente utilizando el DNI
        Cliente.bajaCliente(idProv)
        # Llama al método bajaCliente de la clase Cliente, pasando el ID del cliente para eliminarlo de la base de datos
        mb.showinfo("¡Felicidades!", "Cliente dado de baja")
        # Muestra una ventana de información con el mensaje "Cliente dado de baja"
    
    def on_selectP2(self, event=None):
    # Método para manejar la selección de un cliente en el combobox comboProv2
        indice = self.comboProv2.current()
        # Obtiene el índice seleccionado en el combobox comboProv2
        self.scrolledtext2.config(state="normal")
        # Configura el estado del ScrolledText scrolledtext2 como "normal" para permitir la edición
        self.textProv2 = self.listaDNI2[indice]
        # Obtiene el DNI del cliente seleccionado utilizando el índice
        self.labelProv2.config(text=f"DNI: {self.textProv2}")
        # Configura el texto de la etiqueta labelProv2 para mostrar el DNI del cliente seleccionado
        cli1 = Cliente.obtenerCliente(int(self.textProv2))
        # Obtiene los datos del cliente utilizando el DNI
        mensaje = f"DNI: {cli1.DNI}\nCUIL/CUIT: {cli1.CUIL_CUIT}\nNombre: {cli1.nombre}\nDomicilio: {cli1.domicilio}\nTeléfono: {cli1.telefono}\n"
        # Crea un mensaje con los datos del cliente
        self.scrolledtext2.delete("1.0", tk.END)
        # Borra el contenido actual del ScrolledText scrolledtext2
        self.scrolledtext2.insert(tk.END, mensaje)
        # Inserta el mensaje con los datos del cliente en el ScrolledText scrolledtext2
        self.scrolledtext2.config(state="disabled")
        # Configura el estado del ScrolledText scrolledtext2 como "disabled" para evitar la edición

