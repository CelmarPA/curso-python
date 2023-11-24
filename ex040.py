""" Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
    final, de acordo com sua média atingida:

    – Média abaixo de 5.0: REPROVADO
    – Média entre 5.0 e 6.9: RECUPERAÇÃO
    – Média 7.0 ou superior: APROVADO

    Primeira nota: 7.5
    Segunda nota: 8
    Tirando 7.5 e 8.0 a média do aluno é de 7.8!
    O aluno está APROVADO!

    Primeira nota: 6.5
    Segunda nota: 5
    Tirando 6.5 e 5.0 a média do aluno é de 5.8!
    O aluno está de RECUPERAÇÃO!

    Primeira nota: 2
    Segunda nota: 4
    Tirando 2.0 e 4.0 a média do aluno é de 3.0!
    O aluno está REPROVADO! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Aquele Clássico da Média ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Solicita as notas ao usuário
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

# Calcula a média
media = (n1 + n2) / 2

# Imprime as notas e a média
print(f'Tirando {n1:.1f} e {n2:.1f} a média do aluno é de {media:.1f}!')

# Analisa as médias
if media >= 7:
    print(f'O aluno está {cores["blue"]}APROVADO!{cores["reset"]}')
elif media < 5:
    print(f'O aluno está {cores["red"]}REPROVADO!{cores["reset"]}')
else:
    print(f'O aluno está de {cores["yellow"]}RECUPERAÇÃO!{cores["reset"]}')
