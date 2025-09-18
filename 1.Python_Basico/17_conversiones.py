#De numero a cadena
numero = 123
texto =str(numero)
print("numero convertido a texto:", texto) #Aunque se vea en el resultado un nunmero, directamente cambio su forma a texto

#De cadena a numero
texto_num = "456" 
num = int(texto_num)
print("texto convertido a numero", num)

#De cadena a flotante
texto_flot = 3.14
num_flot = float(texto_flot)
print("texto convertido a flotante", num_flot)

#De numero a flotante
entero = 10
flotante = float(entero)
print("entero a flotante:", flotante)

#De flotante a entero
flotante2 = 9.99
entero2 = int (flotante2)
print("flotante a entero:", entero2)

#De booleano a entero
print(int(True)) #1
print(int(False)) #0

#De entero a booleano
print(bool(0)) #False
print(bool(5)) #True