
# Pregunta 1

for x in range(0,151):
    print(x)

# Pregunta 2

for x in range(5,1001,5):
    print(x)

# Pregunta 3

for x in range(1,101):
    if x%10 is 0:
        print('Coding Dojo')
    elif x%5 is 0:
        print('Coding')
    else:
        print(x)

# Pregunta 4

x = 0
for i in range(1,500_000,2):
    x += i
print(x)

# Pregunta 5

for x in range(2018,0,-4):
    print(x)

# Pregunta 6

lowNum = 4
highNum = 10
mult = 3

for x in range(lowNum, highNum + 1, 1):
    if x%mult is 0:
        print(x)
