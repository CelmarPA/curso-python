""" Desafio 076 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
    sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
    ------------------------------------------------------------
                         LISTAGEM DE PREÇOS
    ------------------------------------------------------------
    Leite.............................................R$   4.50
    Pão de Forma......................................R$   3.00
    Ovos (Dúzia)......................................R$   6.50
    Arroz (5Kg).......................................R$  10.00
    Feijão (1Kg)......................................R$   5.50
    Frango (1Kg)......................................R$  15.00
    Tomate (1Kg)......................................R$   3.50
    Cenoura (1Kg).....................................R$   2.00
    Maçã (1Kg)........................................R$   4.00
    Refrigerante (2L).................................R$   5.00
    ------------------------------------------------------------ """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Lista de Preços ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print('')

# Tupla com lista de preços
produtos = ('Leite', 4.50, 'Pão de Forma', 3.00, 'Ovos (Dúzia)', 6.50, 'Arroz (5kg)', 10.00, 'Feijão (1kg)', 5.50,
            'Frango (1kg)', 15.00, 'Tomate (1kg)', 3.50, 'Cenoura (1kg)', 2.00, 'Maça (1kg)', 4.00,
            'Refrigerante (2l)', 5.0)
# Cabeçalho da lista
print(f'{cores["green"]}-{cores["reset"]}' * 60)
print(f'{cores["blue"]}{"LISTAGEM DE PREÇOS":^60}{cores["reset"]}')
print(f'{cores["green"]}-{cores["reset"]}' * 60)

# Imprime a lista tabulada
for c, p in enumerate(produtos):
    if c % 2 == 0:
        print(f'{produtos[c]:.<50}', end='')
    else:
        print(f'R${produtos[c]:>8.2f}')
print(f'{cores["green"]}-{cores["reset"]}' * 60)