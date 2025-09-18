#Estructura match

opcion = 2

match opcion:
    case 1:
        print("Elegiste la opcion 1")
    case 2:
        print("Elegiste la opcion 2")
    case 3:
        print("Elegiste la opcion 3")
    case _:
        print("Opcion no valida") #Poner "_" es como default

color = "rojo"

match color:
    case "azul":
        print("El color es azul")
    case "rojo":
        print("El color es rojo")
    case "verde":
        print("El color es verde")
    case _:
        print("Color desconocido")

#Condicional if
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

#If con else
numero = 5
if numero %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#If con elif
nota = 7
if nota >=9:
    print("Excelente")
elif nota >=6:
    print("Aprobado")
else:
    print("Reprobado")

#Bucle while
contador = 1
while contador <=5:
    print("contador:", contador)
    contador += 1

#Bucle for
for i in range(1, 6):
    print ("i vale:", i)