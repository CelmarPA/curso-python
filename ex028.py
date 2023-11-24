""" Desafio 028 - Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
    usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
    usuário venceu ou perdeu.

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Vou pensar em um número entre 0 e 5. Tente adivinha...
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Em que número eu pensei? 3
    PROCESSANDO...
    GANHEI! Eu pensei no número 0 e não no 3!
    PARABÈNS! Você conseguiu me vencer!    """

# Importação de bibliotecas
from random import randint
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Jogo da Adivinhação v.1.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'')

print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Vou pensar em um número entre 0 e 5. Tente adivinhar... ":=^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usuário
num = int(input('Em que número eu pensei? '))

# Geral aleatóriamente um número entre 0 e 5
comp = randint(0, 5)

print(f'{cores["lilas"]}PROCESSANDO...{cores["reset"]}')

# Faz um delay de 3 segundo
sleep(1.5)

# Avalia quem venceu
if num != comp:
    print(f'{cores["red"]}GANHEI! Eu pensei no número {comp} e não no {num}!{cores["reset"]}')
else:
    print(f'{cores["yellow"]}PARABÉNS! Você conseguiu me vencer!')
