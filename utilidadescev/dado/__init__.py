# Funções
def leiaDinheiro(p):
    """
    Função para validade um valor numérico
    :param p: Parâmetro a ser verificado
    :return: Retorna um valor float validado
    """
    preco = str(input(p)).replace(',', '.').strip()
    while preco.replace('.', '').isdigit() is False:
        print(f'\033[31mERRO: \"{preco}\" é um preço inválido!\033[m')
        preco = str(input('Digite o preço: R$'))
        if preco.replace('.', '').isdigit() is True:
            break
    return float(preco)
