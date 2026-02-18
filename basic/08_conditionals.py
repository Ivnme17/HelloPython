# Conditionals

my_condition = True

# if
if my_condition:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

# Comparacion
if my_condition == True:
    print("La condición es verdadera")

# is - verifica la identidad del objeto
if my_condition is True:
    print("La condición es verdadera")

# Distinto
if my_condition != True:
    print("La condición es falsa")

# not
if not my_condition:
    print("La condición es falsa")

# or
if my_condition == True or my_condition == False:
    print("La condición es verdadera")

# and
if 5 > 2 and 5 < 10:
    print("5 es mayor que 2 y menor que 10")

# Mi condiciones es True y no es False
if my_condition is True and my_condition is not False:
    print("La condición es verdadera")

# Mi condicion es igual en valor y tipo a True y es igual en tipo a False
if my_condition == True and my_condition == False:
    print("La condición es verdadera")

# if else
if 5 < 2:
    print("5 es menor que 2")
else:
    print("5 no es menor que 2")

# if elif else
if 5 < 2:
    print("5 es menor que 2")
elif 5 == 2:
    print("5 es igual a 2")
else:
    print("5 no es menor que 2 y no es igual a 2")

# Cadena vacía
my_string = ""
if not my_string:
    print("La cadena está vacía")

# Cadena con valor
my_string = "Hola"
if my_string:
    print("La cadena no está vacía")

my_other_string = "Hola mundo"

# Comparar cadenas por contenido
if my_string == my_other_string:
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")

# Comparar cadenas por referencia
if my_string is my_other_string:
    print("Las cadenas son la misma referencia")
else:
    print("Las cadenas son referencias diferentes")


# Comparar cadenas por referencia (negación)
if my_string is not my_other_string:
    print("Las cadenas son referencias diferentes")
else:
    print("Las cadenas son la misma referencia")


# Comparar cadenas por contenido (orden lexicográfico)
# Orden alfabético (ASCII)
if my_string > my_other_string:
    print("La cadena 1 es mayor que la cadena 2")
else:
    print("La cadena 2 es mayor que la cadena 1")

# Comparar longitudes de cadenas
if len(my_string) > len(my_other_string):
    print("La cadena 1 es mayor que la cadena 2")
else:
    print("La cadena 2 es mayor que la cadena 1")

