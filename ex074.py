""" Desafio 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre
    a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

    O valores sorteados foram: 5 7 5 4 6
    O maior valor sorteado foi 7
    O menor valor sorteado foi 4 """

# Importação de bibliotecas
from random import randint, sample
# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Maior e Menor Valores ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Gera uma tupla com 5 número aleatórios
num = tuple(sample(range(10), 5))

# Imprime os resultados
print(f'O valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print('')
# O maior valor
print(f'O maior valor sorteado foi {max(num)}')

# O menor valor
print(f'O menor valor sorteado foi {min(num)}')

print(f'')

# Outra solução

# Gera uma tupla com 5 número aleatórios
# num = tuple(randint(1, 10) for i in range(5))
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# Imprime os resultados
print(f'O valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print('')
# O maior valor
print(f'O maior valor sorteado foi {max(num)}')

# O menor valor
print(f'O menor valor sorteado foi {min(num)}')
