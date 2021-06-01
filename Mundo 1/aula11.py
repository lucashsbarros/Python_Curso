#print('\033[34mOlá, mundo!\033[m')


'''a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))'''

'''nome = 'Guanabara'
print('Olá ! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[30m',nome,'\033[m'))'''


nome = 'Guanabara'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[0;30;44m'}

print('Olá ! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))