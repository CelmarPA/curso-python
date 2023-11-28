""" Desafio 046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
    indo de 10 até 0, com uma pausa de 1 segundo entre eles.
    10 9 8 7 6 5 4 3 2 1 0 BUM! BUM! POOOW!    """

# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Contagem Regressiva ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Contagem regressiva
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'BUM! BUM! POOOW!')
