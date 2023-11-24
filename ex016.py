""" Desafio 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a
    sua porção Inteira.

    Digite um número: 6.127
    O número 6.127 tem a parte Inteira 6. """

# Importação de biblioteca
from math import trunc

# Solicita um número ao usuário
num = float(input('Digite um número: '))

# Imprime o resultado
print(f'O número {num} tem a parte Inteira {trunc(num)}.')
