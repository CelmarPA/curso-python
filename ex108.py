""" Desafio 108 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
    números como um valor monetário formatado.

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
print(f'{cores["lilas"]}{" Formatando Moedas em Python ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
