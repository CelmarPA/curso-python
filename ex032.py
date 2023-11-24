""" Desafio 034 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

    Que ano quer analisar? Coloque 0 para analisar o ano atual: 2000
    O ano 2000 é BISSEXTO!

    Que ano quer analisar? Coloque 0 para analisar o ano atual: 1990
    O ano 1990 NÂO é BISSEXTO! """

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Ano Bissexto ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita o ano ao usuário
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Obtém o ano atual do sistema
atual = datetime.now().year

if ano == 0:
    ano = atual

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÂO é BISSEXTO!')
