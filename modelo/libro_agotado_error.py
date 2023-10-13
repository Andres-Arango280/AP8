from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con título '{self.titulo}' e ISBN {self.isbn} está agotado."
