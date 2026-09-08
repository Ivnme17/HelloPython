class Calculadora(object): 
    # Definimos la clase para simular una calculadora simple
    def __init__ (self): 
    #Empieza con el numero 0
        self.numero = 0 
    def agregarCantidad(self, cantidad): 
    #Agregamos la cantidad al numero actual
        self.numero += cantidad 
    def getCantidad(self): 
        return self.numero 

class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    # añade un método frenar() que reste 10 a la velocidad

    def frenar(self):
        self.velocidad -= 10

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def info(self):
        return f"{self.nombre} gana {self.salario}€"

class Programador(Empleado):
    # hereda de Empleado, añade "lenguaje" y sobreescribe info()
    # para que también muestre el lenguaje
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    
    def info(self):
        return f"{self.nombre} gana {self.salario}€ ({self.lenguaje})"


class SaldoInsuficiente(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# Clase Animal y sus hijas

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "..."

class Perro(Animal):
    # sobreescribe hacer_sonido() para que devuelva "Guau"
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self): # type: ignore
        return "guau"

class Gato(Animal):
    # sobreescribe hacer_sonido() para que devuelva "Miau"
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self): # type: ignore
        return "Miau"

# Clase Vehiculo y sus hijas
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

class Moto(Vehiculo):
    def __init__(self, marca, velocidad_max, cilindrada):
        super().__init__(marca, velocidad_max) # type: ignore
        self.cilindrada = cilindrada

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calificacion(self):
        # devuelve "Sobresaliente", "Notable", "Aprobado" o "Suspenso"
        # según la nota, usando if/elif/else
        resultado = ""
        if self.nota >= 9:
            resultado = "Sobresaliente"
        elif self.nota >= 7:
            resultado = "Notable"
        elif self.nota >= 5:
            resultado = "Aprobado"
        elif self.nota >= 0:
            resultado = "Suspenso"
        
        else: resultado = "No se ha registrado la nota correctamente"
        
        return resultado

# Clase Empleado y sus hijas
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Profesor(Empleado):
    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

class Alumno(Empleado):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.curso = curso

# Clase Figura y sus hijas
class Figura:
    def area(self):
        raise NotImplementedError("Debes implementar este método")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        resultado = 0
        if self.base <= 0 or self.altura <= 0:
            resultado = None
        else:   
            resultado = self.base * self.altura
        
        return resultado

# Clase Forma y sus hijas
class Forma:
    def area(self):
        return 0

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

