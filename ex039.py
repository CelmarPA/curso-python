""" Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se
    ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
    alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

    Ano de nascimento: 2000
    Quem nasceu em 2001 tem 16 anos em 2017.
    Ainda faltam 2 anos para o alistamento.
    Seu alistamento será em 2019!

    Ano de nascimento: 1995
    Quem nasceu em 1995 tem 22 anos em 2017.
    Você já deveria ter se alistado há 4 anos.
    Seu alistamento foi em 2013!

    Ano de nascimento: 1999
    Quem nasceu em 1999 tem 18 anos em 2017.
    Você tem que se alistar IMEDIATAMENTE! """

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Alistamento Militar ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita o ano de nascimento ao usuário
nasc = int(input('Ano de nascimento: '))

# Calcula a idade
atual = datetime.now().year
idade = atual - nasc

# Imprime a idade
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

# Faz a avaliação do alistamento
if idade < 18:
    falta = 18 - idade
    alis = atual + falta
    print(f'Ainda faltam {falta} anos para o alistamento. \n'
          f'Seu alistamento será em {alis}!')
elif idade > 18:
    exc = idade - 18
    alis = atual - exc
    print(f'Você já deveria ter se alistado há {exc} anos. \n'
          f'Seu alistamento foi em {alis}!')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
