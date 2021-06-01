'''Crie um porgrmaa que leia um número inteiro e mostre na tela se ele é par ou impar'''

num = int(input('Digite um número: '))
if (num/2) % 1:
    print('O número {} é impar'.format(num))
else:
    print('O número {} é par'.format(num))

