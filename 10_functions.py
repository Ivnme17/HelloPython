# Funciones

def my_function ():
    print("Esto es una funcion")


my_function ()

# Parametros

def suma_dos_numeros (num1, num2):
    print(num1 + num2)

suma_dos_numeros (5, 7)# Suma dos numeros
suma_dos_numeros ("5", "7")# Suma dos cadenas (concatenación)
suma_dos_numeros (1.4, 2.5)# Suma dos decimales
suma_dos_numeros (True, False)# Suma dos booleanos (1 + 0)
suma_dos_numeros (True, True)# Suma dos booleanos (1 + 1)


# Parametros con return
def suma_dos (num1, num2):
    resultado = num1 + num2
    return resultado

''' 
También se puede hacer de esta manera:
def suma_dos (num1, num2): 
    return num1 + num2

my_resultado = suma_dos (5, 7)
print("El resultado es:", my_resultado)
'''


print("------------------")
print("El resultado es:", suma_dos(5, 7))
print("------------------")


def sum_two_values (num1: int, num2: int):
    if(type(num1) != int or type(num2) != int):
        print("No son enteros")
    else:
        print(num1 + num2)

sum_two_values (5, 7)
sum_two_values ("5", "7")


def mostrar_nombre (nombre: str, apellido: str):
    print(f"Mi nombre es {nombre} y mi apellido es {apellido}")

mostrar_nombre(nombre = "Ivan", apellido = "Martinez")
mostrar_nombre(apellido = "Martinez", nombre = "Ivan")
# mostrar_nombre(nombre = "Ivan") # Error esto no es valido ya que falta el parametro apellido

# Parametros con valor por defecto
def mostrar_nombre_por_defecto (nombre , apellido , alias = "Sin alias"):
    print(f"{nombre}, {apellido}, {alias}")

mostrar_nombre_por_defecto("Ivan", "Martinez")
mostrar_nombre_por_defecto("Ivan", "Martinez", "Ivnme17")

# Función con *param (parametros arbitrarios) todos los argumentos estan definidos por separado
def mostrar_textos_en_mayusculas (*textos):
    for texto in textos:
        print(texto.upper())

mostrar_textos_en_mayusculas("Hola", "adios", "buenas", "Python")

'''
----------------------------------
Funciones de ejemplo IA Y BIG DATA
----------------------------------
'''

