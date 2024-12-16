# EJEMPLO DE POLIMORFISMO

# Clase base que representa un animal genérico
class Animal:
    # Constructor que inicializa el nombre del animal
    def __init__(self, nombre):
        self.nombre = nombre

    # Método genérico que cada subclase sobrescribira
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    # Método genérico para describir al animal
    def descripcion(self):
        return f"Soy un animal llamado {self.nombre}."

# Clase que representa un Perro, hereda de Animal
class Perro(Animal):
    # Constructor que llama al constructor de la clase base
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza  # Atributo adicional específico del perro

    # Sobrescribe el método para hacer un sonido característico del perro
    def hacer_sonido(self):
        return "Guau guau!"

    # Sobrescribe la descripción para incluir la raza
    def descripcion(self):
        return f"Soy un perro llamado {self.nombre} y soy de raza {self.raza}."

# Clase que representa un Gato, hereda de Animal
class Gato(Animal):
    # Constructor que llama al constructor de la clase base
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color  # Atributo adicional específico del gato

    # Sobrescribe el método para hacer un sonido característico del gato
    def hacer_sonido(self):
        return "Miau miau!"

    # Sobrescribe la descripción para incluir el color
    def descripcion(self):
        return f"Soy un gato llamado {self.nombre} y soy de color {self.color}."

# Ejemplo de uso del polimorfismo

def presentar_animal(animal):
    # Esta función acepta cualquier objeto que herede de Animal
    print(animal.descripcion())  # Llama al método de descripción específico de la subclase
    print("Sonido:", animal.hacer_sonido())  # Llama al método de hacer_sonido específico de la subclase

# Creación de instancias de Perro y Gato
perro = Perro("Bobby", "Golden Retriever")
gato = Gato("Mishu", "Negro")

# Uso del polimorfismo para trabajar con ambos objetos
presentar_animal(perro)
presentar_animal(gato)
