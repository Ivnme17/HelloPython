# Manejo de ficheros

#.txt

# r (read) lee el archivo
file = open("files/my_file.txt", "r")
print(file.read())
print(file.read(4)) # lee 4 caracteres se pueden poner tantos caracteres como tengamos en el archivo (x caracteres)
print(file.readline()) # lee una linea
print(file.readlines()) # lee todas las lineas
file.close()

# w (write) sobrescribe el archivo
file = open("files/my_file.txt", "w")
file.write("Mi nombre es Ivan\nMi apellido es Martinez\nTengo 22 años\nEstoy aprendiendo Python")
file.close()

# r+ (read and write) lee y escribe el archivo (tambien se puede hacer w+)
file = open("files/my_file.txt", "r+")
print(file.read())
file.close()

# a (append) agrega al archivo (tambien se puede hacer a+)
file = open("files/my_file.txt", "a")
file.write("\nY estoy muy feliz de aprender Python")
file.close()

# Leer el archivo completo
print("Contenido completo:")
file = open("files/my_file.txt", "r")
for line in file.readlines():
    print(line)
file.close()

# Sobrescribir el archivo
'''file = open("files/my_file.txt", "w")
file.write("\nMe gusta programar")
file.close()'''


# Eliminar archivo
'''import os
os.remove("files/my_file.txt")'''


#.json file
import json

json_file = open("files/my_file.json", "w+")

json_test = {
    "Name":"Ivan", 
    "Surname":"Martinez", 
    "Age":22, 
    "Lenguages":["Python", "Java", "C++"],
    "Website":"https://portfolio-profesional-ivan.vercel.app/"
    }

# Escribir en el archivo JSON con indentación de 4 espacios
json.dump(json_test, json_file, indent = 4)

json_file.close()

with open("files/my_file.json", "r") as json_file:
    for line in json_file.readlines():
        print(line)


json_dict = json.load(open("files/my_file.json"))  
print(json_dict)
print(type(json_dict))
print(json_dict["Name"])


#.csv file

import csv

csv_file = open("files/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Surname", "Age", "Lenguages", "Website"])
csv_writer.writerow(["Ivan", "Martinez", 22, ["Python", "Java", "C++"], "https://portfolio-profesional-ivan.vercel.app/"])

csv_file.close()

with open("files/my_file.csv", "r") as csv_file:
    for line in csv_file.readlines():
        print(line) 

#.xlsx file

#import xlrd Debe instalarse el modulo
#.xml file

import xml

xml_file = open("files/my_file.xml", "w+")
xml_file.write("<root><name>Ivan</name><surname>Martinez</surname><age>22</age><lenguages>Python, Java, C++</lenguages><website>https://portfolio-profesional-ivan.vercel.app/</website></root>")
xml_file.close()

with open("files/my_file.xml", "r") as xml_file:
    for line in xml_file.readlines():
        print(line)

