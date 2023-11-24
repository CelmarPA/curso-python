""" Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
    cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

    Qual é a distância da sua viagem? 150
    Você está prestes a começar um viagem de 150.0km.
    E o preço da sua passagem será de R$75.00

    Qual é a distância da sua viagem? 210
    Você está prestes a começar um viagem de 210.0km.
    E o preço da sua passagem será de R$94.50  """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Custo da Viagem ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita a distância da viagem ao usuário
dist = float(input('Qual é a distancia da sua viagem? '))

# Verifica a distância e calcula o valor
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45

# Imprime o resultado
print(f'Você está prestes a começar uma viagem de {dist}km.')
print(f'E o preço da sua passagem será de R${valor:.2f}!')
