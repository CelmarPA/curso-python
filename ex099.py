""" Desafio 099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
    inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Analisando os valores passados...
    2 9 4 5 7 1 Foram informados 6 valores ao to-do.
    O maior valor informado foi 9. """

# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Função que Descobre o Maior ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


# Função
def maior(*valores):
    print(f'-=' * 30)
    print(f'Analisando os valores passados...')
    sleep(1.0)
    count = maior_v = 0
    for valor in valores:
        print(f'{valor} ', end='')
        sleep(0.3)
        if count == 0:
            maior_v = valor
        else:
            if valor > maior_v:
                maior_v = valor
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior_v}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
