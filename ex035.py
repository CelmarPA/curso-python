""" Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
    formar um triângulo.

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                        Analisador de Triângulos
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Primeiro seguimento: 3.5
    Segundo seguimento: 2.75
    Terceiro seguimento: 4
    Os seguimentos acima PODEM FORMAR um triângulo!

    Primeiro seguimento: 2
    Segundo seguimento: 4
    Terceiro seguimento: 9
    Os seguimentos acima NÂO PODEM FORMAR um triângulo! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Analisando Triângulos v1.0 ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'')

# Solicita a medida dos seguimentos ao usuário
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

# Analisa se é possível a formação de um triangulo
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Os seguimento acima PODEM FORMAR um triângulo!')
else:
    print('Os seguimento acima NÂO PODEM FORMAR um triângulo!')
