'''Escreva um programa que leia dois números inteiros 
e compare, mostrando na tela as seguintes mensagens. 
O primeiro valor é maior, O segundo valor é maior, 
não existe valor maior, os dois são iguais.'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('\033[36;45mO primeiro valor é maior.\033[m')
elif num2 > num1:
    print('\033[36;44mO segundo valor é maior.\033[m')
else:
    print('\033[32;41mNão existe valor maior, os dois são iguais.\033[m')

