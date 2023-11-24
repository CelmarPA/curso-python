""" Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

    Qual é o sálario do funcionário? R$900
    Quem ganhava R$900.00 passa a ganhar R$1035.00 agora.

    Qual é o sálario do funcionário? R$9000
    Quem ganhava R$9000.00 passa a ganhar R$9900.00 agora. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Aumentos Múltiplos ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita o salário do funcionário
salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)

# Imprime os resultados
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.')
