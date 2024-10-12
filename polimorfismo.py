
# creamos una clase gato que hace un sonido caracteristico de su clase
class Gato():
    def sonido(self):
        return "Miau"


# creamos una clase perro que hace un sonido caracteristico de su clase
class Perro():
    def sonido(self):
        return "Guau"

#funcion corre el metodo dentro de la clase que le digamos 
def hacer_sonido(animal):
    print(animal.sonido())
    
#instanciamos un gato y un perro
gato = Gato()
perro = Perro()

#misma funcion que hara lo mismo independiente del parametro ingresado.
hacer_sonido(gato)

#metodo es el mismo y funciona igual tanto para el objeto gato o perro
print(gato.sonido())



####Investigar esto
#Duck typing
#Enlaces dinamicos y estaticos
#Tipo real y declarado
    