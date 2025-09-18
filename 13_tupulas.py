#Una tupla es como una lista pero no se puede modificar
mi_tupla = (10, 20, 30, 40)
print(mi_tupla)

#Tambien se pueden mezclar datos
tupla_mixta = (1, "hola", 3.14, False)
print(tupla_mixta)

#Acceder a un elemento
print(mi_tupla[0]) #primer valor
print (mi_tupla[2]) #tercer valor

#No se puede cambiar un valor (esto da error)
#mi_tupula[1] = 99

#Recorrer la tupla
for valor in mi_tupla:
    print("valor:" , valor)

#Funcion Len devuelve el tamaño
print("tamaño de la tupla: ", len(mi_tupla))

#Se pueden crear tuplas de un solo valor (poner coma)
tupla_uno = (5,)
print(tupla_uno)