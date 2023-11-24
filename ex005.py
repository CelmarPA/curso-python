""" Desafio 005 - Faça um programa que leia um número Inteiro e mostre na tela o seu
    sucessor e seu antecessor.

    Digite um número:
    Analisando o valor 2, seu antecessor é 1 e o sucessor é 3. """

# Solicita o número ao usuário
num = int(input('Digite um número: '))

# Calcula o antecessor e o sucessor
ant = num - 1
suc = num + 1

# Imprime os resultados
print(f'Analisando o valor {num}, seu antecessor é {ant} e o sucessor {suc}.')
