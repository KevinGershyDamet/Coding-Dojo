
class tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        return self

    def vender_producto(self, id): # Primeras entradas, primeras salidas
        for x in range(0, len(self.productos)):
            if self.productos[x].id == id:
                self.productos.pop(x).print_info()
                return self

    def inflacion(self, porcentaje):
        for x in self.productos:
            x.actualizar_precio(porcentaje, True)
        return self

    def liquidacion(self, categoría, porcentaje):
        for x in self.productos:
            if x.categoría == categoría:
                x.actualizar_precio(porcentaje,False)
        return self





