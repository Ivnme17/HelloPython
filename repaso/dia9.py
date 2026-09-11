# Repaso mates simple
notas = [6, 8, 7, 6, 9, 5, 6, 10, 7, 8]

# 1. Media, mediana y moda

# A mano: calcula las tres.
# En Python: calcula la media con sum()/len(), 
# la mediana ordenando la lista con sorted() y 
# cogiendo el valor central (ojo con el caso de longitud par), 
# y la moda contando frecuencias con un diccionario (como el ejercicio de "contar colores" que ya hiciste)\\

def media_lista(lista_numeros):
    resultado = 0
    resultado = sum(lista_numeros) / len(lista_numeros)

    return resultado


print(f"La media es {media_lista(notas)}")

notas = [6, 8, 7, 6, 9, 5, 6, 10, 7, 8]


def mediana_lista_MAL(lista_numeros):
    resultado = 0
    lista_numeros = sorted(lista_numeros)
    # Debo de recorrer la lista y obtener el valor en medio
    resultado = (lista_numeros[lista_numeros[len(lista_numeros)//2]-2]+lista_numeros[lista_numeros[len(lista_numeros)-3]//2]) / 2
    
    return resultado
# notas = sorted(notas)
# print(notas)
# print(notas[notas[len(notas)//2]-2], notas[notas[len(notas)//2]-3])


notas = [6, 8, 7, 6, 9, 5, 6, 10, 7, 8]
moda = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0}

# SOLUCION REAL Y EFECTIVA NO SALE DE LOS LIMITES
def mediana_lista(lista_numeros):
    lista_numeros = sorted(lista_numeros)
    n = len(lista_numeros)
    mitad = n // 2
    
    if n % 2 == 0:
        resultado = (lista_numeros[mitad - 1] + lista_numeros[mitad]) / 2
    else:
        resultado = lista_numeros[mitad]
    
    return resultado

print("La mediana es:", mediana_lista(notas))

for nota in notas:
        match nota:
            case 1: moda[str(nota)] += 1
            case 2: moda[str(nota)] += 1
            case 3: moda[str(nota)] += 1
            case 4: moda[str(nota)] += 1
            case 5: moda[str(nota)] += 1
            case 6: moda[str(nota)] += 1
            case 7: moda[str(nota)] += 1
            case 8: moda[str(nota)] += 1
            case 9: moda[str(nota)] += 1
            case 10:moda[str(nota)] += 1

    # Generar otro diccionario con los numeros que se repiten siendo eso sus  claves y el valor la frecuencia

# FATAL USAR EL MATCH CASE ASI, ESTAMOS HARDCODEANDO CODIGO

#SOLUCION
frecuencias = {}
for nota in notas:
    frecuencias[nota] = frecuencias.get(nota, 0) + 1

print(frecuencias)  # {6: 3, 8: 2, 7: 2, 9: 1, 5: 1, 10: 1}

frecuencia_maxima = max(frecuencias.values())
# Hacemos uso de list comprehension
moda = [nota for nota, frecuencia in frecuencias.items() if frecuencia == frecuencia_maxima]

print("La moda es:", moda)  # [6]

# Ejercicio 2 Varianza y desviacion tipica
notas = [6, 8, 7, 6, 9, 5, 6, 10, 7, 8]
media =  sum(notas) / len(notas)

varianza = sum((nota - media) ** 2 for nota in notas) / len(notas)
desviacion = varianza ** 0.5

print("Varianza:", varianza)
print("Desviación típica:", desviacion)

