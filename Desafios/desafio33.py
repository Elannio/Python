'''Faça um programa que leia 3 números e mostre qual 
é o maior e qual é o menor.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num2 > num3:
    print(f'{num1} é maior e {num3} é menor')
elif num3 > num2:
    print(f'{num3} é maior e {num1} é menor')
elif num2 > num1:
    print(f'{num2} é maior e {num3} é menor')
elif num2 == num1 == num3:
    print('São iguais')
else:
    print(f'{num2} é maior e {num1} é menor')
