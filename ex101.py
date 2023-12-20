""" Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
    nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
    OBRIGATÓRIO nas eleições.

    --------------------------
    Em que ano você nasceu? 2005
    Com 18 anos: VOTO OBRIGATÓRIO.

    --------------------------
    Em que ano você nasceu? 2015
    Com 8 anos: NÃO VOTA.

    --------------------------
    Em que ano você nasceu? 1975
    Com 48 anos: VOTO OBRIGATÓRIO.

    --------------------------
    Em que ano você nasceu? 1915
    Com 108 anos: VOTO OPCIONAL. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Função Para Votação ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


# Função
def votar(nascimento):
    """
    Função para verificação da obrigatoriedade de votação
    :param nascimento: Ano de nascimento do usuário
    :return: A avaliação da análise
    """
    # Importação de bibliotecas
    from datetime import datetime
    # Calcula a idade do usuário
    idade = datetime.now().year - nascimento
    # Avalia a obrigatoriedade do voto
    if 16 >= idade < 18 or idade > 65:
        voto = 'VOTO OPCIONAL.'
    elif 18 <= idade <= 65:
        voto = 'VOTO OBRIGATÓRIO.'
    else:
        voto = "NÃO VOTA."
    # Retorna o resultado da análise
    return f'Com {idade} anos: {voto}'


# Programa principal
print(f'-' * 30)
ano = int(input('Em que ano você nasceu? '))

# Chama a função votar
print(votar(ano))
