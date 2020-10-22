num = int(input("digite um numero"))


def is_par(num):
    if num % 2 == 0:
        return True


if is_par(num) == True:
    print("é par")
else:
    print("impar")