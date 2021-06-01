'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Graus Fahrenheit'''

celsius = float(input('Digite o(s) grau(s) em ºC: '))
fah = ((9 * celsius) / 5) + 32
print('O valor convertido em Fahrenheit é {:.2f}ºF'.format(fah))
