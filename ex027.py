""" Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente.

    Digite seu nome completo: Pedro da Silva Moreira
    Muito prazer em te conhecer!
    Seu primeiro nome é Pedro
    Seu último nome é Moreira """

# Solicita um nome ao usuário
nome = str(input('Digite seu nome completo: ')).strip()

# Cria uma lista do nome
lista = nome.split()

# Imprime o resultado
print(f'Muito prazer em te conhecer! \n'
      f'Seu primeiro nome é {lista[0]} \n'
      f'Seu último nome é {lista[-1]}')
print(f'Seu último nome é {lista[len(lista) - 1]}')
