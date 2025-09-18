#Atributos obligatorios en clases con Python

class Pou:
    def __init__(self, nombre, comida):
        #Atributos necesarios para crear el objeto
        self.nombre = nombre
        self.comida = comida

    def mostrar_info(self):
        print("Nombre: ", self.nombre, "Comida:", self.comida)
        
#Crear objetos (hay que pasar los atributos, si no marca error)
Personaje1 = Pou("Pou1", 100)
Personaje2 = Pou("Pou2", 50)

#Mostrar info
Personaje1.mostrar_info()
Personaje2.mostrar_info()

#Si intento crear un objeto sin dar los atributos, da error
#personaje3 = Pou() --> Da error por que no se señalizo el nombre, ni la comida