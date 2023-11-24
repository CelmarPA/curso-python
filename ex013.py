""" Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
    com 15% de aumento.

    Qual é o sálario do Funcionário? R$4319.43
    Um funcionário que ganhava R$4319.43, com 15% de aumento, passa a receber R$4967.34! """

# Solicita o salário ao usuário
salario = float(input('Qual é sálario do Funcionário? R$'))

# Calcula o novo sálario com 15% de aumento
novo = salario + (salario * 15 / 100)

# Imprime o resultado
print(f'um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}!')
