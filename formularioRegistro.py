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
from ttkthemes import ThemedTk
import tkinter as tk
from usuario import Usuario
# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes


class FormularioRegistro: # se define una clase que crea una ventana de formulario para el registro de adminstradores
    def __init__(self, ventana): # constructor de la clase
        self.tema = "black" # se inicializa varias variables
        self.ventana1 = ventana
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente =  'Franklin Gothic Demi Cond'
        self.ventana21 = ThemedTk()
        self.ventana21.configure(bg=self.back)
        self.ventana21.geometry("900x750")
        self.ventana21.geometry("+10+20")
        self.ventana21.title("2.1 - REGISTRO")
        style = ttk.Style(self.ventana21)
        style.theme_use(self.tema)
        
        #🔙
        self.botonAtras = bt(self.ventana21, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioInicio)
        self.botonAtras.grid(row=0, column=0, sticky='w')

        self.labelSuperior = label(self.ventana21, text="REGISTRO ADMIN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')

        self.labelE = label(self.ventana21, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w')

        # DNI, CUIL_CUIT, nombre, domicilio, user, clave,
        self.labelDNI = label(self.ventana21, text="DNI: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDNI.grid(row=2, column=0, padx=1, pady=1, sticky='w')
        self.entradaDNI = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDNI.grid(row=2, column=1, padx=1, pady=1, sticky='w')

        self.labelCUIL_CUIT = label(self.ventana21, text="CUIL/CUIT: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelCUIL_CUIT.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.entradaCUIL_CUIT = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaCUIL_CUIT.grid(row=3, column=1, padx=1, pady=1, sticky='w')

        self.labelNombre = label(self.ventana21, text="Nombre completo: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelNombre.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.entradaNombre = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaNombre.grid(row=4, column=1, padx=1, pady=1, sticky='w')

        self.labelDomicilio = label(self.ventana21, text="Domicilio: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelDomicilio.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.entradaDomicilio = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaDomicilio.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.labelTel = label(self.ventana21, text="Teléfono: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelTel.grid(row=6, column=0, padx=1, pady=1, sticky='w')
        self.entradaTel = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaTel.grid(row=6, column=1, padx=1, pady=1, sticky='w')

        self.labelUser = label(self.ventana21, text="Usuario: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(row=7, column=0, padx=1, pady=1, sticky='w')
        self.entradaUser = entry(self.ventana21, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(row=7, column=1, padx=1, pady=1, sticky='w')

        self.labelClave = label(self.ventana21, text="Contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(row=8, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(row=8, column=1, padx=1, pady=1, sticky='w')

        self.labelClave2 = label(self.ventana21, text="Repita su contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(row=9, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave2 = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(row=9, column=1, padx=1, pady=1, sticky='w')

        self.labelIden = label(self.ventana21, text="Identificación: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelIden.grid(row=10, column=0, padx=1, pady=1, sticky='w')
        self.entradaIden = entry(self.ventana21, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaIden.grid(row=10, column=1, padx=1, pady=1, sticky='w')

        self.botonRegistro = bt(self.ventana21, text="REGISTRARSE", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.altaNuevoAdministrador)
        self.botonRegistro.grid(row=11, column=1, padx=45, pady=60, sticky='w')
        
        self.ventana21.mainloop()

    def abrirFormularioInicio(self):
        self.ventana1.deiconify()
        self.ventana21.destroy()
        #self.ventana21.withdraw()
        #C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\
        #subprocess.call(["python", "C:\\Users\\mdari\\Desktop\\Ing_Prog\\FrontEnd\\formularioInicio.py"])

    def altaNuevoAdministrador(self):
        usuarios = Usuario.recuperarNombresUser()
        listDni = Usuario.recuperarDNIs()
        #usuarios = usuarios[0]
        dni = f.ingDNI_CUIL(self.entradaDNI.get(), 8, "DNI")
        if(type(dni) is not list):
            dni = f.ingDNI(dni, listDni)
        cuil = f.ingDNI_CUIL(self.entradaCUIL_CUIT.get(), 11)
        nombre = self.entradaNombre.get()
        domi = self.entradaDomicilio.get()
        tel = f.ingNum(self.entradaTel.get(), "El teléfono", 15)
        user = f.ingUser(self.entradaUser.get(), usuarios)
        claveVal = f.ingClaveValida(self.entradaClave.get())
        clave = f.ingClave(self.entradaClave.get(), self.entradaClave2.get())
        iden = f.ingClave(self.entradaIden.get(), f.recuperarIden(), "El código de identificación es incorrecto")
        #print((dni is not list)&(cuil is not list)&(user is not list)&(clave is not list)&(iden is not list))
        dniCuilComparar=False
        dniCuilNoLista = (type(dni) is not list) & (type(cuil) is not list)
        if(dniCuilNoLista):
            dniCuilComparar = f.dniCuilComparar(dni, cuil)
        entrysValidos = ((dniCuilNoLista)&(type(user) is not list)&(type(clave) is not list)&(type(iden) is not list)&(nombre!="")&(domi!="")&(dniCuilComparar)&(type(claveVal) is not list)&(type(tel) is not list))
        if(entrysValidos):
            nuevoAdmi = Administrador(dni, cuil, nombre, domi, int(tel), user, clave)
            mb.showinfo("¡Felicidades!", "Administrador registrado")
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
            if(type(iden) is list):
                mensaje += "\n"+iden[0]
            if(dniCuilComparar==False):
                mensaje += "\nEl DNI y el CUIL/CUIT no coinciden."
            #print(mensaje)
            mb.showerror("Error", mensaje)
        self.entradaDNI.delete(0, tk.END)
        self.entradaCUIL_CUIT.delete(0, tk.END)
        self.entradaNombre.delete(0, tk.END)
        self.entradaDomicilio.delete(0, tk.END)
        self.entradaTel.delete(0, tk.END)
        self.entradaUser.delete(0, tk.END)
        self.entradaClave.delete(0, tk.END)
        self.entradaClave2.delete(0, tk.END)
        self.entradaIden.delete(0, tk.END)

        
        

    

        
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



class FormularioArticulos:
    # consulta
    # recuperar datos
    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1 = ttk.Button(
            self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(
            self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1 = ttk.Button(
            self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información",
                        "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1 = ttk.Button(
            self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1 = st.ScrolledText(
            self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(
                tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")


aplicacion1 = FormularioArticulos()
"""
