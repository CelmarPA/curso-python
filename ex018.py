""" Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
    tangente desse ângulo.

    Digite o ângulo que você deseja: 0,30
    O ângulo de 30,0 tem o SENO de 0,50
    O ângulo de 30,0 tem o COSSENO de 0,87
    O ângulo de 30,0 tem a TANGENTE de 0,58 """

# Importação de bibliotecas
from math import sin, cos, tan, radians

# Solicita o ângulo ao usuário
ang = float(input('Digite o ângulo que você deseja: '))

# Converte de graus para radiano
angulo = radians(ang)

# Imprime os resultados
print(f'O ângulo de {ang:.1f} tem o SENO de {sin(angulo):.2f} \n'
      f'O ângulo de {ang:.1f} tem o COSSENO de {cos(angulo):.2f} \n'
      f'O ãngulo de {ang:.1f} tem a TANGENTE de {tan(angulo):.2f}')
