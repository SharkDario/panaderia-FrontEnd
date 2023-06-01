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
        self.tema = "blue"
        self.back = 'light blue'
        self.backB = 'SteelBlue3'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana3 = ventana
        self.ventana34 = ThemedTk() #tk.Tk()
        self.ventana34.configure(bg=self.back)
        self.ventana34.title("3.5 - RECURSOS HUMANOS")
        self.ventana34.geometry("900x750")
        self.ventana34.geometry("+10+20")

        
        
        self.labelSuperior = label(self.ventana34, text="RECURSOS HUMANOS", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')
        

        self.botonAtras = bt(self.ventana34, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.volverFormularioUsuario)
        self.botonAtras.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.cuaderno1 = ttk.Notebook(self.ventana34)

        #print(self.ventana34.get_themes())
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(self.tema)
        
        #SI: blue, smog, black, adapta
        #EH: kroc, plastik, winxpblue, itft1, aquativo, clam
        #NO: equilux, keramik, elegance, radiance, breeze, clearlooks, ubuntu, yaru, scidmint
        #[ 'alt', 'scidpurple', 'scidpink', 
        #'default', 'scidblue', 'classic', 'xpnative', 
        #, 'scidgrey', 'scidsand', 'scidgreen', 'arc', 'vista', 'winnative']

        self.contratarEmpleado()
        self.consultarEmpleado()
        self.cuaderno1.grid(column=1, row=1, padx=10, pady=10)
        self.ventana34.mainloop()

   

    def volverFormularioUsuario(self):
        self.ventana3.deiconify()
        self.ventana34.destroy()

    def contratarEmpleado(self):
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        #900x750
        self.pagina1.config(width=800, height=750)
        self.cuaderno1.add(self.pagina1, text="Registrar Empleado")
        
        self.labelframe1 = labelF(self.pagina1, text="Registrar Empleado", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.labelFecha = label(self.labelframe1, text='Fecha de contratación:', font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelFecha.grid(column=0, row=0, padx=4, pady=4)
        self.entradaFecha = DateEntry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB, width=15, background=self.backB, foreground='white', borderwidth=2)
        self.entradaFecha.grid(column=1, row=0, padx=4, pady=4)

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

        self.labelUser = label(self.labelframe1, text="Usuario:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(column=0, row=6, padx=4, pady=4)
        self.entradaUser = entry(self.labelframe1, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(column=1, row=6, padx=4, pady=4)

        self.labelClave = label(self.labelframe1, text="Contraseña:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(column=0, row=7, padx=4, pady=4)
        self.entradaClave = entry(self.labelframe1, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(column=1, row=7, padx=4, pady=4)

        self.labelClave2 = label(self.labelframe1, text="Repita la contraseña:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(column=0, row=8, padx=4, pady=4)
        self.entradaClave2 = entry(self.labelframe1, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(column=1, row=8, padx=4, pady=4)
        
        self.labelTipo = label(self.labelframe1, text="Tipo de empleado:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTipo.grid(column=0, row=9, padx=4, pady=4)
        # Combobox creation
        #self.entradaTipo = tk.StringVar() 
        self.comboTipo = ttk.Combobox(self.labelframe1, font=(self.fuente, 20), width = 15)
        # Adding combobox drop down list
        self.comboTipo['values'] = ('Repositor', 'Vendedor', 'Productor')
        self.comboTipo.set('Repositor')
        self.comboTipo.grid(column = 1, row = 9)

        self.botonConfirmar = bt(self.labelframe1, text="Registrar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.altaNuevoEmpleado)
        self.botonConfirmar.grid(column=1, row=10, padx=4, pady=4)
        

    def altaNuevoEmpleado(self):
        usuarios = Usuario.recuperarNombresUser()
        listDni = Usuario.recuperarDNIs()
        #usuarios = usuarios[0]
        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI")
        if(type(dni) is not list):
            dni = f.ingDNI(dni, listDni)
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
        if(dniCuilNoLista):
            dniCuilComparar = f.dniCuilComparar(dni, cuil)
        entrysValidos = ((dniCuilNoLista)&(type(user) is not list)&(type(clave) is not list)&(nombre!="")&(domi!="")&(dniCuilComparar)&(type(claveVal) is not list)&(type(tel) is not list))
        if(entrysValidos):
            #DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, fechaInicio,
            nuevoEmple = Empleado(dni, cuil, nombre, domi, int(tel), user, clave, tipo) #fecha
            idAdmin = Administrador.obtenerId((self.usuario.DNI, ))
            idEmple = Empleado.obtenerId((nuevoEmple.DNI, ))
            self.usuario.contratacion(fecha, idAdmin, idEmple)
            mb.showinfo("¡Felicidades!", "Empleado registrado")
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
            if(type(user) is list):
                mensaje += "\n"+user[0]
            if(type(claveVal) is list):
                mensaje += claveVal[0]
            if(type(clave) is list):
                mensaje += "\n"+clave[0]
            if(dniCuilComparar==False):
                mensaje += "\nEl DNI y el CUIL/CUIT no coinciden."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END)
        self.entradaCUIL.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaDomi.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaUser.delete(0, tk.END)
        self.entradaClave.delete(0, tk.END)
        self.entradaClave2.delete(0, tk.END)

    def consultarEmpleado(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.pagina2.config(width=800, height=750)
        self.cuaderno1.add(self.pagina2, text="Consultar Empleado")
        
        self.labelframe2 = labelF(self.pagina2, text="Consultar Empleado", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.labelDNI2 = label(self.labelframe2, text="DNI:", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI2.grid(column=0, row=0, padx=4, pady=4)
        self.entradaDNI2 = entry(self.labelframe2, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI2.grid(column=1, row=0, padx=4, pady=4)

        self.scrolledtext2 = st.ScrolledText(self.labelframe2, font=(self.fuente, 20), width=35, height=10)
        self.scrolledtext2.grid(column=1, row=1, padx=10, pady=10)

        self.botonConsultar = bt(self.labelframe2, text="Consultar", font=(self.fuente, 20), fg=self.fuenteB, background=self.backB, command=self.verEmpleado)
        self.botonConsultar.grid(column=1, row=10, padx=4, pady=4)
        
    def verEmpleado(self):
        try:
            self.dni2 = int(self.entradaDNI2.get())
        except Exception:
            self.dni2 = self.entradaDNI2.get()
        self.datos = (self.dni2, )
        self.listaDNIs = Empleado.obtenerDNIs()
        self.emple = Empleado.obtenerEmpleado(self.listaDNIs, self.datos, True)
        consulta = self.emple
        if consulta is not False:
            self.scrolledtext2.configure(state='normal')
            #(DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, puesto
            consultaFC = Empleado.verFechaContratacion((consulta[0], ))
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            fechaIni = consultaFC[0][0]
            fechaIni = fechaIni.strftime('%d de %B de %Y')
            if(consulta[8]==1):
                puesto="Repositor"
            elif(consulta[8]==2):
                puesto="Vendedor"
            else:
                puesto="Productor"
            mensaje = "ID: "+str(consulta[0])+"\nDNI: "+str(consulta[1])+"\nCUIL/CUIT: "+str(consulta[2])+"\nNombre: "+consulta[3]+"\nDomicilio: "+consulta[4]+"\nTeléfono: "+str(consulta[5])+"\nUsuario: "+consulta[6]+"\nCargo: "+puesto+"\nFecha de contratación: "+str(fechaIni)
            self.scrolledtext2.delete("1.0", tk.END)
            self.scrolledtext2.insert(tk.END, mensaje)
            self.scrolledtext2.configure(state='disabled')
        else:
            self.entradaDNI2.delete(0, tk.END)
            #self.scrolledtext2.configure(state='normal')
            self.scrolledtext2.delete("1.0", tk.END)
            #self.scrolledtext2.configure(state='disabled')
            mb.showerror("Error", "No existe empleado con el DNI ingresado.")
    

        
        #subprocess.call(["python", "formularioInicio.py"])



#a#['adapta', 'alt', 'blue', 'scidpurple', 'scidpink', 'aquativo', 'itft1', 'equilux', 'elegance', 
        #'default', 'clam', 'black', 'scidblue', 'winxpblue', 'classic', 'radiance', 'scidmint', 'xpnative', 
        #'yaru', 'ubuntu', 'kroc', 'plastik', 'breeze', 'scidgrey', 'scidsand', 'scidgreen', 'clearlooks', 'smog', 'arc', 'vista', 'keramik', 'winnative']
        """
        our_themes = self.ventana34.get_themes()
        print(our_themes)
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use("adapta")

        my_menu = Menu(self.ventana34)
        self.ventana34.config(menu=my_menu)

        theme_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(menu=theme_menu)
        
 def changer(self, theme):
        self.style = ttk.Style(self.cuaderno1)
        self.style.theme_use(theme)

        for t in our_themes:
            theme_menu.add_command(label=t , command=self.changer(t))
        """