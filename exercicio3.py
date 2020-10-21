#exercicio 3

print("qual o seu nome")
nome = input()
tamanho = len(nome)

if tamanho > 0 and tamanho < 5:
    print("seu nome é curto")

elif tamanho > 4 and tamanho < 7:
    print("seu nome é normal")

elif tamanho > 6:
    print("Seu nome é longo")

else:
    print("por favor tente novamente")