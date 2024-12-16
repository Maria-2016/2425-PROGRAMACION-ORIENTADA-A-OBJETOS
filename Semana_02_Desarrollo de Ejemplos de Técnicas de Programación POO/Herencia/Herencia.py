# EJEMPLO DE HERENCIA

# Clase base que representa un Vehículo genérico
class Vehiculo:
    """
    Clase base para representar un vehículo con atributos comunes.
    """
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca                  # Marca del vehículo
        self.modelo = modelo                # Modelo del vehículo
        self.velocidad_maxima = velocidad_maxima  # Velocidad máxima del vehículo

    def describir(self):
        """Muestra la información básica del vehículo."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h")

    def acelerar(self):
        """Simula la acción de acelerar el vehículo."""
        print(f"El {self.modelo} está acelerando...")

# Clase derivada que representa un Automóvil
class Automovil(Vehiculo):
    """
    Clase derivada de Vehiculo que representa un automóvil con atributos adicionales.
    """
    def __init__(self, marca, modelo, velocidad_maxima, puertas):
        super().__init__(marca, modelo, velocidad_maxima)  # Llama al constructor de la clase base
        self.puertas = puertas  # Número de puertas del automóvil

    def abrir_puertas(self):
        """Simula la acción de abrir las puertas del automóvil."""
        print(f"El {self.modelo} está abriendo sus {self.puertas} puertas.")

    def describir(self):
        """Extiende el método describir para incluir el número de puertas."""
        super().describir()
        print(f"Puertas: {self.puertas}")

# Clase derivada que representa una Motocicleta
class Motocicleta(Vehiculo):
    """
    Clase derivada de Vehiculo que representa una motocicleta con atributos adicionales.
    """
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)  # Llama al constructor de la clase base
        self.tipo = tipo  # Tipo de motocicleta (e.g., deportiva, touring, urbana)

    def hacer_caballito(self):
        """Simula la acción de hacer un caballito con la motocicleta."""
        print(f"La motocicleta {self.modelo} está haciendo un caballito.")

    def describir(self):
        """Extiende el método describir para incluir el tipo de motocicleta."""
        super().describir()
        print(f"Tipo: {self.tipo}")

# Ejecución del ejemplo con instancias
if __name__ == "__main__":
    # Creación de un objeto Automovil
    auto = Automovil("Toyota", "Corolla", 180, 4)
    print("\n--- Automóvil ---")
    auto.describir()
    auto.abrir_puertas()
    auto.acelerar()

    # Creación de un objeto Motocicleta
    moto = Motocicleta("Yamaha", "YZF-R1", 299, "Deportiva")
    print("\n--- Motocicleta ---")
    moto.describir()
    moto.hacer_caballito()
    moto.acelerar()
