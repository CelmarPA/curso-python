""" Desafio 014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta
para graus Fahrenheit.

    Informe a temperatura em °C: 31,5
    A temperatura de 31.5°C corresponde a 88,7 ! """

# Solicita a temperatura ao usuário
temp = float(input('Informe a temperatura em °C: '))

# Faz a conversão de graus Celsius para Fahrenheit
f = (9 / 5) * temp + 32  # não é preciso usar os parentes, em razão da ordem de precedência

# Imprime o resultado
print(f'A temperatura de {temp:.2f}°C corresponde a {f:.2f}°F!')
