""" Desafio 062 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
    O programa encerrará quando ele disser que quer mostrar 0 termos.

    Gerador de PA
    -=-=--=-=--=-=--=-=--=-=-
    Primeiro termo: 0
    Razão: 5
    0 5 10 15 20 25 30 35 40 45 PAUSA
    Quantos termos você quer mostrar a mais? 5
    50 55 60 65 70 PAUSA
    Quantos termos você quer mostrar a mais? 0
    Progressão finalizada com 27 termos mostrados. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Super Progressão Aritmética v3.0 ":=^60}{cores["reset"]}')
print(f'{cores["lilas"]}-=-{cores["reset"]}' * 20)

# Enunciado
print(f'=' * 30)
print(f'{"GERADOR DE PA":^30}')
print(f'=' * 30)

# Solicita os dados ao usuário
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Inicialização de variáveis
c = 0

# Formula geral de uma PA: PA = a + (tr) (onde a é o primeiro termo, t o termo e r a razão

while c < 10:
    pa = termo + (c * razao)
    c += 1
    print(f'{pa} {cores["lilas"]}→ {cores["reset"]}', end='')
    # Verifica se foram feitos os 10 termos e pausa
    if c == 10:
        print(f'{cores["red"]}PAUSE!{cores["reset"]}')
        termo = int(input('Quantos termos você quer mostrar a mais? '))
        while termo > 0:
            while termo != 0:
                pa += razao
                termo -= 1
                c += 1
                print(f'{pa} {cores["lilas"]}→ {cores["reset"]}', end='')
            print(f'{cores["red"]}PAUSE!{cores["reset"]}')
            termo = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cores["red"]}{c}{cores["reset"]} termos mostrados.')
