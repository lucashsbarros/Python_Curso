'''Crie um programa que leia um número pelo teclado e mostre na sua tela a sua porção inteira
Exemplo: Digite um numero: 6.127
O número é 6.127 tem a parte inteira 6'''

'''import math
num = float(input('Digite um número: '))
inteiro = math.trunc(num)
print('O número {} tem a parte inteira {}'.format(num, inteiro))'''

'''num = float(input('Digite um número: '))
print(' O número {} tem a parte inteira {}'.format(num, int(num)))'''

from math import trunc

num = float(input('Digite um número: '))
print('O número {} tem a porção inteira {}'.format(num, trunc(num)))