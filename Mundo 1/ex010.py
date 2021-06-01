#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Considere US$1,00 = r$3,27

r = float(input('Digite o valor que você tem na carteira: R$ '))
print('o valor convertido seria = US${:.2f}'.format(r/3.27))

'''r = float(input('digite um valor: '))
d = r/3.27
print ('o valor seria {:.2f}'.format(d))'''