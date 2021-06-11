'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
from time import sleep
e = '=-=' * 3
for par in range(0, 50+2, 2):
    sleep(0.2)
    print(par)
print( e +' FIM ' + e )