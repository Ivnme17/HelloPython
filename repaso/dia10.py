# Mas ejercicios de mates y estadistica

# 1. Rango

temperaturas = [18, 25, 30, 15, 22, 28]

# Calcula el rango a mano y en Python (max() y min()).

minimo_temperatura = min(temperaturas)
maximo_temperatura = max(temperaturas)

rango_temperatura = maximo_temperatura - minimo_temperatura

print("El rango es:", rango_temperatura)


# 2. Percentil (simplificado)

ingresos = [1200, 1500, 1800, 2000, 2200, 2500, 3000, 3200, 4000, 5000]

# Ordena los datos (ya lo están) y calcula el percentil 50 (que ya sabes hacer, es la mediana) y 
# luego el percentil 90 usando esta fórmula simplificada:
# Si la posición no es un número entero, redondea hacia abajo con int() para simplificar.

def mediana_lista(lista_numeros):
    lista_numeros = sorted(lista_numeros)
    n = len(lista_numeros)
    mitad = n // 2
    
    if n % 2 == 0:
        resultado = (lista_numeros[mitad - 1] + lista_numeros[mitad]) / 2
    else:
        resultado = lista_numeros[mitad]
    
    return resultado

print("La mediana (percentil 50) es:",mediana_lista(ingresos))


percentil_90_ingresos = 90 / 100 * (len(ingresos)-1)

print("El percentil 90 de ingresos es:", int(percentil_90_ingresos))

# 3. Covarianza y correlación

horas_estudio = [1, 2, 3, 4, 5]
notas_examen  = [4, 5, 6, 7, 9]

media_x = sum(horas_estudio) / len(horas_estudio)
media_y = sum(notas_examen) / len(notas_examen)

# Covarianza: para cada posición i, multiplicamos (x_i - media_x) por (y_i - media_y)
# zip() empareja elementos de dos (o más) listas según su posición
covarianza = sum((x - media_x) * (y - media_y) for x, y in zip(horas_estudio, notas_examen)) / len(horas_estudio)

# Necesitamos la varianza y desviación típica de cada lista por separado
varianza_x = sum((x - media_x) ** 2 for x in horas_estudio) / len(horas_estudio)
varianza_y = sum((y - media_y) ** 2 for y in notas_examen) / len(notas_examen)

desviacion_x = varianza_x ** 0.5
desviacion_y = varianza_y ** 0.5

correlacion = covarianza / (desviacion_x * desviacion_y)

print("Media horas:", media_x)
print("Media notas:", media_y)
print("Covarianza:", covarianza)
print("Desviación x:", desviacion_x)
print("Desviación y:", desviacion_y)
print("Correlación:", correlacion)

# 5. Teorema de Bayes
# Un test médico para detectar una enfermedad tiene estos datos:

# El 1% de la población tiene la enfermedad → P(enfermo) = 0.01
# Si tienes la enfermedad, el test da positivo el 90% de las veces → P(positivo | enfermo) = 0.9
# Si NO tienes la enfermedad, el test da positivo por error el 5% de las veces → P(positivo | sano) = 0.05

# Calcula P(enfermo | positivo): si el test te da positivo, ¿cuál es la probabilidad real de que estés enfermo?

# Pista: primero necesitas P(positivo) total, que se calcula sumando dos caminos posibles:

# P(positivo) = P(positivo|enfermo) × P(enfermo) + P(positivo|sano) × P(sano)

# (donde P(sano) = 1 - P(enfermo))
p_enfermo = 0.01
p_sano = 1 - p_enfermo

p_positivo_enfermo = 0.9
p_positivo_sano = 0.05

p_positivo = (p_positivo_enfermo * p_enfermo) + (p_positivo_sano * p_sano)
p_enfermo_positivo = (p_positivo_enfermo * p_enfermo) / p_positivo

print("P(sano):", p_sano)
print("P(positivo):", p_positivo)
print("P(enfermo | positivo):", p_enfermo_positivo)
print(f"Si el test da positivo, la probabilidad real de estar enfermo es del {p_enfermo_positivo * 100:.2f}%")