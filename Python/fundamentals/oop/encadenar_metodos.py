class Usuario:
    
    entidad_bancaria = 'Interbank'

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.age = edad
        self.balance_cuenta = 1_000
    
    def agregar_dinero(self, monto):
        self.balance_cuenta += monto
        return self

    def retirar_dinero(self, monto):
        self.balance_cuenta += -monto
        return self
    
    def mostrar_balance(self):
        print('Usuario: ' + self.nombre + ', Balance: $' + str(self.balance_cuenta))
        return self
    
    def transferir_dinero(self, contraparte, monto):
        self.balance_cuenta += -monto
        contraparte.balance_cuenta += monto
        return self
        

Martin = Usuario('Martín', 50)
Kevin = Usuario('Kevin', 27)
Clara = Usuario('Clara', 28)

Martin.agregar_dinero(20).agregar_dinero(250).agregar_dinero(972).mostrar_balance()
Kevin.agregar_dinero(10).agregar_dinero(500).retirar_dinero(40).retirar_dinero(12).mostrar_balance()
Clara.agregar_dinero(5).retirar_dinero(43).retirar_dinero(17).retirar_dinero(31).mostrar_balance()

Martin.transferir_dinero(Clara, 30)
print(Martin.balance_cuenta); print(Clara.balance_cuenta)