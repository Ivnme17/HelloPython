from clases import *

# Ejercicio 1 
# Calcula el área y perímetro de un rectángulo
base = 8
altura = 5

area = base * altura

perimetro = 2 * (base + altura)

print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)

# Ejercicio 2

def es_par(numero):
    # devuelve True si es par, False si no
    return numero % 2 == 0

print(es_par(7))  # False
print(es_par(10)) # True

# Ejercicio 3

numeros = [3, 7, 1, 9, 4, 2]
# imprime solo los números mayores que 4
for numeroMayor4 in numeros:
    if numeroMayor4 > 4:
        print(numeroMayor4) # Resultado: 7, 9

# Ejercicio 4

alumno = {"nombre": "Ivan", "nota": 8.5}
# añade la clave "aprobado" con True o False según la nota
if alumno["nota"] >= 5:
    alumno["aprobado"] = True
else:
    alumno["aprobado"] = False
print(alumno)

# Ejercicio 5
# agregar el metodo frenar() a la clase Coche que reste 10 a la velocidad
mi_coche = Coche("Seat", 120)
mi_coche.frenar()
print("La velocidad del coche es: ", mi_coche.velocidad)
# Ejercicio 6
# Excepciones
def dividir(a, b):
    # maneja el caso de división por cero con try/except
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero"

print(dividir(10, 0)) # Resultado: Error: División por cero

# Ejercicio avanzado 1
# Crea una lista solo con los nombres de los aprobados (nota >= 5)
# usando list comprehension
# Las list comprehensions son una forma concisa de crear listas a partir de otras listas o iterables.

alumnos = [
    {"nombre": "Ana", "nota": 9},
    {"nombre": "Luis", "nota": 4},
    {"nombre": "Marta", "nota": 6.5},
    {"nombre": "Pedro", "nota": 3}
]
# [ EXPRESION   for VARIABLE in ITERABLE   if CONDICION ]
# EXPRESION
aprobados = [alumno["nombre"]
# for VARIABLE in ITERABLE
for alumno in alumnos 
# if CONDICION
if alumno["nota"] >= 5]
resultado = "Los alumnos aprobados son: " + ", ".join(aprobados)
print(resultado)

'''
OTRA VERSION

aprobados = []
for alumno in alumnos:
    if alumno["nota"] >= 5:
        aprobados.append(alumno["nombre"])
'''

# Ejercicio 2 avanzado Clases con herencia

p = Programador("Ivan", 1800, "Python")
print(p.info())  # Ivan gana 1800€ (Python)