""" Desafio 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

    Qual é a velocidade atual do carro? 30
    Tenha um bom dia! Dirija com segurança!

    Qual é a velocidade atual do carro? 120
    MULTADO! Você excedeu o limite permitido que é de 80km/h
    Você deve pagar uma multa de R$280.00!
    Tenha um bom dia! Dirija com segurança!

"""

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Radar Eletrônico ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita a velocidade ao usuário
vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    exc = vel - 80
    multa = exc * 7
    print(f'{cores["red"]}MULTADO! Você excedeu o limite permitido que é de 80km/h! \n'
          f'Você deve pagar uma multa de{cores["reset"]} {cores["yellow"]}R${multa:.2f}!{cores["reset"]}')
    print(f'{cores["yellow"]}Tenha um bom dia! Dirija com segurança!')
else:
    print(f'{cores["yellow"]}Tenha um bom dia! Dirija com segurança!')
