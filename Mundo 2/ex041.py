'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master

'''
from datetime import datetime
ano = datetime.now().strftime('%Y')
# from datetime import date
# ano = date.today().year
print('Estamos no ano {}.'.format(ano))
nasc = int(input('Informa o ano de nascimento do atleta:'))
idade = int(ano) - nasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('O atleta é de categoria: Mirim')
elif idade <= 14:
    print('O atleta é de categoria: Infantil')
elif idade <= 19:
    print('O atleta é de categoria: Junior')
elif idade <= 25:
    print('O atleta é de categoria: Sênior')
else:
    print('O atleta é de categoria: Master')

