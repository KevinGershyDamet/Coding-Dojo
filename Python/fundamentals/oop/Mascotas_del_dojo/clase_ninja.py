
class Ninja:
    
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        print('Soy', self.nombre, 'y estoy sacando a pasear a mi', self.mascota.tipo, self.mascota.nombre)
        self.mascota.jugar()

    def alimentar(self):
        print('Estoy alimentando a mi mascota, que se llama',self.mascota.nombre)
        self.mascota.comer()
    
    def bañar(self):
        print('Estoy bañando a mi mascota')

if __name__ == "__main__":
    print("Archivo ejecutado directamente")
else:
    print("Archivo:", __name__)
