""" Desafio 071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
    qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
    serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

    ================================
                BANCO CEV
    ================================
    Qual valor você quer sacar? R$1234
    Total de 24 cédulas de R$50
    Total de 1 cédulas de R$20
    Total de 1 cédulas de R$10
    Total de 4 cédulas de R$1
    ================================
    Volte sempre ao BANCO CEV! Tenha um bom dia! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Simulador de Caixa Eletrônico ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Imprime o enunciado
print(f'{cores["blue"]}={cores["reset"]}' * 40)
print(f'{cores["green"]}{" BANCO CEV ":^40}{cores["reset"]}')
print(f'{cores["blue"]}={cores["reset"]}' * 40)

# Solicita ao usuário o valor a ser sacado
valor = int(input('Qual valor você quer sacar? R$ '))

# Inicialização de variáveis
total = valor
ced = 50
totalced = 0

while True:

    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced:.2f}!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print(f'{cores["yellow"]}={cores["reset"]}' * 40)
print(f'Volte sempre ao {cores["red"]}BANCO CEV{cores["reset"]}! Tenha um bom dia!')