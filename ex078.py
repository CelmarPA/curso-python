""" Desafio 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
    maior e o menor valor digitado e as suas respectivas posições na lista.

    Digite um valor para Posição 0: 7
    Digite um valor para Posição 1: 2
    Digite um valor para Posição 2: 9
    Digite um valor para Posição 3: 8
    Digite um valor para Posição 4: 3
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Você digitou os valores [7, 2, 9, 8, 3]
    O maior valor digitado foi 9 nas posições 2...
    O menor valor digitado foi 2 nas posições 1...

    Digite um valor para Posição 0: 1
    Digite um valor para Posição 1: 2
    Digite um valor para Posição 2: 1
    Digite um valor para Posição 3: 5
    Digite um valor para Posição 4: 5
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Você digitou os valores [1, 2, 1, 5, 5]
    O maior valor digitado foi 5 nas posições 3... 4...
    O menor valor digitado foi 1 nas posições 0... 2... """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Maior e Menor Valores ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
num = list()
maior = menor = 0

# Solicita os valores ao usuário
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {c}: ')))
    # Analisa o maior e menor valore
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

# Imprime a lista completa
print(f'=-=' * 20)
print(f'Você digitou os valores {num}')

# Defini a posição do maior valor
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, n in enumerate(num):
    if num[c] == maior:
        print(f'{c}... ', end='')

# Defini a posição do menor valor
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, n in enumerate(num):
    if num[c] == menor:
        print(f'{c}... ', end='')
