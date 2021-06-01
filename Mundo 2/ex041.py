'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master

'''
from datetime import datetime
ano = datetime.now().strftime('%Y')
print('Estamos no ano {}.'.format(ano))
nasc = int(input('Informa o ano de nascimento do atleta:'))
idade = int(ano) - nasc
print('O atleta tem {} anos'.format(idade))