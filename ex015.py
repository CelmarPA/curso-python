""" Desafio 015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
    de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
    por km rodado.

    Quantos dias alugados? 8
    # Quantos km rodados? 720
    O total a pagar é de R$588.00! """

# Solicita os dados ao usuário
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

# Calcula o valor a se pagar
diarias = dias * 60
rodados = km * 0.15
total = diarias + rodados

# Imprime o resultado
print(f'O total a pagar é de R${total:.2f}!')
