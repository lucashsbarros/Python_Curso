'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o que preço normal e condição
de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preco = int(input('Informe o valor do produto R$ '))

pag1 = preco - (preco * 1.10)
pag2 = preco - (preco * 1.05)
pag3 = preco
pag4 = preco + (preco * 1.20)
print('Condiçoes de pagamento:')
print('Digite pag1 para pagamento: A vista dinheiro/cheque e ganhe 10% de desconto')
print('Digite pag2 para pagamento: A vista no cartão: e ganhe 5% de desconto')
print('Digite pag3 para pagamento: Em até 2x no cartão: preço normal')
print('Digite pag4 para pagamento: Em 3x ou mais no cartão: Juros de 20% no valor')
# forma_pgto = ['pag1','pag2', 'pag3', 'pag4']
#
# if forma_pgto == 0:
#     print('Pelo pagamento a vista voce recebeu um desconto de 10%'.format(pag1))
# elif forma_pgto == 1:
#     print('Pelo pagamento a vista no cartão voce recebeu um desconto de 5%'.format(pag2))
# elif forma_pgto == 2:
#     print('Pelo pagamento parcelado em 2x no cartão o valor do produto se manteve'.format(pag3))
# elif forma_pgto == 3:
#     print('Pelo pagamento parcelado em 3x no cartão o valor do produto teve um aumento de 20%'.format(pag4))