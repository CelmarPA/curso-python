""" Desafio 081 - Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

    Digite um valor: 3
    Quer continuar? [S/N] s
    Digite um valor: 9
    Quer continuar? [S/N] s
    Digite um valor: 2
    Quer continuar? [S/N] s
    Digite um valor: 5
    Quer continuar? [S/N] s
    Digite um valor: 0
    Quer continuar? [S/N] n
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Você digitou 5 elementos.
    Os valores em ordem decrescente são [9, 5, 3, 2, 0]
    O valor 5 faz parte da lista!
    O valor 5 não foi encontrado na lista! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Extraindo Dados de uma Lista ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
numeros = list()

# Loop para obtenção dos valores
while True:
    numeros.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'=-=' * 30)

# Quantidade de valores na lista
quant = len(numeros)
print(f'Você digitou {quant} elementos.')

# Ordem decrescente da lista
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}.')

# Verifica se a lista possui o valor 5
if 5 in numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
