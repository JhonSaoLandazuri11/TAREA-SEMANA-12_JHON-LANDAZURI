import json

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable con título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

    def to_dict(self):
        return {"titulo": self.info[0], "autor": self.info[1], "categoria": self.categoria, "isbn": self.isbn}