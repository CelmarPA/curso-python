""" Desafio 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
    usuário vai continuar ou não. No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.

    -------------------------------------------
               LOJAS SUPER BARATÃO
    -------------------------------------------
    Nome do produto: Mouse
    Preço: R$50
    Quer continuar [S/N]? S
    Nome do produto: Caneta
    Preço: R$3
    Quer continuar [S/N]? S
    Nome do produto: Notebook
    Preço: R$2550
    Quer continuar [S/N]? S
    Nome do produto: Impressora
    Preço: R$800
    Quer continuar [S/N]? S
    Nome do produto: Monitor
    Preço: R$1250
    Quer continuar [S/N]? n
    ----------------- FIM DO PROGRAMA ----------------------
    O total da compra foi R$4653.00
    Temos 2 produto(s) custando mais de R$1000.00
    O produto mais barato foi Caneta e custa R$3.00 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Estatísticas em Produtos ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Imprime enunciado
print(f'{cores["green"]}-{cores["reset"]}' * 60)
print(f'{cores["blue"]}{"LOJAS SUPER BARATÃO":^60}{cores["reset"]}')
print(f'{cores["green"]}-{cores["reset"]}' * 60)

# Inicialização de variáveis
total = mais_mil = count = menor = 0
barato = ''

# Loop para solicitação dos dados
while True:
    produto = str(input(f'{cores["green"]}Nome do produto: {cores["reset"]}'))
    preco = float(input(f'{cores["green"]}Preço:{cores["reset"]} R$'))
    while preco <= 0:
        preco = float(input(f'{cores["green"]}Preço:{cores["reset"]} R$'))
    # Calcula os resultado
    total += preco
    if preco > 1000:
        mais_mil += 1
    count += 1
    if count == 1 or preco < menor:
        menor = preco
        barato = produto
    # Pergunta se o usuário quer continuar
    opc = str(input(f'{cores["green"]}Quer continuar [S/N]?{cores["reset"]} ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input(f'{cores["green"]}Quer continuar [S/N]?{cores["reset"]} ')).strip().upper()[0]
    if opc == 'N':
        break
# Imprime os resultados
print(f'{cores["red"]}{" FIM DO PROGRAMA ":-^60}{cores["reset"]}')
print(f'{cores["lilas"]}O total da compra foi{cores["reset"]} {cores["blue"]}R${total:.2f}{cores["reset"]} \n'
      f'{cores["lilas"]}Temos {cores["blue"]}{mais_mil} {cores["lilas"]}produto(s) custando mais '
      f'de R$1000.00{cores["reset"]} \n'
      f'{cores["lilas"]}O produto mais barato foi {cores["blue"]}{barato} {cores["lilas"]}e custa '
      f'{cores["blue"]}R${menor:.2f}{cores["reset"]}')
