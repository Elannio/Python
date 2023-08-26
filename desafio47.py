'''Crie um programa que mostre na tela todos os números 
pares que estão no intervalo de 1 até 50.'''

for c in range (1, 50+1):
    if c % 2 == 0:
     print(c, end= ' ')
print('Esses são os números pares de 1 até 50')

for c in range (2, 51, 2):
     print(c, end= ' ')
print('Esses são os números pares de 1 até 50')