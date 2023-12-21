def leiaDinheiro():
    while True:
        preco_str = input('Digite o preço: R$').replace(',', '.')

        if preco_str.replace('.', '').isdigit():
            preco_float = float(preco_str)
            break
        else:
            print('\033[31mERRO: Digite um preço válido!\033[m')

    return preco_float

# Exemplo de uso
preco_inserido = leiaDinheiro()
print(f'O preço inserido é: R${preco_inserido:.2f}')