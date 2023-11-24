""" Desafio 037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
    será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

    Digite um número inteiro: 234
    Escolha uma das bases para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL
    Sua opção:
    234 convertido para HEXADECIMAL é igual a ea
    234 convertido para BINÁRIO é igual a 11101010
    234 convertido para OCTAL é igual a 352 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Conversor de Bases Numéricas ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita um número e uma base para conversão ao usuário
num = int(input('Digite um número inteiro: '))

print(f'Escolha uma das bases para conversão: \n'
      f'[ 1 ] converter para BINÁRIO \n'
      f'[ 2 ] converter para OCTAL \n'
      f'[ 3 ] converter para HEXADECIMAL')

op = int(input('Sua opção: '))

# Faz a conversão pela opção selecionada
if op == 1:
    binario = bin(num)[2:]
    print(f'{num} convertido para BINÁRIO é igual a {cores["red"]}{binario}{cores["reset"]}')
elif op == 2:
    octal = oct(num)[2:]
    print(f'{num} convertido para OCTAL é igual a {cores["lilas"]}{octal}{cores["reset"]}')
elif op == 3:
    hexadecimal = hex(num)[2:]
    print(f'{num} convertido para HEXADECIMAL é igual a {cores["yellow"]}{hexadecimal}{cores["reset"]}')
else:
    print(f'{cores["red"]}Opção inválida! Tente novamente!{cores["reset"]}')
