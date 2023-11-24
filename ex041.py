""" Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
    mostre sua categoria, de acordo sua idade:

    – Até 9 anos: MIRIM
    – Até 14 anos: INFANTIL
    – Até 19 anos: JÚNIOR
    – Até 25 anos: SÊNIOR
    – Acima de 25 anos: MASTER

    Ano de Nascimento: 2000
    O atleta te 17 anos.
    Classificação: JUNIOR

    Ano de Nascimento: 2010
    O atleta te 7 anos.
    Classificação: MIRIM

    Ano de Nascimento: 1997
    O atleta te 20 anos.
    Classificação: SÊNIOR

    Ano de Nascimento: 1995
    O atleta te 22 anos.
    Classificação: MASTER  """

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Classificando Atletas ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita o ano de nascimento ao usuário
ano = int(input('Anos de nascimento: '))

# Calcula a idade
idade = datetime.now().year - ano

# Imprime a idade
print(f'O atleta tem {idade} anos.')

# Classifica os atletas
if idade <= 9:
    print(f'Classificação: MIRIM')
elif 14 >= idade > 9:
    print(f'Classificação: INFANTIL')
elif 19 >= idade > 14:
    print(f'Classificação: JUNIOR')
elif 25 >= idade > 19:
    print(f'Classificação: SÊNIOR')
else:
    print(f'Classificação: MASTER')
