# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.74,'Ivan','Martinez','Ivan')

my_other_tuple = (30, 40, 50)

print(my_tuple)
print(type(my_tuple))

#Acceso a elementos
print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

#Cuenta cuantas veces sale este elemento en la tupla
print(my_tuple.count('Ivan'))

#Devuelve el indice del elemento (la primera ocurrencia)
print(my_tuple.index('Martinez'))

# La tupla a diferencia de las listas es inmutable

# my_tuple[1] = 1.80
# print(my_tuple)

# Concatenacion de tuplas

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas o rebanadas
print(my_sum_tuple[3:6])

# CASO MUY EXCLUSIVO!! Conversion de tupla a lista para insertar valores
# Si queremos insertar  valores o modificar valores que ya estan usaremos listas
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Ivnme17'
my_tuple.insert(1, 'Azul')
print(tuple(my_tuple))

# Borrado
#del my_tuple[2]  TypeError: 'tuple' object doesn't support item deletion
# Podemos borrar la tupla completa pero no un elemento de la tupla
# OJO!! aunque las tuplas no se puedan modificar, podemos borrar la tupla completa ya que es una variable
del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined