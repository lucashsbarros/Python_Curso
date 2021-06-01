'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite'''

vel = float(input('Digite uma velocidade em Km: '))

if vel >= 80:
    mul = (vel - 80) * 7
    print('Você excedeu o limite de velocidade e recebeu uma multa de R${:.2f} '.format(mul))
else:
    print('Boa viagem!')
