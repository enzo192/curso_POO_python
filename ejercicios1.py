#Crear una clase Estudiante, Atributos Nombre, Edad y Grado, Metodos estudiar() = "el estudiante (nombre) esta estudiando"
#Crear un objeto Estudiante y usar el metodo estudiar(), Se debe interactuar con el usuario y este debe brindar los atributos.
#Al escribir "estudiar" utilizar el metodo estudiar() (no case sensitive)


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')
        

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
grado = input("Dime tu grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()