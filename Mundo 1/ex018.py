'''Faça um programa que leia um angulo qualquer e mostre na sua tela o valor do seno, cosseno e tangente desse angulo'''

import math
ang = float(input('Digite um ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('O valor para Seno é {:.2f}\nO valor para Cosseno é {:.2f}\nO valor para Tangente é {:.2f}.'.format(sen, cos, tan))