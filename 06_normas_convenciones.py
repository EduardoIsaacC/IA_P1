#Los nombres no pueden empezar con numero
#!variable =10 -> Da error

Variable = 20 #asi si funciona

#No se puede usar -
#mi-variable = 20 -> Da error

mi_variable = 20 #Si funciona 
print(mi_variable)

#No se puede usar espacios en el nombre
#mi variable = 30 -> Da error

mi_variable2 = 30 #Es correcto
print(mi_variable2)

#Se puede usar mayusculas y minusculas, son diferentes caracteres
edad = 22
EDAD = 30
print (edad, EDAD) #Son 2 variables distintas

#No se pueden usar palabras reservadas
#for = 10 -> Da error
#class = 20 -> Da error

#Convenciones de nombres
mi_variable = "camelCase"  #Se usa poco en Python
mi_variable_larga = "snake_case"    # es la mas comun en python
MI_CONSTANTE = 3.14 #las constantes se escriben en mayusculas
print (mi_variable, mi_variable_larga, MI_CONSTANTE)