class Pou:
    def __init__(self, nombre, comida):
        self.nombre = nombre
        self.comida = comida

    def Alimentar(self):
        print(self.nombre, "Necesita alimento")

#crear objetos
Personaje1 = Pou("Pou1", 100)
Personaje2 = Pou("Pou2", 50)

#mostrar atributos
print("Nombre: ", Personaje1.nombre, "Comida: ", Personaje1.comida)
print("Nombre: ", Personaje2.nombre, "Comida: ", Personaje2.comida)

#cambiar valores
Personaje1.comida = 0
print("Comida acutal de", Personaje1.nombre, ":", Personaje1.comida)

#Usar metodo
if Personaje1.comida == 0:
    Personaje1.Alimentar()