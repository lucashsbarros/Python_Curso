'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''


# Ricardo Rosa quem ensinou esse comando
from datetime import datetime  #Importando a funçao datetime
ano = datetime.now().strftime("%Y")
# datetime.now() - camando para setar o ano atual
# strftime("%Y") - comando para converteu o datetime em STRING e passando apenas a mascara que no caso
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





