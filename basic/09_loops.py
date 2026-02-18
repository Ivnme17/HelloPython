# Bucles

# While
i = 0
while i < 10:
    print(i)
    i += 1

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

my_condition = 0
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if(my_condition == 15):
        print("Es 15")
else: # Es opcional
    print("Mi condición es mayor o igual que 20")

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

print('------------------')
print("Lista:")
print('------------------')

for element in my_list:
    print(element)


my_tuple = (22, 1.74,'Ivan','Martinez','Ivan')

print('------------------')
print("Tupla:")
print('------------------')

for element in my_tuple:
    print(element)


my_set = {"Ivan", "Martinez", 22}

print('------------------')
print("Set:")
print('------------------')

for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Ivan",
    "Apellido":"Martinez",
    "Edad":22,
    "Lenguajes":{"Python", "JavaScript", "PHP"},
    1:1.74
}

print('------------------')
print("Diccionario:")
print('------------------')

for element in my_dict:
    print(element)
else:
    print("El bucle for para diccionario ha finalizado")

# No soy muuy fan de usar break y continue en bucles for, pero se puede
# Suelo usar break en switchs o menús

# Ejemplo de break en for
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

# Ejemplo de continue en for
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

