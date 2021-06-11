'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 Até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
# peso = int(input('Digite o seu peso: '))
# alt = int(input('Digite a sua altura em centimetros: '))
# imc = (peso/(alt * alt))*10000
# print('Seu indice de Massa Corporal é {:.2f}'.format(imc))
# if imc < 18.5:
#     print('Você está abaixo do peso')
# elif imc > 18.5 and imc < 25:
#     print('Você está no peso ideal')
# elif imc > 25 and imc < 30:
#     print('Você está sobrepeso')
# elif imc > 30 and imc < 40:
#     print('Você está obeso')
# else:
#     print('Você está com Obesidade Mórbida')


# MODO CURSO EM VIDEO

peso = float(input('QUal é o seu peso? (Kg) '))
altura = float(input('QUal é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está sobrepeso')
elif 30 <= imc < 40:
    print('Você está obeso')
else:
    print('Você está com Obesidade Mórbida')

