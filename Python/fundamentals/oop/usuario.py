class Usuario:
    
    entidad_bancaria = 'Interbank'

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.age = edad
        self.balance_cuenta = 1_000
    
    def agregar_dinero(self, monto):
        self.balance_cuenta += monto

    def retirar_dinero(self, monto):
        self.balance_cuenta += -monto
    
    def mostrar_balance(self):
        print('Usuario: ' + self.nombre + ', Balance: $' + str(self.balance_cuenta))
    
    def transferir_dinero(self, contraparte, monto):
        self.balance_cuenta += -monto
        contraparte.balance_cuenta += monto
        

Martin = Usuario('Martín', 50)
Kevin = Usuario('Kevin', 27)
Clara = Usuario('Clara', 28)

Martin.agregar_dinero(20); Martin.agregar_dinero(250); Martin.agregar_dinero(972); Martin.mostrar_balance()
Kevin.agregar_dinero(10); Kevin.agregar_dinero(500); Kevin.retirar_dinero(40); Kevin.retirar_dinero(12); Kevin.mostrar_balance()
Clara.agregar_dinero(5); Clara.retirar_dinero(43); Clara.retirar_dinero(17); Clara.retirar_dinero(31); Clara.mostrar_balance()

Martin.transferir_dinero(Clara, 30)
print(Martin.balance_cuenta); print(Clara.balance_cuenta)