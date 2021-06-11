'''Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um
laço for'''
from time import sleep
esp = '=-' * 3
n = int(input('Digite um número: '))
for c in range(0,10+1):
    print(n * c)
    sleep(1)
print(esp + 'FIM' + esp)
