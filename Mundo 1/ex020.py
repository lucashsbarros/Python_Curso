'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

import random
n1 = input('Digite o nome do(a) Primeiro(a) aluno(a): ')
n2 = input('Digite o nome do(a) Segundo(a) aluno(a): ')
n3 = input('Digite o nome do(a) Terceiro(a) aluno(a): ')
n4 = input('Digite o nome do(a) Quarto (a) aluno(a): ')
lista = [n1,n2,n3,n4]
ordem = random.shuffle(lista)

print ('A ordem para entrega dos trabalhos é:{}'.format(lista))

