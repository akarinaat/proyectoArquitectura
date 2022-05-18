from re import A
from tkinter import *

from AdminDB import AdminDB


class IDBoxGUI:

    cuenta = AdminDB()
    # Constructor

    def __init__(self):

        # 1. Definición y creación del objeto frame
        self.root = Tk()
        self.root.title("IDBox")
        self.root.geometry("600x400")
        self.show_frame_login()
        # 
        self.root.mainloop()

        # 4. Obtener los datos de los TextFields
    def show_frame_login(self):

        #Aqui tengo que hacer lo mismo de allá abajo pero para el login



        #Aquí después va el destroy
        #Ya que se haga el login poner el show frame datos
        self.show_frame_datos()

       


    def show_frame_datos(self):
        self.frameDatos = Frame(self.root)
        self.frameDatos.grid(row=0, column=0)

        # Definición y creación de los atributos del frame
        self.lbNombreCuenta = Label(self.frameDatos, text="Cuenta:")
        self.tfNombreCuenta = Entry(self.frameDatos, width=20)

        self.lbEmail = Label(self.frameDatos, text="email:")
        self.tfEmail = Entry(self.frameDatos, width=20)

        self.lbContrasena = Label(self.frameDatos, text="Contraseña:")
        self.tfContrasena = Entry(self.frameDatos, width=20)

        self.lbFechaInicio = Label(self.frameDatos, text="Fecha inicio:")
        self.tfFechaInicio = Entry(self.frameDatos, width=20)

        self.lbFechaFin = Label(self.frameDatos, text="Fecha Fin:")
        self.tfFechaFin = Entry(self.frameDatos, width=20)

        self.bCambiarContrasena = Button(
            self.frameDatos, text="Cambiar contraseña")
        self.bGuardar = Button(self.frameDatos, text="Guardar",
                               command=self.capturarDatos)
        self.bVerCuentas = Button(
            self.frameDatos, text="Ver info cuentas", command=self.consultarCuentas)

        self.taDatos = Text(self.frameDatos, width=40, height=10)

        # 3. Colocar los objetos de los atributos en un layout
        self.lbNombreCuenta.grid(row=0, column=0)
        self.tfNombreCuenta.grid(row=0, column=1)

        self.lbEmail.grid(row=1, column=0)
        self.tfEmail.grid(row=1, column=1)

        self.lbContrasena.grid(row=2, column=0)
        self.tfContrasena.grid(row=2, column=1)

        self.lbFechaInicio.grid(row=3, column=0)
        self.tfFechaInicio.grid(row=3, column=1)

        self.lbFechaFin.grid(row=4, column=0)
        self.tfFechaFin.grid(row=4, column=1)

        self.bCambiarContrasena.grid(row=5, column=0)
        self.bGuardar.grid(row=5, column=1)
        self.bVerCuentas.grid(row=5, column=2)

        self.taDatos.grid(row=6, column=1)

    def obtenerDatos(self):
        nombreCuenta = self.tfNombreCuenta.get()
        email = self.tfEmail.get()
        contrasena = self.tfContrasena.get()
        fechaInicio = self.tfFechaInicio.get()
        fechaFin = self.tfFechaFin.get()

        if nombreCuenta == "" or email == "" or contrasena == "":
            datos = "VACIO"
        else:
            datos = nombreCuenta+"_"+email+"_"+contrasena+"_"+fechaInicio+"_"+fechaFin
        return datos

        # 5. Capturar los datos

    def capturarDatos(self):
        datos = self.obtenerDatos()
        self.taDatos.delete("1.0", END)
        if datos == "VACIO":
            self.taDatos.insert(END, "Algun campo esta vacio...")
        else:
            resultado = self.cuenta.capturar(datos)
            self.taDatos.insert(END, resultado)
        self.limpiarCampos()

    def limpiarCampos(self):
        self.tfNombreCuenta.delete(0, END)
        self.tfEmail.delete(0, END)
        self.tfContrasena.delete(0, END)
        self.tfFechaInicio.delete(0, END)
        self.tfFechaFin.delete(0, END)

    def consultarCuentas(self):
        self.taDatos.delete("1.0", END)

        datos = self.cuenta.consultar()
        self.taDatos.insert(END, datos)


box = IDBoxGUI()
