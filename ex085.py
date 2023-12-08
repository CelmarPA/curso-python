""" Desafio 085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
    única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
    ímpares em ordem crescente.

    Digite o 1º valor: 5
    Digite o 2º valor: 8
    Digite o 3º valor: 2
    Digite o 4º valor: 4
    Digite o 5º valor: 3
    Digite o 6º valor: 7
    Digite o 7º valor: 10
    =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
    Os valores pares digitados foram: [2, 4, 8, 10]
    Os valores ímpares digitados foram: [3, 5, 7] """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Lista de Pares e Ímpares ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
valores = [[], []]

# Solicita sete valores ao usuário e separa os valores pares e ímpares e uma lista composta
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

# Imprime as lista dos valores pares e ímpares
print(f'Os valores pares digitados foram {sorted(valores[0])}.')
print(f'Os valores ímpares digitados foram {sorted(valores[1])}.')
