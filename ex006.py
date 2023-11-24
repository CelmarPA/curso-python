""" Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

    Digite um número:
    O dobro de 85 vale 170.
    O triplo de 85 vale 255.
    A raiz quadrada de 85 é igual a 9,22. """

# Solicita um número ao usuário
num = int(input('Digite um número: '))

# Calcula o dobro, o triplo e a raiz quadrada
dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)

# Imprime os resultados
print(f'O dobro de {num} vale {dobro}. \n'
      f'O triplo de {num} vale {triplo}. \n'
      f'A raiz quadrada de {num} é igual a {raiz:.2f}.')
