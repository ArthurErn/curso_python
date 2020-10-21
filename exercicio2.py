#exercicio 2

print("informe o valor de hora atual")
hora = int(input())

if hora >= 0 and hora <= 11:
    print("Bom dia")

elif hora >= 12 and hora <= 17:
    print("Boa tarde")

elif hora >= 18 and hora <= 23:
    print("Boa noite")

else:
    print("por favor insira um valor entre 0 e 23")
