'''Faça um programa que leia um ano qualquer e mostre 
se ele é bissexto.'''

ano = int(input('Digite um ano: '))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('Não é bissexto')