""" Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
    primeiros termos dessa progressão.

    ================================
          10 TERMOS DE UMA PA
    ================================
    Primeiro termo: 0
    Razão: 2
    0 -> 2 até 10 termo e -> ACABOU """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Progressão Aritmética ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Enunciado
print(f'=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print(f'=' * 30)

# Solicita os dados ao usuário
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Formula geral de uma PA: PA = a + (tr) (onde a é o primeiro termo, t o termo e r a razão

# Gera e imprime a PA
for c in range(0, 10):
    pa = termo + (c * razao)
    print(f'{pa} {cores["yellow"]}\u2192{cores["reset"]} ', end='')
print(f'{cores["red"]}Acabou{cores["reset"]}')
