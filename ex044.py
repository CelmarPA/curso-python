""" Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
    e condição de pagamento:

    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço normal
    – 3x ou mais no cartão: 20% de juros

    =============== LOJAS PHYTON ================
    Preço das compras: R$1500
    FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro / cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
    Qual é a opção? 1
    Sua compra de R$1500.00 vai custar R$1350.00 no final.

    Qual é a opção? 2
    Quantos parcelas? 10
    Sua compra será parcelada em 10x de R$480.00 COM JUROS!
    Sua compra de R$4000.00 vai custar R$4800.00 no final. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Gerenciador de Pagamentos ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'')
print(f'{cores["red"]}{" LOJAS PYTHON ":=^60}{cores["reset"]}')

# Solicita o preço das compras e a forma de pagamento
preco = float(input('Preço das compras: '))

print(f'FORMAS DE PAGAMENTO \n'
      f'[ 1 ] à vista dinheiro / cheque \n'
      f'[ 2 ] à vista cartão \n'
      f'[ 3 ] 2x no cartão \n'
      f'[ 4 ] 3x ou mais no cartão')
op = int(input('Qual é a opção? '))

# Avalia a forma de pagamento
if op == 1:
    valor = preco - (preco * 0.10)
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif op == 2:
    valor = preco - (preco * 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif op == 3:
    parc = preco / 2
    print(f'Sua compra de R${preco:.2f} será parcelada em 2x de R${parc:.2f}!')
elif op == 4:
    prest = int(input('Quantas parcelas? '))
    valor = preco + (preco * 0.20)
    parc = valor / prest
    print(f'Sua compra será parcelada em {prest}x de R${parc:.2f} COM JUROS! \n'
          f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
else:
    print(f'{cores["red"]}Opção inválida! Recomece a operação!{cores["reset"]}')
