#la abstraccion es quitar toda la complejidad de la logica y solo darle lo que necesita el usuario o el dev para que funcione el programa.
#ocultando la logica

class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
        
mi_auto = Auto()

mi_auto.conducir()