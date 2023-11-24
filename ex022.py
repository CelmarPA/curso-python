""" Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:

    – O nome com todas as letras maiúsculas e minúsculas.

    – Quantas letras ao to-do (sem considerar espaços).

    – Quantas letras tem o primeiro nome.

    Digite seu nome completo: Paulo de Souza Marques
    Analisando seu nome...
    Seu nome em maiúsculas é PAULO DE SOUZA MARQUES
    Seu nome em minúsculas é paulo de souza marques
    Seu nome tem ao to-do 19 letras
    Seu primeiro nome é Paulo e ele tem 5 letras """

# Solicita o nome ao usuário
nome = str(input('Digite seu nome completo: ')).strip()

print(f'Analisando seu nome...')

# Imprime o nome em maiúsculas
print(f'Seu nome em maiúsculas é {nome.upper()}')

# Imprime o nome em minúsculas
print(f'Seu nome em minúsculas é {nome.lower()}')

# Imprime a quantidade de letras do nome
print(f'Seu nome tem ao todo {len(nome.replace(' ', ''))} letras')
# print(f'Seu nome tem ao to-do {len(nome) - nome.count} letras')

# Imprime o primeiro nome e quantidade de letras
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')
# print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {nome.find(' '} letras
