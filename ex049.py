""" Desafio 049 - Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora
    utilizando um laço for.
    Digite um número para ver sua tabuada: """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Tabuada v.2.0 ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usuário
num = int(input('Digite um número para ver sua tabuada: '))

# Gera a tabuada
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
