# List comprehension / compresion de listas

my_list= list()
my_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_comprehension_list = [i for i in my_list]
print(my_comprehension_list)

my_range = range(7)
print(my_range)

my_comprehension_list = [i for i in my_range]
print(my_comprehension_list)

#Lo mismo que arriba pero sin uso de variable
my_comprehension_list = [i for i in range(8)]
print(my_comprehension_list)

# Sumar 1 a cada elemento (salto la primera posicion)
my_comprehension_list = [i + 1 for i in range(8)]
print(my_comprehension_list)

# Sumar 2 a cada elemento (salto las dos primeras posiciones)
my_comprehension_list = [i + 2 for i in range(8)]
print(my_comprehension_list)

# Multiplicar por 2 cada elemento (pares)
my_comprehension_list = [i * 2 for i in range(8)]
print(my_comprehension_list)


# Funcion suma 5
def sum_five(number):
    return number + 5


# Aplicar funcion a cada elemento
my_comprehension_list = [sum_five(i) for i in range(8)]
print(my_comprehension_list)