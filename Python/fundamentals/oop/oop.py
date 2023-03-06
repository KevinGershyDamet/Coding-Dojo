# declarar una clase y darle el nombre Usuario
class Usuario:

    nombre_banco = 'BCP' # Este atributo puede cambiar a nivel de ocurrencia, pero también a nivel de la clase total

    def __init__(self): # Estos atributos podrán cambiar para cada ocurrencia de la clase
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

kev = Usuario(); kev.name = 'Kevin'
print(kev.name)

print(kev.nombre_banco)
kev.nombre_banco = 'Interbank'
print(kev.nombre_banco)
Usuario.nombre_banco = 'Scotiabank'
kev = Usuario()
print(kev.nombre_banco)


class persona:
    
    entidad_bancaria = 'Interbank'

    def __init__(self, nombre, edad, correo):

        self.nombre = nombre
        self.age = edad
        self.correo = correo
        self.balance_cuenta = 1_000
    
    def agregar_dinero(self, monto):
        self.balance_cuenta += monto

Kevin = persona('Kev',27,'kevin.gershydamet@gmail.com')
print(Kevin.age); print(Kevin.balance_cuenta)
Kevin.agregar_dinero(15)
print(Kevin.balance_cuenta)
