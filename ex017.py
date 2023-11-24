""" Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
    retângulo. Calcule e mostre o comprimento da hipotenusa.

    Comprimento do cateto oposto: 3,5
    Comprimento do cateto adjacente: 4,75
    A hipotenusa vai medir 5,90. """

# Importação de bibliotecas
from math import sqrt, pow


# Solicita os dados ao usuário
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# Calcula a hipotenusa
hi = sqrt(pow(co, 2) + pow(ca, 2))
# hi = sqrt(co**2 + ca**2)

# Imprime o resultado
print(f'A hipotenusa vai medir {hi:.2f}!')

""" Outra forma de resolver com função hypot """

# Importação de biblioteca
from math import hypot

# Calcula a hipotenusa
hipo = hypot(co, ca)

# Imprime resultado
print(f'A hipotenusa vai medir {hipo:.2f}!')
