'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1250,00, calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%'''

sal = float(input('Digite um salário: R$'))
if sal >= 1250:
    aum = sal + (sal * 0.1)
    print('Seu salário de R${:.2f} teve um aumento de 10%, seu novo salário é: R${:.2f}'.format(sal,aum))
else:
    aum = sal + (sal * 0.15)
    print('Seu salário de R${:.2f} teve um aumento de 15%, seu novo salário é: R${:.2f}'.format(sal,aum))
