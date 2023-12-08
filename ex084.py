""" Desafio 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

    Nome: Maria
    Peso: 70
    Quer continuar? [S/N] s
    Nome: João
    Peso: 100
    Quer continuar? [S/N] s
    Nome: Claudio
    Peso: 85
    Quer continuar? [S/N] s
    Nome: Hélio
    Peso: 100
    Quer continuar? [S/N] s
    Nome: Ana
    Peso: 70
    Quer continuar? [S/N] s
    Nome: Gustavo
    Peso: 88
    Quer continuar? [S/N] n
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Ao to-do, você cadastrou 6 pessoas.
    O maior peso foi de 100.0kg. Peso de [João] [Hélio]
    O menor peso foi de 70.0kg. Peso de [Maria] [Ana] """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Análise de Dados Lista Composta ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
cadastro = list()
dados = list()

# Inicialização de variáveis
maior = menor = 0

# Loop para obtenção do dados
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    # Define maior e menor pesos
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    # Copia os itens de dados para dentro de cadastro
    cadastro.append(dados[:])
    # Limpa a lista temporária dados
    dados.clear()
    opc = str(input('Deseja continuar: [S/N] ')).strip()[0]
    if opc in 'nN':
        break

# Resultados
print(f'=-=' * 20)
print(f'Ao todo você cadastrou {len(cadastro)} pessoas.')

# Pessoas com maior peso
print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

# Pessoas com menor peso
print(f'\nO menor peso foi de {menor:.1f}kg. Peso de ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
