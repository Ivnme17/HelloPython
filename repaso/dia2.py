# tuplas

'''myList = [1,2,3] 
myList.append(4) 
print (myList) 
myTuple = (1,2,3) 
print (myTuple) 
myTuple2 = (1,2,3) 
# myTuple2.append(4)  # This would cause an error since tuples are immutable
print (myTuple2)
'''
miTupla = (1,2,3)
myLista = list(miTupla)
myLista.append(4) # type: ignore laza el Pylance error, pero no es un error de sintaxis
print(myLista) # Resultado: [1, 2, 3, 4]

# Diccionario

myExample = {'someItem': 2, 'otherItem': 20}
myExample['newItem'] = 30
for item in myExample:
    print("Clave %s: Valor: %d" % (item, myExample[item])) # Resultado: someItem 2, otherItem 20, newItem 30

myString = "" 
print (type(myString))

miString = "Hola, soy un string"
print(miString.count("o")) # Resultado: 2 Devuelve el numero de veces que aparece
print(miString.find("s")) # Resultado: 6 Devuelve el indice de la primera ocurrencia del caracter "s"
print(miString.lower()) # Resultado: hola, soy un string Devuelve el string en minusculas
print(miString.upper()) # Resultado: HOLA, SOY UN STRING Devuelve el string en mayusculas
print(miString.replace("Hola", "Adios")) # Resultado: Adios, soy un string Reemplaza la primera ocurrencia de "Hola" por "Adios"
print(miString.strip()) # Resultado: Elimina los espacios en blanco al inicio y al final del string

a = "string" 
print (a[1:3]) # Resultado devuelve tr el ultimo indice no se incluye
print (a[:-1]) # Resultado devuelve strin

# Formateo
# Float
print('The order total comes to %f' % 123.44) 
print('The order total comes to %.2f' % 123.444)

# Strings
a ="abcdefghijklmnopqrstuvwxyz" 
print('%.20s' % a)

f = open(r"C:\Users\FX506\Documents\HelloPython\repaso\fichero.txt", "r") #opens file with name of "fichero.txt"

print(f.read(1)) # Leemos un caracter
print(f.read()) # Leemos todo el contenido del fichero
''' 
Al haber leido el primer caracter del fichero, cuando lanzamos la instruccion read debajo
sigue desde donde habia leido, por lo que no se leera el primer caracter del fichero.
Seguira donde el puntero del fichero se quedo, que es en el segundo caracter.
'''

print(f.readline())  # Leemos la primera linea del fichero
print(f.readline()) # Leemos la segunda linea del fichero

# Hemos creado una lista vacia y vamos a ir añadiendo lineas del fichero a la lista
myList = [] 
for line in f:
    myList.append(line) 
print(myList)


f = open(r"C:\Users\FX506\Documents\HelloPython\repaso\fichero.txt", "w") # Escribimos en el fichero, si no existe lo crea, si existe lo sobreescribe

f.write("Hola, soy un fichero de texto\n")
f.write("Tal vez algún día, me promueva a un archivo real.\n")
f.write("Tío, anhelo ser un archivo de verdad\n")
f.write("Y pasar el rato con todos mis nuevos amigos de archivo real.\n")

f = open(r"C:\Users\FX506\Documents\HelloPython\repaso\fichero.txt", "a") # Abrimos el fichero en modo append, para añadir contenido al final del fichero
f.write("y puedo agregar unos pepinillos a eso")

f.close() # Cerramos el fichero