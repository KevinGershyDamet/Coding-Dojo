

################## Número 1 ##################

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z[0]['y'] = 30
print(z)


################## Número 2 ##################

def recorre_diccionarios(lista):
    for x in range(0,len(lista)):

        llaves = list(lista[x].keys())
        valores = list(lista[x].values())
        texto = ''

        for x in range(0,len(llaves)):
            texto += llaves[x] + ' - ' + valores[x]
            
            if x != len(llaves) - 1:
                texto += ', '
        
        print(texto)

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

recorre_diccionarios(estudiantes)


################## Número 3 ##################

def llave_diccionario(lista, llave):
    for x in lista:
        print(x[llave])

llave_diccionario(estudiantes, 'last_name')


################## Número 4 ##################

def printInfo(diccionario):
    for x in diccionario:
        print(len(diccionario[x]),' ',x.upper())
        for y in diccionario[x]:
            print(y)
        print('')

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

