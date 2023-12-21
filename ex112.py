""" Desafio 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma
    função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados
    para aceitar apenas valores que seja monetários.

    Digite o preço: R$barato
    ERRO: "barato" é um preço inválido!
    Digite o preço: R$
    ERRO: "" é um preço inválido!
    Digite o preço: R$850,99

    --------------------------
         RESUMO DO VALOR
    --------------------------
    Preço analisado:  R$850,99
    Dobro do preço:   R$1701,98
    Metade do preço:  R$425,50
    80% de aumento:   R$1148,84
    35% de redução:   R$663,77
    -------------------------- """

# Importação de pacotes
from utilidadescev import dado, moeda

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Entrada de Dados Monetários ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Programa principal
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
