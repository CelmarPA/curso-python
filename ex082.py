""" Desafio 082 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
    extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.

    Digite um valor: 6
    Quer continuar? [S/N] s
    Digite um valor: 2
    Quer continuar? [S/N] s
    Digite um valor: 7
    Quer continuar? [S/N] s
    Digite um valor: 8
    Quer continuar? [S/N] s
    Digite um valor: 3
    Quer continuar? [S/N] s
    Digite um valor: 9
    Quer continuar? [S/N] n
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    A lista completa é [6, 2, 7, 8, 3, 9]
    A lista de pares é [6, 2, 8]
    A lista de ímpares é [7, 3, 9] """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Dividindo Valores em Várias Listas ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
numeros = list()
pares = list()
impares = list()

# Loop para obtenção dos valores
while True:
    numeros.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break

# Verificação dos valores pares e ímpares
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'=-=' * 20)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
