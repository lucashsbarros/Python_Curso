'''Condiçoes Simples e Compostas
Estrutura sequencial - Todos os exercicios anteriores foram desse tipo.

Estrutura condicional
if carro.esquerda():
    bloco True

else:
    bloco False


'''
# Condição Comum
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')

print('--FIM--')'''

# Condição Simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=3 else'carro velho')
print('--FIM--')