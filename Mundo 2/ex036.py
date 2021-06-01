'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programador
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado'''

casa = int(input('Qual o valor da casa? '))
sal = int(input('Qual o seu salário? '))
anos = int(input('Qual a quantidade de anos para pagamento? '))
meses = int(anos * 12)
print('A quantidade de anos revertida é em {} meses'.format(meses))
parc = (casa / meses)

print('O valor mensal a ser pago é R${:.2f} '.format(parc))

if parc > (0.30 * sal):
    print('Infelizmente não é possivel efetuar o empréstimo')
else:
    print('PARABÉNS ! Seu empréstimo foi aprovado.!!! ')
parcasa = (sal * 30)/100
print ('Pois o valor da parcela não pode ser maior que R$ {:.2f}'.format(parcasa))
