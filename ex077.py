""" Desafio 077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
    mostrar, para cada palavra, quais são as suas vogais.
    Na palavra APRENDER temos a e e
    Na palavra PROGRAMAR temos o a a
    Na palavra LINGUAGEM temos i u a e
    Na palavra PYTHON temos o
    Na palavra CURSO temos u o
    Na palavra GRATIS temos a i
    Na palavra ESTUDAR temos e u a
    Na palavra PRATICAR temos a i a
    Na palavra TRABALHAR temos a a a
    Na palavra MERCADO temos e a o
    Na palavra PROGRAMADOR temos o a a o
    Na palavra FUTURO temos u u o
    """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Contando Vogais ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')

for c, p in enumerate(palavras):
    print(f'Na palavra {p.upper()} temos ', end='')
    for v in p.lower():
        if v.lower() in 'aeiou':
            print(f'{v} ', end='')
    print(f'')
