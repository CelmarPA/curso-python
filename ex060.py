""" Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

    5! = 5 x 4 x 3 x 2 x 1 = 120

    Digite um número para
    calcular o seu Fatorial: 6
    Calculando 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720 """

# Importação de bibliotecas
from math import factorial

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Cálculo do Fatorial ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

print(f'Digite um número para ')

# Solicita um número ao usuário
num = int(input('calcular o seu Fatorial: '))

# Inicialização de variáveis
c = num

# Calculo do fatorial
fatorial = factorial(num)

print(f'{num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else f' = ', end='')
    c -= 1

print(f'{fatorial}')

i = num
f = 1
print(f'{num}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    print(f' x ' if i > 1 else f' = ', end='')
    f *= i
    i -= 1

print(f'{f}')
