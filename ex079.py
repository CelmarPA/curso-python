""" Desafio 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
    digitados, em ordem crescente.

    Digite um valor: 5
    Valor adicionado com sucesso...
    Quer continuar? [S/N] s
    Digite um valor: 9
    Valor adicionado com sucesso...
    Quer continuar? [S/N] s
    Digite um valor: 3
    Valor adicionado com sucesso...
    Quer continuar? [S/N] s
    Digite um valor: 9
    Valor duplicado! Não vou adicionar...
    Quer continuar? [S/N] s
    Digite um valor: 3
    Valor duplicado! Não vou adicionar...
    Quer continuar? [S/N] s
    Digite um valor: 7
    Valor adicionado com sucesso...
    Quer continuar? [S/N] n
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Você digitou os valores [3, 5, 7, 9] """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Valores Únicos em Uma Lista ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
numeros = list()

# Loop para obtenção dos valores
while True:
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print(f'Valor duplicado! Não vou adicionar...')
    else:
        print(f'Valor adicionado com sucesso...')
        numeros.append(valor)
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'=-=' * 20)
print(f'Você digitou os valores {sorted(numeros)}')
