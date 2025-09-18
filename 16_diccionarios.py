#Un diccionario guarda pares clave:valor
mi_dic = {
    "nombre" : "Eduardo",
    "edad" : "21",
    "pais" : "México"
}
print(mi_dic)

#Acceder a un valor con la clave
print(mi_dic["nombre"])
print(mi_dic["edad"])

#Modificar un valor
mi_dic["edad"] = 30
print("edad modificada: ", mi_dic)

#Agregar un nuevo par
mi_dic["ciudad"] = "Guadalajara"
print("diccionario con ciudad:", mi_dic)

#Eliminar un par
del mi_dic["pais"]
print("diccionario sin pais:", mi_dic)

#Recorrer claves
for clave in mi_dic:
    print("clave:", clave)

#Recorrer valores
for valor in mi_dic.values():
    print("valor:" , valor)

#Recorrer claves y valores
for clave, valor in mi_dic.items():
    print(clave, ":", valor)

#Tamaño del diccionario
print ("tamaño del diccionario:", len(mi_dic))