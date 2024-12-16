# EJEMPLO DE ABSTRACCIÓN

# Clase base que representa un vehículo genérico
class Vehiculo:
    """
    Clase base para modelar vehículos genéricos. Proporciona atributos comunes y
    funcionalidades básicas para los vehículos.
    """
    def __init__(self, marca, modelo, velocidad_maxima, capacidad):
        """
        Inicializa un vehículo con los atributos básicos.
        :param marca: Marca del vehículo (string)
        :param modelo: Modelo del vehículo (string)
        :param velocidad_maxima: Velocidad máxima en km/h (entero)
        :param capacidad: Capacidad de pasajeros (entero)
        """
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.capacidad = capacidad

    def mostrar_informacion(self):
        """Imprime la información del vehículo."""
        print(f"Vehículo: {self.marca} {self.modelo}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Capacidad: {self.capacidad} pasajeros")

    def encender(self):
        """Simula encender el vehículo."""
        print(f"El {self.marca} {self.modelo} está encendido.")

# Clase derivada para un automóvil
class Automovil(Vehiculo):
    """
    Representa un automóvil que hereda las propiedades de Vehiculo.
    """
    def __init__(self, marca, modelo, velocidad_maxima, capacidad, tipo_motor):
        """
        Inicializa un automóvil con un tipo de motor adicional.
        :param tipo_motor: Tipo de motor (string, e.g., gasolina, eléctrico)
        """
        super().__init__(marca, modelo, velocidad_maxima, capacidad)
        self.tipo_motor = tipo_motor

    def mostrar_informacion(self):
        """Sobrescribe el método para incluir información del motor."""
        super().mostrar_informacion()
        print(f"Tipo de motor: {self.tipo_motor}")

    def acelerar(self):
        """Simula el automóvil acelerando."""
        print(f"El automóvil {self.marca} {self.modelo} está acelerando.")

# Clase derivada para una motocicleta
class Motocicleta(Vehiculo):
    """
    Representa una motocicleta que hereda las propiedades de Vehiculo.
    """
    def __init__(self, marca, modelo, velocidad_maxima, capacidad, tipo_manubrio):
        """
        Inicializa una motocicleta con un tipo de manubrio adicional.
        :param tipo_manubrio: Tipo de manubrio (string, e.g., deportivo, clásico)
        """
        super().__init__(marca, modelo, velocidad_maxima, capacidad)
        self.tipo_manubrio = tipo_manubrio

    def mostrar_informacion(self):
        """Sobrescribe el método para incluir información del manubrio."""
        super().mostrar_informacion()
        print(f"Tipo de manubrio: {self.tipo_manubrio}")

    def hacer_caballito(self):
        """Simula la acción de hacer un caballito con la motocicleta."""
        print(f"La motocicleta {self.marca} {self.modelo} está haciendo un caballito.")

# Funcionalidad para comparar la velocidad entre dos vehículos
def comparar_velocidad(vehiculo_1, vehiculo_2):
    """
    Compara las velocidades máximas de dos vehículos.
    :param vehiculo_1: Instancia de Vehiculo
    :param vehiculo_2: Instancia de Vehiculo
    """
    if vehiculo_1.velocidad_maxima > vehiculo_2.velocidad_maxima:
        print(f"El {vehiculo_1.marca} {vehiculo_1.modelo} es más rápido que el {vehiculo_2.marca} {vehiculo_2.modelo}.")
    elif vehiculo_1.velocidad_maxima < vehiculo_2.velocidad_maxima:
        print(f"El {vehiculo_2.marca} {vehiculo_2.modelo} es más rápido que el {vehiculo_1.marca} {vehiculo_1.modelo}.")
    else:
        print(f"Ambos vehículos tienen la misma velocidad máxima.")

# Instancias de diferentes tipos de vehículos
vehiculo_1 = Automovil("Toyota", "Corolla", 180, 5, "gasolina")
vehiculo_2 = Motocicleta("Kawasaki", "Ninja", 200, 2, "deportivo")

# Mostrar información de los vehículos
vehiculo_1.mostrar_informacion()
vehiculo_2.mostrar_informacion()

# Simular acciones
vehiculo_1.encender()
vehiculo_1.acelerar()
vehiculo_2.encender()
vehiculo_2.hacer_caballito()

# Comparar velocidades
comparar_velocidad(vehiculo_1, vehiculo_2)
