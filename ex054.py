""" Desafio 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
    não atingiram a maioridade e quantas já são maiores.

    Em que ano a 1ª pessoa nasceu? 2010
    Em que ano a 2ª pessoa nasceu? 1960
    Em que ano a 3ª pessoa nasceu? 2011
    Em que ano a 4ª pessoa nasceu? 1970
    Em que ano a 5ª pessoa nasceu? 2015
    Em que ano a 6ª pessoa nasceu? 1940
    Em que ano a 7ª pessoa nasceu? 2016

    Ao to-do tivemos 3 pessoas maiores de idade
    E também tivemos 4 pessoas menores de idade """

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Grupo da Maioridade ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Ano atual
atual = datetime.now().year

# Inicialização de variáveis
maiores = 0
menores = 0

# Solicita o ano de nascimentos das sete pessoas
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if (atual - ano) >= 18:
        maiores += 1
    else:
        menores += 1

# Imprime o Resultado
print(f'Ao todo tivemos {maiores} pessoa(s) maior(es) de idade! \n'
      f'E também tivemos {menores} pessoa(s) menor(es) de idade!')
