# Creando una clase
class User:

    def __init__(self, nombre):
        # Método constructor
        self.nombre=nombre
        
    def saludar(self, saludo):
        print(saludo+self.nombre)
