""" Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
    ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

    Primeiro aluno: Paulo
    Segundo aluno: Ana
    Terceiro aluno: Pedro
    Quarto aluno: Maria
    O aluno escolhido foi Maria """

# Importação de bibliotecas
from random import choice

# Solicita o nome dos alunos ao usuário
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

# Coloca os nomes em uma lista
alunos = [a1, a2, a3, a4]

# Faz o sorteio de um nome da lista
escolhido = choice(alunos)

# Imprime o resultado
print(f'O aluno escolhido foi {escolhido}!')


