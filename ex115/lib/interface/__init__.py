# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}


def leiaInt(n):
    """
    Função de validação de número inteiro
    :param n: Parâmetro que será validade
    :return: Retorna o valor validado
    """
    while True:
        try:
            num = str(input(n)).strip()
            valor = int(num)
            break
        except (ValueError, TypeError):
            print(f'{cores["red"]}ERRO: Por favor, digite um número inteiro válido!{cores["reset"]}')
            return 0
        except KeyboardInterrupt:
            print(f'\n{cores["red"]}O usuário preferiu não digitar esse número.')
            return 1
    return valor


def linha(tam=42):
    """
    Função para imprimir linha
    :param tam: Parâmetro do tamanho da linha
    :return: A linha impressa
    """
    return '-' * tam


def cabecalho(txt):
    """
     Função para imprimir cabeçalho
    :param txt: Parâmetro que recebe o texto que vai ficar dentro do cabeçalho
    :return: O cabeçalho
    """
    print(linha())
    print(f'{cores["lilas"]}', end='')
    print(f'{txt}'.center(len(linha())))
    print(f'{cores["reset"]}', end='')
    print(linha())


def menu(lista):
    """
    Função para criação de menu
    :param lista: Parâmetro com a lista de itens do menu
    :return: A opção selecionada e validada
    """
    cabecalho('MENU PRINCIPAL')
    count = 1
    for item in lista:
        print(f'{cores["yellow"]}{count}{cores["reset"]} - {cores["blue"]}{item}{cores["reset"]}')
        count += 1
    print(linha())
    opc = leiaInt(f'{cores["yellow"]}Sua Opção: {cores["reset"]}')
    return opc
