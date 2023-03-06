
class CuentaBancaria:

    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, tasa_int, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def retirar(self, amount):
        if CuentaBancaria.puede_retirar(self.balance, amount):
            self.balance += -amount
        else:
            print('fondos insuficientes')
        return self

    # método de clase para cambiar el nombre del banco - NO SE PUEDE ACCEDER A ATRIBUTOS DE INSTANCIA AQUÍ
    @classmethod
    def cambiar_nombre_banco(cls,name):
        cls.nombre_banco = name
        
    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase 
        for account in cls.todas_las_cuentas:
            sum += account.balance
        return sum
    
    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

Interbank = CuentaBancaria(0.1, 100)
BCP = CuentaBancaria(0.2,10500)

print(CuentaBancaria.todas_las_cuentas)
print(CuentaBancaria.todos_los_balances())
BCP.nombre_banco = 'BCP'
print(BCP.nombre_banco)

CuentaBancaria.cambiar_nombre_banco('BCP')
print(Interbank.nombre_banco)



