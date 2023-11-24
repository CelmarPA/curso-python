""" Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.

    Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    Qual é a sua jogada? 0
    JO
    KEN
    PO!!!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Computador jogou Tesoura
    Jogador jogou Pedra
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    JOGADOR VENCE

    Qual é a sua jogada? 1
    JO
    KEN
    PO!!!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Computador jogou Papel
    Jogador jogou Papel
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    EMPATE """

# Importação de bibliotecas
from random import randint
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" GAME: Pedra, Papel e Tesoura ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Imprime as opções
print(f'Suas opções: \n'
      f'[ 0 ] PEDRA \n'
      f'[ 1 ] PAPEL \n'
      f'[ 2 ] TESOURA')

# Solicita a jogada ao usuário
jogador = int(input('Qual é a sua jogada? '))

# Gera a jogada do computador
computador = randint(0, 2)

# Inicialização de variáveis
jogada_jog = ''
jogada_comp = ''
vitoria = ''

# Avalia o vencedor
if jogador == 0:
    jogada_jog = 'Pedra'
    if computador == 2:
        jogada_comp = 'Tesoura'
        vitoria = 'JOGADOR VENCE'
    elif computador == 1:
        jogada_comp = 'Papel'
        vitoria = 'COMPUTADOR VENCE'
    else:
        jogada_comp = jogada_jog
        vitoria = 'EMPATE'
elif jogador == 1:
    jogada_jog = 'Papel'
    if computador == 0:
        jogada_comp = 'Pedra'
        vitoria = 'JOGADOR VENCE'
    elif computador == 2:
        jogada_comp = 'Tesoura'
        vitoria = 'COMPUTADOR VENCE'
    else:
        jogada_comp = jogada_jog
        vitoria = 'EMPATE'
elif jogador == 2:
    jogada_jog = 'Tesoura'
    if computador == 1:
        jogada_comp = 'Papel'
        vitoria = 'JOGADOR VENCE'
    elif computador == 0:
        jogada_comp = 'Pedra'
        vitoria = 'COMPUTADOR VENCE'
    else:
        jogada_comp = jogada_jog
        vitoria = 'EMPATE'
else:
    print(f'{cores["red"]}Jogada inválida! Tente novamente!')
    exit()
# Imprime resultado
sleep(0.5)
print(f'JO')
sleep(0.5)
print(f'KEN')
sleep(0.5)
print(f'PO!!!')

print(f'-=-' * 10)
print(f'Computador jogou {jogada_comp} \n'
      f'Jogador jogou {jogada_jog}')
print(f'-=-' * 10)
print(vitoria)
