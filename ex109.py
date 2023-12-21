""" Desafio 109 - Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
    desenvolvida no desafio 108.

    Digite o preço: R$500
    A metade de R$500,00 é R$250,00
    O dobro de R$500,00 é R$1000,00
    Aumentando 10%, temos R$550,00
    Diminuindo 13%, temos R$435,00 """

# Importação de funções
from modulos import moeda

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Formatando Moedas em Python v2.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
