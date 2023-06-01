import sys
#from FrontEnd.formularioUsuario import FormularioUsuario
# Hay que ejecutar esta línea antes de importar el módulo.
sys.path.append("C:/Users/mdari/Desktop/Ing_Prog/BackEnd/")
# Ahora se puede importar el módulo.
from administrador import Administrador
from empleado import Empleado
from usuario import Usuario
from formularioUsuario import FormularioUsuario
from funciones import funciones as f
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import Entry as entry
from tkinter import Label as label
from PIL import Image, ImageTk, ImageDraw
from tkinter import Button as bt
from ttkthemes import ThemedTk
import tkinter as tk

# sys.path.insert(0, r"C:/Users/mdari/Desktop/Ing_Prog/BackEnd/administrador.py")
# sys.path.insert(0, r'C:/Users/mdari/Desktop/Ing_Prog/FrontEnd')
# tkinter.font.families() para ver las fuentes


class FormularioSesion:
    def __init__(self, ventana):
        self.tema = "black"
        self.ventana1 = ventana
        self.back = 'light blue'
        self.backB = 'LightSalmon1'
        self.fuenteB = 'gray20'
        self.fuente = 'Franklin Gothic Demi Cond'
        self.ventana22 = ThemedTk()
        self.ventana22.configure(bg=self.back)
        self.ventana22.geometry("900x750")
        self.ventana22.geometry("+10+20")
        self.ventana22.title("2.2 - SESION")
        style = ttk.Style(self.ventana22)
        style.theme_use(self.tema)
        self.botonAtras = bt(self.ventana22, text="⬅️", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.abrirFormularioInicio)
        self.botonAtras.grid(row=0, column=0, sticky='w')

        self.labelSuperior = label(self.ventana22, text="INICIAR SESIÓN", font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelSuperior.grid(row=0, column=1, padx=10, sticky='w')

        self.labelE = label(self.ventana22, font=(self.fuente, 30), fg=self.fuenteB, background=self.back)
        self.labelE.grid(row=1, column=0, pady=20, sticky='w')

        self.labelUser = label(self.ventana22, text="Usuario: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelUser.grid(row=2, column=0, padx=1, pady=1, sticky='w')
        self.entradaUser = entry(self.ventana22, font=(self.fuente, 20), fg=self.fuenteB)
        self.entradaUser.grid(row=2, column=1, padx=1, pady=1, sticky='w')

        self.labelClave = label(self.ventana22, text="Contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave = entry(self.ventana22, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave.grid(row=3, column=1, padx=1, pady=1, sticky='w')

        self.labelClave2 = label(self.ventana22, text="Repita su contraseña: ", font=(self.fuente, 20), fg=self.fuenteB, background=self.back)
        self.labelClave2.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.entradaClave2 = entry(self.ventana22, font=(self.fuente, 20), show="•", fg=self.fuenteB)
        self.entradaClave2.grid(row=4, column=1, padx=1, pady=1, sticky='w')

        self.botonIniciarS = bt(self.ventana22, text="INICIAR SESIÓN", font=(self.fuente, 20), bg=self.backB, fg=self.fuenteB, command=self.iniciarSesionAdminEmple)
        # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        self.botonIniciarS.grid(row=5, column=1, padx=45, pady=60, sticky='w')
        
       
        self.ventana22.mainloop()

    def abrirFormularioInicio(self):
        self.ventana1.deiconify()
        self.ventana22.destroy()

    def abrirFormularioUsuario(self, tipo):
        self.ventana22.withdraw()
        aplicacion3 = FormularioUsuario(self.ventana22, tipo)

    def iniciarSesionAdminEmple(self):
        usuarios = Usuario.recuperarNombresUser()
        #usuarios = usuarios[0]
        user = self.entradaUser.get()
        clave = f.ingClave(self.entradaClave.get(), self.entradaClave2.get())
        entryValido = (type(clave) is not list)
        mensaje=""
        bandeIS = False
        if(entryValido):
            usuarioIng = Usuario.iniciarSesion(user, clave)
            if(usuarioIng!=[]):
                #aqui volvemos a la lista de 1 tupla, en solo 1 tupla
                usuarioIng = usuarioIng[0]
                #print(usuarioIng)
                tipo=usuarioIng[8]
                if(tipo==1): #Administrador
                    userOld = Administrador.obtenerAdmi(usuarioIng[1]) 
                else: #Empleado
                    listDNI = Empleado.obtenerDNIs()
                    userOld = Empleado.obtenerEmpleado(listDNI, (usuarioIng[1], ))
                mb.showinfo("¡Felicidades!", f"Bienvenid@ {usuarioIng[3]}")
                bandeIS=True
            else:
                mensaje += "\nUsuario y/o contraseña incorrectos."
        self.entradaUser.delete(0, tk.END)
        self.entradaClave.delete(0, tk.END)
        self.entradaClave2.delete(0, tk.END)
        if(bandeIS):
            #Aqui inicia sesion
            #if(tipo==1): #Administrador
            #    print("Abrir Formulario con todas las opciones")
                #print(admiOld)
            #else: #Empleado
            #    print("Abrir Formulario con las opciones particulares del tipo de empleado")
            #directamente con userOld verificaremos que modulos puede usar en el formularioUsuario
            #utilizando un try except para ver si tiene el atributo idTipoEmpleado
            self.abrirFormularioUsuario(userOld)
        else:
            if(type(clave) is list):
                mensaje += "\n"+clave[0]
            mb.showerror("Error", mensaje)
            #self.entradaUser.delete(0, tk.END)
            #self.entradaClave.delete(0, tk.END)
            #self.entradaClave2.delete(0, tk.END)

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
