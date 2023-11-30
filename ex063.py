""" Desafio 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
    de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

     -------------------------------------
            SEQUÊNCIA DE FIBONACCI
     -------------------------------------
     Quantos termos você quer mostrar? 10
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     0 1 1 2 3 5 8 13 21 34 FIM
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Fibonacci v1.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

print(f'-' * 30)
print(f'{"SEQUÊNCIA DE FIBONACCI":^30}')
print(f'-' * 30)

# Solicita quantos termos para a sequência
termos = int(input('Quantos termos você quer mostrar? '))

# Primeiro e segundo termos
t1 = 0
t2 = 1

# Inicialização de variáveis
c = 3

# Imprime os dois primeiros termos
print(f'~' * 60)
print(f'{t1} → {t2} → ', end='')

# Gera a sequência de Fibonacci
while c <= termos:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    c += 1
print(f'FIM')
print(f'~' * 60)