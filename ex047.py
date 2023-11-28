""" Desafio 047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Contagem de Pares ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Mostra todos os pares de 1 até 50
for c in range(1, 51):
    if c % 2 == 0:
        print(f'{c} ', end='')
print(f'Acabou')

# Mostra todos os pares de 1 até 50
for c in range(2, 51, 2): # Essa solução gera menos iterações
    print(f'{c} ', end='')
print(f'Acabou')
