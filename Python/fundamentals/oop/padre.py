local_val = "unicornios mágicos"

def square(x):
    return x * x

class Usuario:

    def __init__(self, name):
        self.name = name

    def di_hola(self):
        return "hola"

print(__name__)

if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)

