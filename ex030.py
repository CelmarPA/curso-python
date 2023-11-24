""" Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

    Me diga um número qualquer: 5
    O número 5 é ÍMPAR! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Par ou Ímpar ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita um número ao usuário
num = int(input(f'{cores["lilas"]}Me diga um número qualquer: {cores["reset"]}'))

# Verifica se o número é par ou ímpar
if num % 2 == 0:
    print(f'O número {num} é {cores["blue"]}PAR{cores["reset"]}!')
else:
    print(f'O número {num} é {cores["blue"]}ÍMPAR{cores["reset"]}!')
