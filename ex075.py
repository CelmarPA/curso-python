""" Desafio 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
    mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.

    Digite um número: 5
    Digite outro número: 9
    Digite mais um número: 2
    Digite o último número: 3
    Você digitou os valores (5, 9, 2, 3)
    O valor 9 apareceu 1 vez(es)
    O valor 3 apareceu na 4ª posição
    Os valores pares digitados foram 2

    Digite um número: 2
    Digite outro número: 4
    Digite mais um número: 6
    Digite o último número: 8
    Você digitou os valores (2, 4, 6, 8)
    O valor 9 apareceu 0 vez(es)
    O valor 3 apareceu não apareceu em nenhuma posição
    Os valores pares digitados foram 2 4 6 8 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Análise de Dados ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print('')

# Solicita os valores ao usuário
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

# Armazena os números em uma tupla
num = (n1, n2, n3, n4)

# Imprime os valores adicionados
print(f'Você digitou os valores: {num}')

# Quantas vezes o número 9 aparece
print(f'O número 9 apareceu {num.count(9)} vez(es)')

# Primeira posição do valor 3
if 3 not in num:
    print(f'O valor 3 apareceu não apareceu em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')

# Quais foram o número pares
print(f'Os valores pares digitados foram ', end='')
for p in num:
    if p % 2 == 0:
        print(f'{p} ', end='')
