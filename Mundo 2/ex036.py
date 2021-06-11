'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programador
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado'''

casa = float(input('Qual o valor da casa?R$ '))
sal = float(input('Qual o seu salário?R$ '))
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
print('Pois o valor da parcela não pode ser maior que R$ {:.2f}'.format(parcasa))




# MODO CURSO EM VIDEO

# casa = float(input('Valor da casa: R$'))
# salario = float(input('Salário do comprador: R$'))
# anos = int(input('Quantos anos de financiamento? '))
# prestacao = casa / (anos * 12)
# minimo = salario * 30/100
# print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = '')
# print(' a prestação será de R${:.2f}'.format(prestacao))
# if prestacao <= minimo:
#     print('Empréstimo pode ser CONCEDIDO!')
# else:
#     print('Empréstimo NEGADO !')