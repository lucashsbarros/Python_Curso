'''faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma àrea de 2mª.'''


base = float(input('Digite o tamanho da base: '))
altura = float(input('Digite o tamanho da altura '))
area = base*altura
print('A area dessas metragens é: {}m², e é necessário {:.2f}L de tintas para pintá-la '.format(area,area/2))