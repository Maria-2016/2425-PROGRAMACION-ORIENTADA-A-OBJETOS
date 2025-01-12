
#Sistema de Reservas de una Tienda en Línea

# Definimos una clase Producto que representará los productos disponibles en la tienda.
class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        """
        Inicializa un producto con un nombre, precio y cantidad disponible.
        :param nombre: El nombre del producto.
        :param precio: El precio del producto.
        :param cantidad_disponible: La cantidad de productos disponibles para la venta.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        """
        Método que define cómo se muestra el objeto Producto como cadena.
        """
        return f"{self.nombre} - ${self.precio} (Disponibles: {self.cantidad_disponible})"

    def actualizar_stock(self, cantidad):
        """
        Actualiza la cantidad de stock disponible.
        :param cantidad: Cantidad a agregar o reducir al stock actual.
        """
        self.cantidad_disponible += cantidad


# Clase Reserva que se encarga de realizar reservas de productos.
class Reserva:
    def __init__(self, producto, cantidad, cliente):
        """
        Inicializa una reserva con un producto, cantidad y cliente.
        :param producto: Instancia de la clase Producto que se va a reservar.
        :param cantidad: La cantidad del producto que se va a reservar.
        :param cliente: El nombre del cliente que hace la reserva.
        """
        self.producto = producto
        self.cantidad = cantidad
        self.cliente = cliente
        self.estado = "Pendiente"  # Estado de la reserva, por defecto es "Pendiente"

    def confirmar_reserva(self):
        """
        Método para confirmar la reserva si hay suficiente stock disponible.
        """
        if self.producto.cantidad_disponible >= self.cantidad:
            self.producto.actualizar_stock(-self.cantidad)  # Reducimos el stock disponible
            self.estado = "Confirmada"
            print(f"Reserva confirmada para {self.cliente}: {self.cantidad} unidades de {self.producto.nombre}.")
        else:
            self.estado = "Cancelada"
            print(f"Reserva cancelada para {self.cliente}: No hay suficiente stock de {self.producto.nombre}.")

    def __str__(self):
        """
        Método que devuelve un resumen de la reserva.
        """
        return f"Cliente: {self.cliente}, Producto: {self.producto.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}"


# Clase Tienda que gestionará los productos y las reservas.
class Tienda:
    def __init__(self):
        """
        Inicializa una tienda con una lista vacía de productos y reservas.
        """
        self.productos = []
        self.reservas = []

    def agregar_producto(self, producto):
        """
        Agrega un producto a la tienda.
        :param producto: Instancia de la clase Producto.
        """
        self.productos.append(producto)

    def realizar_reserva(self, producto, cantidad, cliente):
        """
        Realiza una reserva de un producto para un cliente.
        :param producto: Instancia de la clase Producto que se va a reservar.
        :param cantidad: La cantidad del producto que el cliente desea reservar.
        :param cliente: El nombre del cliente que realiza la reserva.
        """
        reserva = Reserva(producto, cantidad, cliente)
        self.reservas.append(reserva)
        reserva.confirmar_reserva()


# **Ejemplo de uso del sistema:**
# Creamos una tienda y algunos productos.
tienda = Tienda()

producto1 = Producto("Laptop", 800, 5)
producto2 = Producto("Smartphone", 400, 10)

# Agregamos los productos a la tienda.
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Realizamos algunas reservas.
tienda.realizar_reserva(producto1, 3, "Juan Pérez")  # Reserva de 3 laptops
tienda.realizar_reserva(producto2, 5, "Ana Gómez")   # Reserva de 5 smartphones
tienda.realizar_reserva(producto1, 3, "Luis Fernández")  # Intento de reservar 3 laptops (pero solo hay 2 disponibles)

# Imprimimos el estado actual de las reservas.
for reserva in tienda.reservas:
    print(reserva)

# Mostramos el stock restante de los productos.
print(f"\nStock restante de {producto1.nombre}: {producto1.cantidad_disponible}")
print(f"Stock restante de {producto2.nombre}: {producto2.cantidad_disponible}")
