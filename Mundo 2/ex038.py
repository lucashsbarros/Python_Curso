'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
- 0 primeiro valor é maior
- O segundo valor é maior
- não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo número '))
if n1 > n2:
    print('O primeiro número que é {} é maior que o segundo número que é {}.'.format(n1,n2))
elif n1 < n2:
    print('O segundo número que é {} é maior que o primeiro número que é {}.'.format(n2,n1))
elif n1 == n2:
    print('Os dois números são iguais')


# MODO CURSO EM VIDEO
# Apenas colocou a terceira condição da seguinte forma:

# else:
#     print('Os dois números são iguais')