'''Faça um programa que leia um número inteiro e diga 
se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot = 0

for c in range (1, num+1):
    if num % c == 0:
        print('\033[34m', end=" ")
        tot+=1
    else:
        print('\033[m', end=" ")
    print(c, end=" ")
if tot ==2:
    print('\n\033[mE por isso ele é primo')
else:
    print('\n\033[mE por isso ele não é primo')

#Só será primo se o número for divisível por ele e por 0, então apenas duas vezes