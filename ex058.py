""" Desafio 058 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
    o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

    Sou seu computador...
    Acabei de pensar em um número entre 0 e 10.
    Será que você consegue adivinhar qual foi?
    Qual é o seu palpite? 4
    Mais... tente mais uma vez.
    Qual é o seu palpite? 7
    Mais... tente mais uma vez.
    Qual é o seu palpite? 10
    Menos... tente mais uma vez.
    Qual é o seu palpite? 9
    Acertou com 4 tentativas. Parabéns! """

# Importação de bibliotecas
from random import randint

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Jogo da Adivinhação v2.0 ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Enunciado do programa
print(f'Sou seu computador... \n'
      f'Acabei de pensar em um número entre 0 e 10. \n'
      f'Será que você consegue adivinhar qual foi?')

# Solicita um número ao usuário
num = int(input('Qual é o palpite? '))

# Gera o número para o computador
comp = randint(0, 10)

# Inicialização de variáveis
count = 1

while num != comp:
    if num < comp:
        print(f'Mais... tente mais uma vez.')

    elif num > comp:
        print(f'Menos... tente mais uma vez.')
    count += 1
    num = int(input('Qual é o palpite? '))

print(f'Acertou com {count} tentativas. Parabéns! """')
