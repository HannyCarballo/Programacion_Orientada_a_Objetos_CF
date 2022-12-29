# Creando una clase
class User:
    nombre = "Uriel"
    def saludar(self):
        print("Hola, mi nombre es"+self.nombre)

uriel = User()
uriel.saludar()

cody = User()
cody.nombre = "Cody"

print(uriel.nombre)
print(cody.nombre)