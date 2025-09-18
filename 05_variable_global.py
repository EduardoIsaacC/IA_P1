#La palabra "global" esta reservada en Python, por lo tanto no se puede utilizar
variable_global = 10 #De esta forma si se puede comentar

#Palabras reservadas en Python
#and, es un operador logico que evalua dos expresiones y devuelve TRUE si son verdaderas
#as, Se utiliza para asignar un alias a un modulo o recurso importado
#assert, comprueba si una expresion es verdadera, si no lo es, lanza una excepcion, generalmente utilizada para depuracion
#async, Declara una funcion como asincrona, lo que permite que su ejecucion no bloquee el hilo principal del programa
#await, pausa la ejecucion de una funcion asincrona hasta que una operacion asincrona previamente iniciada se complete
#break, interrumpe un bucle antes de que se complete, terminando la ejecucion de la estructura que lo contiene
#class, palabra clave que define una nueva clase
#continue, hace que el programa salte a la siguiente iteración de un bucle, omitiendo el resto del código en la iteración actual.
#def, se utiliza para declarar una nueva función, especificando su nombre, parámetros y el bloque de código que ejecutará.
#del, elimina objetos o sus referencias, como claves en un diccionario o variables, liberando así recursos.
#else, parte de una estructura condicional que ejecuta un bloque de código si las condiciones anteriores no se cumplen.
#finally,bloque de código que se ejecuta siempre al final de una estructura try-except, sin importar si hubo una excepción.
#for, inicia un bucle que itera sobre una secuencia, como una lista o un rango, ejecutando el código interno en cada iteración.
#global, declara una variable como global, permitiendo que se acceda y modifique fuera del alcance local de una función.
#elif, parte de una estructura condicional que permite evaluar múltiples condiciones si las anteriores no se cumplen.
#except, captura y maneja excepciones en un bloque try, permitiendo que el programa continúe sin interrumpirse.
#False, valor booleano que representa la falsedad lógica en Python.
#from, se usa para importar elementos específicos de un módulo, como funciones o clases, sin necesidad de importar todo el módulo.
#if, inicia una estructura condicional que evalúa una expresión, ejecutando el bloque de código correspondiente si es verdadera.
#import, incorpora módulos o bibliotecas externas en el código, habilitando el uso de sus funciones, clases u objetos.
#in, comprueba si un elemento está presente dentro de una secuencia, como una lista, tupla o cadena de caracteres.
#is, compara la identidad de dos objetos, verificando si son exactamente el mismo objeto en memoria.
#lambda, define funciones anónimas y de una sola línea, que pueden ser utilizadas en cualquier parte del código donde se necesite una función simple.
#nonlocal, permite modificar variables dentro de funciones anidadas que no pertenecen a la función local, pero tampoco son globales.
#None, representa la ausencia de valor o un valor nulo en Python.
#not, operador lógico de negación, que invierte el valor de una expresión booleana.
#or, operador lógico que evalúa dos expresiones y devuelve True si al menos una de ellas es verdadera.
#pass, permite dejar bloques de código vacíos sin generar errores, útil como marcador de posición en funciones o bucles.
#raise, genera una excepción manualmente, permitiendo que el programador indique situaciones de error específicas.
#return, finaliza la ejecución de una función y devuelve un valor al llamador de la función.
#True, valor booleano que representa la verdad lógica en Python.
#try, bloque de código que intenta ejecutar operaciones que podrían generar excepciones, permitiendo el manejo adecuado de errores.
#while, inicia un bucle que se ejecuta mientras una condición dada sea verdadera.
#with, palabra clave que facilita la gestión de recursos, como archivos, asegurando que se cierren o liberen adecuadamente después de su uso.
#yield, se utiliza dentro de funciones generadoras para devolver valores de manera pausada, permitiendo que se reanude su ejecución posteriormente.
import keyword
print(keyword.kwlist)