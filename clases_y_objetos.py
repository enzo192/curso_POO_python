
# #Forma erronea no es optimo ni posible para crear programas


# celular1_marca = "samsung"
# celular2_marca = "apple"
# celular3_marca = "huawey"

# celular1_modelo = "S23"
# celular2_modelo = "Iphone 15 pro"
# celular3_modelo = "P20 pro"

# celular1_camaraT = "48MP"
# celular2_camaraT = "48MP"
# celular3_camaraT = "12MP"

# celular1_camaraF = "24MP"
# celular2_camaraF = "24MP"
# celular3_camaraF = "8MP"


# # tampoco es optimo


# celulares = []

# celulares[0] = ["samsung","s23","24mp","12mp"]
# #------------------------------------------------------------


#CLASES Y OBJETOS #1


'''
#para definir las clases se usa PascalCase
class Celular():
    #atributos estaticos
    marca = "Samsung"
    modelo = "S23"
    camara = "48mpx"

#intanciar un objeto = intancia de clase = objeto  
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()
print(celular1.marca)

'''


#CLASES Y OBJETOS #2

#esta clase es para crear un objeto. En este caso un celular.
class Celular:
    #constructor se ejecuta siempre 
    def __init__(self, marca, modelo, camara):
        #definir propiedades
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

#vamos a crear el objeto celular1 con la clase "funcion" Celular(), le pasamos los valores de las propiedades 
celular1 = Celular("Samsung","S23","48Mpx")
#otro celular con otras propiedades
celular2 = Celular("Apple","Iphone 15 pro","48Mpx")

print(celular2.marca)
