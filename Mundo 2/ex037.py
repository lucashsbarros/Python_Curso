'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

from time import sleep

num = int(input('Digite um número inteiro: '))
bin = bin(num)
oct = oct(num)
hex = hex(num)
print('Temos 3 tipos de conversão:\n- Para conversão em BINARIO digite: bin\n- Para conversão em Octal digite: oct')
print('- Para conversão em Hexadecimal: hex')
usuario = input('Informe o time de conversão que deseja:').lower()
lista = ['bin','oct', 'hex']
print('-=' * 25)
print('Efetuando conversão, aguarde ...')
sleep(3)
print('Pronto! \nConversão realizada')
if usuario == 'bin':
    print('O valor em binário é: {}'.format(bin))
elif usuario == 'oct':
    print('O valor em Octal é: {}'.format(oct))
else:
    print('O valor em Hexadecimal é: {}'.format(hex))


# MODO CURSO EM VIDEO

# num = int(input('Digite um número inteiro: '))
# print( '''Escolha uma das bases para conversão:
# [1] converter para BINÁRIO
# [2] converter para OCTAL
# [3] converter para hexadecimal''')
# opcao = int(input('Sua opção: '))
# if opcao == 1:
#     print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
# elif opcao == 2:
#     print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
# elif opcao == 3:
#     print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
# else:
#     print('Opção inválida. Tente novamente.')