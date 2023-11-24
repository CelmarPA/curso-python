""" Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
    dólares ela pode comprar.

    Quanto dinheiro você tem na carteira? R$19.88
    Com R$19,88 você pode comprar US$4.09 """

# Solicita o valor ao usuário
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))

# Calcula a quantidade de dolar que podem ser comprados
dol = dinheiro / 4.86

# Imprime o resultado
print(f'Com R${dinheiro:.2f} você pode comprar US${dol:.2f}.')
