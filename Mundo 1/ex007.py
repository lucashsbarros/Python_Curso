#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
soma = n1+n2
med = (n1+n2)/2
print('A soma das duas notas é {:.2f} \ne a sua média é {:.2f}'.format(soma,med))