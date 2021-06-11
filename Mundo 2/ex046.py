'''Faça um programa que mostre na tela uma contagem regressiva para o estou de fofos de artificio, indo de 10 até
0, com uma pausa de 1 segundo entre eles'''
from time import sleep
import emoji
emotion = ':tada: '
for n in range(10, 0, -1):
    print(n)
    sleep(1)
print(emoji.emojize((emotion) * 3 + 'Feliz Ano Novo! ' + (emotion) * 3, use_aliases=True))


