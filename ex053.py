""" Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
    espaços. Exemplos de palíndromos:

    APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


    Digite uma frase: Gustavo Guanabara
    O inverso de GUSTAVOGUANABARA é ARABANAUGOVATSUG
    A frase digitada não é um palíndromo! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Detector de Palíndromo ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita uma frase ao usuário:
frase = str(input('Digite uma frase: ')).upper().strip()

# Separa a frase em palavras
palavras = frase.split()

# Junta as palavras retirando os espaços
junto = ''.join(palavras)

# Inicialização de variáveis
inverso = ''

# Inverte a frase e verifica se é um palíndromo
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

# Imprime a frase inversa
print(f'O inverso de {junto} é {inverso}')

# Imprime o resultado
if junto == inverso:
    print(f'A frase digitada é um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')

