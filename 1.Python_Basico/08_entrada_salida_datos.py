#La funcion input pide datos al usuario y siempre devuelve texto (str)

nombre = input("Dime tu nombre: ")
print("Hola", nombre)

#Si se desea un numero, tendra que convertirlo
edad = int(input("CUantos años tienes: "))
print("Tu edad es:", edad)

#Se pueden pedir varios datos 
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))
suma = numero1 +numero2
print ("La suma es:", suma)

#Tambien se puede concatenar texto con +
color = input("Cual es tu color favorito: ")
print("Tu color favorito es " + color)