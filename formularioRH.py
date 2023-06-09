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

class FormularioRH:
    def __init__(self, ventana, usuario):
        self.usuario = usuario
        self.tema = "itft1" #itft1 smog
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana34 = ThemedTk() #tk.Tk()
        #self.ventana34.set_theme_advanced(self.tema)
        self.ventana34.configure(bg=self.back)
        self.ventana34.title("3.5 - RECURSOS HUMANOS") #titulo de la ventana
        self.ventana34.geometry("900x750") # tamanno de la ventana
        self.ventana34.geometry("+10+20") #posicion en la pantalla
        
        self.labelSuperior = label(self.ventana34, text="RECURSOS HUMANOS", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        # boton para ir a la ventana anterior 
        self.botonAtras = bt(self.ventana34, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana34) # se crea un cuaderno para la ventana
        
        # el estilo para el cuaderno
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        # la pagina para contratar un empleado (lo hace un administrador)
        self.contratarEmpleado()
        # la pagina para consultar un empleado mediante el combobox
        self.consultarEmpleado()
        # se posiciona el cuaderno
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana34.mainloop() # se crea la ventana34

    def volverFormularioUsuario(self):
        self.ventana3.deiconify() # reaparece la ventana3
        self.ventana34.destroy() # se cierra la ventana34

    def contratarEmpleado(self):
        # se agrega la pagina1 al cuaderno
        self.pagina1 = ttk.Frame(self.cuaderno1)
        # se configura su tamanno
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Registrar Empleado")
        # 
        self.labelframe1 = labelF(self.pagina1, text="Registrar Empleado", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        # label y entrada de la fecha de contratacion
        self.labelFecha = label(self.labelframe1, text='Fecha de contratación:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFecha.grid(column=0, row=0, padx=4, pady=4)
        self.entradaFecha = DateEntry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFecha.grid(column=1, row=0, padx=4, pady=4)
        # label y entrada del dni
        self.labelDNI = label(self.labelframe1, text="DNI:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI.grid(column=0, row=1, padx=4, pady=4)
        self.entradaDNI = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI.grid(column=1, row=1, padx=4, pady=4)
        # label y entrada del CUIL
        self.labelCUIL = label(self.labelframe1, text="CUIL/CUIT:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCUIL.grid(column=0, row=2, padx=4, pady=4)
        self.entradaCUIL = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCUIL.grid(column=1, row=2, padx=4, pady=4)
        # label y entrada del nombre
        self.labelNombre = label(self.labelframe1, text="Nombre:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre.grid(column=0, row=3, padx=4, pady=4)
        self.entradaNombre = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre.grid(column=1, row=3, padx=4, pady=4)
        # label y entrada del domicilio
        self.labelDomi = label(self.labelframe1, text="Domicilio:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDomi.grid(column=0, row=4, padx=4, pady=4)
        self.entradaDomi = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDomi.grid(column=1, row=4, padx=4, pady=4)
        # label y entrada del telefono
        self.labelTel = label(self.labelframe1, text="Teléfono:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTel.grid(column=0, row=5, padx=4, pady=4)
        self.entradaTel = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaTel.grid(column=1, row=5, padx=4, pady=4)
        # label y entrada del usuario
        self.labelUser = label(self.labelframe1, text="Usuario:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(column=0, row=6, padx=4, pady=4)
        self.entradaUser = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(column=1, row=6, padx=4, pady=4)
        # label y entrada de la clave
        self.labelClave = label(self.labelframe1, text="Contraseña:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(column=0, row=7, padx=4, pady=4)
        self.entradaClave = entry(self.labelframe1, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(column=1, row=7, padx=4, pady=4)
        # label y entrada de la clave2 para repetirla
        self.labelClave2 = label(self.labelframe1, text="Repita la contraseña:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(column=0, row=8, padx=4, pady=4)
        self.entradaClave2 = entry(self.labelframe1, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(column=1, row=8, padx=4, pady=4)
        #label y combo del tipo de empleado
        self.labelTipo = label(self.labelframe1, text="Tipo de empleado:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipo.grid(column=0, row=9, padx=4, pady=4)
        # Combobox creation
        #self.entradaTipo = tk.StringVar() 
        self.comboTipo = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15)
        # Adding combobox drop down list
        self.comboTipo['values'] = ('Repositor', 'Vendedor', 'Productor')
        self.comboTipo.set('Repositor')
        self.comboTipo.grid(column = 1, row = 9)
        #boton confirmar para dar de alta a un nuevo empleado
        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoEmpleado)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevoEmpleado(self):
        usuarios = Usuario.recuperarNombresUser() # se recuperan los nombres de usuario
        listDni = Usuario.recuperarDNIs() # se recuperan los dnis
        #usuarios = usuarios[0]
        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI") # se valida el DNI
        if(type(dni) is not list): # si el dni no es lista, entonces es valido
            dni = f.ingDNI(dni, listDni) # se verifica que no exista en la bd
        cuil = f.ingDNI_CUIL(self.entradaCUIL.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomi.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)
        user = f.ingUser(self.entradaUser.get(), usuarios)
        claveVal = f.ingClaveValida(self.entradaClave.get())
        clave = f.ingClave(self.entradaClave.get(), self.entradaClave2.get())
        fecha = datetime.strptime(self.entradaFecha.get(), '%m/%d/%y') #datetime.strptime("5-26-2023", '%m-%d-%Y')
        tipo = self.comboTipo.get()
        dniCuilComparar=False
        dniCuilNoLista = (type(dni) is not list) & (type(cuil) is not list) 
        if(dniCuilNoLista): # si el cuil y el dni no son listas entonces se verifica si
            dniCuilComparar = f.dniCuilComparar(dni, cuil) # el dni y cuil coinciden para ser validos
        entrysValidos = ((dniCuilNoLista)&(type(user) is not list)&(type(clave) is not list)&(nombre!="")&(domi!="")&(dniCuilComparar)&(type(claveVal) is not list)&(type(tel) is not list))
        if(entrysValidos): # si todas las entradas dan True, entonces se da de alta
            #DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, fechaInicio,
            # se crea un objeto de tipo Empleado que se guardara en la tabla usuarios en la base de datos
            nuevoEmple = Empleado(dni, cuil, nombre, domi, int(tel), user, clave, tipo)
            # se obtiene el id del administrador que contrata al empleado mediante el dni
            idAdmin = Administrador.obtenerId((self.usuario.DNI, ))
            # se obtiene el id del empleado que se dio de alta anteriormente mediante el dni
            idEmple = Empleado.obtenerId((nuevoEmple.DNI, ))
            # se instancia el metodo contratacion del objeto Administrador, para dar de alta una contratacion en la tabla contratacion en la BD
            self.usuario.contratacion(fecha, idAdmin, idEmple)
            mb.showinfo("¡Felicidades!", "Empleado registrado")
        else:
            mensaje=""
            if(type(dni) is list): # si alguna variable es una lista, entonces guarda un unico valor que es el mensaje de error
                mensaje += dni[0]
            if(type(cuil) is list):
                mensaje += "\n"+cuil[0]
            if(nombre == ""):
                mensaje += "\nEl nombre no puede estar vacío."
            if(domi == ""):
                mensaje += "\nEl domicilio no puede estar vacío."
            if(type(tel) is list):
                mensaje += "\n"+tel[0]
            if(type(user) is list):
                mensaje += "\n"+user[0]
            if(type(claveVal) is list):
                mensaje += claveVal[0]
            if(type(clave) is list):
                mensaje += "\n"+clave[0]
            if(dniCuilComparar==False):
                mensaje += "\nEl DNI y el CUIL/CUIT no coinciden."
            # inserta el mensaje en la ventana de error
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END) # se eliminan los valores escritos en las entradas
        self.entradaCUIL.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaDomi.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaUser.delete(0, tk.END)
        self.entradaClave.delete(0, tk.END)
        self.entradaClave2.delete(0, tk.END)

    def consultarEmpleado(self):
        self.pagina2 = ttk.Frame(self.cuaderno1) # se posiciona la pagina2 en el cuaderno1
        self.pagina2.config(width=800, height=750) # se configura su tamanno
        self.cuaderno1.add(self.pagina2, text="Consultar Empleado") # se agrega el texto
        
        self.labelframe2 = labelF(self.pagina2, text="Consultar Empleado", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        # label y entrada del dni del empleado a consultar
        self.labelDNI2 = label(self.labelframe2, text="DNI:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI2.grid(column=0, row=0, padx=4, pady=4)
        self.entradaDNI2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI2.grid(column=1, row=0, padx=4, pady=4)
        # scrolledtext donde se pondran los datos del empleado
        self.scrolledtext2 = st.ScrolledText(self.labelframe2, font=(self.fuente, 20), width=35, height=10)
        self.scrolledtext2.grid(column=1, row=1, padx=10, pady=10)
        # boton consultar para accionar verEmpleado
        self.botonConsultar = bt(self.labelframe2, text="Consultar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.verEmpleado)
        self.botonConsultar.grid(column=1, row=10, padx=4, pady=4)
        
    def verEmpleado(self):
        try: #obtiene el dni2
            self.dni2 = int(self.entradaDNI2.get())
        except Exception:
            self.dni2 = self.entradaDNI2.get()
        self.datos = (self.dni2, )
        self.listaDNIs = Empleado.obtenerDNIs() # obtiene la lista de dnis de empleados
        self.emple = Empleado.obtenerEmpleado(self.listaDNIs, self.datos, True) # se obtiene al empleado, como no es nuevo, se le pasa el argumento True
        consulta = self.emple # se guarda el objeto empleado en consulta
        if consulta is not False: # si la consulta no es False, entonces existe el dni de empleado en la bd
            self.scrolledtext2.configure(state='normal') # se configura para poder editar
            #(DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, puesto
            consultaFC = Empleado.verFechaContratacion((consulta[0], )) # se consulta la fecha de contratacion
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # se ponen las fechas en espannol
            fechaIni = consultaFC[0][0] # consultaFC = [(valor,)]      fechaIni = valor
            fechaIni = fechaIni.strftime('%d de %B de %Y') # se muestra la fecha en ese formato "9 de Junio de 2023"
            if(consulta[8]==1): 
                puesto="Repositor"
            elif(consulta[8]==2):
                puesto="Vendedor"
            else:
                puesto="Productor"
            # se guarda en mensaje todos los datos del empleado
            mensaje = "ID: "+str(consulta[0])+"\nDNI: "+str(consulta[1])+"\nCUIL/CUIT: "+str(consulta[2])+"\nNombre: "+consulta[3]+"\nDomicilio: "+consulta[4]+"\nTeléfono: "+str(consulta[5])+"\nUsuario: "+consulta[6]+"\nCargo: "+puesto+"\nFecha de contratación: "+str(fechaIni)
            self.scrolledtext2.delete("1.0", tk.END)
            self.scrolledtext2.insert(tk.END, mensaje) # se inserta el mensaje en el scrolledtext
            self.scrolledtext2.configure(state='disabled')
        else:
            self.entradaDNI2.delete(0, tk.END)
            self.scrolledtext2.delete("1.0", tk.END)
            # se imprime el mensaje de error
            mb.showerror("Error", "No existe empleado con el DNI ingresado.")
    
