# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos encapsulados
        self.__nombre = nombre
        self.__edad = edad

    # Métodos getter y setter para encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")

    # Método para mostrar información
    def mostrar_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

# Clase derivada: Estudiante (Herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera

    # Polimorfismo: Sobrescritura de método
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Carrera: {self.carrera}"

# Clase derivada: Profesor (Herencia)
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Polimorfismo: Sobrescritura de método
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Materia: {self.materia}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear objetos
    estudiante = Estudiante("Ana", 20, "Ingeniería en Sistemas")
    profesor = Profesor("Maria", 30, "Programación Orientada a Objetos")

    # Mostrar información de los objetos
    print(estudiante.mostrar_informacion())
    print(profesor.mostrar_informacion())

    # Encapsulación: Modificar atributos usando métodos
    estudiante.set_edad(21)
    print(f"Edad actualizada del estudiante: {estudiante.get_edad()}")

    # Polimorfismo en acción
    personas = [estudiante, profesor]
    for persona in personas:
        print(persona.mostrar_informacion())
