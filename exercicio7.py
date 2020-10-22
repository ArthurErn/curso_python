num = int(input("Digite um numero"))
porcentagem = int(input("Digite uma porcentagem"))


def soma_calc_percentual(val, percent):
    val = val + (val * (percent / 100))
    return val


print(soma_calc_percentual(num, porcentagem))
