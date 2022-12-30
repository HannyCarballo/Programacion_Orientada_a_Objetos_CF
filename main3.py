# Devuelve el mayor

"""
# Sin polimorfismo
def retornaElMayor(a,b):
    #isinstance()
    if isinstance(a,int) and isinstance(b,int):
        if a>b:
            return a
        return b
    if isinstance(a,str) and isinstance(b,str):
        palabras=[a,b]
        palabras.sort()
        return palabras[0]

    if isinstance(a,list) and isinstance(b,list):
        if len(a)>len(b):
            return a
        return b

print(retornaElMayor("Uriel","Alejandro"))
print(retornaElMayor([1,2,3],[1,2]))
"""

# Con polimorfismo
class Numero:
    value=0
    def __init__(self,value):
        self.value=value

    def compare(self,numero):
        if numero.value>self.value:
            return numero.value
        return self.value

class Cadena:
    value=""
    def __init__(self,value):
        self.value=value

    def compare(self,cadena):
        palabras=(self.value,cadena.value)
        palabras.sort()
        return palabras[0]

class Lista:
    value=[]
    def __init__(self,value):
        self.value=value

    def compare(self,lista):
        if len(self.value)>len(lista.value):
            return self.value
        return lista.value

def retornaElMayor(a,b):
    return a.compare(b)

num_uno=Numero(10)
num_dos=Numero(2)
print(retornaElMayor(num_uno,num_dos))

cad_uno=Cadena("Hanny")
cad_dos=Cadena("Benoni")
print(retornaElMayor(cad_uno,cad_dos))