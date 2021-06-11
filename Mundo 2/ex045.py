'''
Crie um programa que faça o computador jogar Jokenpo com você

'''

# # forma 1
# import random
#
# print(' Vamos jogar JOKENPÔ !!! ')
#
# usuario = input('Digite a sua escolha: ').lower()
#
# lista = ['pedra', 'papel', 'tesoura']
# pc = random.choice(lista)
# print('A escolha do computador foi: {}'.format(pc))
# resultado = ""
# if pc == usuario:
#     resultado = "Empate"
# elif usuario == 'pedra' and pc == 'tesoura':
#     resultado = 'Você venceu!'
# elif usuario == 'papel' and pc == 'pedra':
#     resultado = 'Você venceu!'
# elif usuario == 'tesoura' and pc == 'papel':
#     resultado = 'Você venceu!'
# else:
#     resultado = 'Computador venceu'
# print(resultado)
#
# # forma 2
#
# import random
#
# print(' Vamos jogar JOKENPÔ !!! ')
#
# usuario = input('Digite a sua escolha: ').lower()
#
# lista = ['pedra', 'papel', 'tesoura']
# pc = random.choice(lista)
# print('A escolha do computador foi: {}'.format(pc))
#
# if pc == usuario:
#     print('Empate')
# elif usuario == 'pedra' and pc == 'tesoura':
#     print('Você venceu!')
# elif usuario == 'pedra' and pc == 'papel':
#     print('Computador venceu')
# elif usuario == 'papel' and pc == 'tesoura':
#     print('Computador venceu')
# elif usuario == 'papel' and pc == 'pedra':
#     print('Você venceu!')
# elif usuario == 'tesoura' and pc == 'pedra':
#     print('Computador venceu')
# elif usuario == 'tesoura' and pc == 'papel':
#     print('Você venceu!')


# MODO CURSO EM VIDEO

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
print('''SUas opçães:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO.')
sleep(1)
print('KEN..')
sleep(1)
print('PÔ!!!')
sleep(2)

print('-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {} '.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')