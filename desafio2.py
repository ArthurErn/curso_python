aux = 10

for num in range(9):
    print(num, end=' ')
    for num2 in range(9):
        print(aux)
        aux -= 1
        break

print(2*'=')

numero = 0
numero2 = 10

while numero < 9:
    print(numero, end=' ')
    numero += 1
    while numero2 >= 2:
        print(numero2)
        numero2 -= 1
        break

print(2*'=')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)










