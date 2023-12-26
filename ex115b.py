""" Desafio 115 - Vamos criar um menu em Python, usando modularização.

    --------------------------------------
                MENU PRINCIPAL
    --------------------------------------
    1 - Ver pessoas cadastradas
    2 - Cadastrar nova Pessoa
    3 - Sair do Sistema
    --------------------------------------
    Sua Opção: 1
    --------------------------------------
              PESSOAS CADASTRADAS
    --------------------------------------
    Ana Paula Vieira        32 anos
    Cláudio Mendonça        18 anos
    --------------------------------------
                MENU PRINCIPAL
    --------------------------------------
    1 - Ver pessoas cadastradas
    2 - Cadastrar nova Pessoa
    3 - Sair do Sistema
    --------------------------------------
    Sua Opção: 2
    --------------------------------------
                NOVO CADASTRO
    --------------------------------------
    Nome: Zuleide Lima
    Idade: 55
    Registro de Zuleide adicionado.
    --------------------------------------
        Saindo do sistema... Até logo!
    -------------------------------------- """

# Importação de pacotes e modulos
from ex115.lib. interface import *
from ex115.lib. arquivo import *
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" SISTEMA ARQUIVO v1.0 ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Programa principal
# Inicialização do arquivo
arq = 'cadastro.txt'

if not localizar_arquivo(arq):
    print(f'{cores["yellow"]}Criando arquivo de cadastro...{cores["reset"]}')
    sleep(1.5)
    criar_arquivo(arq)

while True:
    # Lista com os itens do menu
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    # Verifica as opções escolhidas
    if opcao == 1:  # Lista as pessoas cadastradas
        cabecalho('Opção 1')
        ler_arquivo(arq)
    elif opcao == 2:  # Cadastra nova pessoa
        cabecalho('Opção 2')
    elif opcao == 3:  # Sai do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{cores["red"]}ERRO: Digite uma opção válida!{cores["reset"]}')
    sleep(1.5)
