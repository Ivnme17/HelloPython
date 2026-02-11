# Clases

class ClaseVacia:
    pass

class Persona:
    # Constructor
    def __init__(self, nombre, apellido, alias = "Sin alias"):
        self.nombre_completo = f"{nombre} {apellido} ({alias})"
        self.nombre = nombre #Propiedad privada
        self.apellido = apellido #Propiedad privada
        self.alias = alias #Propiedad privada

    def get_nombre (self):
        return self.nombre

    def get_apellido (self):
        return self.apellido

    def get_alias (self):
        return self.alias

    def caminar (self):
        print(f"{self.nombre_completo} está caminando")

# Zona de ejecución
mi_persona = Persona("Ivan", "Martinez", "Ivnme17")
print(mi_persona.nombre_completo)
print(mi_persona.get_nombre())
print(mi_persona.get_apellido())
print(mi_persona.get_alias())
mi_persona.caminar()

print("------------------")

otra_persona = Persona("Juan", "Perez")
otra_persona.nombre_completo = "Pablo Perez (Con alias)" # No es recomendable modificar directamente el atributo
print(otra_persona.nombre_completo)
otra_persona.caminar()

# Ejemplo de tipado dinámico
otra_persona.nombre_completo = 666
print(otra_persona.nombre_completo)
otra_persona.caminar()