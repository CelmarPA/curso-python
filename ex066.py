""" Desafio 066 - Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
    digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
    soma entre elas (desconsiderando o flag).

    Digite um valor (999 para parar): 4
    Digite um valor (999 para parar): 3
    Digite um valor (999 para parar): 5
    Digite um valor (999 para parar): 999
    A soma dos 3 valores foi 12! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Vários Número Com Flag ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma = count = 0

# Loop para obtenção dos valores
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'A soma dos {count} valores foi {soma}!')
