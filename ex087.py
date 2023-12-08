""" Desafio 087 - Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.

    Digite um valor para [0, 0]: 1
    Digite um valor para [0, 1]: 2
    Digite um valor para [0, 2]: 3
    Digite um valor para [1, 0]: 4
    Digite um valor para [1, 1]: 5
    Digite um valor para [1, 2]: 6
    Digite um valor para [2, 0]: 7
    Digite um valor para [2, 1]: 8
    Digite um valor para [2, 2]: 9
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
    [ 1 ] [ 2 ] [ 3 ]
    [ 4 ] [ 5 ] [ 6 ]
    [ 7 ] [ 8 ] [ 9 ]
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-
    A soma dos valores pares é 20.
    A soma dos valores da terceira coluna é 18.
    O maior valor da segunda linha é 6. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Matriz em Python ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Outra forma de inicialização matriz = [list([0, 0, 0]) for c in range(0, 3)]

# Inicialização de variáveis
soma_par = soma_coluna = maior = 0

# Loop para criação da matriz 3 x 3
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        # Soma os número pares
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        # SOma os números da terceira coluna
        if matriz[linha][2]:
            soma_coluna += matriz[linha][coluna]
        # Maior valor da segunda linha
        if linha == 1:
            maior = 0
        else:
            if matriz[1][coluna] > maior:
                maior = matriz[1][coluna]

print(f'=-=' * 20)
# Imprime a matriz formatada
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ] ', end='')
    print(f'')
print(f'=-=' * 20)

# Imprime os resultados
print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {maior}.')
