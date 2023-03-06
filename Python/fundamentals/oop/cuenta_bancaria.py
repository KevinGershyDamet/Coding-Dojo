
class CuentaBancaria:

    cuentas_creadas = []

    def __init__(self, tasa = 0.01, monto_inicial = 0):
        self.tasa = tasa
        self.balance = monto_inicial
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


cuenta_BCP = CuentaBancaria(0.0425, 10_000)
cuenta_Interbank = CuentaBancaria(0.01, 35_000)

cuenta_BCP.deposito(300).deposito(50).deposito(180).retiro(310).generar_interes().mostrar_info_cuenta()
cuenta_Interbank.deposito(5000).deposito(2800).retiro(50).retiro(120).retiro(100).retiro(80).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()