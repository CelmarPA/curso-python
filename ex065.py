""" Desafio 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
    entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
    usuário se ele quer ou não continuar a digitar valores.

    Digite um número: 4
    Quer continuar? [S/N] s
    Digite um número: 2
    Quer continuar? [S/N] s
    Digite um número: 8
    Quer continuar? [S/N] s
    Digite um número: 9
    Quer continuar? [S/N] n

    Você digitou 4 números e a média foi 5.75
    O maior valor foi 9 e o menor foi 2 """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{" Tratando Vários Valores v1.0 ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
opcao = 'S'
count = menor = maior = soma = 0

# Faz as verificações
while opcao == 'S':
    num = int(input('Digite um número: '))
    if count == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
    count += 1
    soma += num
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SsNn':
        print(f'Opção inválida. Tente novamente:')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

# Calcula a média
media = soma / count

# Imprime o resultado
print(f'Você digitou {count} números e a média foi {media:.2f} \n'
      f'O maior valor foi {maior} e o menor foi {menor}')
