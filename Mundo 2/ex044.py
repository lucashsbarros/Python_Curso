'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o que preço normal e condição
de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
# from time import sleep
# preco = int(input('Informe o valor do produto R$ '))
#
# pag1 = preco - (preco * 0.10)
# pag2 = preco - (preco * 0.05)
# pag3 = preco
# pag4 = preco + (preco * 0.20)
# print('-=' * 40)
# print('Condiçoes de pagamento:')
# print('Digite pag1 para pagamento: A vista dinheiro/cheque e ganhe 10% de desconto')
# print('Digite pag2 para pagamento: A vista no cartão: e ganhe 5% de desconto')
# print('Digite pag3 para pagamento: Em até 2x no cartão: preço normal')
# print('Digite pag4 para pagamento: Em 3x ou mais no cartão: Juros de 20% no valor')
#
# usuario = input('Digite a sua forma de pagto: ').lower()
# lista = ['pag1','pag2', 'pag3', 'pag4']
#
# if usuario == 'pag1':
#     print('-=' * 40)
#     print('Calculando...')
#     sleep(3)
#     print('A escolha de pagamento foi a vista. \nValor atualizado R${:.2f}'.format(pag1))
#
# elif usuario == 'pag2':
#     print('-=' * 40)
#     print('Calculando...')
#     sleep(3)
#     print('A escolha de pagamento foi a vista no cartão.\nValor atualizado R${:.2f}'.format(pag2))
# elif usuario == 'pag3':
#     print('A escolha de pagamento foi: Em até 2x no cartão,\nValor permanece o mesmo R${:.2f}'.format(pag3))
# elif usuario == 'pag4':
#     print('-=' * 40)
#     print('Calculando...')
#     sleep(4)
#     print('A esoclha de pagamento foi: Em 3x ou mais no cartão, \nValor atualizado R${:.2f}'.format(pag4))
#


print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totparc,parcela))
else:
     total = preço
     print ('OPÇÃO INVÁLIDA de pagamento. Tente Novamente')
print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format(preço, total))

