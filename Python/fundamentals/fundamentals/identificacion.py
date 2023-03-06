""" Declaración de variables
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
"""
""" Careación de arreglo
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
fruit = ('blueberry', 'strawberry', 'banana')
"""


person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Objeto

print(type(fruit)) # Imprime el tipo de variable mencionado
print(pizza_toppings[1]) # Imprime el índice 1 del arreglo mencionado
pizza_toppings.append('Mushrooms') # Agrega un elemento al final del arreglo (como push() en Javascript)
print(person['name']) # Muestra en la consola el atributo 'name' del objeto mencionado
person['name'] = 'George' # Modifica el atributo seleccionado
person['eye_color'] = 'blue' # Modifica el atributo seleccionado
print(fruit[2]) # Imprime el índice 2 del arreglo fruta

if num1 > 45: # Condicionales
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # Loop definido
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # Loop indefinido
    print(x)
    x += 1

pizza_toppings.pop() # Elimina el primer valor del arreglo
pizza_toppings.pop(1) # Elimina del arreglo al elemento con índice #1

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # Función
    for num in range(10):
        print('Hello')

print_hello_ten_times() # Se llama a la función

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)