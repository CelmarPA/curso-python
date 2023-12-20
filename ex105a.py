""" Desafio 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
    um dicionário com as seguintes informações:

    – Quantidade de notas
    – A maior nota
    – A menor nota
    – A média da turma
    – A situação (opcional)

    # Programa principal
    resp = notas(5.5, 9.5, 10, 6.5, sit=True
    print(resp)

    {'total': 4, 'maior': 10, 'menor': 5.5, 'média': 7.875, 'situação': 'BOA'} """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Analisando e Gerando Dicionários ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)


# Função
def notas(*n, sit=False):
    soma = 0
    for v in n:
        soma += v
    media = soma / len(n)
    nota = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': media}
    if sit is True:
        if media < 6:
            nota['situação'] = 'RUIM'
        elif 6 < media < 7:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'BOA'
    return nota


# Programa principal
resp = notas(5.5, 6.5, 6.5, sit=True)
print(resp)
