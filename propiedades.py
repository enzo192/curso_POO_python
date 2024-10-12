class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    #GET
    @property
    def nombre(self):
        return self.__nombre
    
    #SET
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    #DELET
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
#GET   
enzo = Persona("Enzo",32)

nombre = enzo.nombre
print(nombre)

#SET
enzo.nombre = "ruddy"

nombre = enzo.nombre
print(nombre)

#DEL
del enzo.nombre
