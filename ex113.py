""" Desafio 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
    digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

    Digite um número inteiro: 7
    Digite um número real: 5.5
    O valor inteiro digitado foi 7 e o real foi 5.5

    ERRO: por favor digite um número inteiro válido.
    Digite um número inteiro:
    ERRO: por favor digite um número real válido.
    Digite um número real:
    Usuário preferiu não digitar esse número. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Funções Aprofundadas em Python ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


# Funções
def leiaInt(n):
    while True:
        try:
            num = str(input(n)).strip()
            valor = int(num)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            quit(print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m'))
    return valor


def leiaFloat(n):
    while True:
        try:
            num = str(input(n)).strip().replace(',', '.')
            valor = float(num)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            quit(print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m'))

    return valor


# Programa principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

