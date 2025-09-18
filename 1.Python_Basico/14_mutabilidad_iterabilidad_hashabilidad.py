#Las listas son mutables (se pueden cambiar)
mi_lista = [1, 2, 3]
print(mi_lista)
mi_lista[0] = 99
print("Lista modificada:", mi_lista)

#Las tuplas son inmutables (no se pueden cambiar)
mi_tupla = (1, 2, 3)
print(mi_tupla)
#mi_tupla[0] = 99 ->Da error

#Las cadenas (strings) tambien son inmutables
texto = "python"

#texto[0] = "p" da error
print(texto)

#Iterables: se pueden recorrer con un for
for letra in texto:
    print("letra:", letra)

for numero in mi_lista:
    print("numero:", numero)

#Hashables: se pueden usar como clave en un diccionario
mi_dic = { (1,2): "tupla", "clave": 123 }
print(mi_dic)

#Una lista no es hashable, da error si se usa como clave
#mi_dic = { [1.2] "Lista"} -> Da error