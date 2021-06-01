'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa'''

'''import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa do {:.2f}'. format(hip))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('A hipotenusa dos valores é {:.2f}'.format(hypot(co, ca)))




