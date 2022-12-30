# Creando una clase
class User:
    def __init__(self, nombre):
        # Método constructor
        self._nombre=nombre
        
    def saludar(self, saludo):
        print(saludo+self.nombre)

class Empleado(User):
    #propiedades unicamente de esta clase
    __salario = 0

    def modificar_salario(self,salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)

    def saludar(self):
        super().saludar("Hola!")
        print("Mi nombre es "+self._nombre+" y gano: "+str(self.salario))

empleado = Empleado("Hannita :)")
# se pueden modificar una propiedad privada
print(empleado.__salario)