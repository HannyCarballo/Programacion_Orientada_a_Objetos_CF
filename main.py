# Creando una clase
class User:
    nombre = "Uriel"
    def saludar(self, saludo):
        print(saludo+self.nombre)

uriel = User()
uriel.saludar("Aloha! Mi nombre es: ")