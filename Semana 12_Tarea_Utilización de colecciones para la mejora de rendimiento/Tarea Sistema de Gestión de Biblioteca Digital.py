# Semana 12_Tarea: Utilización de colecciones para la mejora de rendimiento
# Tarea: Sistema de Gestión de Biblioteca Digital

class Libro:
    # Representa un libro en la biblioteca
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla para almacenar título y autor (inmutables)
        self.categoria = categoria  # Categoría del libro
        self.isbn = isbn  # Código ISBN del libro

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    # Representa a un usuario de la biblioteca
    def __init__(self, nombre, user_id):
        self.nombre = nombre  # Nombre del usuario
        self.user_id = user_id  # ID único del usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {[libro.datos[0] for libro in self.libros_prestados]}"


class Biblioteca:
    # Clase que gestiona la biblioteca
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        # Agrega un libro a la biblioteca
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        # Elimina un libro de la biblioteca si existe
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        # Registra un usuario en la biblioteca
        if usuario.user_id in self.usuarios_registrados:
            print("ID de usuario ya registrado.")
        else:
            self.usuarios_registrados[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")

    def eliminar_usuario(self, user_id):
        # Elimina un usuario si está registrado
        if user_id in self.usuarios_registrados:
            del self.usuarios_registrados[user_id]
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        # Presta un libro a un usuario
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[user_id]
            libro = self.libros_disponibles.pop(isbn)  # Elimina el libro de la lista de disponibles
            usuario.libros_prestados.append(libro)  # Lo añade a la lista de libros prestados del usuario
            print(f"Libro '{libro.datos[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        # Devuelve un libro a la biblioteca
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro  # Lo vuelve a añadir a los libros disponibles
                    print(f"Libro '{libro.datos[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        # Busca libros según el criterio especificado (título, autor o categoría)
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio, '').lower() == valor.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        # Lista los libros prestados a un usuario específico
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("No tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
biblioteca = Biblioteca()

# Creación de libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-84-376-0494-7")
libro2 = Libro("1984", "George Orwell", "Distopía", "978-0451524935")

# Creación de un usuario
usuario1 = Usuario("María Rocío", "001")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario en la biblioteca
biblioteca.registrar_usuario(usuario1)

# Prestar un libro al usuario
biblioteca.prestar_libro("001", "978-84-376-0494-7")

# Listar los libros prestados al usuario
biblioteca.listar_libros_prestados("001")

# Devolver un libro a la biblioteca
biblioteca.devolver_libro("001", "978-84-376-0494-7")

