'''Crie um programa que leia o nome completo de uma pessoa e mostre
1)O nome com todas as letras maiúsculas
2)O nome com todas as letras minúsculas
3)Quantas letras ao todo (sem considerar os espaços)
4)Quantas letras tem o primeiro nome
'''


nome = str(input('Digite o seu nome completo: '))

print(nome.upper().strip())
print(nome.lower().strip())
print(len(nome.replace(' ','').strip()))
pri = nome.split()
print(pri[0])
print(len(pri[0]))


