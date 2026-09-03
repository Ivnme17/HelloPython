# Ejercicio 1
# Manejo de ficheros + excepciones
from clases import *

def leer_notas(ruta): 
    resultado = None
    # lee un fichero de texto con una nota por línea
    # devuelve la media, y si el fichero no existe, captura
    # la excepción y devuelve None en vez de petar
    try:
        # with-as es una forma de abrir un fichero y asegurarse de que se cierra 
        # automáticamente al salir del bloque
        with open(ruta, "r") as f:
            # List comprehension para leer las notas y convertirlas a float
            notas = [float(linea.strip()) for linea in f]
            media = sum(notas) / len(notas)
            resultado = media
            return resultado
    except FileNotFoundError:
        print("Error: El fichero no existe")
        return resultado
    except ValueError:
        print("Error: El fichero contiene datos no numéricos")
        return resultado

ficheroNotas = r"C:\Users\FX506\Documents\HelloPython\repaso\notas.txt"
print("Media de notas:", leer_notas(ficheroNotas))
#leer_notas(ficheroNotas)

inventario = {
    "frutas": {"manzana": 10, "pera": 5},
    "verduras": {"lechuga": 3, "tomate": 8}
}
# Ejercicio 2
# Diccionarios anidados + bucles
# recorre todo el inventario e imprime cada producto con su cantidad,
# y al final el total de unidades sumando todo
# .items() devuelve una lista de tuplas (clave, valor) para cada elemento del diccionario
# categoria(frutas, verduras), productos({manzana: 10, pera: 5}, {lechuga: 3, tomate: 8})
suma = 0
for categoria, productos in inventario.items():
    print(f"Categoría: {categoria}") # Categoría: frutas, Categoría: verduras
# producto(manzana, pera), producto(lechuga, tomate) cantidad(10, 5), cantidad(3, 8)
    for producto, cantidad in productos.items(): 
        print(f"Producto: {producto}, Cantidad: {cantidad}") 
        suma += cantidad
print(f"Total de unidades: {suma}") # Total de unidades: 26

# Ejercicio 3
# Función que devuelve función (closures) — un poco más avanzado
# La funcion superior crear_multiplicador devuelve una función que multiplica por el factor dado
# Es decir, una funcion que se lleva pegado el valor del factor y 
# lo usa para multiplicar el numero que le pasemos a la funcion interna multiplicar_por_factor
def crear_multiplicador(factor):
    # debe devolver una función que multiplique por "factor"
    def multiplicar_por_factor(numero):
        return numero * factor
    return multiplicar_por_factor

doble = crear_multiplicador(2)
print(doble)
print(type(doble))  
print(doble(5))  # 10

# si cantidad > saldo, lanza SaldoInsuficiente con un mensaje
# si no, devuelve saldo - cantidad
def retirar(saldo, cantidad):
    if(cantidad > saldo):
        # raise hace que se lance la excepcion
        raise SaldoInsuficiente("Saldo insuficiente para retirar la cantidad solicitada")
    else:
        return saldo - cantidad

print(retirar(100, 50)) # 50

# retirar(50, 100) # SaldoInsuficiente: Saldo insuficiente para retirar la cantidad solicitada

# Ejercicios de IA y BIG DATA

# 1. Estadística básica a mano (la base de todo en ML)
notas = [7.5, 8, 6, 9.5, 4, 7, 8.5]

# Calcula:
# - la media
# - el valor máximo y mínimo
# - cuántos valores hay por encima de la media
contadorNotas = 0
media = 0
maximo = 0
minimo = 0
for nota in notas:
    nota = float(nota) # convertimos a float por si acaso
    # Media de notas
    media = sum(notas) / len(notas)
    # Valor máximo y mínimo
    maximo = max(notas)
    minimo = min(notas)
    # Valores por encima de la media
    contadorNotas = sum(1 for nota in notas if nota > media)
print(f"Hay {contadorNotas} notas por encima de la media {media}")
print(f"Nota máxima: {maximo}, Nota mínima: {minimo}")    
