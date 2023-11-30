""" Desafio 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
    usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
    foi a soma entre eles (desconsiderando o flag).

    Digite um número [999 para parar]: 8
    Digite um número [999 para parar]: 2
    Digite um número [999 para parar]: 1
    Digite um número [999 para parar]: 7
    Digite um número [999 para parar]: 999

    Você digitou 4 números e a soma entre eles foi 18. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Tratando Vários Valores v1.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usuário
num = int(input('Digite um número [999 para parar]: '))

# Inicialização de variáveis
count = 0
soma = 0

# Solicita valores ao usuário
while num != 999:
    count += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count} números e a soma entre eles foi {soma}.')
