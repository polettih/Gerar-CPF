from random import randint

def gerar_cpf(formatado=False):
    nove_digitos = ''.join([str(randint(0, 9)) for _ in range(9)])

    soma_1 = sum(int(n) * i for n, i in zip(nove_digitos, range(10, 1, -1)))
    digito_1 = (soma_1 * 10 % 11) % 10

    soma_2 = sum(int(n) * i for n, i in zip(nove_digitos + str(digito_1), range(11, 1, -1)))
    digito_2 = (soma_2 * 10 % 11) % 10

    cpf = f'{nove_digitos}{digito_1}{digito_2}'

    if formatado:
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return cpf

# Exemplo de uso:
print(gerar_cpf(formatado=True))
