""" Desafio 098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
    passo. Seu programa tem que realizar três contagens através da função criada:

    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Contagem de 1 até 10 de 1 em 1
     1 2 3 4 5 6 7 8 9 10 FIM!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Contagem de 10 até 0 de 2 e 2
     10 8 6 4 2 0 FIM!
     -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Agora é sua vez de personalizar a contagem!
     Início: 10
     Fim : 100
     Passo: 8
     -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Contagem de 10 até 100 de 8 em 8
     10 18 26 34 42 50 58 66 74 82 90 98 FIM! """

# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Função de Contador ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)
    if i < f:
        count = i
        while count <= f:
            print(f'{count} ', end='')
            sleep(0.5)
            count += p
        print('FIM!')
    else:
        count = i
        while count >= f:
            print(f'{count} ', end='')
            sleep(0.5)
            count -= p
        print('FIM!')


# Programa principal

# Contagem automática inicial do programa
contador(1, 10, 1)
contador(10, 0, 2)

# Solicita os dados para a contagem ao usuário
print(f'-=' * 20)
print(f'Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Chama a função contador
contador(inicio, fim, passo)
