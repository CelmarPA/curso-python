""" Desafio 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até
    vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

    Digite um número entre 0 e 20: 90
    Tente novamente. Digite um número entre 0 e 20: 16
    Você digitou o número dezesseis
    Digite um número entre 0 e 20: 0
    Você digitou o número zero """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Número por Extenso ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Tupla com os números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Loop para validação do número solicitado
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numeros[num]}')
    opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc in 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^60}')
