class CuentaBancaria:

    cuentas_creadas = []

    def __init__(self, tasa = 0.01, monto_inicial = 0, banco = 'BCP'):
        self.tasa = tasa
        self.balance = monto_inicial
        self.banco = banco
        CuentaBancaria.cuentas_creadas.append(self)
    
    def deposito(self, monto):
        self.balance += monto
        return self
    
    def retiro(self, monto):
        self.balance -= monto
        return self
    
    def mostrar_info_cuenta(self):
        print('Balance: $',self.balance)
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa
        return self
    
    @classmethod
    def imprimir_cuentas(cls):
        for x in cls.cuentas_creadas:
            print('Balance: $', x.balance)


class Usuario:
    
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.age = edad
        self.cuenta = []
    
    def crear_cuenta(self, tasa, monto, banco):
        self.cuenta.append(CuentaBancaria(tasa, monto, banco))
    
    def deposito(self, monto, numero): # el parámetro cuenta indica el orden de cuenta a modificar (en orden de creación)
        self.cuenta[numero - 1].deposito(monto)
        return self
    
    def retiro(self, monto, numero):
        self.cuenta[numero - 1].retiro(monto)
        return self

Kev = Usuario('Kev', 27)
Kev.crear_cuenta(0.0425, 30_000, 'Interbank')
Kev.crear_cuenta(0.01, 500, 'BCP')

print(Kev.cuenta[0].banco, ': $', Kev.cuenta[0].balance, ' | ', Kev.cuenta[1].banco, ': $', Kev.cuenta[1].balance)
Kev.deposito(3000, 2).retiro(500, 2).deposito(2000, 1)
print(Kev.cuenta[0].banco, ': $', Kev.cuenta[0].balance, ' | ', Kev.cuenta[1].banco, ': $', Kev.cuenta[1].balance)


