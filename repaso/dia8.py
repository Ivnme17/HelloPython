#Examen de repaso Python (≈60 min)
# Bloque 1 — Fundamentos y condicionales (10 min)

# 1.1 Escribe una función clasificar_edad(edad) que devuelva:

# "Bebé" si edad < 2
# "Niño" si edad < 12
# "Adolescente" si edad < 18
# "Adulto" en cualquier otro caso

def clasificar_edad(edad):
    resultado = ""
    
    if(edad < 2):
        resultado = "Bebé"
    elif(edad < 12):
        resultado = "Niño"
    elif(edad < 18):
        resultado = "Adolescente"
    else: resultado = "Adulto"
    
    return resultado
# 1.2 Usando match-case (o if/elif si tu versión de Python es anterior a 3.10), crea una función dia_semana(numero) que reciba un número del 1 al 7 y devuelva el nombre del día correspondiente, o "Número inválido" si está fuera de rango.

def dia_semana(numero):
    resultado = ""
    
    match numero:
        case 1: resultado = "Lunes"
        case 2: resultado = "Martes"
        case 3: resultado = "Miercoles"
        case 4: resultado = "Jueves"
        case 5: resultado = "Viernes"
        case 6: resultado = "Sabado"
        case 7: resultado = "Domingo"
        case _: resultado = "Numero invalido"

    return resultado
# Variables de ejemplo

edad = 7
dia = 5
diaError = "5"

print("Mi hijo tiene 7 anios, mi hijo es todavia un",clasificar_edad(edad))
print("Hoy es el quinto dia de la semana, es decir, hoy es", dia_semana(dia))
print("Hoy es el quinto dia de la semana, es decir, hoy es", dia_semana(diaError))


# Bloque 2 — Bucles y comprehensions (10 min)

# 2.1 Dada la lista temperaturas = [22, 35, 18, 40, 15, 29, 33], usa una list comprehension para crear una lista solo con las temperaturas superiores a 25.
temperaturas = [22, 35, 18, 40, 15, 29, 33]
temperaturas_Mayores_Veinticinco = [temperatura for temperatura in temperaturas  if(temperatura > 25)]

for temperaturaMayor in temperaturas_Mayores_Veinticinco :
    print("Las temperaturas mayores a 25 son:",temperaturaMayor)


# 2.2 Usando un while, simula una cuenta atrás desde 10 hasta 0, imprimiendo cada número, y cuando llegue a 0 imprime "¡Despegue!".
contador = 10

while(contador >0):
    print(contador)
    contador -= 1;

print("Despegue!")

# 2.3 Dado el diccionario:

# python
# inventario = {"manzanas": 10, "peras": 0, "platanos": 5, "naranjas": 0}
# recórrelo con un for e imprime solo los productos con cantidad mayor que 0, en formato "producto: cantidad".

inventario = {"manzanas": 10, "peras": 0, "platanos": 5, "naranjas": 0}

# for producto, cantidad in inventario:
#     for cantidad in inventario[producto]:
#         if(cantidad > 0):
#             print(inventario[producto],":",cantidad)



# Bloque 3 — Funciones avanzadas (10 min)

# 3.1 Crea una función crear_saludo(idioma) que sea una closure: debe devolver una función que reciba un nombre y salude según el idioma elegido ("es" → "Hola, {nombre}", "en" → "Hello, {nombre}", cualquier otro → "??? {nombre}").

def recibe_nombre(nombre):
    mensaje = ""
    def crear_saludo(idioma):
        match idioma:
            case "es": mensaje ="Hola",nombre
            case "en": mensaje = "Hello", nombre
            case _: mensaje = nombre
        return mensaje
    return crear_saludo

nombre_a_recibir = recibe_nombre("Pepe")
print(nombre_a_recibir("es"))

# 3.2 Crea una excepción personalizada EdadInvalidaError y una función validar_edad(edad) que la lance si edad < 0 o edad > 120, y si es válida, devuelva la edad.

class EdadInvalidaError(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_edad(edad):
    mensajeError = EdadInvalidaError("No es valida la edad")
    if(edad < 0 or edad > 120):
        raise mensajeError
    else: return edad
        

edad = 9
#edadError = 130
print("Tienes:", validar_edad(edad))
#print("Tienes:", validar_edad(edadError))

# Bloque 4 — Clases, herencia y polimorfismo (20 min)

# 4.1 Crea una clase base Empleado con __init__(self, nombre, salario_base) y un método calcular_salario() que devuelva salario_base.

class Empleado :
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        salario_base = self.salario_base
        return salario_base

trabajador = Empleado("Javier", 1200)

print("El salario de este trabajador es de:", trabajador.calcular_salario())

# 4.2 Crea dos clases hijas:

class Comercial(Empleado):
    def __init__(self,nombre,salario_base,ventas):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
    def calcular_salario(self):
            salario_base = self.salario_base + (self.ventas * 0.1)
            return salario_base


class Gerente(Empleado):
    def __init__(self,nombre,salario_base,bonus):
            super().__init__(nombre, salario_base)
            self.bonus = bonus
    def calcular_salario(self):
            salario_base = self.salario_base + self.bonus
            return salario_base
    

# Comercial(Empleado), que añade ventas en el constructor y sobreescribe calcular_salario() para devolver salario_base + (ventas * 0.1) (comisión del 10%)
# Gerente(Empleado), que añade bonus en el constructor y sobreescribe calcular_salario() para devolver salario_base + bonus

# 4.3 Crea una lista con un Comercial y un Gerente, recórrela con un for y, usando polimorfismo (sin isinstance), imprime el nombre y el salario calculado de cada uno.
empleados = [Comercial("Fulanito",1200,2), Gerente("Menganito",1300,5)]

for empleado in empleados:
    print(empleado.nombre, empleado.calcular_salario())

# 4.4 Ahora usa isinstance() para recorrer esa misma lista y, además del salario, imprime un mensaje distinto según sea Comercial o Gerente (por ejemplo, mencionando sus ventas o su bonus respectivamente).

# Bloque 5 — Ficheros y manejo de errores (10 min)

# 5.1 Escribe una función guardar_empleados(lista_empleados, ruta) que reciba la lista de empleados del bloque 4 y escriba en un fichero de texto una línea por empleado con formato "Nombre: salario calculado".

# 5.2 Escribe una función leer_empleados(ruta) que lea ese fichero y, si no existe, capture la excepción con un try/except y devuelva una lista vacía en vez de petar.

# TERMINAR BLOQUE MANIANA Y EMPEZAR CON EL DIA 9