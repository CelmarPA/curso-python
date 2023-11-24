""" Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

    Uma distância em metros: 3
    A medida de 3.0m corresponde a
    0.003km
    0.03hm
    0.3dam
    30dm
    300cm
    3000mm """

# Solicita a distância ao usuário
dist = float(input('Uma distância em metros: '))

# Faz a conversão das unidades
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

# Imprime os resultados
print(f'A medida de {dist:.1f}m corresponde a \n'
      f'{km}km \n'
      f'{hm}hm \n'
      f'{dam}dam \n'
      f'{dm:.0f}dm \n'
      f'{cm:.0f}cm \n'
      f'{mm:.0f}mm')
