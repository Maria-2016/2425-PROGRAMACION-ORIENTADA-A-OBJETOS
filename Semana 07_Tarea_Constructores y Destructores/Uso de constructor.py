
# Implementación de Constructores constructores (__init__) en Python

# Clase que representa un Producto
class Producto:
    def __init__(self, nombre, precio):
        # Constructor: inicializa el nombre y precio del producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        # Método para mostrar la información del producto
        print(f"Producto: {self.nombre}, Precio: ${self.precio:.2f}")

# === Ejemplo de uso ===
# Crear un objeto de la clase Producto
producto1 = Producto("Laptop", 1200.50)
producto2 = Producto("Teléfono", 799.99)

# Mostrar la información de los productos
producto1.mostrar_info()
producto2.mostrar_info()

# === Explicación del código ===
# 1. El constructor (__init__) se utiliza para inicializar los atributos de cada producto.
# 2. El método mostrar_info imprime los detalles del producto en un formato claro.
# 3. Este ejemplo demuestra la utilidad de los constructores con un caso simple y directo.
