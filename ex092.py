""" Desafio 092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
    em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
    salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

    Nome: Gustavo
    Ano de Nascimento: 1978
    Carteira de Trabalho (0 não tem): 1234
    Ano de contratação: 1995
    Salário: R$1000
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    {'nome': 'Gustavo', 'idade': 40, 'ctps': 1234, 'contratação': 1995, 'salário': 1000}
    nome tem o valor Gustavo
    idade tem o valor 40
    ctps tem o valor 1234
    contratação tem o valor 1995
    salário tem o valor 1000
    aposentadoria tem o valor 52 """

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Cadastro de Trabalhador ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários
cadastro = dict()

# Solicita os dados aos usuário
cadastro['nome'] = str(input(f'Nome: '))
nascimento = int(input(f'Anos de Nascimento: '))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# Verifica se o usuário possui carteira de trabalho
if cadastro['ctps'] == 0:
    # Imprime os dados
    print(f'-=' * 30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
else:
    # Completa o cadastro e imprime os dados
    cadastro['contratação'] = int(input(f'Ano de Contratação: '))
    cadastro['salário'] = float(input(f'Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] - nascimento + 35
    print(f'-=' * 30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
