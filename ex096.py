""" Desafio 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
    (largura e comprimento) e mostre a área do terreno.

    Controle de Terrenos
    --------------------
    LARGURA (m): 4.5
    COMPRIMENTO (m): 8
    A área de um terreno de 4.5 x 8.0 é de 36.0m². """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Função que Calcula Área ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)


# Funções
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a}m².')


# Programa Principal
print(f'{"Controle de Terrenos":^30}')
print(f'-' * 30)

# Solicita os dados ao usuário
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

# Chama a função para calcular a área
area(largura, comprimento)
