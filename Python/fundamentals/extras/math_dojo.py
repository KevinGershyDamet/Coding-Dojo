
class mate_dojo:

    def __init__(self):
        self.resultado = 0
    
    def suma(self, num1, *nums):
        self.resultado += num1
        for x in nums:
            self.resultado += x
        return self
    
    def resta(self, num1, *nums):
        self.resultado -= num1
        for x in nums:
            self.resultado -= x
        return self

total = mate_dojo()
x = total.suma(2).suma(2,5,1).resta(2,3).resultado
print(x)

total.resultado = 0
y = total.suma(1,5).resta(3,7).suma(10,1,1,1,1).resta(2,2,2,2).resultado
print(y)
