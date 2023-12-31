""" Desafio 088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
    jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

    ------------------------------------------
                JOGUE NA MEGA SENA
    ------------------------------------------
    Quantos jogos você quer que eu sorteie? 4
    -=-=--=-=- SORTEANDO 4 JOGOS -=-=--=-=-
    Jogo 1: [4, 8, 10, 20, 26, 38]
    Jogo 2: [4, 8, 10, 20, 26, 38]
    Jogo 3: [4, 8, 10, 20, 26, 38]
    Jogo 4: [4, 8, 10, 20, 26, 38]
    -=-=--=-=-=- < BOA SORTE! > -=-=--=-=-=-
    """

# Importação de bibliotecas
from random import randint
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Palpites Mega Sena ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'')

# Enunciando do programa
print(f'{cores["lilas"]}-{cores["reset"]}' * 40)
print(f'{cores["blue"]}{"JOGUE NA MEGA SENA":^40}{cores["reset"]}')
print(f'{cores["lilas"]}-{cores["reset"]}' * 40)

# Solicita a quantidade de jogos
quant = int(input('Quantos jogos você quer que eu sorteie? '))

# Inicialização de listas
jogos = [list([0, 0, 0, 0, 0, 0]) for _ in range(0, quant)]  # Iniciailiza a lista jogos com a quantidade de jogos

# Loop para geração dos números dos jogos
for c, j in enumerate(jogos):
    for i in range(0, 6):
        palpite = randint(1, 60)
        while palpite in j:
            palpite = randint(1, 60)
        jogos[c][i] = palpite

# Imprime os jogos sorteados
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2, end='')
print(f'{cores["green"]}{f" SORTEANDO {len(jogos)} JOGOS "}{cores["reset"]}', end='')
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2)
for k in range(0,  quant):
    print(f'{cores["blue"]}  Jogo {k + 1}: {sorted(jogos[k])}{cores["reset"]}')
    sleep(1)
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2, end='')
print(f'{cores["green"]}{f" < BOA SORTE! > "}{cores["reset"]}', end='')
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2)
