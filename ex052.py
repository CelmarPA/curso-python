""" Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

    Digite um número: 10
    1 2 3 4 5 6 7 8 9 10
    O número 10 foi divisível 4 vezes
    Por isso ele NÂO É PRIMO!

    Digite um número: 13
    1 2 3 4 5 6 7 8 9 10 11 12 13
    O número 13 foi divisível 2 vezes
    Por isso ele É PRIMO! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Números Primos ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usuário
num = int(input('Digite um número: '))

# Inicialização de variáveis
count = 0

# Verifica se o número é primo
for i in range(1, num + 1):
    if num % i == 0:
        print(f'{cores["yellow"]}{i} {cores["reset"]}', end='')
        count += 1
    else:
        print(f'{cores["red"]}{i} {cores["reset"]}', end='')

print(f'\nO número {num} foi divisível {count} vezes.')

if count == 2:
    resp = 'É PRIMO!'
else:
    resp = 'NÃO É PRIMO!'

print(f'E por isso ele {resp}')
