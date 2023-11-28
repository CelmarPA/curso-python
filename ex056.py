""" Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

    ------- 1ª PESSOA --------
    Nome: João
    Idade: 22
    Sexo [M/F]: M
    ------- 3ª PESSOA --------
    Nome: Maria
    Idade: 12
    Sexo [M/F]: F
    ------- 4ª PESSOA --------
    Nome: Claudio
    Idade: 75
    Sexo [M/F]: M
    ------- 1ª PESSOA --------
    Nome: Ana
    Idade: 9
    Sexo [M/F]: F
    A média de idade do grupo foi de 29,5 anos
    O homem mais velho tem 75 anos e se chama Cláudio.
    AO to-do são 2 mulheres com menos de 20 anos """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Analisador Completo ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma_idade = 0
mais_velho = 0
nome_velho = ''
menos_20 = 0

# Solicita os dados ao usuário:
for i in range(1, 5):
    print(f'-------- {i}ª PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    # Soma das idades
    soma_idade += idade
    # Verifica a idade e o nome do homem mais velho
    if i == 1 and sexo[0] == 'M':
        mais_velho = idade
        nome_velho = nome
    if sexo[0] == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    # Conta quantas mulheres tem menos de 20 anos
    if 'F' in sexo[0] and idade < 20:
        menos_20 += 1

# Calcula a média da idades
media = soma_idade / 4
# Imprime a média das idades
print(f'A média da idade do grupo foi de {media:.2f} anos.')

# Imprime o nome e a idade do homem mais velho
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')

# Imprime quantas mulheres tem menos de 20 anos
print(f'Ao todo são {menos_20} mulher(es) com menos de 20 anos.')
