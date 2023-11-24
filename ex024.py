""" Desafio 024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

    Em que cidade você nasceu? Rio de Janeiro
    False """

# Solicita o nome da cidade ao usuário
cidade = str(input("Em que cidade você nasceu? ")).strip().upper()

# Imprime se a cidade começa com Santo ou não
print('SANTO' in cidade.split()[0])
