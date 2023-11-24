""" Desafio 020 - O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

    Primeiro aluno: Paulo
    Segundo aluno: Ana
    Terceiro aluno: Pedro
    Quarto aluno: Maria
    A ordem de apresentação será
    ['Pedro', 'Ana', 'Maria', 'Paulo'] """

# Importação de bibliotecas
from random import shuffle

# Solicita os nomes ao usuário
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

# Coloca os nomes em uma lista
alunos = [a1, a2, a3, a4]

# Embaralha a lista
shuffle(alunos)  # O shuffle retorna a lista defina embaralhada, não é necessário criar um outra lista

# Imprime o resultado
print(f'A ordem de apresentação será \n'
      f'{alunos}')
