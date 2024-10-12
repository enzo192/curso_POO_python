#HERENCIA MULTIPLE
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola estoy hablando un poco")    


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        #se usa super() y no self() por que queremos acceder al metodo de la clase padre
        print(f'Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')

roberto = EmpleadoArtista("Roberto",32,"colombiano","Cantar","2 millones","Google")

roberto.presentarse()

herencia = issubclass(EmpleadoArtista,Artista)
instancia = isinstance(roberto,EmpleadoArtista)
print(herencia)
print(instancia)