""" Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal
    (IMC) e mostre seu status, de acordo com a tabela abaixo:

    – IMC abaixo de 18,5: Abaixo do Peso
    – Entre 18,5 e 25: Peso Ideal
    – 25 até 30: Sobrepeso
    – 30 até 40: Obesidade
    – Acima de 40: Obesidade Mórbida

    Qual é seu peso? (kg) 87
    Qual é a sua altura? (m) 1.97
    O IMC dessa pessoa é de 22.4
    PARABÉNS, você está na faixa de PESO NORMAL!
    Você está em OBESIDADE!
    Você está em OBESIDADE MÓRBIDA, cuidado!
    Você está em ABAIXO DO PESO normal! """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{" Índice de Massa Corporal ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita os dados aos usuário
peso = float(input('Qual é seu peso (kg)? '))
altura = float(input('Qual é a sua altura (m)? '))

# Calcula o IMC
imc = peso / (pow(altura, 2))

# Imprime o IMC
print(f'O IMC dessa pessoa é de {imc:.1f}')
# Avalia o IMC
if imc <= 18.5:
    print(f'Você está em ABAIXO DO PESO normal!')
elif imc <= 25:
    print(f'PARABÉNS, você está na faixa de PESO NORMAL!')
elif imc <= 30:
    print(f'Você está em SOBRE PESO!')
elif imc <= 40:
    print(f'Você está em OBESIDADE!')
else:
    print(f'Você está em OBESIDADE MÓRBIDA, cuidado!')
