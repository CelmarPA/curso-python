""" Desafio 048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
    encontram no intervalo de 1 até 500.
    A soma de todos os 83 valores solicitados é 20667 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Contagem de Pares ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma = 0
count = 0
# Define os múltiplos de 3 e realiza a soma
for c in range(1, 501, 2):  # Conta apenas os números ímpares
    if c % 3 == 0:
        soma += c
        count += 1
print(f'A soma de todos os {count} valores solicitados é {soma}!')
