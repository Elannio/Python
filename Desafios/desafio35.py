'''Desenvolva um programa que leia o comprimento de 
3 retas e diga ao usuário se elas podem ou não formar 
um triângulo.'''

lado1 = float(input('Digite o lado1: '))
lado2 = float(input('Digite o lado2: '))
lado3 = float(input('Digite o lado3: '))

if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado2 + lado3 > lado1:
    print('\033[31;44mPode formar um triângulo\033[m')
else:
    print('\033[31;44mNão pode formar um triângulo\033[m')