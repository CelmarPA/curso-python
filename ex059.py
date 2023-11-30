""" Desafio 059 - Crie um programa que leia dois valores e mostre um menu na tela:

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

    Primeiro valor: 5
    Segundo valor: 8
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    >> Qual é a sua opção? 1
     A soma entre 5 + 8 é 13
        =-==-==-==-==-==-==-==-==-=
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        >> Qual é a sua opção? 5
        Finalizando...
        =-==-==-==-==-==-==-==-==-=
        Fim do programa! Volte sempre!
     """
# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Criando um Menu de Opções ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita dois números ao usuário
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

# Inicialização de variáveis
opcao = 0

while opcao != 5:
    print(f' ' * 3, f'[ 1 ] somar')
    print(f' ' * 3, f'[ 2 ] multiplica')
    print(f' ' * 3, f'[ 3 ] maior')
    print(f' ' * 3, f'[ 4 ] novos números')
    print(f' ' * 3, f'[ 5 ] sair do programa')
    opcao = int(input(f'>>>>> Qual é a sua opção? '))

    # Realiza a soma
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    # Realiza a multiplicação
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    # Verifica qual maior
    elif opcao == 3:
        if n1 > n2:
            res = f'o maior é {n1}'
        elif n2 > n1:
            res = f'o maior é {n2}'
        else:
            res = f'os dois são iguais'
        print(f'Entre {n1} e {n2} {res}')
    # Solicita novos números
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    # Finaliza o programa
    elif opcao == 5:
        print(f'Finalizando...')
        sleep(1.5)
    else:
        print(f'Opção inválida. Tente novamente!')
    # Imprime a delimitação de cada opção
    print(f'=-=' * 10)

# Imprime a mensagem final
print(f'Fim do programa! Volte sempre!')
