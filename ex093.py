""" Desafio 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
    do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
    tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

    Nome do jogador: Joelson
    Quantas partidas Joelson jogou? 5
    Quantos gols na partida 0? 2
    Quantos gols na partida 1? 1
    Quantos gols na partida 2? 0
    Quantos gols na partida 3? 0
    Quantos gols na partida 4? 3
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    {'nome': 'Joelson', 'gols': [2, 1, 0, 0, 3], 'total': 6}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    O campo nome tem o valor Joelson.
    O campo gols tem o valor [2, 1, 0, 0, 3].
    O campo total tem o valor 6.
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    O jogador Joelson jogou 5 partidas.
        => Na partida 0, fez 2 gols.
        => Na partida 1, fez 1 gols.
        => Na partida 2, fez 0 gols.
        => Na partida 3, fez 0 gols.
        => Na partida 4, fez 3 gols.
    Foi um total de 6 gols. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Cadastro de Jogador de Futebol ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários e listas
cadastro = dict()
gols = list()

# Inicialização de variáveis
total = 0

# Solicita os dados ao usuário
cadastro['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))

# Loop para obtenção dos gols por partidas
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))

# O dicionário recebe a lista de gols e o valor total de gols
cadastro['gols'] = gols[:]
cadastro['total'] = sum(gols)

# Imprime o dicionário
print(f'-=' * 30)
print(cadastro)
print(f'-=' * 30)

# Loop para impressão dos valores dos campos
for k, v in cadastro.items():
    print(f'O campos {k} tem o valor {v}.')
print(f'-=' * 30)

# Estatísticas do jogador
print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas.')

# Loop para obtenção do saldo de gols
for c, v in enumerate(cadastro['gols']):
    print(f'    => na partida {c}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')
