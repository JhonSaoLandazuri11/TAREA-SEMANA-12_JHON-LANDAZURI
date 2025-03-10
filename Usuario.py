import json

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {[libro.info[0] for libro in self.libros_prestados]}"

    def to_dict(self):
        return {"nombre": self.nombre, "id_usuario": self.id_usuario, "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]}