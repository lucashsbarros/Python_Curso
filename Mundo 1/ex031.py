'''Desenvolva um programa que pergunte a distancia de uma viagem em KM.Calcule o preço da passagem,
cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas'''

dist = float(input('Me diga a distancia da viagem em Km: '))
if dist < 200:
    pre1 = dist * 0.50
    print('O valor da passagem ficou em R${} '.format(pre1))
else:
    pre2 = dist * 0.45
    print('O valor da passagem com desconto ficou em R${}'.format(pre2))
