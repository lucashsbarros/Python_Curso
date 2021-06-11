'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''


# Ricardo Rosa quem ensinou esse comando
from datetime import datetime  #Importando a funçao datetime
ano = datetime.now().strftime("%Y")
# datetime.now() - camando para setar o ano atual
# strftime("%Y") - comando que converteu o datetime em STRING e passando apenas a mascara que no caso
# foi apenas o anos "%Y".
print('Estamos no ano de {}.'.format(ano))
nasc = int(input('Insira o ano de nascimento: '))
idade = int(ano) - nasc
print('Você tem {:.0f} anos.'.format(idade))
if idade < 18:
     print('Voce ainda não precisa se alistar! \n Pois ainda falta {} anos para a sua vez.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar!!! ')
elif idade > 18:
    print('Já passou a hora de você se alistar! \n Você está atrasado {} anos'.format(idade - 18))


# MODO CURSO EM VIDEO

# from datetime import date
# atual  = date.today().year
# nasc = int(input('Ano de Nascimento: '))
# idade = atual - nasc
# print('Quem nasceu e, {} tem {} anos em {}.'.format(nasc,idade,atual))
# if idade == 18:
#     print('Você tem que se alistar IMEDIATAMENTE')
# elif idade < 18:
#     saldo = 18 - idade
#     print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
#     ano = atual + saldo
#     print('Seu alistamento será em {}'.format(ano))
# elif idade > 18:
#     saldo = idade - 18
#     print('Você já deveria ter se alistado há {} anos'.format(saldo))
#     ano = atual - saldo
#     print('Seu alistamento foi em {}.'.format(ano))

