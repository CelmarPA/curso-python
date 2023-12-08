""" Desafio 089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
    de cada aluno individualmente.

    Nome: Pedro
    Nota 1: 4.5
    Nota 2: 7
    Quer continuar: [S/N] s
    Nome: Maria
    Nota 1: 9.5
    Nota 2: 6.5
    Quer continuar: [S/N] s
    Nome: João
    Nota 1: 4.5
    Nota 2: 3
    Quer continuar: [S/N] s
    Nome: Gustavo
    Nota 1: 5.5
    Nota 2: 4
    Quer continuar: [S/N] n
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Nº. NOME          MÉDIA
    -------------------------
    0   Pedro          5.8
    1   Pedro          8.0
    2   Pedro          3.8
    3   Pedro          4.8
    -------------------------
    Mostrar notas de qual aluno? (999 interrompe): 1
    Notas de Maria são [9.5, 6.5]
    -------------------------
    Mostrar notas de qual aluno? (999 interrompe): 3
    Notas de Gustavo são [5.5, 4.0]
    -------------------------
    Mostrar notas de qual aluno? (999 interrompe): 999
    FINALIZANDO...
    <<< VOLTE SEMPRE >>> """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Boletim ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'')

# Inicialização de listas
dados = list()
boletim = list()
notas = list()
notas_boletim = list()
media = 0
soma = 0
count = 1
while True:
    # Solicita o nome do aluno
    nome = str(input('Nome: '))
    # Coloca o nome do aluno em uma lista de dados temporários
    dados.append(nome)
    notas.append(nome)
    # Adiciona notas em um boteim de apenas notas
    notas_boletim.append(notas[:])
    notas.clear()
    # Loop para solicitação das duas notas
    for i in range(0, 2):
        nota = float(input(f'Nota {i+1}: '))
        # Coloca as notas do aluno em uma lista temporária
        dados.append(nota)
        notas.append(nota)
        # Soma as notas para o cálculo da média
        soma += nota
    # Calcula a média
    media = soma / 2
    # Coloca a média do aluno em uma lista temporária
    dados.append(media)
    # Faz uma cópia de dados dentro da lista boletim
    boletim.append(dados[:])
    notas_boletim.append(notas[:])
    notas.clear()
    # Limpa as listas temporária dados
    dados.clear()
    # Zerá a soma
    soma = 0
    # Solicita se o usuário deseja continuar
    opc = str(input('Deseja continuar: [S/N] ')).strip()[0]
    if opc in 'nN':
        break

# Imprime o boletim com as médias
print(f'=-=' * 20)
print(f'{"Nº":<3} {"NOME":<15} {"MÉDIA":>5}')
print(f'-' * 30)
for c, a in enumerate(boletim):
    print(f'{c:<3} {a[0]:<15} {a[3]:^5}')

# Menu com notas individuais
print(boletim)