'''
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja
como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos
built-in e módulos externos, oferecidos no Pypi.'''

'''Importa todas as "bebidas e doces"
    import bebida
    import doce

Importar apenas 1 item, no caso abaixo seria o pudim
    from doce import pudim

Exemplo de bibliote comum MATH
    >> math
    ceil - arredonda para cima
    floor - arredonda para baixo
    trunc - truncar o numero, elimina o numero após a virgula
    pow - potencia
    sqrt - calcula a raiz quadrada
    factorial - calcula fatoriais

Se eu colocar o comando > import math < o sistema irá importar todas as funcões acima
Para importar apenas um modulo > from math import sqrt  <
Para importar um ou mais modulo > from math import sqrt, pow  <
'''

'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num,raiz))'''


'''from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num,floor(raiz)))'''

'''import random
num = random.randint(1, 10)
print(num)'''

import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))








