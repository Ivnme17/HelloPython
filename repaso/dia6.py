# Creacion de una IA muy basica

import random
from datetime import datetime

respuestas = {
    "hola": ["¡Hola! ¿Qué tal?", "¡Buenas! ¿Cómo estás?"],
    "como estas": ["Muy bien, gracias por preguntar", "Ahí vamos, ¿y tú?"],
    "nombre": ["Soy un bot muy simple hecho en Python", "Me llamo PyBot"],
    "python": ["Python me parece un gran lenguaje", "¡Python es lo mío!"],
    "triste": ["Siento que te sientas así, ¿quieres hablar de ello?"],
    "adios": ["¡Hasta luego!", "Nos vemos, cuídate"]
}
historial = []

def generar_respuesta(mensaje):
    mensaje = mensaje.lower()  # normalizamos a minúsculas
    
    for palabra_clave, lista_respuestas in respuestas.items():
        if palabra_clave in mensaje:
            return random.choice(lista_respuestas)
    
    return "No te he entendido muy bien, ¿puedes reformularlo?"


def guardar_historial(historial):
    # Genera el nombre del fichero con fecha y hora actuales
    marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")  # noqa: DTZ005
    ruta = f"conversacion_{marca_tiempo}.txt"
    
    with open(ruta, "w", encoding="utf-8") as f:
        for usuario, bot in historial:
            f.write(f"Tú: {usuario}\n")
            f.write(f"PyBot: {bot}\n")
    
    print(f"Conversación guardada en {ruta}")

def chat():
    print("PyBot: ¡Hola! Escribe 'adios' para salir.")
    
    while True:
        entrada_usuario = input("Tú: ")
        
        if "adios"  in entrada_usuario.lower():
            respuesta = random.choice(respuestas["adios"])
            print("PyBot:", respuesta)
            historial.append((entrada_usuario, respuesta))
            break
        
        respuesta = generar_respuesta(entrada_usuario)
        print("PyBot:", respuesta)
        historial.append((entrada_usuario, respuesta))
    guardar_historial(historial)  # Guardamos el historial después de cada mensaje
chat()





# Y al salir del bucle, después del break, imprime:
print(f"\nHan sido {len(historial)} mensajes intercambiados")