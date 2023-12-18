""" Desafio 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
    e mostre uma mensagem com tamanho adaptável.

    Ex:
     escreva(‘Olá, Mundo!’) Saída:
        ~~~~~~~~~~~~~
         Olá, Mundo!
        ~~~~~~~~~~~~~ """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Um Print Especial ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


# Função
def escreva(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}  ')
    print(f'~' * tam)


# Programa Principal
txt = str(input('Digite uma mensagem: '))

# Chama a função escreva
escreva(txt)
