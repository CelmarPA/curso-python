""" Desafio 061 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
    termos da progressão usando a estrutura while.

    Gerador de PA
    -=-=--=-=--=-=--=-=--=-=-
    Primeiro termo: 2
    Razão: 5 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Progressão Aritmética v2.0 ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Enunciado
print(f'=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print(f'=' * 30)

# Solicita os dados ao usuário
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Inicialização de variáveis
c = 0

# Formula geral de uma PA: PA = a + (tr) (onde a é o primeiro termo, t o termo e r a razão

while c < 10:
    pa = termo + (c * razao)
    c += 1
    print(f'{pa} → ', end='')

print(f'{cores["red"]}Acabou!{cores["reset"]}')
