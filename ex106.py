""" Desafio 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
    manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Interactive Helping System In Python ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)


# Funções
def titulo(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)


def ajuda():
    from time import sleep
    comando = ''
    while comando != 'fim':
        print(f'\033[0;97;42m', end='')
        titulo('SISTEMA DE AJUDA PyHELP')
        print(f'\033[m')
        comando = str(input('Função ou Biblioteca > ')).strip().lower()
        if comando == 'fim':
            print(f'\033[97;41m', end='')
            titulo('ATÉ LOGO!')
            print(f'\033[m')
            break
        print(f'\033[97;44m', end='')
        titulo('Acessando o manual do comando')
        print(f'\033[m')
        sleep(1.5)
        print(f'\033[30;107m')
        help(comando)
        print(f'\033[m')
    print()


# Programa principal
ajuda()
