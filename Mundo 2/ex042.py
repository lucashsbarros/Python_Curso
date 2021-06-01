'''Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
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
    if r1 == r2 == r3 == r1:
        print('Esse triangulo é Equilátero ')
    elif r1 != r2 != r3 != r1:
        print('Esse triangulo é Escaleno')
    elif r1 == r2 != r3 == r1 or r1 != r2 == r3 != r1:
        print('Esse triangulo é Isósceles')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')