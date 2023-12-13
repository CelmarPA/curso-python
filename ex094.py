""" Desafio 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
    em um dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade
    C) Uma lista com as mulheres
    D) Uma lista de pessoas com idade acima da média

    Nome: Gustavo
    Sexo: [M/F] M
    Idade: 40
    Quer continuar? [S/N] s
    Nome: Pedro
    Sexo: [M/F] M
    Idade: 22
    Quer continuar? [S/N] s
    Nome: Maria
    Sexo: [M/F] F
    Idade: 33
    Quer continuar? [S/N] s
    Nome: Paula
    Sexo: [M/F] F
    Idade: 12
    Quer continuar? [S/N] n
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    - O grupo tem 4 pessoas.
    - A média de idade é de 26,75 anos.
    - As mulheres cadastradas foram: Maria Paula
    - Lista das pessoas que estão acima da média>

    nome = Gustavo; sexo = M; idade = 40;

    nome = Maria; sexo = F; idade = 33;
    << ENCERRADO >> """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Unindo Dicionários e Listas ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários e listas
cadastro = list()
pessoas = dict()
soma_idade = 0

while True:
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        print(f'ERRO! Por favor, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    while 0 > pessoas['idade'] or pessoas['idade'] > 120:
        print(f'ERRO! Por favor, digite  uma idade válida.')
        pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())

    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opc not in "SN":
        print(f'ERRO! Responda apenas S ou N.')
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'-=' * 30)
# Estatísticas
print(f'A) O grupo tem {len(cadastro)} pessoa(s).')

# Calcula a média da idades
for c, v in enumerate(cadastro):
    soma_idade = sum(pessoa['idade'] for pessoa in cadastro)
media = soma_idade / len(cadastro)
print(f'B) A média de idade é de {media:.2f} anos.')

# Mulheres cadastradas
print(f'C) As mulheres cadastradas foram: ', end='')
for c, v in enumerate(cadastro):
    if cadastro[c]['sexo'] == 'F':
        print(f'{cadastro[c]["nome"]} ', end='')
    else:
        print(f'Não foram cadastradas.', end='')

# Pessoas acima da média da idade
print(f'\nD) Lista das pessoas que estão acima da média:')
for c, v in enumerate(cadastro):
    if cadastro[c]['idade'] > media:
        print(f'    nome = {cadastro[c]["nome"]}; sexo = {cadastro[c]["sexo"]}; idade = {cadastro[c]["idade"]};')
    else:
        print('     Não há pessoas acima da média!')
# Imprime a mensagem final
print('<< ENCERRADO >>')
