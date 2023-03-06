
class producto:

    productos = []

    def __init__(self, nombre, precio, categoría):
        self.nombre = nombre
        self.precio = float(precio)
        self.categoría = categoría
        self.id = len(producto.productos) + 1
        producto.productos.append(self)

    def actualizar_precio(self, cambio_porcentaje, está_elevado):
        if está_elevado is True:
            self.precio += self.precio*(cambio_porcentaje/100)
        else:
            self.precio -= self.precio*(cambio_porcentaje/100)

    def print_info(self):
        print('Product:',self.nombre, '| Price:', self.precio, 'USD | Type:', self.categoría)

