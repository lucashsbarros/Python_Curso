#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu sálario atual: R$'))
print('Seu novo sálario com aumento de 15% é de: R${:.2f}'.format(salario+(salario*15/100)))