# Funções
def aumentar(preco=0.0, porcentagem=0, formatacao=False):
    """
    Função para calcular um aumento percentual de um valor
    :param preco: Parâmetro que irá receber o aumento
    :param porcentagem: Valor da porcentagem de aumento
    :param formatacao: Parâmetro que define se o valore será ou não formatado
    :return: Retorna o valor com aumento percentual definido
    """
    valor = preco + (preco * porcentagem / 100)
    return valor if formatacao is False else moeda(valor)


def diminuir(preco=0.0, porcentagem=0, formatacao=False):
    """
    Função para calcular a redução percentual de um valor
    :param preco: Parâmetro que irá receber a redução
    :param porcentagem: Valor da porcentagem de redução
    :param formatacao: Parâmetro que define se o valore será ou não formatado
    :return: Retorna o valor com redução percentual definida
    """
    valor = preco - (preco * porcentagem / 100)
    return valor if formatacao is False else moeda(valor)


def dobro(preco=0.0, formatacao=False):
    """
    Função para calcular o dobro de um valor
    :param preco: Parâmetro que irá ser dobrado
    :param formatacao: Parâmetro que define se o valore será ou não formatado
    :return: Returna o dobro do valor escolhido
    """
    valor = preco * 2
    return valor if formatacao is False else moeda(valor)


def metade(preco=0.0, formatacao=False):
    """
        Função para calcular a metade de um valor
        :param preco: Parâmetro que irá ser reduzido a metade
        :param formatacao: Parâmetro que define se o valore será ou não formatado
        :return: Returna a metade do valor escolhido
        """
    valor = preco / 2
    return moeda(valor) if formatacao is True else valor


def moeda(preco=0.0, cifra='R$'):
    """
    Função para formatação em formado monetário
    :param preco: Parâmetro que irá receber a formatação
    :param cifra: Parâmetro para definição da cifra
    :return: Retorna o valor formatado na moeda selecionada
    """
    return f'{cifra}{preco:.2f}'.replace('.', ',')


def moeda2(preco=0.0, cod='pt_BR.UTF-8'):
    """
    Função para formatação em formado monetário
    :param preco: Parâmetro que ira receber a formatação
    :param cod: Parâmetro que recebe o código regional para definição da cifra
    :return: Retorna o valor formatado na moeda do país do sistema
    """
    # Importação da biblioteca locale
    from locale import setlocale, LC_ALL, currency
    # Define a localidade padrão para a do sistema
    setlocale(LC_ALL, f'{cod}')
    # Formata o preço como moeda com grouping ativado
    return currency(preco, grouping=True)


def resumo(preco, aumento=10, reducao=5):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print(f'-' * 30)


def titulo(txt):
    print(f'-' * 30)
    print(f'{txt}'.center(30))
    print(f'-' * 30)