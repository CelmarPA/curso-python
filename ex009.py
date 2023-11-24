""" Desafio 009 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

    Digite um número para ver sua tabuada: 6
    ============
    6 x  1 = 6
    6 x  2 = 12
    6 x  4 = 24
    6 x  5 = 30
    6 x  6 = 36
    6 x  7 = 42
    6 x  8 = 48
    6 x  9 = 54
    6 x 10 = 60
    ============
    """
# Solicita um número ao usuário
num = int(input('Digite um número para ver sua tabuada: '))

# Imprime a tabuada
print(f'=' * 12)
print(f'{num} x  1 = {num * 1}')
print(f'{num} x  2 = {num * 2}')
print(f'{num} x  3 = {num * 3}')
print(f'{num} x  4 = {num * 4}')
print(f'{num} x  5 = {num * 5}')
print(f'{num} x  6 = {num * 6}')
print(f'{num} x  7 = {num * 7}')
print(f'{num} x  8 = {num * 8}')
print(f'{num} x  9 = {num * 9}')
print(f'{num} x 10 = {num * 10}')
print(f'=' * 12)
