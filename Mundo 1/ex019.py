'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido'''

import random
n1 = input('Digite o nome do(a) Primeiro(a) aluno(a): ')
n2 = input('Digite o nome do(a) Segundo(a) aluno(a): ')
n3 = input('Digite o nome do(a) Terceiro(a) aluno(a): ')
n4 = input('Digite o nome do(a) Quarto (a) aluno(a): ')
lista = [n1,n2,n3,n4]
esc = random.choice(lista)
print('O aluno escolhido foi {}'.format(esc))



