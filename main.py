# Creando una clase
class User:
    def __init__(self, nombre):
        # Método constructor
        self.nombre=nombre
        
    def saludar(self, saludo):
        print(saludo+self.nombre)

class Empleado(User):
    #propiedades unicamente de esta clase
    salario = 0

    def modificar_salario(self,salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

empleado = Empleado("Hannita :)")
empleado.saludar("Hola! me llamo ")
empleado.modificar_salario(1000)
empleado.ver_salario()