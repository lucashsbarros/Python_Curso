#Escreva um programa que leia um valor em metros e exiba ele convertido em centimentro e milimetros
#KM HM DAM M DM CM MM


n1 = float(input('Digite um valor em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
print('O valor {} em: \n Kilometros é {}Km\n Em Hectometro é {}Hm\n Em Decametro é {}Dam\n Em Decimetro é {}Dm\n Em centimetros é  {}cm \n Em milimetros é {}mm'.format(n1,km,hm,dam,dm,cm,mm))
