""" Desafio 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
    pelo usuário. O programa será interrompido quando o número solicitado for negativo.

    Quer ver a tabuada de qual valor? 3
    --------------------------------------
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    3 x 10 = 30
    --------------------------------------
    Quer ver a tabuada de qual valor? -1
    --------------------------------------
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    3 x 10 = 30
    --------------------------------------
    Quer ver a tabuada de qual valor? -1
    --------------------------------------
    PROGRAMA TABUADA ENCERRADO. Volte sempre!
    """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Tabuada v3.0 ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print(f'-' * 35)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num:2} x {c} = {num * c}')
    print(f'-' * 35)
print(f'{cores["red"]}PROGRAMA TABUADA ENCERRADO{cores["reset"]}. Volte sempre!')
