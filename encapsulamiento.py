#encapsulamiento permite proteger atributos, para obtener datos encapsulados debemos usar GETters y SETters.

class MiClase:
    def __init__(self):
        #aca estamos diciendo que es un atributo privado. _al inicio indica "privado" __al inicio indica "muy privado"
        self.__atributo_privado = "Valor"
    
    #Tambien hay metodos privados    
    def _hablar(self):
        print("hola, como estas")
        
objeto = MiClase()
#puedo acceder si es privado pero no si es muy privado.
objeto._hablar()

#-------------------------------------------------------------------------------------------------------

#creamos la clase persona
class Persona:
    def __init__(self, nombre, edad):
        #con atributos privados a los que debemos acceder con get o set.
        self._nombre = nombre
        self._edad = edad
    
    #creamos una funcion para obtener el valor del atributo privado   
    def get_nombre(self):
        return self._nombre
    
    #creamos una funcion SET para modificar el valor del atributo privado
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

#instanciamos un objeto de la clase persona    
enzo = Persona("Enzo",32)

#usamos la funcion GET para traer el nombre
nombre = enzo.get_nombre()
print(nombre)

#usamos la funcion SET para modificar el nombre
enzo.set_nombre("ruddy")

#usamos la funcion GET para traer el nuevo nombre
nombre = enzo.get_nombre()
print(nombre)

