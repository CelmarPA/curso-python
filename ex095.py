""" Desafio 095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
    de detalhes do aproveitamento de cada jogador.

    --------------------------------
    Nome do jogador: Joelson
    Quantas partidas Joelson jogou? 2
    Quantos gols na partida 0? 3
    Quantos gols na partida 1? 2
    Quer continuar? [S/N] s
    --------------------------------
    Nome do jogador: Pedrão
    Quantas partidas Joelson jogou? 3
    Quantos gols na partida 0? 2
    Quantos gols na partida 1? 0
    Quantos gols na partida 2? 4
    Quer continuar? [S/N] s
    --------------------------------
    Nome do jogador: Wesley
    Quantas partidas Joelson jogou? 4
    Quantos gols na partida 0? 0
    Quantos gols na partida 1? 0
    Quantos gols na partida 2? 0
    Quantos gols na partida 3? 0
    Quer continuar? [S/N] n
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    cod nome              gols                total
    ------------------------------------------------
    0 Joelson            [3, 2]               5
    1 Pedrão             [2, 0, 4]            6
    2 Wesley             [0, 0, 0, 0]         0
    ------------------------------------------------
    Mostra dados de qual jogador? 1
    -- LEVANTAMENTO DO JOGADOR Pedrão:
       No jogo 0 fez 2 gols.
       No jogo 1 fez 0 gols.
       No jogo 2 fez 4 gols.
    ------------------------------------------------
    Mostra dados de qual jogador? 2
    -- LEVANTAMENTO DO JOGADOR Wesley:
       No jogo 0 fez 0 gols.
       No jogo 1 fez 0 gols.
       No jogo 2 fez 0 gols.
       No jogo 3 fez 0 gols.
    ------------------------------------------------
    Mostra dados de qual jogador? 5
    ERRO! Não existe jogador com código 5! Tente novamente.
    ------------------------------------------------
    Mostra dados de qual jogador? 999
    << VOLTE SEMPRE >> """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Aprimorando os Dicionários ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários e listas
jogador = dict()
jogadores = list()
gols = list()

# Solicita os dados ao usuário
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    # Loop para saldo de gols
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    # Copia a lista gols para dentro do dicionário jogador
    jogador['gols'] = gols[:]
    # Copia o total de gols do jogador
    jogador['total'] = sum(gols)
    # Copia o dicionário jogador para a lista jogadores
    jogadores.append(jogador.copy())
    # Limpa a lista gols
    gols.clear()
    # Pergunta se o usuário deseja continuar
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        print(f'ERRO! Responda apenas S ou N.')
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'-=' * 30)

# Imprime a tabela de jogadores
print(f'{"cod":<3} {"nome":<15} {"gols":<20} {"total":<6}')
print(f'-' * 50)
for c, v in enumerate(jogadores):
    print(f'{c:>3} {v["nome"]:<15}', f'{v["gols"]}'.ljust(20), f'{v["total"]:<6}')
print(f'-' * 50)

# Mostra os dados do jogador selecionado
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    if resp >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {resp}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"].upper()}:')
        for i, g in enumerate(jogadores[resp]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
print(f'<< VOLTE SEMPRE >>')
