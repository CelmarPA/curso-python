""" Desafio 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
    todos os valores pares sorteados pela função anterior.

    Sorteando 5 valores da lista: 5 7 9 2 4 PRONTO!
    Somando so valores pares de [5, 7, 9, 2, 4], temos 6 """

# Importação de Bibliotecas
from random import randint
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Funções Para Sortear e Somar ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)


# Funções para sorteio e funcção para soma
def sortear():
    valores = []  # Cria uma lista vazia para os valores sorteados
    print(f'Sorteando 5 valores da lista: ', end='')
    # Loop para sorteio dos valores
    for i in range(0, 5):
        valor = randint(1, 10)
        valores.append(valor)
        print(f'{valor} ', end='')
        sleep(0.5)
    print(f'PRONTO!')
    # Chama a função para somar os valores pares da lista sorteada
    somapar(valores)


def somapar(val):
    soma = 0  # Inicializa a variável soma
    # Loop para soma dos valores pares
    for v in val:
        if v % 2 == 0:
            soma += v
    sleep(0.5)
    print(f'Somando os valores pares de {val}, temos {soma}.')


# Programa Principal
sortear()  # Chama a função sortear
