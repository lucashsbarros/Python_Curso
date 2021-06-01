'''Desenvolva um programa que pergunte a distancia de uma viagem em KM.Calcule o preço da passagem,
cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas'''

'''distancia = float(input('QUal a distancia da sua viagem ? '))
print ('Você esta preste a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

distancia = float(input('QUal a distancia da sua viagem ? '))
print ('Você esta preste a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
