""" Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

    Informe um número: 3234
    Analisando o número 3234
    Unidade: 4
    Dezena 3
    Centena: 2
    Milhar: 3 """

# Solicita um número de 0 a 9999 ao usuário
num = int(input('Informe um número: '))

# Define as unidades, dezenas, centenas e milhar
unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print(unidade)
print(dezena)
print(centena)
print(milhar)
