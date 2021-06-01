'''
Crie um programa que faça o computador jogar Jokenpo com você

'''

# forma 1
import random

print(' Vamos jogar JOKENPÔ !!! ')

usuario = input('Digite a sua escolha: ').lower()

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print('A escolha do computador foi: {}'.format(pc))
resultado = ""
if pc == usuario:
    resultado = "Empate"
elif usuario == 'pedra' and pc == 'tesoura':
    resultado = 'Você venceu!'
elif usuario == 'papel' and pc == 'pedra':
    resultado = 'Você venceu!'
elif usuario == 'tesoura' and pc == 'papel':
    resultado = 'Você venceu!'
else:
    resultado = 'Computador venceu'
print(resultado)

# forma 2

import random

print(' Vamos jogar JOKENPÔ !!! ')

usuario = input('Digite a sua escolha: ').lower()

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print('A escolha do computador foi: {}'.format(pc))

if pc == usuario:
    print('Empate')
elif usuario == 'pedra' and pc == 'tesoura':
    print('Você venceu!')
elif usuario == 'pedra' and pc == 'papel':
    print('Computador venceu')
elif usuario == 'papel' and pc == 'tesoura':
    print('Computador venceu')
elif usuario == 'papel' and pc == 'pedra':
    print('Você venceu!')
elif usuario == 'tesoura' and pc == 'pedra':
    print('Computador venceu')
elif usuario == 'tesoura' and pc == 'papel':
    print('Você venceu!')
