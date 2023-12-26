""" Desafio 114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
    Consegui acessar o site Pudim com sucesso!
    O site Pudim não está acessível no momento. """

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Site está Acessível? ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


# Funções
def testSite(url):
    from requests import get, ConnectionError
    try:
        resp = get(url)
        if resp.status_code == 200:
            print(f'\033[34mConsegui acessar o site \"{url}\" com sucesso!\033[m')
        else:
            print(f'O site \"{url}\" não está acessível no momento.')
    except ConnectionError:
        print(f'\033[31mO site \"{url}\" não está acessível no momento.\033[m')


# Programa principal
testSite('https://www.pudim.com.br')
