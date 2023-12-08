""" Desafio 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já
    na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

    Digite um valor: 7
    Adicionado no final da lista...
    Digite um valor: 2
    Adicionado na posição 0 da lista...
    Digite um valor: 5
    Adicionado na posição 1 da lista...
    Digite um valor: 9
    Adicionado no final da lista...
    Digite um valor: 3
    Adicionado na posição 1 da lista...
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    O valores digitados em ordem foram [2, 3, 5, 7, 9] """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Lista Ordenada ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
numeros = list()

# Ordena a lista sem repetições
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'=-=' * 20)
print(f'Os valores digitados em ordem foram {numeros}')
