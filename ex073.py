""" Desafio 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
    na ordem de colocação. Depois mostre:

    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Bragantino.

    =-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Lista de times do Brasileirão: (...)
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Os 5 primeiros são: (...)
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Os 4 últimos são: (...)
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Times em ordem alfabética: [...]
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    O Chapecoense está na 8ª posição """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Times de Futebol ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print('')

# Tupla com a classificação do brasileirão 2023
times = ('Palmeiras', 'Atlético_MG', 'Flamengo', 'Grêmio', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Santos', 'Vasco da Gama',
         'Bahia', 'Goiás', 'Coritiba', 'América-MG')

# Imprime a lista de times
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)
print(f'Lista de times do Brasileirão: {times}')
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)

# Os cinco primeiros
print(f'Os 5 primeiros são: {times[:5]}')
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)

# Quatro últimos
print(f'Os 4 últimos são: {times[-4:]}')
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)

# Times em ordem alfabética
print(f'Times é ordem alfabética: {sorted(times)}')
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)

# Posição do Bragantino
print(f'O Bragantino está na {times.index('Bragantino') + 1}ª posição')
print(f'{cores["yellow"]}=-={cores["reset"]}' * 20)
