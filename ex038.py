""" Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os mostrando tela uma mensagem:

    – O primeiro valor é maior
    – O segundo valor é maior
    – Não existe valor maior, os dois são iguais

    Primeiro número: 4
    Segundo número: 1
    O PRIMEIRO valor é maior!
    Primeiro número: 9
    Segundo número: 15
    O SEGUNDO valor é maior!
    Primeiro número: 12
    Segundo número: 12
    Os dois valores são IGUAIS! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Comparando Números ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita dois número inteiros ao usuário
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO valor é maior!')
elif n1 < n2:
    print(f'O SEGUNDO valor é maior!')
else:
    print(f'Os dois valores são IGUAIS!')
