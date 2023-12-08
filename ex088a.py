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

# Inicialização de variáveis
tot = 1

# Inicialização de lista
lista = list()
jogos = list()

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    # Imprime os jogos sorteados
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2, end='')
print(f'{cores["green"]}{f" SORTEANDO {len(jogos)} JOGOS "}{cores["reset"]}', end='')
print(f'{cores["lilas"]}-=-=-{cores["reset"]}' * 2)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'{cores["lilas"]}-=-=-={cores["reset"]}' * 2, end='')
print(f'{cores["green"]}{f" < BOA SORTE! > "}{cores["reset"]}', end='')
print(f'{cores["lilas"]}-=-=-={cores["reset"]}' * 2)
