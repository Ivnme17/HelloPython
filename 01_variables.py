# Variables

# Es un ejemplo no pondremos nombres tan largos a las variables
my_string_variable = "My String Variable"
print(my_string_variable)

int_variable = 6
print(int_variable)

float_variable = 6.6
print(float_variable)

boolean_variable = True
print(boolean_variable)

# Concatenación
print('--------------------------------------------------------')
print('Concatenación')
print('--------------------------------------------------------')

print("Este es el valor de: ", my_string_variable)
print("Vamos a contar hasta el seis: 1, 2, 3, 4, 5,",int_variable)

#Tambien podemos guardar estos datos en una variable
longitud_cadena = len(my_string_variable)
print("La longitud de la cadena es: ",longitud_cadena)

#Transformar variables
print('--------------------------------------------------------')
print('Transformar tipos de variables')
print('--------------------------------------------------------')

my_int_variable = 3
print(my_int_variable)
print(type(my_int_variable))

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_cadena_variable = "6"
print(my_cadena_variable)
print(type(my_cadena_variable))

my_cadena_to_int_variable = int(my_cadena_variable)
print(my_cadena_to_int_variable)
print(type(my_cadena_to_int_variable))

# Funciones del sistema
print('--------------------------------------------------------')
print('Funciones del sistema')
print('--------------------------------------------------------')
#Longitud de cadena funcionalidad que viene precargada en el sistema
print("La longitud de la cadena es: ",len(my_string_variable))



#Definir variables en una sola linea
#OJO! con abusar de esta sintaxis
nombre, apellido, edad  = 'Ivan', 'Martinez',22
print('Mi nombre es ',nombre, ', mi primer apellido es ', apellido, ' y tengo', edad, 'años')


# Uso de  sistema de input

nombre = input('Como te llamas: ')
edad = input('Cuantos años tienes? ')

# Sobreescribir variables 
''' 

En cuanto introducimos datos en el input al usar la misma variable que 
hemos usado anteriormente se sobreescribe/machaca el valor anterior.

'''
print(nombre)
print(edad)

#Forzar tipo de variable
address : str = "Mi direccion"

# Podemos seguir cambiando su valor 
# De lo que nos sirve ': type' es para obligar el uso de ese tipo de dato en esa variable
# Pero siempre se podria cambiar
address = 12

print(address)
print(type(address))