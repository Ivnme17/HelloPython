'''
----------------------------------
Funciones de ejemplo IA Y BIG DATA
----------------------------------
'''

# 1. Función para normalizar datos (preprocesamiento)
def normalizar_datos(datos):
    """
    Normaliza una lista de datos al rango [0, 1]
    """
    min_val = min(datos)
    max_val = max(datos)
    
    if max_val == min_val:
        return [0] * len(datos)
    
    return [(x - min_val) / (max_val - min_val) for x in datos]

# Ejemplo de uso
datos_muestra = [10, 20, 30, 40, 50]
datos_normalizados = normalizar_datos(datos_muestra)
print(f"Datos originales: {datos_muestra}")
print(f"Datos normalizados: {datos_normalizados}")
print()

# 2. Función para calcular distancia euclidiana (algoritmos de clustering)
def distancia_euclidiana(punto1, punto2):
    """
    Calcula la distancia euclidiana entre dos puntos
    """
    if len(punto1) != len(punto2):
        raise ValueError("Los puntos deben tener la misma dimensión")
    
    suma_cuadrados = sum((a - b) ** 2 for a, b in zip(punto1, punto2))
    return suma_cuadrados ** 0.5

# Ejemplo de uso
punto_a = [1, 2, 3]
punto_b = [4, 6, 8]
distancia = distancia_euclidiana(punto_a, punto_b)
print(f"Distancia euclidiana entre {punto_a} y {punto_b}: {distancia:.4f}")
print()

# 3. Función de activación sigmoide (redes neuronales)
def sigmoide(x):
    """
    Función de activación sigmoide para redes neuronales
    """
    import math
    return 1 / (1 + math.exp(-x))

# Ejemplo de uso
valores = [-2, -1, 0, 1, 2]
print("Valores de la función sigmoide:")
for val in valores:
    print(f"sigmoide({val}) = {sigmoide(val):.4f}")
print()

# 4. Función para calcular precisión (métricas de evaluación)
def calcular_precision(y_true, y_pred):
    """
    Calcula la precisión de un modelo de clasificación
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Las listas deben tener el mismo tamaño")
    
    correctas = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    total = len(y_true)
    
    return correctas / total

# Ejemplo de uso
y_verdadero = [1, 0, 1, 1, 0, 1, 0, 0]
y_predicho = [1, 0, 0, 1, 0, 1, 1, 0]
precision = calcular_precision(y_verdadero, y_predicho)
print(f"Precisión del modelo: {precision:.4f} ({precision*100:.2f}%)")
print()

# 5. Función para dividir datos en entrenamiento y prueba (machine learning)
def dividir_datos(datos, test_size=0.2, random_state=None):
    """
    Divide los datos en conjuntos de entrenamiento y prueba
    """
    import random
    
    if random_state:
        random.seed(random_state)
    
    datos_copy = datos.copy()
    random.shuffle(datos_copy)
    
    split_index = int(len(datos_copy) * (1 - test_size))
    
    train_data = datos_copy[:split_index]
    test_data = datos_copy[split_index:]
    
    return train_data, test_data

# Ejemplo de uso
dataset = list(range(1, 21))  # Dataset de ejemplo
train, test = dividir_datos(dataset, test_size=0.3, random_state=42)
print(f"Dataset completo: {dataset}")
print(f"Datos de entrenamiento: {train}")
print(f"Datos de prueba: {test}")
print()

# 6. Función para calcular promedio móvil (análisis de series temporales)
def promedio_movil(datos, ventana):
    """
    Calcula el promedio móvil de una serie de datos
    """
    if ventana <= 0:
        raise ValueError("La ventana debe ser mayor que 0")
    
    if ventana > len(datos):
        raise ValueError("La ventana no puede ser mayor que el tamaño de los datos")
    
    promedios = []
    for i in range(len(datos) - ventana + 1):
        ventana_actual = datos[i:i + ventana]
        promedio = sum(ventana_actual) / ventana
        promedios.append(promedio)
    
    return promedios

# Ejemplo de uso
ventas_mensuales = [100, 120, 115, 130, 125, 140, 135, 150, 145, 160]
prom_3_meses = promedio_movil(ventas_mensuales, 3)
print(f"Ventas mensuales: {ventas_mensuales}")
print(f"Promedio móvil (3 meses): {prom_3_meses}")
print()

# 7. Función para procesar texto (NLP - Natural Language Processing)
def limpiar_texto(texto):
    """
    Limpia y preprocesa texto para análisis NLP
    """
    import re
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar caracteres especiales y números
    texto = re.sub(r'[^a-z\s]', '', texto)
    
    # Eliminar espacios extra
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    return texto

def contar_palabras(texto):
    """
    Cuenta la frecuencia de palabras en un texto
    """
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

# Ejemplo de uso
texto_ejemplo = "El aprendizaje automático es fascinante. El machine learning transforma datos en conocimiento."
texto_limpio = limpiar_texto(texto_ejemplo)
frecuencia_palabras = contar_palabras(texto_ejemplo)

print(f"Texto original: {texto_ejemplo}")
print(f"Texto limpio: {texto_limpio}")
print(f"Frecuencia de palabras: {frecuencia_palabras}")