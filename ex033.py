""" Desafio 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

    Primeiro valor: 7
    Segundo valor: 2
    Terceiro valor: 4

    O menor valor digitado foi 2
    O maior valor digitado foi 7 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Maior e Menor Valores ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita os número ao usuário
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Verifica qual é o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verifica qual é o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Imprime o resultado
print(f'O menor valor digitado foi {menor} \n'
      f'O maior valor digitado foi {maior}')
