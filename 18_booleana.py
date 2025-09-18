#Operadores de comparacion
print (5 == 5) #igualdad -> TRUE
print (5 != 3) #diferente -> TRUE
print (10 > 3) #mayor que -> TRUE
print (2 < 8) #menor que -> TRUE
print (5 >= 5) #mayor o igual -> TRUE
print (4 <= 6) #menor o igual -> TRUE

#Operadores logicos
print (True and True) #True
print (True and False) #False
print (True or False) #True
print (not True)    #False

#Comvinando expresiones
edad = 20
print (edad > 18 and edad < 30) #True si edad esta entre 18 y 30
print (edad < 18 or edad > 65) #True si edad es menor a 18 o mayor a 65
print (not (edad == 20))    #False por que edad si es 20