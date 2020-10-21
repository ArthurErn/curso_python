import re
expr = re.compile(r'\.')

#exercicio 1

print("informe um numero inteiro")
inteiro = input()


while expr.search(inteiro):
    print("por favor digite um valor inteiro")
    inteiro = input()

soma = int(inteiro) % 2

if soma == 0:
    print("voce tem um numero par")

else:
    print("voce tem um numero impar")
