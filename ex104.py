""" Desafio 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input()
    do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

    ----------------------
    Digite um número: 4

    # Programa principal
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o número {n}.') """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Validando Entrada de Dados em Python ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


# Função
def leiaInt(num):
    while num.isnumeric() is False:
        print(f'\033[91mERRO! Digite um número inteiro válido.\033[0m')
        num = str(input('Digite um número: '))
    return int(num)


# Programa principal
print(f'-' * 30)
n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')
