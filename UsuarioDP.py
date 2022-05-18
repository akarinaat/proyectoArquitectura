class UsuarioDP:

    #Constructor del usuario:
    def __init__(self,datos=""):
        if(datos == ""):
            self.nombreCuenta  = ""
            self.email = ""
            self.contrasena   = ""
            self.fechaInicio  = ""
            self.fechaFin = ""
        else:
            st = datos.split("_")

            self.nombreCuenta = st[0]
            self.email = st[1]
            self.contrasena = st[2]
            self.fechaInicio = st[3]
            self.fechaFin = st[4]

    def toString(self):
        return self.nombreCuenta+"_"+self.email+"_"+self.contrasena+"_"+self.fechaInicio+"_"+self.fechaFin       