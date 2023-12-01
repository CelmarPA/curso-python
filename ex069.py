""" Desafio 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
    deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.

    ------------------------------
         CADASTRE UMA PESSOA
    ------------------------------
    Idade: 33
    Sexo [S/N]: M
    ------------------------------
    Quer continuar? S
    ------------------------------
         CADASTRE UMA PESSOA
    ------------------------------
    Idade: 12
    Sexo [S/N]: F
    ------------------------------
    Quer continuar? 25
    Quer continuar? S
    ------------------------------
         CADASTRE UMA PESSOA
    ------------------------------
    Idade: 25
    Sexo [S/N]: F
    ------------------------------
    Quer continuar? n
    ========= FIM DO PROGRAMA ========
    Total de pessoas com mais de 18 anos: 2
    Ao to-do temos 1 homens cadastrados
    E temos 1 mulher(es) com menos de 20 anos """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Análise de Dados do Grupo ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
maior18 = 0
homens = 0
mulher20 = 0

while True:
    # Imprime o enunciado
    print(f'-' * 30)
    print((f'{"Cadastre uma pessoa":^30}'.upper()))
    print(f'-' * 30)
    # Solicita e valida os dados
    idade = int(input('Idade: '))
    while 0 >= idade or idade > 110:
        idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    # Verificações da condições
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if idade > 20 and sexo == 'F':
        mulher20 += 1
    # Solicita ao usuário se quer continuar
    print(f'-' * 20)
    opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while opc not in "SN":
        opc = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'Total de pessoas com mais de 18 anos: {maior18} \n'
      f'Ao todo temos {homens} homen(s) cadatrado(s) \n'
      f'E temos {mulher20} mulher(es) com mais de 20 anos')
