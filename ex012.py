""" Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

    Qual é o preço do produto? R$123.95
    O produto que custava R$123.95, na promoção com desconto de 5% vai custar R$117.75! """

# Solicita o valor ao usuário
valor = float(input('Qual é o preço do produto? R$'))

# Calcula o desconto de 5%
desconto = valor - (valor * 5 / 100)

# Imprime o resultado
print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}!')
