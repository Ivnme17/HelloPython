print("Mi primer mensaje en python")
print("Mas facil de lo que pensaba")

a = "0"
b = "2"
c= "3"
d= 4

print(a + b)

print(int(c) + d)

# int(variable)– lanza variable a entero
# str(variable)– lanza variable a cadena de texto
# float(variable)– lanza variable a flotante (número con decimal)

print (3 + 4) 
print (3 - 4) 
print (3 * 4) 
print (3 / 4) 
print (3 % 2) 

print (3 ** 4) 
# 3 to the fourth power (potencia) 

print (3 // 4) 
#floor division (redondea hacia abajo)

a = 0 
a += 2 
print (a) #Resultado: 2

a = "0"
a += "2"
print (a) #Resultado: 02

a = 3 
a += 2 
print (a) #Resultado: 5

a = "3"
a += "2"
print (a) #Resultado: 32

# Comentario de una linea

''' Comentario de bloques'''

''' print("We are in a comment") print ("We are still in a comment") ''' 
print("We are out of the comment")

#Funciones en python

#Definicion de una funcion
def saludar():
    print("Hola, bienvenido a python")

#LLamada a la funcion
saludar()

def sumar(a, b):
    return print(a + b)

sumar(3, 4) #Resultado: 7

# Variable globarl
cadena = "Hola, soy una variable global"
def mostrar_variable_global():
    print(cadena)

num1 = 10
num2 = 5

if num1 > num2:
    print("num1 es mayor que num2")
elif num1 < num2:
    print("num1 es menor que num2")
else:
    print("num1 es igual a num2")

# Para la variable a se incrementara en 1 hasta que llegue a 3
for a in range(1,3): 
    print (a) # Resultado: 1, 2

a = 1 
while a <10: 
    print (a) 
    a+=1

    sampleList = [1,2,3,4,5,6,7,8] 
    print (sampleList[1]) # Resultado: 2

    sampleList = [1,2,3,4,5,6,7,8] 
    for a in sampleList: 
        print (a) # Resultado: 1, 2, 3, 4, 5, 6, 7, 8

    sampleList.append(9)

    for a in sampleList: 
        print (a) # Resultado: 1, 2, 3, 4, 5, 6, 7, 8, 9

    lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

    sampleList.count(1) # Resultado: 2

    sampleList.index(1) # Resultado: 0

    sampleList.insert(1, 10) # Inserta el valor 10 en la posicion 1

    sampleList.remove(1) # Elimina el primer elemento que encuentre con el valor 1

    sampleList.pop() # Elimina el ultimo elemento de la lista

    sampleList.reverse() # Invierte el orden de los elementos en la lista

    sampleList.sort() # Ordena los elementos de la lista de menor a mayor