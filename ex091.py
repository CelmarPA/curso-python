""" Desafio 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
    maior número no dado.

    Valores sorteados:
        O jogador1 tirou 6
        O jogador2 tirou 1
        O jogador3 tirou 6
        O jogador4 tirou 5
    Ranking dos jogadores:
        1º lugar: jogador1 com 6
        2º lugar: jogador3 com 6
        3º lugar: jogador4 com 5
        4º lugar: jogador2 com 1 """

# Importação de bibliotecas
from random import randint
from operator import itemgetter
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Jogo de Dados ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários e listas
dados = dict()
ranking = list()

# Realiza as jogadas de cada jogador
for c in range(1, 5):
    dados[f'    jogador{c}'] = randint(1, 6)

print(f'Valores sorteados:')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Faz o racking
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
# ranking = sorted(dados.items(), key=lambda x: x[1], reverse=True)

print(f'Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
