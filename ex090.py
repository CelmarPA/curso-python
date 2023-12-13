""" Desafios 090 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.

    Nome: Joaquim
    Média de Joaquim: 4.5
    Nome é igual a Joaquim
    Média é igual a 4.5
    Situação é Reprovado """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Dicionário em Python ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários e listas
boletim = dict()

# Solicita os dados ao usuário
boletim['nome'] = str(input('Nome: '))
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))

# Verifica a situação do aluno
if boletim['média'] < 5:
    situacao = f'{cores["red"]}Reprovado{cores["reset"]}'
elif 5 >= boletim['média'] < 7:
    situacao = f'{cores["yellow"]}Recuperação{cores["reset"]}'
else:
    situacao = f'{cores["blue"]}Aprovado{cores["reset"]}'

boletim['situação'] = situacao

print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

for k, v in boletim.items():
    print(f'{k.capitalize()} é igual a {v}')
