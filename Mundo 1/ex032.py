'''Faça um porgrama que leia um ano qualquer e mostre se ele é BISSEXTO'''

ano = int(input('Digite um ano: '))
if ano%4== 0 and ano%100 != 0:
        print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))