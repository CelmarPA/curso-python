""" Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
    da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
    salário ou então o empréstimo será negado.

    Valor da casa: R$80000
    Salário do comprador: R$1600
    Quantos anos de financiamento? 7
    Para Pegar uma cosa de R$80000.00 em 7 anos a prestação será de R$952.38!
    Empréstimo NEGADO!

    Valor da casa: R$80000
    Salário do comprador: R$10000
    Quantos anos de financiamento? 7
    Para Pegar uma cosa de R$80000.00 em 7 anos a prestação será de R$952.38!
    Empréstimo pode ser CONCEDIDO! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Aprovando Empréstimo ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita o valor da casa, salário e prestações ao usuário
valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

# Calculo da prestação mensal
prest = valor / (anos * 12)

print(f'Para pegar uma casa de R${valor:.2f} em {anos} anos a prestação será de {prest:.2f}!')

# Avalia se o empréstimo pode ou não ser concedido
if prest <= (salario * 0.30):
    print(f'Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO!')
