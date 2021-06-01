'''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o
 Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(),
 capitalize(), title(), strip(), junção com join().'''

'''
- Fatiamento - é conseguir pegar pedações dela
    frase = Curso em Video
     -frase[9]
      Busca a letra V da frase
    
    - frase[9:13] = ele pega do 9 ao 13, porém exclui o 13 
      Busca da Letra V até E = Vide
    
    - frase [9:21]
      Sendo que só há 20 bloquinhos, o python vai buscar até o limite que nó caso é o 20.
      
    - frase [9:21:2]
     Fara o mesmo , do 9 ao 21 porém pulando de 2 em 2
     
     frase[:5]
     Omite o inicio começa do caracter ZERO até ao 4 ja que remove o 5
     
     frase [15:]
     Indica o inicio até o final - que no caso daria MUNDO 1
      
     frase [9::3]
     Vai começar no NOVE e vai até o final e pulando de 3 em 3 = Veph 

- Analise - é saber informações da string
    len(frase) = Qual o comprimento dessa frase?
    frase.count('o') = Está pedindo para o programa contar quantas vezes existe a letra 'o' minuscula = na frase daria 3 letras 'o'
    frase.count('o',0,13) = Uma contagem já com fatiamento , contando do 0 até 13 (lembrando que o 13 será excluido) = na frase daria apenas 1 'o'
    frase.find('deo') = encontrar parcela da palavra , no caso irá mostrar o inicio do 'DEO' que seria o 11
    frase.find('Android') = ele retorna o valor -1, já que não existe nessa frase
    'Curso' in frase = existe a palavra curso em frase? Se sim = true, se não = false
    
- Transformação
    frase.replace('Python, 'Android) = Ele irá substituir na frase Python por Android
    frase.upper() = a frase toda irá ficar em MAIUSCULA
    frase.lower() = a frase irá ficar em MINUSCULA
    frase.capitalize() = joga todas os caracteres em minusculo e a PRIMEIRA LETRA da frase será em Maiscula
    frase.title() = analiza quantas palavras hpa na frase e faz uma quebra e faz um capitaliza em CADA palavras, sendo asim, deixa em maiusculo cada letra INICIO de palavra
    
    - frase= ___Aprenda_Python__ (os _ são espaços)
      frase.strip() = remove espaços inuteis na frase que no caso da frase acima seriam as posisoes 0,1,2,17 e 18
      frase.rstrip() = remove os ULTIMOS espaçoS = Removendo os espaços 17 e 18
      frase.lstrip() = remove os PRIMEIROS espaços = removando os espaços 0,1,2
      
- Divisão
Frase = Curso_em_Video_Python (os _ são espaços)
    frase.split() = ele refaz os indices sendo assim a Palavra Curso fica com posição de 0 a 4, palavra EM fica com 
posição 0 e 1, palavra Video com posições de 0 a 4 e palavra Python com posições de 0 a 5 e essa separação vira outra lista
que no caso será de 0, 1, 2 e 3 

- Junção
    '-'.join(frase) = Junta todos os elementos com espaçamento utilizando o '-' = Curso-em-Video-Pyton
    
    
    


'''
