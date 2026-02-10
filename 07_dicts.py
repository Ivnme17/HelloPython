# Diccionarios/ Mapas

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Ivan", "Apellido":"Martinez", "Edad":22, 1:"Python"}

print(my_other_dict)

my_dict = {
    "Nombre":"Ivan",
    "Apellido":"Martinez",
    "Edad":22,
    "Lenguajes":{"Python", "JavaScript", "PHP"},
    1:1.74
}

print(my_dict)

print(len(my_other_dict))

# Longitud del diccionario
print(len(my_dict))

# Busqueda por clave
print(my_dict["Nombre"])

print(my_dict[1])

# Actualizar valor
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Agregar nuevo valor
my_dict["Calle"] = "Calle 123"
print(my_dict)

# Eliminar valor
del my_dict["Calle"]
print(my_dict)

# Busqueda por clave (retorna False si no existe)
print("Ivan" in my_dict)
print("Nombre" in my_dict)
print("Calle" in my_dict)

# Metodos del diccionario
print(my_dict.items()) # Retorna pares clave-valor
print(my_dict.keys()) # Retorna solo las claves
print(my_dict.values()) # Retorna solo los valores

# Convertir a lista y ver los valores
print(list(my_dict.values()))

# Crear nuevo diccionario con claves de otro diccionario, pero sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Ejemplo con lista
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

# Ejemplo con diccionario
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)


# Asignar valor a todas las claves
my_new_dict = dict.fromkeys(my_dict, "Ivan")
print(my_new_dict)


# Convertir a tupla
print(tuple(my_new_dict))

# Convertir a set
print(set(my_new_dict))

# Convertir a diccionario
print(dict.fromkeys(my_new_dict.values()))

# Rebuscando...
print(dict.fromkeys(list(my_new_dict.values())))
print(dict.fromkeys(list(my_new_dict.keys())))
print(dict.fromkeys(list(my_new_dict.keys())).keys())

# Limpiar diccionario
my_dict.clear()
print(my_dict)

# Copiar diccionario
my_dict = my_other_dict.copy()
print(my_dict)


# Eliminar todo el diccionario
del my_dict
# print(my_dict) # NameError: name 'my_dict' is not defined


