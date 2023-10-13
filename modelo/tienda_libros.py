class TiendaLibros:
    def __init__(self):
        self.catálogo = {}
        self.carrito = CarroCompras()

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.isbn not in self.catálogo:
            print("El libro con ISBN {} no se encuentra en el catálogo.".format(libro.isbn))
            return

        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)