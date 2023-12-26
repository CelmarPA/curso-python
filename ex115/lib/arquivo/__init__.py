# Importação de pacotes e modulos
from ex115.lib. interface import *

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}


def localizar_arquivo(nome):
    """
    Função para localizar o arquivo
    :param nome: Parâmetro que recebe o nome do arquivo a ser localizado
    :return: Verdadeiro se o arquivo for localizado e falso se não for localizado
    """
    try:
        with open(nome, 'r') as file:
            file.read()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
        Função para criação do arquivo
        :param nome: Parâmetro que recebe o nome do arquivo a ser criado
        :return: Não tem retorno
        """
    try:
        with open(nome, 'w') as file:
            file.write('')
    except Exception as erro:
        print(f'{cores["red"]}Houve um ERRO ao criar o arquivo, {erro}{cores["reset"]}')
    else:
        print(f'{cores["blue"]}Arquivo \"{nome}\" criado com sucesso!{cores["reset"]}')


def ler_arquivo(nome):
    """
    Função para ler o arquivo
    :param nome: Parâmetro que recebe o nome do arquivo a ser lido
    :return: Não tem retorno
    """
    try:
        with open(nome, 'rt') as file:
            a = file.readlines()
    except Exception as erro:
        print('Erro ao ler o arquivo!', erro)
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        file.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    """
    Função para cadastro de pessoas
    :param arquivo: Parâmetro que recebe o nome do arquivo que irá receber o cadastro
    :param nome: Parâmetro que contém o nome da pessoa cadastrada
    :param idade: Parâmetro que contém a idade da pessoa cadastrada
    :return: Não tem retorno
    """
    try:
        with open(arquivo, 'a') as file:
            conteudo = f'{nome};{idade}\n'
            file.write(conteudo)
            print(f'{cores["blue"]}Novo registro de {nome} adicionado!{cores["reset"]}')
    except Exception as erro:
        print(f'{cores["red"]}Houve um ERRO na abertura do arquivo!{erro}{cores["reset"]}')
    finally:
        file.close()
