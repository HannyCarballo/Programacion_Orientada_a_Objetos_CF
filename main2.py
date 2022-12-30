from abc import ABC, abstractmethod

# clase abstracta
class EstructuraAbstracta(ABC):
    
    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


class Hash(EstructuraAbstracta):
    data = {}
 
    def obtener(self,key):
        data[key]
 
    def agregar(self,key,value):
        datos[llave]=valor

class Queue(EstructuraAbstracta):
    data = []
 
    def obtener(self):
        data[0]
 
    def agregar(self,key,value):
        datos[len(datos)-1]=valor


class FilaBanco:
    def __init__(self,almacen_usuarios):
        if not isinstance(almacen_usuarios,EstructuraAbstracta):
            raise ValueError("Store is not supported")

        self.usuarios = almacen_usuarios

    def siguiente_usuario(self,numero):
        # Implementacion
        return self.obtener(numero)

    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar(numero,usuario)

FilaBanco(Queue())