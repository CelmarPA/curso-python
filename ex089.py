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
    1   Maria          8.0
    2   João           3.8
    3   Gustabo        4.8
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

# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Boletim ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
dados = list()
boletim = list()
notas = list()
medias = list()

# Inicialização de variáveis
media = soma = 0

while True:
    # Solicita o nome do aluno
    nome = str(input('Nome: '))
    # Coloca o nome do aluno em uma lista de dados temporários
    dados.append(nome)
    # Loop para solicitação das duas notas
    for i in range(0, 2):
        nota = float(input(f'Nota {i+1}: '))
        # Coloca as notas do aluno em uma lista temporária
        notas.append(nota)
        # Soma as notas para o cálculo da média
        soma += nota
    # Calcula a média
    media = soma / 2
    # Faz uma cópia da lista notas para uma lista de dados temporários
    dados.append(notas[:])
    # Coloca a média calculada do aluno em uma lista de médias
    medias.append(media)
    # Faz uma cópia de dados dentro da lista boletim
    boletim.append(dados[:])
    # Limpa as listas temporária dados
    notas.clear()
    dados.clear()
    # Zera a soma e a média para novo loop
    soma = 0
    media = 0
    # Solicita se o usuário deseja continuar
    opc = str(input('Deseja continuar: [S/N] ')).strip()[0]
    if opc in 'nN':
        break

# Imprime o boletim com as médias
print(f'=-=' * 20)
print(f'{"Nº":<3} {"NOME":<15} {"MÉDIA":>5}')
print(f'-' * 30)
for c, a in enumerate(boletim):
    print(f'{c:<3} {a[0]:<15} {medias[c]:^5.1f}')
print(f'-' * 30)

# Menu com notas individuais
while True:
    # Solicita o código do aluno que deseja verificar as notas
    aluno = int(input(f'Mostra nota de qual aluno? (999 interrompe) '))
    # Se o código digitado for 999 faz break
    if aluno == 999:
        break
    # Faz o loop para imprimir o nome e as noras
    for i, hist in enumerate(boletim):
        # Se o código do aluno estiver no boletim esse será impresso
        if aluno == i:
            print(f'Notas de {hist[0]} são {hist[1]}')
            print(f'-' * 30)
        elif aluno >= len(boletim):
            print('Aluno não encontrado no banco de dados. Tente novamente!')
            break
# Mensagem final do programa
print(f'=-=' * 20)
print(f'FINALIZANDO...')
sleep(1)
print(f'<< VOLTE SEMPRE! >>')
