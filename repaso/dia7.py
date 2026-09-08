# Clases, herencia y condicionales
# Ejercicio 1 Crea un perro y un gato, imprime su nombre y su sonido

from clases import *

perro = Perro("Dalmata 1")
gato = Gato("Con botas")

print("Mi dalmata hace:",perro.hacer_sonido())
print("Soy el gato Con botas:",gato.hacer_sonido())

# Ejercicio 2 Crea una moto e imprime sus detalles(atributos de la clase padre) y la cilindrada(metodo propio)
m = Moto("Yamaha", 180, 600)
print(m.marca, m.velocidad_max, m.cilindrada)

# Ejericio 3 Condicionales mas metodos de clase


e = Estudiante("Ivan", 8)
print(e.calificacion())  # Notable

# Ejercicio 4 Herencia multiple y uso de isinstance
personas = [Profesor("Marta", "Python"), Alumno("Ivan", "DAW")]
# Tenemos una lista denominada personas que tienen dentro un objeto en este caso un Profesor y un Alumno

# El isinstance nos ayuda a saber si la informacion contenida en personas es de un tipo u otro
for persona in  personas:
    if isinstance(persona, Profesor):
        print("Soy la profesora",persona.nombre)
    elif isinstance(persona, Alumno):
        print("Soy un alumno y mi nombre es:",persona.nombre)

# Ejercicio 5 clase abstracta simple y condicional de validacion

r = Rectangulo(5, 3)
print(r.area())  # 15

r2 = Rectangulo(-2, 3)
print(r2.area())  # None

# Ejercicio 6 Polimorfismo mas bucle con condicional

formas = [Circulo(3), Cuadrado(4), Circulo(1)]

# Recorre "formas", calcula el área de cada una
# e imprime solo las que tengan área mayor que 10

for forma in formas:
    areaForma = forma.area()
    
    if areaForma > 10:
        print("El area de las formas es:",areaForma)
    
