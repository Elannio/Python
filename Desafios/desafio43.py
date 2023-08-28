'''Desenvolva uma lógica que leia o peso e a altura de 
uma pessoa, calcule seu imc e mostre seu status, 
de acordo com a tabela abaixo: abaixo de 18.5: abaixo 
do peso; entre 18.5 e 25: peso ideal; 25 até 30: 
sobrepeso; 30 até 40: obesidade; acima de 40: 
obesidade mórbida.'''

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.2f} então está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu imc é de {imc:.2f} então está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu imc é de {imc:.2f} então está no sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu imc é de {imc:.2f} então está com obesidade.')
elif imc >= 40:
    print(f'Seu imc é de {imc:.2f} então está com obesidade mórbida.')