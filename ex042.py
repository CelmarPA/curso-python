""" Desafio 042 - Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
    tipo de triângulo será formado:

    – EQUILÁTERO: todos os lados iguais
    – ISÓSCELES: dois lados iguais, um diferente
    – ESCALENO: todos os lados diferentes

    Primeiro seguimento: 3
    Segundo seguimento: 4
    Terceiro seguimento: 5
    Os seguimentos acima PODEM FORMAR um triângulo ESCALENO!

    Primeiro seguimento: 3
    Segundo seguimento: 3
    Terceiro seguimento: 4
    Os seguimentos acima PODEM FORMAR um triângulo ISÓSCELES!

    Primeiro seguimento: 7
    Segundo seguimento: 7
    Terceiro seguimento: 7
    Os seguimentos acima PODEM FORMAR um triângulo EQUILÁTERO!

    Primeiro seguimento: 1
    Segundo seguimento: 9
    Terceiro seguimento: 8
    Os seguimentos acima NÃO PODEM FORMAR um triângulo! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Analisando Triângulos v2.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita os seguimentos ao usuário
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

# Analisa se é possível formar um Triângulo
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print(f'Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print(f'EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print(f'ISÓSCELES!')
    else:
        print(f'ESCALENO!')
else:
    print(f'Os seguimentos acima NÃO PODEM FORMAR um triângulo!')
