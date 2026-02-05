# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n con escapado"
print(my_scape_string)

#Formateo

name, surname, age = 'Ivan', 'Martinez', 22

#Formateo + seguro
print('Mi nombre es %s %s y mi edad es %d ' % (name, surname, age))

#Formateo se le puede pasar cualquier tipo de datos
print('Mi nombre es {} {} y mi edad es {} ' .format(name, surname, age))

#Formateo rapido y limpio
print(f'Mi nombre es {name} {surname} y mi edad es {age} ')

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)

# Division

language_slice = language[1:3]
print(language_slice) 

language_slice = language[1:]
print(language_slice) 

language_slice = language[0:6:2]
print(language_slice) 

language_slice = language[-2]
print(language_slice) 

# Reverse

reverse_language = language[::-1]
print(reverse_language)


# Funciones
lenguaje = 'python'
print(len(lenguaje))

print(lenguaje.capitalize())

print(lenguaje.upper())

print(lenguaje.lower())

print(lenguaje.count('t'))

print(lenguaje.isnumeric())

print('1'.isnumeric())

print(lenguaje.upper().isupper())

print(lenguaje.lower().isupper())

print(lenguaje.lower().islower())

print(lenguaje.startswith('py'))
