""" Desafio 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
    número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
    tela o processo de cálculo do fatorial.

    # Programa principal
    print(fatorial(5))
    ---------------------
    120

    # Programa principal
    print(fatorial(5, show=True))
    ---------------------
    5 x 4 x 3 x 2 x 1 = 120

    help(fatorial) """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Função Para Fatorial ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


# Função
def fatorial(num, show=False):
    """
    Calcula o Fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não o processo de cálculo
    :return: O valor do Fatorial de uma número num
    """
    fat = 1
    print(f'-' * 30)
    for c in range(num, 0, -1):
        fat *= c
        if show is True:
            print(f'{c}{' x ' if c > 1 else ' = '}', end='')
    return fat


# Programa principal
print(fatorial(5))
print(fatorial(5, show=True))
print(help(fatorial))
