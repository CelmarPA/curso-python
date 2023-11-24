""" Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em
    que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

    Digite uma frase:    Amanda ama Pedro
    A letra A aparece 5 vezes na frase.
    A primeira letra A apareceu na posição 1
    A última letra A apareceu na posição 10  """

# Solicita uma frase ao usuário
frase = str(input('Digite uma frase: ')).strip(). lower()

# Imprime o resultado
print(f'A letra A aparece {frase.count('a')} vezes na frase.')

print(f'A primeira letra A apareceu na posição {frase.find('a') + 1}')

print(f'A última letra A apareceu na posição {frase.rfind('a') + 1}')
