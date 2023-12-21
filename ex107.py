""" Desafio 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
    metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

    Digite o preço: R$500
    A metade de 500.0 é R$250.0
    O dobro de 500.0 é 1000.0
    Aumentando 10%, temos 550.0
    Diminuindo 13%, temos 435.0 """

# Importação de funções
from modulos import moeda

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Exercitando Módulos em Python ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
