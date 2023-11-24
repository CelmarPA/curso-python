""" Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

    Qual é seu nome completo? Mario da Silva Mendonça
    Seu nome tem Silva? True  """

# Solicita um nome ao usuário
nome = str(input('Qual é seu nome completo? ')).strip().upper()

# Imprime o resultado
print(f'Seu nome tem Silva? {'SILVA' in nome}')
