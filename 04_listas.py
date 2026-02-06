# Listas
# Dos maneras de inicializar una lista
my_list= list()
my_other_list = []

print(len(my_list))

my_list = [35, 22, 35, 22, 12, 12, 31, 10, 13, 5, 6, 25]

print(my_list)

print(len(my_list))

my_other_list = [22, 1.74, 'Ivan', 'Martinez']
print(my_other_list)

# tipo de datos de la lista <class 'list'>
print(type(my_other_list))

# tipo de datos de la primera posicion de la lista 
print(type(my_other_list[0]))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

# IndexError

#print(my_other_list[4])

#print(my_other_list[-5])

# .count() cuenta cuantas veces aparece un elemento (valor)
print(my_other_list.count('Ivan'))

# Desempaquetado de variables 
age, height, name, surname = my_other_list
print(name)

# Complicarse la vida
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]

print(age)

# Concatenar listas
print(my_list + my_other_list)

# print(my_list - my_other_list) No se puede restar listas

#Insertar elementos
my_other_list.append('Ivnme17')
print(my_other_list)

'''Insertar en una posicion especifica 
(el elemento que estaba en esa posicion 
y siguientes se desplazan a la derecha)
'''

my_other_list.insert(1, 'Rojo')
print(my_other_list)

'''
Remove elimina la primera ocurrencia del elemento especificado
osea si hay multiples ocurrencias solo elimina una
la primera que encuentra
'''

my_list.remove(35)
print(my_list)


'''
Pop elimina el ultimo elemento de la lista
y devuelve el elemento eliminado
'''

print(my_list.pop())
print(my_list)

#Podemos especificar el indice del elemento a eliminar
print(my_list.pop(2))
print(my_list)


#Eliminar elemento por indice
del my_list[1]
print(my_list)

#Usamos copy() para copiar la lista
my_new_list = my_list.copy()

#Eliminar todos los elementos
my_list.clear()

print(my_list)
print(my_new_list)

'''
Reverse() reversa el orden de la lista
Primero hay que llamar a la funcion reverse()
y luego imprimir la lista

No podemos imprimir directamente la funcion reverse()

print(my_new_list.reverse())

OJO!! Si hacemos esto devolvera None
'''

my_new_list.reverse()
print(my_new_list)

#Ordenamos la lista (por defecto de menor a mayor)
my_new_list.sort()
print(my_new_list)

#Modificar elemento por indice
my_other_list[1] = 'Verde'
print(my_other_list)


#Ejemplo de tipado dinamico
my_list='Hola python'
print(my_list)
print(type(my_list))

my_list=['Hola python']
print(my_list)
print(type(my_list))