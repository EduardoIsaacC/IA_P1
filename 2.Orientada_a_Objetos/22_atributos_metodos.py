class Pou:
    Comida = 100

    def Alimentar(self):
        print('Alimentalo')


Personaje = Pou()

print("Alimento que debe de tener:", Personaje.Comida)

Personaje.Comida = 0

print("Alimento actual de Pou:", Personaje.Comida)

if Personaje.Comida == 0:
    Personaje.Alimentar()