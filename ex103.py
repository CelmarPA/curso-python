""" Desafio 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
    de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
    dado não tenha sido informado corretamente.

    ---------------------
    Nome do jogador: Romário
    Número de Gols: 33
    O jogador Romário fez 33 gol(s) no campeonato.

    ---------------------
    Nome do jogador:
    Número de Gols: 2
    O jogador <desconhecido> fez 2 gol(s) no campeonato.

    ---------------------
    Nome do jogador:
    Número de Gols:
    O jogador <desconhecido> fez 0 gol(s) no campeonato. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Ficha do Jogador ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)


# Função
def ficha(j='', gol=''):
    if j == '':
        j = '<desconhecido>'
    if gol == '':
        gol = 0
    return f'O jogador {j} fez {gol} gol(s) no campeonato.'


# Programa principal
print(f'-' * 30)
print(ficha(str(input('Nome do jogador: ')).strip(), str(input('Número de gols: ').strip())))
