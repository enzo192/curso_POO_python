#METODOS #3

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    #una funcion dentro de una clase es un metodo. Son para definir las acciones del objeto
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular("Samsung","S23","48Mpx")
celular2 = Celular("Apple","Iphone 15 pro","48Mpx")

celular2.llamar()#Estas haciendo un llamado desde un: Iphone 15 pro 