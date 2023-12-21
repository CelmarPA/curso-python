""" Desafio 110 - Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na
    tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

    --------------------------
         RESUMO DO VALOR
    --------------------------
    Preço analisado:  R$500,00
    Dobro do preço:   R$1000,00
    Metade do preço:  R$250,00
    80% de aumento:   R$900,00
    35% de redução:   R$325,00
    -------------------------- """

# Importação de funções
from modulos import moeda

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Reduzindo Ainda Mais Seu Programa ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
