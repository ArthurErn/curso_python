import re
expr = re.compile(r'\d{3}?\.\d{3}?\.\d{3}?\-\d{2}$')

cpf = input("Digite um CPF: ")


def is_valid(cpf):
    if expr.search(cpf):
        print(f"{cpf} é válido")
    else:
        print(f"{cpf} é inválido")


is_valid(cpf)

