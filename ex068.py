""" Desafio 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
    jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

    =-==-==-==-==-==-==-==-==-==-==-==-==-=
            VAMOS JOGAR PAR OU ÍMPAR
    =-==-==-==-==-==-==-==-==-==-==-==-==-=
    Diga um valor: 6
    Par ou Ímpar? [P/I] I
    -------------------------------------------------------
      Você jogou 6 e o computador 10. Total de 16 deu PAR!
    -------------------------------------------------------
    Você PERDEU!
    =-==-==-==-==-==-==-==-==-==-==-==-==-=
    GAME OVER! Vocè venceu 0 vezes.

    =-==-==-==-==-==-==-==-==-==-==-==-==-=
            VAMOS JOGAR PAR OU ÍMPAR
    =-==-==-==-==-==-==-==-==-==-==-==-==-=
    Diga um valor: 8
    Par ou Ímpar? [P/I] P
    -------------------------------------------------------
      Você jogou 8 e o computador 2. Total de 10 deu PAR!
    -------------------------------------------------------
    Você VENCEU!
    Vamos jogar novamente...
    =-==-==-==-==-==-==-==-==-==-==-==-==-=
    GAME OVER! Vocè venceu 0 vezes.
    Diga um valor: 8
    Par ou Ímpar? [P/I] P """

# Importação de bibliotecas
from random import randint

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Jogo do Par Ou Ímpar ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
count = 0

# Imprime enunciado
print(f'-=-' * 10)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^30}')
print(f'-=-' * 10)

# Loop para jogo
while True:
    # Solicita um número ao usuário
    num = int(input('Diga um valor: '))
    # Jogada do computador
    comp = randint(0, 10)
    # Solicita a opção
    opc = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    # Validação da opção
    while opc not in 'PI':
        opc = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    # Verifica se é par ou ímpar
    if (comp + num) % 2 == 0:
        result = 'P'
        resp = 'PAR'
    else:
        result = 'I'
        resp = 'Ímpar'
    # Imprime o resultado
    print(f'-' * 40)
    print(f'Você jogou {num} e o computador {comp}. Total de {num + comp} deu {resp}!')
    print(f'-' * 40)
    # Define o ganhador e imprime o resultado
    if opc == result:
        count += 1
        print(f'Você {cores["green"]}VENCEU!{cores["reset"]} \n'
              f'Vamos jogar novamente...')
        print(f'-=-' * 10)
    else:
        print(f'Você {cores["yellow"]}PERDEU{cores["reset"]}')
        print(f'-=-' * 10)
        break
print(f'{cores["red"]}GAME OVER!{cores["reset"]} Você venceu {cores["blue"]}{count}{cores["reset"]} vezes.')
