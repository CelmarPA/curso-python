""" Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o
    menor peso lidos.

    Peso da 1ª pessoa: 85.6
    Peso da 2ª pessoa: 90.2
    Peso da 3ª pessoa: 18.9
    Peso da 4ª pessoa: 70.7
    Peso da 5ª pessoa: 65.5

    O maior peso lido foi de 90.2kg
    O menor peso lido foi de 48.9Kg """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Maior e Menor da Sequência ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
maior = 0
menor = 0

# Solicita os peso das 5 pessoas ao usuário
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa (kg): '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior}kg. \n'
      f'O menor peso lido foi {menor}kg.')
