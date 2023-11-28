""" Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
    que forem pares. Se o valor digitado for ímpar, desconsidere-o.
    Digite o 1 valor: 8

    Você informou 1 números PARES e a soma foi 8! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Soma dos Pares ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma = 0
count = 0

# Solicita os números ao usuário e realiza a soma dos pares
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        count += 1
print(f'Você informou {count} número(s) PARES e a soma foi {soma}!')
