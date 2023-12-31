""" Desafio 083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
    deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
    Digite a expressão: ((a+b) * c)
    Sua expressão é válida!
    Digite a expressão: ((a+b)*(a*c)-2
    Sua expressão está errada! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Dividindo Valores em Várias Listas ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
parenteses = list()

expressao = str(input('Digite a expressão: '))

for p in expressao:
    if p == '(':
        parenteses.append('(')
    elif p == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print(f'Sua expressão é válida!')
else:
    print(f'Sua expressão está errada!')
