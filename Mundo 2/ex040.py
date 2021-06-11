'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando quma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1+n2)/2
print('A sua média foi: {:.2f}'.format(med))
if med < 5:
    print('Você foi reprovado!')
elif med >= 5 and med <= 6.9:
#elif 6.9 > med >= 5:
    print(' Voce está de recuperação!')
elif med >= 7:
    print('Parabens, voce foi aprovado')