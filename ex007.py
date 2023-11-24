""" Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

    Primeira nota do aluno: 5,5
    Segunda nota do aluno: 2
    A média entre 5,5 e 2,0 é igual a 3,8.
    """

# Solicita as notas ao usuário
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

# Calcula a média do aluno
media = (n1 + n2) / 2

# Imprime o resultado
print(f'A média entre {n1:.1f} e {n2:.1f} é igual a {media:.1f}.')
