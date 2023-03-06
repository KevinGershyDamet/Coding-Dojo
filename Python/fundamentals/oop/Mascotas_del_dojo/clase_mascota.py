
class Mascota:

    def __init__(self, nombre, tipo, golosinas, salud, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
    
    def dormir(self):
        print('Soy',self.nombre,'y estoy durmiendo')
    
    def comer(self):
        print('Soy',self.nombre,'y estoy comiendo')

    def jugar(self):
        print('Soy',self.nombre,'y estoy jugando')

    def sonido(self):
        print('Soy',self.nombre,'y estoy haciendo un sonido')



class De_contrabando(Mascota):

    def __init__(self, nombre, tipo, golosinas, salud, energia, cuidado_especial, comida_rara):
        super().__init__(nombre, tipo, golosinas, salud, energia)
        self.cuidado_especial = cuidado_especial
        self.comida_rara = comida_rara
    
    def aviso(self):
        import random
        lugares = ['una selva peligrosa', 'un desierto caluroso', 'las profundidades del océano', 'otro planeta']
        print('Vengo de contrabando. Me secuestraron de', lugares[random.randint(0,3)])



if __name__ == "__main__":
    print("Archivo ejecutado directamente")
else:
    print("Archivo:", __name__)