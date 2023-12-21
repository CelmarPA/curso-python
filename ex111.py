""" Desafio 111 - Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
    Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo
    funcionando.

    --------------------------
         RESUMO DO VALOR
    --------------------------
    Preço analisado:  R$500,00
    Dobro do preço:   R$1000,00
    Metade do preço:  R$250,00
    80% de aumento:   R$900,00
    35% de redução:   R$325,00
    -------------------------- """

# Importação de pacotes
from utilidadescev import moeda

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Transformando Módulos em Pacotes ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)
