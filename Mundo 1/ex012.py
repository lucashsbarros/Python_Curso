#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

pre = float(input('Digite o valor do produto: R$'))
#pre = pre - (pre*5/100)
print('o valor novo do produto com 5% de desconto é de: R${:.2f}'.format(pre-(pre*5/100)))
