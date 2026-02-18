# Expresiones regulares

import re

# match - Busca al inicio de la cadena si coincide con el patrón (case insensitive con re.I)

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search - Busca en toda la cadena si coincide con el patrón

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall - Busca todas las coincidencias en toda la cadena

findall = re.findall("lección", my_string, re.I)
print(findall)

# split - Divide la cadena en partes usando el patrón como separador

print(re.split(":", my_string))

# sub - Reemplaza todas las coincidencias con el patrón

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patrones de expresiones regulares

# Para aprender y validar expresiones regulares: https://regex101.com

# Patrones básicos 
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

# Otra forma de buscar
pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

# Buscar números
pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

# Buscar dígitos
pattern = r"\d"
print(re.findall(pattern, my_string))

# Buscar no dígitos
pattern = r"\D"
print(re.findall(pattern, my_string))

# Buscar caracteres alfanuméricos
pattern = r"[l].*"
print(re.findall(pattern, my_string))

# Validar email
email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

# Validar email con dominio .mx
email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))