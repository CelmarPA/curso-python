""" Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
    errado, peça a digitação novamente até ter um valor correto.

    Informe seu sexo: [M/F] n
    Dados inválidos. Por favor, informe seu sexo: l
    Dados inválidos. Por favor, informe seu sexo: w
    Sexo m registrado com sucesso! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Validação de Dados ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita o sexo ao usuário:
sexo = str(input('Informe seus sexo: ')).strip()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))

print(f'Sexo {sexo} registrado com sucesso!')
