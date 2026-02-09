# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario debido a la sintaxis

my_other_set = {"Ivan", "Martinez", 22}

print(type(my_other_set)) 

print(len(my_other_set))

my_other_set.add('Ivnme17')
print(my_other_set) # Los sets no son estructuras ordenadas

my_other_set.add('Ivnme17')
print(my_other_set) # Los sets no admiten repetidos

# Los sets ordenan de forma aleatoria debido al hash

''' 
¿Qué es un hash?
El hash es una función que convierte una cadena de caracteres en un número entero
El hash es utilizado para optimizar la búsqueda de elementos en un set
'''
# Verificar si un elemento existe en el set
print('Ivan' in my_other_set)
print('Iban' in my_other_set)


# Eliminar un elemento del set
my_other_set.remove('Ivan')
print(my_other_set)

# Limpiar el set
my_other_set.clear()
print(my_other_set)

print(len(my_other_set))

# Eliminar el set
del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined

# Convertir set a lista (no es recomendable debido a que los sets no son ordenados)
my_set = {'Ivan', 'Martinez', 22}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"JavaScript", "Python", "PHP"}

my_new_set = my_set.union(my_other_set)
# No admite valores duplicados!!
print(my_new_set.union(my_set))

# Union con otros sets
print(type(my_other_set)) # Inicialmente es un diccionario
print(my_new_set.union(my_new_set).union(my_set).union({'Java','SQL','C++'}))

# Diferencia
print(my_new_set.difference(my_set))
