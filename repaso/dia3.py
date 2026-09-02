# Clases   
# Importamos el archivo de clases para poder usar la clase Calculadora
from clases import *
# Podemos usar * si queremos importar todas las clases del archivo, 
# o podemos importar solo la clase que queremos usar, por ejemplo: 
# from clases import Calculadora

# Inicializamos la clase Calculadora y creamos un objeto de la clase Calculadora
calculadoraSimple = Calculadora() 

# Agregamos una cantidad al numero actual de la calculadora
calculadoraSimple.agregarCantidad(2)
# Mostramos el numero actual de la calculadora
print(calculadoraSimple.getCantidad()) 

# Manejo de errores y excepciones
# La variable1 es un string
var1 = '1' 
# Intentamos sumar 1 a la variable1, pero como es un string, lanzara una excepcion
try: var1 = var1 + 1
# Para evitar la linea de error, podemos capturar la excepcion y mostrar un mensaje de error
except: print(var1, " is not a number") 
print(var1)

# Tratar de manejar errores de manera mas elegante
# Para arreglar el error, podemos convertir la variable1 a un numero entero antes de sumarle 1
var1 = '1' 
try:  var2 = var1 + 1 
except: var2 = int(var1) + 1 
print(var2)