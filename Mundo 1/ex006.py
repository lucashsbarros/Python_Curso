#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada '

n = int(input('Digite um número: '))
'''dob = (n*2)
tri = (n*3)
qua = (n**(1/2))
print('O dobro do valor {} é = {}, \nO triplo é = {} \nE a raiz quadra é = {:.2f} '.format(n,dob,tri,qua))'''
#print('O dobro do valor {} é = {}, \n0 triplo é = {} \nE a raiz quadra é = {:.2f} '.format(n,(n*2),(n*3),(n**(1/2))))
print('O dobro do valor {} é = {} \n0 triplo é = {} \nE a raiz quadra é = {:.2f} '.format(n,(n*2),(n*3),pow(n,(1/2))))