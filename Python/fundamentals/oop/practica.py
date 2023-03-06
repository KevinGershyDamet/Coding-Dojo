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
            

class cuenta_extranjera(CuentaBancaria):

    def __init__(self, tasa, monto_inicial, banco, ganancia_extra):
        super().__init__(tasa, monto_inicial, banco)
        self.balance += ganancia_extra

    def retiro(amount):
        super().retiro(amount)


nueva = cuenta_extranjera(0.03, 3_000, 'Scotia', 1_500)
print(nueva.balance)


# # Primero se debe crear el archivo aritmética
# import aritmética
# print(aritmética.sumar(5, 8))
# print(aritmética.restar(10, 5))
# print(aritmética.multiplicar(12, 6)) 

# # para anular un comportamiento del padre, el hijo solo debe tener una función con el mismo nombre, pero que realice un objetivo diferente


# # Entradas y salidas
# color_favorito = input('¿Cuál es tu color favorito? ') # la entrada toma un prompt, que debe ser una cadena
# print(f'Tu color favorito is: {colo_favorito}') # salida, imprime el color dado en la consola
