'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Digite a quantidade de KM percorrido: '))
dia = float(input('Digite a quantidade de Dias que o carro foi alugado: '))
valor = (km * 0.15) + (dia * 60)

print(' O valor do aluguel do veiculo foi:R${:.2f}. '.format(valor))