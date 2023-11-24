""" Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
    quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
    uma área de 2 metros quadrados.

    Largura da parede: 2,5
    Altura da parede: 1,75
    Sua parede tem a dimensão de 2,5 x 1,75 e sua área é de 4,375m².
    Para pintar essa parede, você precisará de 2,1785l de tinta. """

# Solicita a largura e altura da parede
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

# Calcula a área e a quantidade de tinta
area = largura * altura
tinta = area / 2

# Imprime os resultados
print(f'Sua parede tem dimensão de {largura} x {altura} e sua área é de {area:.3f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.4f}l de tinta.')
