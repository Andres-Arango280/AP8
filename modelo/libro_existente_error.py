from tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias_libro):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias_libro = existencias_libro

    def __str__(self):
        return f"El libro con título '{self.titulo}' e ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias_libro}"
