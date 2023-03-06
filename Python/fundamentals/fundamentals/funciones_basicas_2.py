
def cuenta_regresiva(tope):
    arreglo = []
    for x in range(tope,-1,-1):
        arreglo.append(x)
    return arreglo

print(cuenta_regresiva(8))



def imp_y_dev(valor1,valor2):
    print(valor1)
    return valor2

print(imp_y_dev(1,5))



def sumando(lista):
    return lista[0] + len(lista)

print(sumando([10, 3, 7, 8]))



def lista_nueva(lista):
    nuevo = []
    if len(lista) < 2:
        print('La lista debe tener al menos dos elementos')
        return
    else:
        for x in lista:
            if x > lista[1]:
                nuevo.append(x)
    print(len(nuevo))
    if len(nuevo) < 2:
        return False
    else:
        return nuevo

print(lista_nueva([3,2,5,6]))



def largo_valor(a,b):
    arreglo = []
    for x in range(0,a):
        arreglo.append(b)
    return arreglo

print(largo_valor(5,2))