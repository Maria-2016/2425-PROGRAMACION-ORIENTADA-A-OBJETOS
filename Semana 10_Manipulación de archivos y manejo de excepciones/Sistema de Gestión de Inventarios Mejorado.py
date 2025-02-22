import os

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto  # Atributo privado para el ID del producto
        self.__nombre = nombre
        self.__cantidad = int(cantidad)  # Convertir a entero
        self.__precio = float(precio)  # Convertir a flotante

    # Getters
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = int(cantidad)

    def set_precio(self, precio):
        self.__precio = float(precio)

    def __str__(self):
        return f"ID: {self.__id_producto}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: ${self.__precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo='Inventario_Mejorado.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde un archivo de texto."""
        if not os.path.exists(self.archivo):  # Verificar si el archivo existe
            return

        with open(self.archivo, 'r') as file:
            for line in file:
                try:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
                except ValueError:
                    print(f"Error al cargar línea: {line.strip()} (Formato incorrecto)")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        with open(self.archivo, 'w') as file:
            for producto in self.productos:
                file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario, validando que el ID no se repita."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID."""
        productos_filtrados = [p for p in self.productos if p.get_id() != id_producto]
        if len(productos_filtrados) == len(self.productos):
            print("Producto no encontrado.")
        else:
            self.productos = productos_filtrados
            print("Producto eliminado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto por ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        for p in resultados:
            print(p)
        if not resultados:
            print("No se encontraron productos.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

# Interfaz de usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Cantidad y precio deben ser valores numéricos.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad.strip() else None
            precio = float(precio) if precio.strip() else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
