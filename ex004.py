""" Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as
    informações possíveis sobre ele. """

# Solicita algo ao usuário
n = input("Digite algo: ")

# Verifica as informações
print(f'O valor digite é do tipo primitivo {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
