'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar triangulo'''
print('-=' * 15)
print('Analisando um triangulo' )
print('-=' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print('-=' * 15)
print('Analisando os dados...')
from time import sleep
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
