

from pymongo import MongoClient
from UsuarioDP import UsuarioDP
import os


class AdminDB:

    def capturar(self, datos):
        resultado = ""

        try:
            # 1 .Primer intento guardarlo en un archivo
            archivoOut = open("Usuarios.txt", "a")  # El a es de append
            # para que escriba al final de lo que
            # encuentre en el archivo y no lo
            # sobreescriba

            # Con base de datos Mongo
            CONNECTION_STRING = "mongodb+srv://m001-student:m001-mongodb-basics@idbox.sk5wx.mongodb.net/test"
            usuario = UsuarioDP(datos)
            insertarUsuario = "String de mongo para insertar usuario en el cluster"

            # 2. Almacenar los datos en el archivo
            archivoOut.write(datos+"\n")

            # Para la base de datos es algo así como
            # Con el findOne

            # 3. Cerrar el archivo
            archivoOut.close()

            # Con mongo sería algo así como
            # conexion.close() o algo así

            resultado = "Datos capturados: " + datos
        except:

            resultado = "Error en la Captura de Datos del Usuario..."

        return resultado

    def consultar(self):
        datos = ""

        # Por el momento lo vamos a hacer con el archivo
        # Mas a delante lo haremos desde la base en mongo :)

        # 1. Abrir el archivo para leer
        archivoIn = open("Usuarios.txt", "r")

        for line in archivoIn.readlines():

            usuariodp = UsuarioDP(line)

            datos += usuariodp.toString()

        # 3. Cerrar el archivo
        archivoIn.close()

        return datos


#     def get_database():

#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#         CONNECTION_STRING = "mongodb+srv://m001-student:m001-mongodb-basics@idbox.sk5wx.mongodb.net/test"
#     # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient

#         client = MongoClient(CONNECTION_STRING)

#     # Create the database for our example (we will use the same database throughout the tutorial
#         return client['users']

# # This is added so that many files can reuse the function get_database()
#     if __name__ == "__main__":

#     # Get the database
#         dbname = get_database()
