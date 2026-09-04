# REPASO IA Y BIG DATA

# Ejercicio 1 Normalización de datos (paso típico antes de entrenar un modelo)

valores = [10, 20, 30, 40, 50]

# Normaliza cada valor entre 0 y 1 usando la fórmula:
# (valor - minimo) / (maximo - minimo)
# Guarda el resultado en una nueva lista "valores_normalizados"
valores_normalizados = []
minimo = min(valores)
maximo = max(valores)

for valor in valores:
    valor_normalizado = (valor - minimo) / (maximo - minimo)
    valores_normalizados.append(valor_normalizado)

print(f"Valores normalizados: {valores_normalizados}") # Valores normalizados: [0.0, 0.25, 0.5, 0.75, 1.0]

# Ejercicio 2: Contar frecuencias (como un mini value_counts de Pandas)

colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
frecuencias_colores = {"rojo": 0, "azul": 0, "verde": 0}

for color in colores:
    if color in frecuencias_colores:
        frecuencias_colores[color] += 1 # Si el color ya está en el diccionario, incrementa su contador
    else:
        frecuencias_colores[color] = 1 # Si el color no está en el diccionario, inicializa su contador a 1

print(f"Frecuencias de colores: {frecuencias_colores}") # Frecuencias de colores: {'rojo': 3, 'azul': 2, 'verde': 1}
# Cuenta cuántas veces aparece cada color
# y guárdalo en un diccionario, ej: {"rojo": 3, "azul": 2, "verde": 1}

# Ejercicio 3: Limpieza de datos (quitar valores nulos/erróneos)

datos = [23, None, 45, "N/A", 12, None, 67]

# Crea una nueva lista solo con los valores numéricos válidos
# (descarta None y "N/A")
datos_limpios = []
for dato in datos:
    if isinstance(dato, (int, float)): # Verifica si el dato es un número
        datos_limpios.append(dato)

print(f"Datos limpios: {datos_limpios}") # Datos limpios: [23, 45, 12, 67]

datosCadena = ["23", "45", "N/A", "12", "67"]
datosLimpiosCadena = []
for dato in datosCadena:
    if dato.isdigit(): # Verifica si el dato es un número en forma de cadena
        datosLimpiosCadena.append(int(dato)) # Convierte a int y agrega a la lista
print(f"Datos limpios de cadena: {datosLimpiosCadena}") # Datos limpios de cadena: [23, 45, 12, 67]


# Con list comprehension, podemos hacer lo mismo en una sola línea
for dato in datosCadena: datosLimpiosCadena = [int(dato) for dato in datosCadena if dato.isdigit()]
print(f"Datos limpios de cadena (list comprehension): {datosLimpiosCadena}") # Datos limpios de cadena (list comprehension): [23, 45, 12, 67]

#  Ejercicio 4 Separar datos en dos grupos (como un mini train/test split)

dataset = list(range(1, 21))  # 20 elementos

# Divide "dataset" en dos listas:
# - "entrenamiento" con el 80% de los datos
# - "prueba" con el 20% restante
# Pista: usa len() para calcular cuántos elementos son el 80%
# los dos puntos se usan para hacer slicing de listas, ej: lista[inicio:fin]
# si estan delante de los dos puntos, significa "desde el inicio hasta fin-1"
# si estan detrás de los dos puntos, significa "desde inicio hasta el final"
entrenamiento = dataset[:int(len(dataset) * 0.8)] # Primer 80%

prueba = dataset[int(len(dataset) * 0.8):] # Último 20%

print(f"Datos de entrenamiento: {entrenamiento}") # Datos de entrenamiento: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(f"Datos de prueba: {prueba}") # Datos de prueba: [17, 18, 19, 20]

# EL SWITCH DE PYTHON (match-case) es una forma más elegante de hacer if-elif-else
dia = 3

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case _:  # el "_" es el equivalente al "default" del switch
        print("Día no válido")
        

# Match-case es de la version 3.10 de Python, si tu versión es anterior, usa if-elif-else
dia = 3

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
else:
    print("Día no válido")

# Ejercicio 5: match-case para calificaciones

nota = 7

# Usa match-case para imprimir:
# 9 o 10 -> "Sobresaliente"
# 7 u 8 -> "Notable"
# 5 o 6 -> "Aprobado"
# cualquier otro caso -> "Suspenso"
# Pista: en match-case puedes agrupar valores así: case 9 | 10:

match nota:
    case 9 | 10:
        print("Sobresaliente")
    case 7 | 8:
        print("Notable")
    case 5 | 6:
        print("Aprobado")
    case _: #default
        print("Suspenso")
        
# Diccionario de funciones — el truco más "pythonico" y el que de verdad imita a un switch
# Generamos las funciones que queremos usar en el diccionario
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b

# Dentro del diccionario, las claves son los nombres de las operaciones y los valores son las funciones
operaciones = {
    "sumar": sumar,
    "restar": restar,
    "multiplicar": multiplicar
}
# lambda a, b: a + b es una función anónima que hace lo mismo que sumar(a, b)
comando = "sumar"
resultado = operaciones.get(comando, lambda a, b: "Comando no reconocido")(3, 5)
# variable = diccionario.get(clave, valor_por_defecto)(argumentos)
print(resultado)  # 8

# Ejercicio para practicar la alternativa con diccionario

# Crea un diccionario "notas_texto" que traduzca:
# 9 o 10 -> "Sobresaliente"
# 7 u 8  -> "Notable"
# 5 o 6  -> "Aprobado"
# Cualquier nota fuera de esos rangos -> "Suspenso"
#
# Pista: como los diccionarios no soportan rangos como claves directamente,
# necesitas otra estrategia. Piensa en usar rangos o comprueba con un bucle
# sobre .items() del diccionario, o combina el diccionario con un poco de lógica.
notas_texto = {
    (9, 10): "Sobresaliente",
    (7, 8): "Notable",
    (5, 6): "Aprobado"
}

for nota in range(0, 11):  # Probamos con todas las notas del 0 al 10
    texto = "Suspenso"  # Valor por defecto
    for rango, descripcion in notas_texto.items():
        if nota in range(rango[0], rango[1] + 1):  # +1 porque el rango es inclusivo (Ejemplo: rango (9, 10) incluye 9 y 10)
            texto = descripcion
            break
    print(f"Nota: {nota}, Descripción: {texto}")

