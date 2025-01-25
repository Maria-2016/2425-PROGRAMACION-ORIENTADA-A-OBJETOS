
# Implementación de constructores (__init__) y destructores (__del__) en Python

# Clase que representa un Producto
class Producto:
    def __init__(self, nombre, precio):
        # Constructor: inicializa el nombre y precio del producto
        self.nombre = nombre
        self.precio = precio
        print(f"Producto '{self.nombre}' creado con éxito.")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto es eliminado o sale del ámbito
        print(f"Producto '{self.nombre}' eliminado y recursos liberados.")

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

# Eliminar un producto manualmente
# Esto activará el destructor para ese objeto
print("\nEliminando producto1...")
del producto1

# === Explicación del código ===
# 1. El constructor (__init__) inicializa los atributos del objeto al crearlo.
# 2. El destructor (__del__) libera recursos o realiza tareas de limpieza al eliminar el objeto.
# 3. En este ejemplo, se muestra un mensaje cuando el objeto es creado y eliminado.
# 4. Los destructores se activan automáticamente cuando el objeto sale del ámbito o se elimina manualmente con 'del'.
