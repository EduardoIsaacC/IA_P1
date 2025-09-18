#Definir una funcion simple
def saludar():
    print("Hola dede una funcion")

#Llamar a la funcion
saludar()

#Funcion con parametros
def sumar(a, b):
    resultado = a + b
    print("La suma es:" , resultado)

sumar(5, 3)
sumar (10, 20)

#Funcion que devuelve un valor con return
def multiplicar(x, y):
    return x * y

producto = multiplicar(4, 6)
print("El producto es:", producto)

#Funcion con valor por defecto
def saludar_persona(nombre = "invitado"):
    print("Hola", nombre)

saludar_persona("Eduardo")
saludar_persona()

#Orden de los argumentos
def saludar(nombre, edad):
    print(f"¡Muy buenas, {nombre}!")
    print(f"Usted tiene {edad} años.")

saludar("Eduardo", 21)