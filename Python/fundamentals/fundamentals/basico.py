
# Pass se puede colocar en bloques de código en donde aún falta realizar desarrollo (al inicio de cada bloque debe haber necesariamente una línea de código como mínimo)

tupla = (1,2,'hola') #inmutable
lista = [1, 2, 'hola'] #sí es posible cambiar sus valores

print(lista[2])
lista[1] = 5
print(lista)

persona = {'nombre': 'Kev', 2: 4, 'escuela': 'UP'}
print(persona['nombre'])

print(type(1.4))

print(len(lista))

import random
rand_num = random.randint(2,5)
print(rand_num)

print(type(1j))


name = 'Kev'
print('me llamo',name) # La coma insertará automáticamente un espacio entre ambos componentes
print('me llamo'+name)

# Para concatenar texto con números, se recomienda usar comas


x = 1
y = 'holalalalalalal'
print(y+str(x))
z= '3'
print(x+int(z))

print(f'me llamo {name} y me encanta sumar {x} con {y} y que dé resultados buenos')
# Otra forma más antigua:
print('hola soy {} y me encanta{} y además {}'.format(name, x, y))
# Aún más antiguo
print("Mi nombre es %s y tengo %d" % (name, x))


print(y.title()) # Devuelve las primeras letras de cada palabra en mayúsculas
print(y.upper())
print(y.lower())
print(y.count('la')) # Cuenta cuántas veces aparece la cadena ahí
print(y.split())
print(y.find('h'))
print(y.endswith('la'))

lista_rara = ['hola','chau',1,'uno']
print(2*lista_rara)

lista_rara.append(1)
print(lista_rara)

print(lista_rara[2:])
print(len(lista_rara))

print(min([1,1,2,3,5]))
print(sorted([4,1,2,7,4]))

print(lista_rara.pop(3))
print(lista_rara.index('hola'))



findesemana = {"Dom": "Domingo", "Sáb": "Sábado"} # notación literal
capitales = {} # crea un diccionario vacío y luego agrega valores
capitales["svk"] = "Bratislava"
capitales["deu"] = "Berlin"
capitales["dnk"] = "Copenhagen"

print(capitales["svk"])
print(findesemana["Dom"])

value_removed = capitales.pop('svk') # eliminará la clave 'svk' y devolverá su valor
del capitales['dnk'] # eliminará la clave y no devolverá nada

print(len(findesemana))

print(findesemana.items())

x = 20
if x > 15:
    print('mayor que 15')
elif x > 5:
    print('mayor que 5')


for x in range(0, 8, 2):
    print(x)
# salida: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# salida: 5, 2

for x in 'Hello':
    print(x)
# salida: 'H', 'e', 'l', 'l', 'o'

mi_lista = ["abc", 123, "xyz"]
for i in range(0, len(mi_lista)):
    print(i, mi_lista[i])
# salida: 0 abc, 1 123, 2 xyz
    
# O 
    
for v in mi_lista:
    print(v)
# salida: abc, 123, xyz

mi_dicc = { "name": "Noelle", "languaje": "Python" }
for k in mi_dicc:
    print(mi_dicc[k])
# salida: Noelle, Python


for count in range(0,5):
    print("looping =", count)


count = 0
while count <= 5:
    print("looping - ", count)
    count += 1


y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Sentencia else final")

# continue se usa para pasar a la siguiente iteración


x = [1,2,3]
x += [0]
print(x)

y = 3
if not y:
    print('hola')
    print(not y)


def funcion1(a,b):
    x = a**2 + 2*a - b
    return x

print(funcion1(3,4))


def saludo(nombre = '', apellido = '', edad = '15', profesion = 'economista'):
    print(f'Hola {nombre} {apellido}, soy {profesion} y tengo {edad} años')



print(saludo('Kev','H'))


def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())





b = 500
def foobar():
    b = 300
    print(b)
    return 500

foobar() # 300, 300

def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo() # toma el valor de 10, pero muestra 1, 3, 5
print(y) # 10
