#Una cadena se puede escribir con comillas dobles o simples
texto1 = "Hola mundo"
texto2 = 'Hola maestro'
print (texto1, texto2)

#Se pueden concatenar cadenas con +
saludo = "Hola" + "amigos"
print (saludo)

#Tambien se pueden multiplicar
eco = "hey!" * 3
print(eco)

#Los strings son como listas de caracteres
frase = "python"
print(frase[0]) #muestra la letra p
print(frase[2]) #muestra la letra t

#Se pueden recorrer con for 
for letra in frase:
    print(letra)

#Funcion Len devuelve el tamaño
print("El tamaño de la frase es:", len(frase))