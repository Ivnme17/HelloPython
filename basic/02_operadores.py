# Operadores

#Operadores aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(int(10 / 2))
print(10 % 2)

# Division entera
print(10 // 3)

# Exponente
print(2 ** 3)


print(int(2 ** 3 + 3 - 7 / 1 // 4))


print("Hola " + "Python")
print("Hola" + str(5))
print("Hola" * 5)
print("Hola" * int(2.5 * 2))
print("Hola " * (2 ** 3))

#Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Operadores Comparativos con cadenas
#Compara la longitud de las cadenas 
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")#Orden alfabetico
#print("aaaa" >= "ABAA") Orden alfabetico tambien tiene encuenta mayusculas
print(len("aaaa") >= len("abaa"))#Longitud
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


#Operadores Logicos
# && // y !
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 > 4 or ("Hola" > "Python" and 4 == 4))

print(not(3 > 4))