from Usuario import Usuario
from Libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.usuarios = {}  # Diccionario de ID de usuario a objeto Usuario

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario dado de baja: {usuario.nombre}")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("Este usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Inicialización con libros y usuarios preexistentes
biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro("1984", "George Orwell", "Ficción", "123456"))
biblioteca.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "789101"))
biblioteca.registrar_usuario(Usuario("Carlos Pérez", "001"))