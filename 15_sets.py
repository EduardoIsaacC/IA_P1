#Un set es una coleccion desordenada y sin elementos repetidos
mi_set = {1, 2, 3, 4, 4, 2}
print(mi_set) #los repetidos se eliminan

#Se pueden mezclar tipos de datos
set_mixto = {1, "hola", 3.14, True}
print(set_mixto)

#Agregar elementos
mi_set.add(5)
print("despues de agregar:", mi_set)

#Eliminar elementos
mi_set.remove(2)
print("despues de eliminar:", mi_set)

#Recorrer un set
for valor in mi_set:
    print("valor:", valor)

#Tamaño del set
print("Tamaño del set:", len(mi_set))

#No se pueden acceder por indice
# print(mi_set[0]) -> Da error

#Un set vacio se crea con set()
set_vacio = set()
print(set_vacio)