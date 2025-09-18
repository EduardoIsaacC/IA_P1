#Una lista guarda varios valores en una sola variable
mi_lista = [10, 20, 30, 40]
print(mi_lista)

#Se puede mezclar diferentes tipos de datos
lista_mixta = [1, "Hola", 3.14, True]
print(lista_mixta)

#Acceder a un elemento (se empieza desde 0)
print(mi_lista[0]) #primer elemento
print(mi_lista[2]) #tercer elemento

#Modificar un valor
mi_lista[1] = 99
print(mi_lista)

#Agregar valores
mi_lista.append(50)
print(mi_lista)

#Eliminar valores
mi_lista.remove(30)
print(mi_lista)

#Recorrer la lista con un for
for valor in mi_lista:
    print('valor:', valor)

#Funcion Len devuelve el tamaño
print("tamaño de la lista:", len(mi_lista))