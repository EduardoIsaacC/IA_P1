#Utilizacion de *args en las clases

class Pou:
    def __init__(self, *comidas):
        #*args guarda varios valores en una tupla
        self.comidas = comidas

    def mostrar_comidas(self):
        print("Lista de comidas:", self.comidas)

#Crear objeto con varios valores
Personaje1 = Pou("manzana", "pizza", "agua")
Personaje2 = Pou("pan")

#Mostrar
Personaje1.mostrar_comidas()
Personaje2.mostrar_comidas()

#Recorrer los valores
for comida in Personaje1.comidas:
    print("Pou tiene:", comida)