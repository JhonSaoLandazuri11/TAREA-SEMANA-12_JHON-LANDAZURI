from Usuario import Usuario
from Libro import Libro
import json

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.usuarios = {}  # Diccionario de ID de usuario a objeto Usuario
        self.cargar_datos()

    def guardar_datos(self):
        data = {
            "libros": [libro.to_dict() for libro in self.libros_disponibles.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }
        with open("biblioteca.json", "w") as f:
            json.dump(data, f, indent=4)

    def cargar_datos(self):
        try:
            with open("biblioteca.json", "r") as f:
                data = json.load(f)
                for libro in data.get("libros", []):
                    self.agregar_libro(Libro(libro["titulo"], libro["autor"], libro["categoria"], libro["isbn"]))
                for usuario in data.get("usuarios", []):
                    user = Usuario(usuario["nombre"], usuario["id_usuario"])
                    for libro in usuario["libros_prestados"]:
                        user.libros_prestados.append(Libro(libro["titulo"], libro["autor"], libro["categoria"], libro["isbn"]))
                    self.registrar_usuario(user)
        except FileNotFoundError:
            print("No se encontraron datos previos, iniciando biblioteca vacía.")

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        self.guardar_datos()
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.guardar_datos()
            print(f"Libro eliminado: {libro}")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            self.guardar_datos()
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            self.guardar_datos()
            print(f"Usuario dado de baja: {usuario.nombre}")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.guardar_datos()
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
                    self.guardar_datos()
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")


# Inicialización con libros y usuarios preexistentes
biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro("1984", "George Orwell", "Ficción", "123456"))
biblioteca.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "789101"))
biblioteca.registrar_usuario(Usuario("Carlos Pérez", "001"))