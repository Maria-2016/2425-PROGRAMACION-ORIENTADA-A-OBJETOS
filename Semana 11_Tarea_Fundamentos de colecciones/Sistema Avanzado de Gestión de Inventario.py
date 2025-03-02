import json
import os

# Clase producto
class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def to_dict(self):
        """Convierte el producto a un diccionario para su almacenamiento en JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    """
    Clase que gestiona el inventario de la tienda.
    """

    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario para almacenar productos por ID
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print("Producto agregado con éxito.")
        else:
            print("El ID del producto ya existe en el inventario.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre y los muestra."""
        encontrados = [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario en una nueva ventana."""
        if self.productos:
            inventario_texto = "\n".join([str(p.to_dict()) for p in self.productos.values()])
            archivo_mostrar = "inventario_mostrar.txt"
            with open(archivo_mostrar, "w") as file:
                file.write(inventario_texto)
            os.system(f"notepad {archivo_mostrar}")  # Abre el archivo en el bloc de notas
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self):
        """Guarda el inventario en un archivo JSON."""
        with open(self.archivo, "w") as file:
            json.dump({k: v.to_dict() for k,v in self.productos.items()}, file, indent=4)
        print(f"Inventario guardado en {self.archivo}")

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo JSON o lo crea si no existe."""
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = {id_p: Producto.from_dict(p) for id_p, p in data.items()}
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No se encontró un archivo de inventario válido. Creando un nuevo inventario...")
            self.guardar_inventario()


# Menú interactivo
def menu():
    """Interfaz de usuario en la consola."""
    archivo = input("Ingrese el nombre del archivo de inventario (sin extensión): ") + "_inventario.json"
    inventario = Inventario(archivo)

    while True:
        print("\n--- Menú de Gestión de Inventario - TechStore ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(nueva_cantidad) if nueva_cantidad else None,
                                           float(nuevo_precio) if nuevo_precio else None)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_inventario()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()

