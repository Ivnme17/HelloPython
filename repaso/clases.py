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


