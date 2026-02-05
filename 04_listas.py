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

#Ejemplo de tipado dinamico
my_list='Hola python'
print(my_list)
print(type(my_list))

my_list=['Hola python']
print(my_list)
print(type(my_list))