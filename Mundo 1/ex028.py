'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o npumero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
import random
numusuario  = int(input('Digite um número entre 0 e 5:'))
num0 = 0
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
lista = [num0,num1,num2,num3,num4,num5]
esc = random.choice(lista)
print('O número escolhido pelo computador foi: {}'.format(esc))
if numusuario == esc:
    print('Parábens, você ganhou do computador!')
else:
    print('Desculpe, mas o computador venceu dessa vez')
print('-----FIM-----')